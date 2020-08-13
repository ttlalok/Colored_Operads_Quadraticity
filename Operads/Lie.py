from quadraticity import *
from tree_constructor import left_tree_constructor, perm_left_tree_constructor, right_tree_constructor


# Generators

B_type = TypeOfVertex('B', [1, 1], 1)


# Relations

lie_tree1 = left_tree_constructor(B_type, B_type)
lie_tree2 = perm_left_tree_constructor(B_type, B_type)
lie_tree3 = right_tree_constructor(B_type, B_type)
lie_poly = TreePolynomial([lie_tree1, lie_tree2, lie_tree3], [1, -1, -1])
lie_rel = GroebnerRelation(lie_poly, 0, 'Lie')

lie = GroebnerBasis([lie_rel])

# main

basis = GroebnerBasis()
basis.merge_bases(lie)

quadraticity_check(basis, 'Lie_log.tex')
