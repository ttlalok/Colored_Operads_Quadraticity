"""
This file solves the following problem: given a tree and a subtree find the sequence of operations m_{\alpha \beta},
such that m_{\alpha \beta}(subtree) = tree.
"""


from basic import *
from tree_polynomial import TreePolynomial


class MOperation:
    # This is the class of operations m_{\alpha, \beta}
    def __init__(self, type_, generator, position, shuffle=Permutation()):
        self.type = type_  # type is a string, can be 'above' meaning the generator grafted from above or 'below'
        self.generator = generator  # object of type TypeOfVertex
        self.position = position
        self.shuffle = shuffle

    def __str__(self):
        if self.type == 'above':
            return 'operation: graft ' + self.generator.label + ' ' + self.type + ' on position ' + str(self.position) + '; shuffle: ' + str(self.shuffle)
        else:
            return 'operation: graft the tree on ' + self.generator.label + ' in slot number ' + str(self.position) + '; shuffle: ' + str(self.shuffle)

    def apply_to_tree(self, tree):
        new_corolla = ColoredTree(self.generator.create_vertex())
        if self.type == 'above':
            return graft(tree, new_corolla, self.position, self.shuffle)
        if self.type == 'below':
            return graft(new_corolla, tree, self.position, self.shuffle)

    def can_be_applied_to(self, tree):
        if self.type == 'above':
            # find target leaf:
            target_leaf = None
            for leaf in tree.leaves:
                if leaf.label == self.position:
                    target_leaf = leaf
            # check colour compatibility:
            if self.generator.output_color != target_leaf.color:
                return False
            # check shuffle property:
            candidate = self.apply_to_tree(tree)
            if not candidate.is_shuffle_tree:
                return False
        if self.type == 'below':
            # check colour compatibility:
            bottom_color = self.generator.input_colors[self.position - 1]
            top_color = tree.root.output_color
            if bottom_color != top_color:
                return False
            # check shuffle property:
            candidate = self.apply_to_tree(tree)
            if not candidate.is_shuffle_tree:
                return False
        return True


class SeqMOperation:
    # Wrapping for a sequence of m_operations
    def __init__(self):
        self.operations = []

    def append_operation(self, m_operation):
        self.operations.append(m_operation)

    def extend(self, other):
        self.operations.extend(other.operations)

    def __str__(self):
        res = 'Seq of operations:'
        for operation in self.operations:
            res += '\n' + str(operation)
        return res

    def apply_to_tree(self, tree):
        cur_tree = tree
        for operation in self.operations:
            cur_tree = operation.apply_to_tree(cur_tree)
        return cur_tree

    def can_be_applied_to(self, tree):
        cur_tree = tree
        for operation in self.operations:
            if not operation.can_be_applied_to(cur_tree):
                return False
            cur_tree = operation.apply_to_tree(cur_tree)
        return True

    def apply_to_poly(self, poly):
        res = TreePolynomial()
        for i, tree in enumerate(poly.trees):
            cf = poly.coeffs[i]
            res = res + TreePolynomial([self.apply_to_tree(tree)], [cf])
        return res


def compute_permutation(tree_start, tree_goal):
    start = [leaf.label for leaf in tree_start.leaves]
    goal = [leaf.label for leaf in tree_goal.leaves]
    p_start = Permutation(*start)
    p_goal = Permutation(*goal)
    res = p_goal * p_start.inverse()
    return res


def process_one_vertex_above(tree, subtree, border_vertex, position_of_target_vertex, operations_log):
    target_vertex = border_vertex.children[position_of_target_vertex]
    index_of_target_edge_in_tree = border_vertex.min_descendant_list[position_of_target_vertex]
    index_of_target_edge_in_subtree = subtree.relabelling_dict[index_of_target_edge_in_tree]

    # getting new subtree:
    new_subtree_set = subtree.subtree_set + [target_vertex]
    new_subtree = tree.find_subtree_by_set(new_subtree_set)

    # computing permutation:
    tree_start = graft(subtree.normal_subtree, ColoredTree(target_vertex.type.create_vertex()), index_of_target_edge_in_subtree)
    shuffle = compute_permutation(tree_start, new_subtree.normal_subtree)

    # setting operation:
    operation = MOperation('above', target_vertex.type, index_of_target_edge_in_subtree, shuffle)
    operations_log.append_operation(operation)
    return new_subtree


def process_border(tree, subtree, operations_log):
    while subtree.border:
        border_vertex = subtree.border[0]
        for child_position in range(len(border_vertex.children)):
            child = border_vertex.children[child_position]
            if child not in subtree.subtree_set and not isinstance(child, Leaf):
                subtree = process_one_vertex_above(tree, subtree, border_vertex, child_position, operations_log)
    return subtree


def process_one_vertex_below(tree, subtree, operations_log):
    subtree_root = subtree.subtree_set[0]
    # getting new subtree:
    new_subtree_set = [subtree_root.parent] + subtree.subtree_set
    new_subtree = tree.find_subtree_by_set(new_subtree_set)

    # computing the permutation:
    tree_start = graft(ColoredTree(subtree_root.parent.type.create_vertex()), subtree.normal_subtree, subtree_root.index_in_parent)
    shuffle = compute_permutation(tree_start, new_subtree.normal_subtree)
    operation = MOperation('below', subtree_root.parent.type, subtree_root.index_in_parent, shuffle)
    operations_log.append_operation(operation)

    new_subtree = process_border(tree, new_subtree, operations_log)
    return new_subtree


def get_seq_of_m(tree, subtree):
    operation_log = SeqMOperation()
    new_subtree = process_border(tree, subtree, operation_log)
    subtree_root = new_subtree.subtree_set[0]
    while subtree_root.parent:
        new_subtree = process_one_vertex_below(tree, new_subtree, operation_log)
        subtree_root = new_subtree.subtree_set[0]
    return operation_log
