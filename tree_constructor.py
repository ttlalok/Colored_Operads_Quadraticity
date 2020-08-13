"""
This file contains functions for easier tree construction.
"""

from basic import *


def right_tree_constructor(lvl1_generator, lvl2_generator):
    """

    :param lvl1_generator: The type of vertex for the first level generator (closest to the root).
    :param lvl2_generator: The type of vertex for the second level generator.
    :return: A quadratic tree with three leaves labelled (1, 2, 3), growing rightwards.
    """
    assert isinstance(lvl1_generator, TypeOfVertex), 'The first generator should be an instance of TypeOfVertex'
    assert isinstance(lvl2_generator, TypeOfVertex), 'The second generator should be an instance of TypeOfVertex'
    return graft(lvl1_generator.create_corolla(), lvl2_generator.create_corolla(), 2)


def left_tree_constructor(lvl1_generator, lvl2_generator):
    """

    :param lvl1_generator: The type of vertex for the first level generator (closest to the root).
    :param lvl2_generator: The type of vertex for the second level generator.
    :return: A quadratic tree with three leaves labelled (1, 2, 3), growing leftwards.
    """
    assert isinstance(lvl1_generator, TypeOfVertex), 'The first generator should be an instance of TypeOfVertex'
    assert isinstance(lvl2_generator, TypeOfVertex), 'The second generator should be an instance of TypeOfVertex'
    return graft(lvl1_generator.create_corolla(), lvl2_generator.create_corolla(), 1)


def perm_left_tree_constructor(lvl1_generator, lvl2_generator):
    """

    :param lvl1_generator: The type of vertex for the first level generator (closest to the root).
    :param lvl2_generator: The type of vertex for the second level generator.
    :return: A quadratic tree with three leaves labelled (1, 3, 2), growing leftwards.
    """
    assert isinstance(lvl1_generator, TypeOfVertex), 'The first generator should be an instance of TypeOfVertex'
    assert isinstance(lvl2_generator, TypeOfVertex), 'The second generator should be an instance of TypeOfVertex'
    return graft(lvl1_generator.create_corolla(), lvl2_generator.create_corolla(), 1, Permutation(1, 3, 2))


def tern_balanced_tree_constructor(lvl1_generator, lvl2_left_generator, lvl2_right_generator, leaf_labels):
    """

    :param lvl1_generator: The type of vertex for the first level generator (closest to the root).
    :param lvl2_left_generator: The type of vertex for the left second level generator.
    :param lvl2_right_generator: The type of vertex for the right second level generator.
    :param leaf_labels: The labelling of the leaves (should be of length 4).
    :return: A ternary Y-shaped tree.
    """
    assert isinstance(lvl1_generator, TypeOfVertex), 'The first generator should be an instance of TypeOfVertex'
    assert isinstance(lvl2_left_generator, TypeOfVertex), 'The second generator should be an instance of TypeOfVertex'
    assert isinstance(lvl2_right_generator, TypeOfVertex), 'The third generator should be an instance of TypeOfVertex'
    return graft(left_tree_constructor(lvl1_generator, lvl2_left_generator), lvl2_right_generator.create_corolla(), 3,
                 Permutation(*leaf_labels))
