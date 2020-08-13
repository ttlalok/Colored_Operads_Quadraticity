from quadraticity import *
from tree_constructor import left_tree_constructor, perm_left_tree_constructor, right_tree_constructor


# Generators:
a_type = TypeOfVertex('\\alpha', [0, 0], 0)
d_type = TypeOfVertex('d', [0, 1], 0)
e_type = TypeOfVertex('e', [1, 0], 0)

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

# Leib:
leib1_tree1 = right_tree_constructor(e_type, a_type)
leib1_tree2 = left_tree_constructor(a_type, e_type)
leib1_tree3 = perm_left_tree_constructor(a_type, e_type)
leib1_poly =TreePolynomial([leib1_tree1, leib1_tree2, leib1_tree3], [1, -1, -1])
leib1_rel = GroebnerRelation(leib1_poly, 0, 'Leib1')

leib2_tree1 = perm_left_tree_constructor(d_type, a_type)
leib2_tree2 = left_tree_constructor(a_type, d_type)
leib2_tree3 = right_tree_constructor(a_type, e_type)
leib2_poly = TreePolynomial([leib2_tree1, leib2_tree2, leib2_tree3], [1, -1, -1])
leib2_rel = GroebnerRelation(leib2_poly, 0, 'Leib2')

leib3_tree1 = left_tree_constructor(d_type, a_type)
leib3_tree2 = right_tree_constructor(a_type, d_type)
leib3_tree3 = perm_left_tree_constructor(a_type, d_type)
leib3_poly = TreePolynomial([leib3_tree1, leib3_tree2, leib3_tree3], [1, -1, -1])
leib3_rel = GroebnerRelation(leib3_poly, 0, 'Leib3')

leib = GroebnerBasis([leib1_rel, leib2_rel, leib3_rel])


# main

basis = GroebnerBasis()  # Create a blank GroebnerBasis object
basis.merge_bases(com)
basis.merge_bases(leib)

quadraticity_check(basis, 'DCom_log.tex')
