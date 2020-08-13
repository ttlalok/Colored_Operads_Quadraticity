"""
This file contains all the basics of the project.

Classes:
Leaf -- leaves of a tree.
ColoredVertex -- vertices of a tree.
TypeOfVertex -- wrapping class for ColoredVertex. Should be thought of as a type of generator in an operad.
ColoredTree -- a colored tree.
ColoredSubtree -- wrapping class for data characterizing a subtree of a colored tree.
"""

from permutation import Permutation
from random import randint
import copy

INF = float('inf')


class Leaf:
    def __init__(self, label_int, parent, index):
        self.id = randint(0, 10 ** 5)
        self.label = label_int
        self.parent = parent
        self.children = []
        self.index_in_parent = index  # 1-based index
        self.min_descendant_list = [self.label]

    def __eq__(self, other):
        return self.id == other.id

    def __ne__(self, other):
        return not self.__eq__(other)

    def __str__(self):
        return 'leaf ' + str(self.label)

    def same_type_and_numeration(self, other):
        return self.label == other.label


class ColoredVertex:
    def __init__(self, label, input_colors, output_color):
        self.type = None
        self.id = randint(0, 10 ** 5)
        self.label = label
        self.input_colors = input_colors
        self.output_color = output_color
        self.arity = len(input_colors)
        self.children = [Leaf(i, self, i) for i in range(1, len(input_colors) + 1)]
        self.parent = None
        self.index_in_parent = None  # 1-based index
        self.min_descendant_list = [i for i in range(1, len(input_colors) + 1)]

    def __str__(self):
        return self.label + str(self.min_descendant_list)

    def __eq__(self, other):
        return self.id == other.id

    def __ne__(self, other):
        return not self.__eq__(other)

    def same_type(self, other):
        return self.label == other.label

    def same_type_and_numeration(self, other):
        if self.label != other.label:
            return False
        for i in range(len(self.min_descendant_list)):
            if self.min_descendant_list[i] != other.min_descendant_list[i]:
                return False
        return True


class TypeOfVertex:
    def __init__(self, label, input_colors, output_color):
        self.label = label
        self.input_colors = input_colors
        self.output_color = output_color
        self.arity = len(input_colors)

    def create_vertex(self):
        vertex = ColoredVertex(self.label, self.input_colors, self.output_color)
        vertex.type = self
        return vertex

    def create_corolla(self):
        vertex = ColoredVertex(self.label, self.input_colors, self.output_color)
        vertex.type = self
        return ColoredTree(vertex)


class ColoredTree:
    # We will keep the list of all subtrees, each subtree is an instance of class ColoredSubtree
    def __init__(self, root):  # root is a ColoredVertex
        self.root = root
        self.arity = root.arity
        self.leaves = root.children
        root.parent = None
        self.bfs_nodes = [root] + root.children
        self.subtree_markings_for_bfs_nodes = [False]

        # rendering self as a subtree:
        d = dict((i, i) for i in range(1, self.arity + 1))
        subtree = ColoredSubtree([root], self, self, d, [])
        self.list_of_subtrees = [subtree]

    def __eq__(self, other):
        if len(self.bfs_nodes) != len(other.bfs_nodes):
            return False
        for i, node in enumerate(self.bfs_nodes):
            if not node.same_type_and_numeration(other.bfs_nodes[i]):
                return False
        return True

    def __ne__(self, other):
        return not self.__eq__(other)

    def __str__(self):
        res = 'Tree on vertices: '
        for ver in self.bfs_nodes:
            if not isinstance(ver, Leaf):
                res += str(ver)
        return res

    def is_corolla(self):
        for child in self.root.children:
            if not isinstance(child, Leaf):
                return False
        return True

    def is_divisible_by(self, other):
        for subtree in self.list_of_subtrees:
            if subtree.normal_subtree == other:
                return True
        return False

    def is_shuffle_tree(self):
        for ver in self.bfs_nodes:
            if not isinstance(ver, Leaf):
                desc_list = ver.min_descendant_list
                for i in range(len(desc_list) - 1):
                    if desc_list[i] > desc_list[i + 1]:
                        return False
        return True

    def find_subtree(self, other):
        for subtree in self.list_of_subtrees:
            if subtree.normal_subtree == other:
                return subtree
        return None

    def find_subtree_by_set(self, subtree_set):
        subtree_id_set = set(vertex.id for vertex in subtree_set)
        for my_subtree in self.list_of_subtrees:
            my_subtree_set = my_subtree.subtree_set
            my_subtree_id_set = set(vertex.id for vertex in my_subtree_set)
            if my_subtree_id_set == subtree_id_set:
                result = my_subtree
                return result
        return None

    def relabel_leaves_by_permutation(self, perm):
        new_tree = copy.deepcopy(self)
        for ver in new_tree.bfs_nodes:
            if isinstance(ver, Leaf):
                ver.label = perm(ver.label)
                ver.min_descendant_list = [ver.label]
            else:
                for i, desc in enumerate(ver.min_descendant_list):
                    ver.min_descendant_list[i] = perm(desc)
        new_tree.list_of_subtrees = get_subtrees(new_tree)
        return new_tree


class ColoredSubtree:
    """
    This is a wrapping class for a tuple (subtree vertices set, separated subtree, normalized subtree, relabelling dict, border).
    border is a list of vertices with a non-leaf descendant outside of the subtree.
    """

    def __init__(self, subtree_set, separated_subtree, normal_subtree, relabelling_dict, border):
        self.subtree_set = subtree_set
        self.separated_subtree = separated_subtree
        self.normal_subtree = normal_subtree
        self.relabelling_dict = relabelling_dict
        self.border = border


# The following are the technical functions needing for handling the divisibility for colored trees.


def set_subtree_markings(tree, subtree):
    for i, node in enumerate(tree.bfs_nodes):
        for subtree_node in subtree:
            if node == subtree_node:
                tree.subtree_markings_for_bfs_nodes[i] = True


def clear_subtree_markings(tree):
    for i, node in enumerate(tree.bfs_nodes):
        tree.subtree_markings_for_bfs_nodes[i] = False


def separate_subtree(subtree, tree_source):
    set_subtree_markings(tree_source, subtree)
    tree = copy.deepcopy(tree_source)
    clear_subtree_markings(tree_source)
    # cutting off everything below the root of the subtree:
    for i, mark in enumerate(tree.subtree_markings_for_bfs_nodes):
        if mark:
            root = tree.bfs_nodes[i]
            root.parent = None
            root.index_in_parent = None
            tree.root = root
            break
    degree = 0
    for i, mark in enumerate(tree.subtree_markings_for_bfs_nodes):
        if mark:
            node = tree.bfs_nodes[i]
            for j, child in enumerate(node.children):
                if isinstance(child, Leaf):
                    degree += 1
                else:
                    if not tree.subtree_markings_for_bfs_nodes[tree.bfs_nodes.index(child)]:
                        leaf_label = child.min_descendant_list[0]
                        new_leaf = Leaf(leaf_label, node, j + 1)
                        node.children[j] = new_leaf
                        degree += 1
    # housekeeping
    tree.arity = degree
    tree.bfs_nodes = get_breadth_first_nodes(tree.root)
    dfs_nodes = get_depth_first_nodes(tree.root)
    tree.leaves = [ver for ver in dfs_nodes if isinstance(ver, Leaf)]
    return tree


def normalize_subtree(subtree_source):
    subtree = copy.deepcopy(subtree_source)
    root = subtree.root
    list_of_vertices = get_breadth_first_nodes(root)
    num_of_leaves = 0
    existing_labeling = []
    for ver in list_of_vertices:
        if isinstance(ver, Leaf):
            num_of_leaves += 1
            existing_labeling.append(ver.label)
    normal_labeling = list(range(1, num_of_leaves + 1))
    existing_labeling.sort()
    relabel_dict = dict()
    for i, item in enumerate(existing_labeling):
        relabel_dict.update({item: normal_labeling[i]})
    target_labels = []
    for leaf in subtree.leaves:
        target_labels.append(relabel_dict[leaf.label])
    relabel(subtree.leaves, target_labels)
    # need to adjust min descendant:
    for ver in list_of_vertices:
        if not isinstance(ver, Leaf):
            ver.min_descendant_list = [relabel_dict[x] for x in ver.min_descendant_list]
    return subtree, relabel_dict


def relabel(leaves, target):
    assert len(leaves) == len(target)
    for i, leaf in enumerate(leaves):
        leaf.label = target[i]


def get_border(subtree_set):
    border = []
    for vertex in subtree_set:
        for child in vertex.children:
            if not isinstance(child, Leaf) and not child in subtree_set:
                border.append(vertex)
                break
    return border


def get_breadth_first_nodes(root):
    nodes = []
    stack = [root]
    while stack:
        cur_node = stack[0]
        stack = stack[1:]
        nodes.append(cur_node)
        for child in cur_node.children:
            stack.append(child)
    return nodes


def get_depth_first_nodes(root):
    nodes = []
    stack = [root]
    while stack:
        cur_node = stack[0]
        stack = stack[1:]
        nodes.append(cur_node)
        for child in reversed(cur_node.children):
            stack.insert(0, child)
    return nodes


def get_vertex_masks(root):
    bfs_nodes = get_breadth_first_nodes(root)
    non_leaves = [ver for ver in bfs_nodes if not isinstance(ver, Leaf)]
    leaves = [ver for ver in bfs_nodes if isinstance(ver, Leaf)]
    n = len(non_leaves)
    res = []
    count = pow(2, n)
    for i in range(count):
        mask = []
        for j in range(n):
            if i & (1 << j) > 0:
                mask.append(non_leaves[j])
        mask.extend(leaves)
        res.append(mask)
    return res


def get_subtree_from_mask(root, mask):
    nodes = []
    stack = [root]
    while stack:
        cur_node = stack[0]
        stack = stack[1:]
        if cur_node not in mask:
            nodes.append(cur_node)
            for child in reversed(cur_node.children):
                stack.insert(0, child)
    return nodes


def get_all_subtrees(tree):
    res = []
    nonleaves = [ver for ver in tree.bfs_nodes if not isinstance(ver, Leaf)]
    for root in nonleaves:
        masks = get_vertex_masks(root)
        for mask in masks:
            subtree = get_subtree_from_mask(root, mask)
            if subtree not in res and subtree:
                res.append(subtree)
    return res


def get_subtrees(tree):
    result = []
    subtree_set_list = get_all_subtrees(tree)
    for st in subtree_set_list:
        border = get_border(st)
        separated_subtree = separate_subtree(st, tree)
        normal_subtree, relabelling_dict = normalize_subtree(separated_subtree)
        subtree = ColoredSubtree(st, separated_subtree, normal_subtree, relabelling_dict, border)
        result.append(subtree)
    return result


# The following are printing functions, mainly used for debugging.


def print_vertex(vertex):
    print('\t', vertex)
    print('\t parent:', vertex.parent)
    print('\t children:')
    for child in vertex.children:
        print('\t \t', child.label)


def print_tree(tree):
    print('Tree with ', len(tree.bfs_nodes), ' vertices, degree = ', tree.arity)
    root = tree.root
    bfs_nodes = get_breadth_first_nodes(root)
    for i, node in enumerate(bfs_nodes):
        print('\t node #', i)
        if not isinstance(node, Leaf):
            print_vertex(node)


def print_subtree(subtree):
    print('Subtree on vertices:')
    for ver in subtree.subtree_set:
        print('\t', ver)
    print('Separated subtree:')
    print_tree(subtree.separated_subtree)
    print('Normal subtree:')
    print_tree(subtree.normal_subtree)
    print('Relabelling dict:', subtree.relabelling_dict)
    print('Border:')
    print(*subtree.border)


# The following is a function of utmost importance -- grafting of two trees.


def graft(bottom_tree_source, top_tree_source, position, shuffle=Permutation()):
    bottom_tree = copy.deepcopy(bottom_tree_source)
    top_tree = copy.deepcopy(top_tree_source)
    n = bottom_tree.arity
    m = top_tree.arity

    # finding target leaf
    target_leaf = None
    for leaf in bottom_tree.leaves:
        if leaf.label == position:
            target_leaf = leaf
    parent_of_target_leaf = target_leaf.parent
    if parent_of_target_leaf.input_colors[target_leaf.index_in_parent - 1] != top_tree.root.output_color:
        print('Grafting ERROR for: ', bottom_tree, top_tree, position, shuffle)
        raise ValueError('Input/output colouring mismatch!')

    # refactor min descendant for vertices in the top tree:
    top_tree_nodes = top_tree.bfs_nodes
    for node in top_tree_nodes:
        node.min_descendant_list = [x + position - 1 for x in node.min_descendant_list]

    # refactor min descendant for vertices in the bottom tree:
    bottom_tree_nodes = bottom_tree.bfs_nodes
    for node in bottom_tree_nodes:
        # print('node:', node)
        # print('grafting position=', position)
        for bla, descendant in enumerate(node.min_descendant_list):
            if descendant > position:
                # print('changing')
                node.min_descendant_list[bla] = descendant + m - 1
                # print('new node:', node)

    # get new list of leaves:
    new_leaves = []
    for leaf in bottom_tree.leaves:
        if leaf.label == position:
            for top_leaf in top_tree.leaves:
                top_leaf.label = top_leaf.label + position - 1
                new_leaves.append(top_leaf)
        elif leaf.label < position:
            new_leaves.append(leaf)
        else:
            leaf.label = leaf.label + m - 1
            new_leaves.append(leaf)
    bottom_tree.leaves = new_leaves

    # get new leaves numeration
    new_leaves_numeration_ingot = [leaf.label for leaf in new_leaves]
    new_leaves_numeration = [shuffle(i) for i in new_leaves_numeration_ingot]
    relabel(bottom_tree.leaves, new_leaves_numeration)

    # grafting:
    parent_of_target_leaf.children[target_leaf.index_in_parent - 1] = top_tree.root
    top_tree.root.parent = parent_of_target_leaf
    top_tree.root.index_in_parent = target_leaf.index_in_parent

    # housekeeping:
    bottom_tree.bfs_nodes = get_breadth_first_nodes(bottom_tree.root)
    bottom_tree.subtree_markings_for_bfs_nodes = [False] * len(bottom_tree.bfs_nodes)
    bottom_tree.arity = n + m - 1

    # need to relabel min desc lists:
    for node in bottom_tree.bfs_nodes:
        if not isinstance(node, Leaf):
            node.min_descendant_list = [shuffle(x) for x in node.min_descendant_list]

    # computing new list of subtrees:
    bottom_tree.list_of_subtrees = get_subtrees(bottom_tree)

    return bottom_tree
