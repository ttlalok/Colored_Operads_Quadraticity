"""
This file contains the class TreePolynomial, and functions for converting trees and polynomials to LaTex
"""


from basic import *


class TreePolynomial:
    def __init__(self, trees=[], coeffs=[]):
        reduced_trees, reduced_coeffs = self.reduce_input(trees, coeffs)
        self.trees = reduced_trees
        self.coeffs = reduced_coeffs

    def __bool__(self):
        return bool(self.trees)

    def __len__(self):
        return len(self.trees)

    def __eq__(self, other):
        if len(self) != len(other):
            return False
        for i, tree1 in enumerate(self.trees):
            TREE_PRESENT = False
            for j, tree2 in enumerate(other.trees):
                if tree1 == tree2 and self.coeffs[i] == other.coeffs[j]:
                    TREE_PRESENT = True
            if not TREE_PRESENT:
                return False
        return True

    def __ne__(self, other):
        return not self.__eq__(other)


    def reduce_input(self, trees, coeffs):
        added = [False] * len(trees)
        res_trees = []
        res_coeffs = []
        for i, tree1 in enumerate(trees):
            if not added[i]:
                for j, tree2 in enumerate(trees):
                    if i != j:
                        if tree1 == tree2:
                            added[i] = True
                            added[j] = True
                            cf = coeffs[i] + coeffs[j]
                            if cf != 0:
                                res_trees.append(tree1)
                                res_coeffs.append(cf)
        for i, tree in enumerate(trees):
            if not added[i]:
                res_trees.append(tree)
                res_coeffs.append(coeffs[i])
        return res_trees, res_coeffs


    def same_trees(self, other):
        if len(self.trees) != len(other.trees):
            return False
        for tree in self.trees:
            if tree not in other.trees:
                return False
        return True

    def poly_too_big(self):
        for cf in self.coeffs:
            if cf > 100 or cf < -100:
                return True
        return False

    def __add__(self, other):
        added1 = [False] * len(self.trees)
        added2 = [False] * len(other.trees)
        new_trees = []
        new_coeffs = []
        for i, tree1 in enumerate(self.trees):
            for j, tree2 in enumerate(other.trees):
                if tree1 == tree2:
                    added1[i] = True
                    added2[j] = True
                    cf = self.coeffs[i] + other.coeffs[j]
                    if cf != 0:
                        new_trees.append(tree1)
                        new_coeffs.append(cf)
        for i, tree in enumerate(self.trees):
            if not added1[i]:
                new_trees.append(tree)
                new_coeffs.append(self.coeffs[i])
        for j, tree in enumerate(other.trees):
            if not added2[j]:
                new_trees.append(tree)
                new_coeffs.append(other.coeffs[j])
        return TreePolynomial(new_trees, new_coeffs)

    def negative(self):
        new_coeffs = [-cf for cf in self.coeffs]
        return TreePolynomial(self.trees, new_coeffs)

    def __sub__(self, other):
        return self + other.negative()

    def __mul__(self, number):
        if number != 0:
            return TreePolynomial(self.trees, [cf * number for cf in self.coeffs])

    def __rmul__(self, other):
        return self.__mul__(other)

    def __neg__(self):
        return self.__mul__(-1)

    def __str__(self):
        res = 'Polynomial: '
        for i, tree in enumerate(self.trees):
            if i != 0:
                res += ' + '
            res += str(self.coeffs[i]) + '*' + '{' + str(tree) + '}'
        return res


def tree_to_latex(tree):
    stack = [tree.root]
    result = ''
    while stack:
        cur_node = stack.pop()
        if isinstance(cur_node, str):
            result += cur_node
        else:
            result += str(cur_node.label)
        if isinstance(cur_node, ColoredVertex):
            result += '('
        if not isinstance(cur_node, str):
            if cur_node.parent is not None:
                if cur_node.index_in_parent == cur_node.parent.arity:
                    stack.append(')')
                else:
                    stack.append(',')
            for child in reversed(cur_node.children):
                stack.append(child)
    return result


def poly_to_latex(poly, underline_indices=[]):
    result = ''
    if not poly.coeffs:
        result += '0'
    for i in range(len(poly.coeffs)):
        if i > 0 and i % 4 == 0:
            result += '\\\\ \n & '
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
        if i in underline_indices:
            result += '\\underline{'
        result += tree_to_latex(tree)
        if i in underline_indices:
            result += '}'
    return result
