"""
This file computes the set of small common multiples of two colored trees.
"""

from basic import *
from m_alpha_beta import MOperation, SeqMOperation, get_seq_of_m


def overlapping_possible(small_tree, big_tree, small_tree_vertex, big_tree_vertex, log):
    if isinstance(small_tree_vertex, Leaf):
        return True
    # log has type SeqMOperation
    if isinstance(big_tree_vertex, Leaf):
        small_tree_sprout_set = [x for x in get_depth_first_nodes(small_tree_vertex) if not isinstance(x, Leaf)]
        small_tree_sprout_subtree = small_tree.find_subtree_by_set(small_tree_sprout_set)
        big_tree = graft(big_tree, small_tree_sprout_subtree.normal_subtree, big_tree_vertex.label)
        cosprout_set = [x for x in big_tree.bfs_nodes if not isinstance(x, Leaf) and x not in small_tree_sprout_set]
        cosprout_subtree = big_tree.find_subtree_by_set(cosprout_set)
        log.extend(get_seq_of_m(big_tree, cosprout_subtree))
        return True
    else:
        if small_tree_vertex.label != big_tree_vertex.label:
            return False
        else:
            for i in range(len(big_tree_vertex.children)):
                small_tree_child = small_tree_vertex.children[i]
                big_tree_child = big_tree_vertex.children[i]
                if not overlapping_possible(small_tree, big_tree, small_tree_child, big_tree_child, log):
                    return False
            return True


def get_list_of_gammas(small_tree_source, big_tree_source):
    result = []
    small_tree = copy.deepcopy(small_tree_source)
    big_tree = copy.deepcopy(big_tree_source)
    small_tree_root = small_tree.root
    for node in big_tree.bfs_nodes:
        if node.label == small_tree_root.label:
            log = SeqMOperation()
            if overlapping_possible(small_tree, big_tree, small_tree_root, node, log):
                result.append(log.apply_to_tree(big_tree))
    return result
