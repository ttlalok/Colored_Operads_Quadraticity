from quadraticity import *
from tree_constructor import left_tree_constructor, perm_left_tree_constructor, right_tree_constructor

a_type = TypeOfVertex('a', [0, 0], 0)

# Com:
com1_tree1 = left_tree_constructor(a_type, a_type)
com1_tree2 = perm_left_tree_constructor(a_type, a_type)
com1_poly = TreePolynomial([com1_tree1, com1_tree2], [1, -1])
com1_rel = GroebnerRelation(com1_poly, 1, 'Com1')

com2_tree1 = left_tree_constructor(a_type, a_type)
com2_tree2 = right_tree_constructor(a_type, a_type)
com2_poly = TreePolynomial([com2_tree1, com2_tree2], [1, -1])
com2_rel = GroebnerRelation(com2_poly, 1, 'Com2')

com = GroebnerBasis([com1_rel, com2_rel])


# main

basis = GroebnerBasis()
basis.merge_bases(com)

quadraticity_check(basis, 'Com_log.tex')
