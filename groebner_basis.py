# The file implements the Groebner basis mechanics

from basic import *
from m_alpha_beta import *
from tree_polynomial import *


class GroebnerRelation:
    # A tree polynomial with a chosen leading term
    def __init__(self, poly, lt_index=0, label=''):
        self.poly = poly
        self.lt_index = lt_index
        self.lt = poly.trees[lt_index]
        self.lt_coeff = poly.coeffs[lt_index]
        self.label = label

    def __str__(self):
        return 'Relation ' + self.label + ':' + str(self.poly) + ' ; lt index= ' + str(self.lt_index)

    def set_lt(self, new_lt_index):
        self.lt_index = new_lt_index
        self.lt = self.poly.trees[new_lt_index]
        self.lt_coeff = self.poly.coeffs[new_lt_index]

    def can_reduce_tree(self, tree):
        result = tree.is_divisible_by(self.lt)
        return result

    def can_reduce_poly(self, poly):
        result = False
        for tree in poly.trees:
            if self.can_reduce_tree(tree):
                result = True
                break
        return result

    def reduce_mono(self, tree, tree_cf):
        if not self.can_reduce_tree(tree):
            return TreePolynomial([tree], [tree_cf])
        print('Call to reduce mono: ', tree_cf, '*', tree, ' by ', self.label)
        lt_subtree = tree.find_subtree(self.lt)
        new_cf = tree_cf / self.lt_coeff
        seq_of_m = get_seq_of_m(tree, lt_subtree)
        res = TreePolynomial([tree], [tree_cf])
        for i, tree in enumerate(self.poly.trees):
            # print('substracting:', TreePolynomial([seq_of_m.apply_to_tree(tree)], [(tree_cf / self.lt_coeff) * self.poly.coeffs[i]]))
            res = res - TreePolynomial([seq_of_m.apply_to_tree(tree)], [(tree_cf / self.lt_coeff) * self.poly.coeffs[i]])
        #print('Result:', res)
        return res

    def reduce_poly(self, poly, log):
        if poly.poly_too_big():
            return poly

        res = poly
        reduction_stage = -1
        while self.can_reduce_poly(res):
            res_start = copy.deepcopy(res)
            reduction_stage += 1
            # print('reduction stage: ', reduction_stage)
            changes = TreePolynomial()
            underline_indices = []
            for i, tree in enumerate(res.trees):
                tree_cf = res.coeffs[i]
                if self.can_reduce_tree(tree):
                    underline_indices.append(i)
                    # print('Reducing the tree: ', tree, ' with ', self.label, self.lt_index, '\n')
                    # print('result of tree reduction :', self.reduce_mono(tree, tree_cf) - TreePolynomial([tree], [tree_cf]))
                    changes = (changes - TreePolynomial([tree], [tree_cf]) + self.reduce_mono(tree, tree_cf))
            log.append('&' + poly_to_latex(res, underline_indices=underline_indices) + ' \stackrel{ ' + self.label + ' }{=} ' +  ' \\\\ \n')
            res = res + changes

            if res.same_trees(res_start):
                break
            if res.poly_too_big():
                break
        return res

    def relation_to_latex(self):
        poly = self.poly
        result = '\n Relation ' + self.label + ': \n $$ \n'
        if not poly.coeffs:
            result += '0'
        for i in range(len(poly.coeffs)):
            if i == self.lt_index:
                result += '\\underline{'
            cf = poly.coeffs[i]
            tree = poly.trees[i]
            if cf < 0:
                result += ' - '
                if cf != -1:
                    result += str(-cf) + '*'
            else:
                if i != 0:
                    result += ' + '
                    if cf != 1:
                        result += str(cf) + '*'
                else:
                    if cf != 1:
                        result += str(cf) + '*'
            result += tree_to_latex(tree)
            if i == self.lt_index:
                result += '}'
        result += '\n $$ \n'
        return result


class GroebnerBasis:
    # A bunch of Groebner relations
    def __init__(self, list_of_relations=[]):
        self.relations = list_of_relations
        self.lts = [relation.lt for relation in list_of_relations]

    def set_lt_for_all(self, new_lt_index):
        for relation in self.relations:
            relation.set_lt(new_lt_index)
        self.lts = [relation.lt for relation in self.relations]

    def append_relation(self, relation):
        self.relations.append(relation)
        if relation.lt not in self.lts:
            self.lts.append(relation.lt)

    def merge_bases(self, other):
        new_relations = self.relations + other.relations
        new_lts = [relation.lt for relation in new_relations]
        self.relations = new_relations
        self.lts = new_lts

    def can_reduce_tree(self, tree):
        for relation in self.relations:
            if relation.can_reduce_tree(tree):
                return True
        return False

    def can_reduce_poly(self, poly):
        # print('Checking if basis can reduce poly')
        # print('Basis contains relations:', len(self.relations))
        for relation in self.relations:
            if relation.can_reduce_poly(poly):
                # print('relation CAN reduce poly')
                return True
        return False

    def reduce_poly(self, poly, log):
        print('Reducing poly with basis: ', poly)
        if poly.poly_too_big():
            return poly
        res = poly
        # we keep a counter for reduction turns to avoid infinite looping
        cycle_counter = 0
        # we will keep a log of all polynomials appeared as the result to cut off infinite looping early
        spoly_log = []
        while self.can_reduce_poly(res):
            if cycle_counter >= 1000:
                break
            if res in spoly_log:
                print('CYCLE!')
                break
            res_copy = copy.deepcopy(res)
            for relation in self.relations:
                if relation.can_reduce_poly(res):
                    print('reducing with relation ', relation.label)
                    res = relation.reduce_poly(res, log)
            if res.same_trees(res_copy):
                print('SAME TREES; BREAKING')
                break
            # we dont want to include the original poly in spoly_log:
            if cycle_counter > 0:
                spoly_log.append(res)
            cycle_counter += 1
        print('Reduction completed')
        log.append('&' + poly_to_latex(res) + '\\\\ \n')
        return res

    def basis_to_latex(self):
        result = ''
        for relation in self.relations:
            result += relation.relation_to_latex()
        return result

