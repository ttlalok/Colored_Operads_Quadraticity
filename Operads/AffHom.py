from quadraticity import *
from tree_constructor import left_tree_constructor, perm_left_tree_constructor, right_tree_constructor

B_type = TypeOfVertex('B', [0, 0], 0)
m_type = TypeOfVertex('m', [0, 1], 1)
n_type = TypeOfVertex('n', [1, 0], 1)
i_type = TypeOfVertex('i', [0], 1)


lie_tree1 = left_tree_constructor(B_type, B_type)
lie_tree2 = perm_left_tree_constructor(B_type, B_type)
lie_tree3 = right_tree_constructor(B_type, B_type)
lie_poly = TreePolynomial([lie_tree1, lie_tree2, lie_tree3], [1, -1, -1])
lie_rel = GroebnerRelation(lie_poly, 0, 'Lie')

lie = GroebnerBasis([lie_rel])


# AH-1:
aha1_tree1 = left_tree_constructor(m_type, B_type)
aha1_tree2 = right_tree_constructor(m_type, m_type)
aha1_tree3 = perm_left_tree_constructor(n_type, m_type)
aha1_poly = TreePolynomial([aha1_tree1, aha1_tree2, aha1_tree3], [1, 1, -1])
aha1_rel = GroebnerRelation(aha1_poly, 0, 'AH1-1')

aha2_tree1 = left_tree_constructor(m_type, B_type)
aha2_tree2 = perm_left_tree_constructor(n_type, m_type)
aha2_tree3 = right_tree_constructor(m_type, m_type)
aha2_poly = TreePolynomial([aha2_tree1, aha2_tree2, aha2_tree3], [-1, 1, -1])
aha2_rel = GroebnerRelation(aha2_poly, 0, 'AH1-2')

aha3_tree1 = right_tree_constructor(n_type, B_type)
aha3_tree2 = left_tree_constructor(n_type, n_type)
aha3_tree3 = perm_left_tree_constructor(n_type, n_type)
aha3_poly = TreePolynomial([aha3_tree1, aha3_tree2, aha3_tree3], [-1, 1, -1])
aha3_rel = GroebnerRelation(aha3_poly, 0, 'AH1-3')

aha4_tree1 = perm_left_tree_constructor(m_type, B_type)
aha4_tree2 = right_tree_constructor(m_type, n_type)
aha4_tree3 = left_tree_constructor(n_type, m_type)
aha4_poly = TreePolynomial([aha4_tree1, aha4_tree2, aha4_tree3], [1, 1, -1])
aha4_rel = GroebnerRelation(aha4_poly, 0, 'AH1-4')

aha5_tree1 = right_tree_constructor(n_type, B_type)
aha5_tree2 = perm_left_tree_constructor(n_type, n_type)
aha5_tree3 = left_tree_constructor(n_type, n_type)
aha5_poly = TreePolynomial([aha5_tree1, aha5_tree2, aha5_tree3], [1, 1, -1])
aha5_rel = GroebnerRelation(aha5_poly, 0, 'AH1-5')

aha6_tree1 = perm_left_tree_constructor(m_type, B_type)
aha6_tree2 = left_tree_constructor(n_type, m_type)
aha6_tree3 = right_tree_constructor(m_type, n_type)
aha6_poly = TreePolynomial([aha6_tree1, aha6_tree2, aha6_tree3], [-1 , 1, -1])
aha6_rel = GroebnerRelation(aha6_poly, 0, 'AH1-6')

aha = GroebnerBasis([aha1_rel, aha2_rel, aha3_rel, aha4_rel, aha5_rel, aha6_rel])


# AH-2:

ahb_tree1 = graft(i_type.create_corolla(), B_type.create_corolla(), 1)
ahb_tree2 = graft(m_type.create_corolla(), i_type.create_corolla(), 2)
ahb_tree3 = graft(n_type.create_corolla(), i_type.create_corolla(), 1)
ahb_poly = TreePolynomial([ahb_tree1, ahb_tree2, ahb_tree3], [1, 1, -1])
ahb_rel = GroebnerRelation(ahb_poly, 0, 'AH2')

ahb = GroebnerBasis([ahb_rel])


# main

basis = GroebnerBasis()
basis.merge_bases(lie)
basis.merge_bases(aha)
basis.merge_bases(ahb)

quadraticity_check(basis, 'AffHom_log.tex')
