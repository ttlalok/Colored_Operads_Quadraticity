from quadraticity import *
from tree_constructor import *

# Generators:
i_type = TypeOfVertex('i', [1], 0)
a_type = TypeOfVertex('a', [0, 0], 0)
l_type = TypeOfVertex('l', [0, 1], 1)
r_type = TypeOfVertex('r', [1, 0], 1)

# Relations:
# Com:
com1_tree1 = left_tree_constructor(a_type, a_type)
com1_tree2 = right_tree_constructor(a_type, a_type)
com1_poly = TreePolynomial([com1_tree1, com1_tree2], [1, -1])
com1_rel = GroebnerRelation(com1_poly, 0, 'Com1')

com2_tree1 = perm_left_tree_constructor(a_type, a_type)
com2_tree2 = right_tree_constructor(a_type, a_type)
com2_poly = TreePolynomial([com2_tree1, com2_tree2],[1, -1])
com2_rel = GroebnerRelation(com2_poly, 0, 'Com2')

com = GroebnerBasis([com1_rel, com2_rel])


# MulA

mula1_tree1 = left_tree_constructor(r_type, r_type)
mula1_tree2 = perm_left_tree_constructor(r_type, r_type)
mula1_poly = TreePolynomial([mula1_tree1, mula1_tree2], [1, -1])
mula1_rel = GroebnerRelation(mula1_poly, 0, 'MulA1')

mula2_tree1 = left_tree_constructor(r_type, l_type)
mula2_tree2 = right_tree_constructor(l_type, r_type)
mula2_poly = TreePolynomial([mula2_tree1, mula2_tree2], [1, -1])
mula2_rel = GroebnerRelation(mula2_poly, 0, 'MulA2')

mula3_tree1 = right_tree_constructor(l_type, l_type)
mula3_tree2 = perm_left_tree_constructor(r_type, l_type)
mula3_poly = TreePolynomial([mula3_tree1, mula3_tree2], [1, -1])
mula3_rel = GroebnerRelation(mula3_poly, 1, 'MulA3')

mula = GroebnerBasis([mula1_rel, mula2_rel, mula3_rel])

# MulB

mulb1_tree1 = perm_left_tree_constructor(r_type, r_type)
mulb1_tree2 = right_tree_constructor(r_type, a_type)
mulb1_poly = TreePolynomial([mulb1_tree1, mulb1_tree2], [1, -1])
mulb1_rel = GroebnerRelation(mulb1_poly, 0, 'MulB1')

mulb2_tree1 = right_tree_constructor(l_type, r_type)
mulb2_tree2 = perm_left_tree_constructor(l_type, a_type)
mulb2_poly = TreePolynomial([mulb2_tree1, mulb2_tree2], [1, -1])
mulb2_rel = GroebnerRelation(mulb2_poly, 1, 'MulB2')

mulb3_tree1 = left_tree_constructor(r_type, r_type)
mulb3_tree2 = right_tree_constructor(r_type, a_type)
mulb3_poly = TreePolynomial([mulb3_tree1, mulb3_tree2], [1, -1])
mulb3_rel = GroebnerRelation(mulb3_poly, 0, 'MulB3')

mulb4_tree1 = perm_left_tree_constructor(r_type, l_type)
mulb4_tree2 = left_tree_constructor(l_type, a_type)
mulb4_poly = TreePolynomial([mulb4_tree1, mulb4_tree2],[1, -1])
mulb4_rel = GroebnerRelation(mulb4_poly, 0, 'MulB4')

mulb5_tree1 = left_tree_constructor(r_type, l_type)
mulb5_tree2 = perm_left_tree_constructor(l_type, a_type)
mulb5_poly = TreePolynomial([mulb5_tree1, mulb5_tree2], [1, -1])
mulb5_rel = GroebnerRelation(mulb5_poly, 0, 'MulB5')

mulb6_tree1 = right_tree_constructor(l_type, l_type)
mulb6_tree2 = left_tree_constructor(l_type, a_type)
mulb6_poly = TreePolynomial([mulb6_tree1, mulb6_tree2], [1, -1])
mulb6_rel = GroebnerRelation(mulb6_poly, 1, 'MulB6')

mulb = GroebnerBasis([mulb1_rel, mulb2_rel, mulb3_rel, mulb4_rel, mulb5_rel, mulb6_rel])

# InA

ina1_tree1 = graft(a_type.create_corolla(), i_type.create_corolla(), 1)
ina1_tree2 = graft(i_type.create_corolla(), r_type.create_corolla(), 1)
ina1_poly = TreePolynomial([ina1_tree1, ina1_tree2], [1, -1])
ina1_rel = GroebnerRelation(ina1_poly, 1, 'InA1')

ina2_tree1 = graft(a_type.create_corolla(), i_type.create_corolla(), 2)
ina2_tree2 = graft(i_type.create_corolla(), l_type.create_corolla(), 1)
ina2_poly = TreePolynomial([ina2_tree1, ina2_tree2], [1, -1])
ina2_rel = GroebnerRelation(ina2_poly, 1, 'InA2')

ina = GroebnerBasis([ina1_rel, ina2_rel])

# InB

inb1_tree1 = graft(r_type.create_corolla(), i_type.create_corolla(), 2)
inb1_tree2 = graft(l_type.create_corolla(), i_type.create_corolla(), 1)
inb1_poly = TreePolynomial([inb1_tree1, inb1_tree2], [1, -1])
inb1_rel = GroebnerRelation(inb1_poly, 1, 'InB')

inb = GroebnerBasis([inb1_rel])


# main

basis = GroebnerBasis()
basis.merge_bases(com)
basis.merge_bases(mula)
basis.merge_bases(mulb)
basis.merge_bases(ina)
basis.merge_bases(inb)

quadraticity_check(basis, 'ICom_log.tex')
