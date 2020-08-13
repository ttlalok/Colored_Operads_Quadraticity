from quadraticity import *
from tree_constructor import left_tree_constructor, perm_left_tree_constructor, right_tree_constructor


# Generators:

a_type = TypeOfVertex('\\alpha', [0, 0], 0)
B_type = TypeOfVertex('\\beta', [1, 1], 1)
d_type = TypeOfVertex('d', [0, 1], 0)
e_type = TypeOfVertex('e', [1, 0], 0)
m_type = TypeOfVertex('m', [0, 1], 1)
n_type = TypeOfVertex('n', [1, 0], 1)

# Relations:

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

# Lie:
lie_tree1 = left_tree_constructor(B_type, B_type)
lie_tree2 = perm_left_tree_constructor(B_type, B_type)
lie_tree3 = right_tree_constructor(B_type, B_type)
lie_poly = TreePolynomial([lie_tree1, lie_tree2, lie_tree3], [1, -1, -1])
lie_rel = GroebnerRelation(lie_poly, 0, 'Lie')

lie = GroebnerBasis([lie_rel])

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

# Mor:
mor1_tree1 = right_tree_constructor(d_type, B_type)
mor1_tree2 = left_tree_constructor(d_type, d_type)
mor1_tree3 = perm_left_tree_constructor(d_type, d_type)
mor1_poly = TreePolynomial([mor1_tree1, mor1_tree2, mor1_tree3], [1, 1, -1])
mor1_rel = GroebnerRelation(mor1_poly, 0, 'Mor1')

mor2_tree1 = perm_left_tree_constructor(e_type, B_type)
mor2_tree2 = left_tree_constructor(d_type, e_type)
mor2_tree3 = right_tree_constructor(e_type, d_type)
mor2_poly = TreePolynomial([mor2_tree1, mor2_tree2, mor2_tree3], [1, 1, -1])
mor2_rel = GroebnerRelation(mor2_poly, 0, 'Mor2')

mor3_tree1 = right_tree_constructor(d_type, B_type)
mor3_tree2 = perm_left_tree_constructor(d_type, d_type)
mor3_tree3 = left_tree_constructor(d_type, d_type)
mor3_poly = TreePolynomial([mor3_tree1, mor3_tree2, mor3_tree3], [-1, 1, -1])
mor3_rel = GroebnerRelation(mor3_poly, 0, 'Mor3')

mor4_tree1 = left_tree_constructor(e_type, B_type)
mor4_tree2 = right_tree_constructor(e_type, e_type)
mor4_tree3 = perm_left_tree_constructor(d_type, e_type)
mor4_poly = TreePolynomial([mor4_tree1, mor4_tree2, mor4_tree3], [-1, 1, -1])
mor4_rel = GroebnerRelation(mor4_poly, 0, 'Mor4')

mor5_tree1 = perm_left_tree_constructor(e_type, B_type)
mor5_tree2 = right_tree_constructor(e_type, d_type)
mor5_tree3 = left_tree_constructor(d_type, e_type)
mor5_poly = TreePolynomial([mor5_tree1, mor5_tree2, mor5_tree3], [-1, 1, -1])
mor5_rel = GroebnerRelation(mor5_poly, 0, 'Mor5')

mor6_tree1 = left_tree_constructor(e_type, B_type)
mor6_tree2 = perm_left_tree_constructor(d_type, e_type)
mor6_tree3 = right_tree_constructor(e_type, e_type)
mor6_poly = TreePolynomial([mor6_tree1, mor6_tree2, mor6_tree3], [1, 1, -1])
mor6_rel = GroebnerRelation(mor6_poly, 0, 'Mor6')

mor = GroebnerBasis([mor1_rel, mor2_rel, mor3_rel, mor4_rel, mor5_rel, mor6_rel])

# S-Mod:
smod1_tree1 = left_tree_constructor(m_type, a_type)
smod1_tree2 = right_tree_constructor(m_type, m_type)
smod1_poly = TreePolynomial([smod1_tree1, smod1_tree2], [1, -1])
smod1_rel = GroebnerRelation(smod1_poly, 1, 'SMod1')

smod2_tree1 = left_tree_constructor(m_type, a_type)
smod2_tree2 = perm_left_tree_constructor(n_type, m_type)
smod2_poly = TreePolynomial([smod2_tree1, smod2_tree2], [1, -1])
smod2_rel = GroebnerRelation(smod2_poly, 1, 'SMod2')

smod3_tree1 = perm_left_tree_constructor(m_type, a_type)
smod3_tree2 = right_tree_constructor(m_type, n_type)
smod3_poly = TreePolynomial([smod3_tree1, smod3_tree2], [1, -1])
smod3_rel = GroebnerRelation(smod3_poly, 1, 'SMod3')

smod4_tree1 = right_tree_constructor(n_type, a_type)
smod4_tree2 = left_tree_constructor(n_type, n_type)
smod4_poly = TreePolynomial([smod4_tree1, smod4_tree2], [1, -1])
smod4_rel = GroebnerRelation(smod4_poly, 1, 'SMod4')

smod5_tree1 = right_tree_constructor(n_type, a_type)
smod5_tree2 = perm_left_tree_constructor(n_type, n_type)
smod5_poly = TreePolynomial([smod5_tree1, smod5_tree2], [1, -1])
smod5_rel = GroebnerRelation(smod5_poly, 1, 'SMod5')

smod6_tree1 = perm_left_tree_constructor(m_type, a_type)
smod6_tree2 = left_tree_constructor(n_type, m_type)
smod6_poly = TreePolynomial([smod6_tree1, smod6_tree2], [1, -1])
smod6_rel = GroebnerRelation(smod6_poly, 1, 'SMod6')

smod = GroebnerBasis([smod1_rel, smod2_rel, smod3_rel, smod4_rel, smod5_rel, smod6_rel])

# lra:
lra1_tree1 = left_tree_constructor(e_type, m_type)
lra1_tree2 = right_tree_constructor(a_type, e_type)
lra1_poly = TreePolynomial([lra1_tree1, lra1_tree2], [1, -1])
lra1_rel = GroebnerRelation(lra1_poly, 0, 'LR-A1')

lra2_tree1 = left_tree_constructor(e_type, n_type)
lra2_tree2 = perm_left_tree_constructor(a_type, e_type)
lra2_poly = TreePolynomial([lra2_tree1, lra2_tree2], [1, -1])
lra2_rel = GroebnerRelation(lra2_poly, 0, 'LR-A2')

lra3_tree1 = right_tree_constructor(d_type, n_type)
lra3_tree2 = left_tree_constructor(a_type, d_type)
lra3_poly = TreePolynomial([lra3_tree1, lra3_tree2], [1, -1])
lra3_rel = GroebnerRelation(lra3_poly, 0, 'LR-A3')

lra4_tree1 = perm_left_tree_constructor(e_type, m_type)
lra4_tree2 = right_tree_constructor(a_type, d_type)
lra4_poly = TreePolynomial([lra4_tree1, lra4_tree2], [1, -1])
lra4_rel = GroebnerRelation(lra4_poly, 0, 'LR-A4')

lra5_tree1 = right_tree_constructor(d_type, m_type)
lra5_tree2 = perm_left_tree_constructor(a_type, d_type)
lra5_poly = TreePolynomial([lra5_tree1, lra5_tree2], [1, -1])
lra5_rel = GroebnerRelation(lra5_poly, 0, 'LR-A5')

lra6_tree1 = perm_left_tree_constructor(e_type, n_type)
lra6_tree2 = left_tree_constructor(a_type, e_type)
lra6_poly = TreePolynomial([lra6_tree1, lra6_tree2], [1, -1])
lra6_rel = GroebnerRelation(lra6_poly, 0, 'LR-A6')

lra = GroebnerBasis([lra1_rel, lra2_rel, lra3_rel, lra4_rel, lra5_rel, lra6_rel])

# LR-B (LR2):
lrb1_tree1 = right_tree_constructor(B_type, m_type)
lrb1_tree2 = left_tree_constructor(m_type, e_type)
lrb1_tree3 = perm_left_tree_constructor(n_type, B_type)
lrb1_poly = TreePolynomial([lrb1_tree1, lrb1_tree2, lrb1_tree3], [1, -1, -1])
lrb1_rel = GroebnerRelation(lrb1_poly, 0, 'LR-B1')

lrb2_tree1 = perm_left_tree_constructor(B_type, m_type)
lrb2_tree2 = left_tree_constructor(m_type, d_type)
lrb2_tree3 = right_tree_constructor(m_type, B_type)
lrb2_poly = TreePolynomial([lrb2_tree1, lrb2_tree2, lrb2_tree3], [-1, -1, -1])
lrb2_rel = GroebnerRelation(lrb2_poly, 0, 'LR-B2')

lrb3_tree1 = left_tree_constructor(B_type, n_type)
lrb3_tree2 = right_tree_constructor(n_type, d_type)
lrb3_tree3 = perm_left_tree_constructor(n_type, B_type)
lrb3_poly = TreePolynomial([lrb3_tree1, lrb3_tree2, lrb3_tree3], [-1, -1, 1])
lrb3_rel = GroebnerRelation(lrb3_poly, 0, 'LR-B3')

lrb4_tree1 = right_tree_constructor(B_type, n_type)
lrb4_tree2 = perm_left_tree_constructor(m_type, e_type)
lrb4_tree3 = left_tree_constructor(n_type, B_type)
lrb4_poly = TreePolynomial([lrb4_tree1, lrb4_tree2, lrb4_tree3], [1, -1, -1])
lrb4_rel = GroebnerRelation(lrb4_poly, 0, 'LR-B4')

lrb5_tree1 = perm_left_tree_constructor(B_type, n_type)
lrb5_tree2 = right_tree_constructor(n_type, e_type)
lrb5_tree3 = left_tree_constructor(n_type, B_type)
lrb5_poly = TreePolynomial([lrb5_tree1, lrb5_tree2, lrb5_tree3], [-1, -1, 1])
lrb5_rel = GroebnerRelation(lrb5_poly, 0, 'LR-B5')

lrb6_tree1 = left_tree_constructor(B_type, m_type)
lrb6_tree2 = perm_left_tree_constructor(m_type, d_type)
lrb6_tree3 = right_tree_constructor(m_type, B_type)
lrb6_poly = TreePolynomial([lrb6_tree1, lrb6_tree2, lrb6_tree3], [-1, -1, 1])
lrb6_rel = GroebnerRelation(lrb6_poly, 0, 'LR-B6')

lrb = GroebnerBasis([lrb1_rel, lrb2_rel, lrb3_rel, lrb4_rel, lrb5_rel, lrb6_rel])


# main

basis = GroebnerBasis()

basis.merge_bases(lrb)
basis.merge_bases(lra)

basis.merge_bases(mor)
basis.merge_bases(smod)

basis.merge_bases(com)
basis.merge_bases(lie)
basis.merge_bases(leib)

quadraticity_check(basis, 'Lie_Rinehart_log.tex')
