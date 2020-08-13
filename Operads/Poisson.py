"""
This is classical version of Poisson algebras, with associative (but not commutative) operation a,
and Lie bracket B.
"""

from quadraticity import *
from tree_constructor import left_tree_constructor, perm_left_tree_constructor, right_tree_constructor

# Generators:
a_type = TypeOfVertex('a', [0, 0], 0)
b_type = TypeOfVertex('b', [0, 0], 0)
B_type = TypeOfVertex('B', [0, 0], 0)


# As
arel1_tree1 = left_tree_constructor(a_type, a_type)
arel1_tree2 = right_tree_constructor(a_type, a_type)
arel1_poly = TreePolynomial([arel1_tree1, arel1_tree2], [1, -1])
arel1_rel = GroebnerRelation(arel1_poly, 1, 'ARel-1')

arel2_tree1 = left_tree_constructor(a_type, b_type)
arel2_tree2 = perm_left_tree_constructor(b_type, a_type)
arel2_poly = TreePolynomial([arel2_tree1, arel2_tree2], [1, -1])
arel2_rel = GroebnerRelation(arel2_poly, 1, 'ARel-2')

arel3_tree1 = right_tree_constructor(b_type, b_type)
arel3_tree2 = left_tree_constructor(b_type, b_type)
arel3_poly = TreePolynomial([arel3_tree1, arel3_tree2], [1, -1])
arel3_rel = GroebnerRelation(arel3_poly, 0, 'ARel-3')

arel4_tree1 = perm_left_tree_constructor(a_type, a_type)
arel4_tree2 = right_tree_constructor(a_type, b_type)
arel4_poly = TreePolynomial([arel4_tree1, arel4_tree2], [1, -1])
arel4_rel = GroebnerRelation(arel4_poly, 1, 'ARel-4')

arel5_tree1 = right_tree_constructor(b_type, a_type)
arel5_tree2 = perm_left_tree_constructor(b_type, b_type)
arel5_poly = TreePolynomial([arel5_tree1, arel5_tree2], [1, -1])
arel5_rel = GroebnerRelation(arel5_poly, 0, 'ARel-5')

arel6_tree1 = perm_left_tree_constructor(a_type, b_type)
arel6_tree2 = left_tree_constructor(b_type, a_type)
arel6_poly = TreePolynomial([arel6_tree1, arel6_tree2], [1, -1])
arel6_rel = GroebnerRelation(arel6_poly, 1, 'ARel-6')

arel = GroebnerBasis([arel1_rel, arel2_rel, arel3_rel, arel4_rel, arel5_rel, arel6_rel])


# Lie:
lie_tree1 = left_tree_constructor(B_type, B_type)
lie_tree2 = perm_left_tree_constructor(B_type, B_type)
lie_tree3 = right_tree_constructor(B_type, B_type)
lie_poly = TreePolynomial([lie_tree1, lie_tree2, lie_tree3], [1, -1, -1])
lie_rel = GroebnerRelation(lie_poly, 0, 'Lie')

lie = GroebnerBasis([lie_rel])


# Poisson
pois1_tree1 = right_tree_constructor(B_type, a_type)
pois1_tree2 = left_tree_constructor(a_type, B_type)
pois1_tree3 = perm_left_tree_constructor(b_type, B_type)
pois1_poly = TreePolynomial([pois1_tree1, pois1_tree2, pois1_tree3], [1, -1, -1])
pois1_rel = GroebnerRelation(pois1_poly, 1, 'Pois-1')

pois2_tree1 = perm_left_tree_constructor(B_type, a_type)
pois2_tree2 = left_tree_constructor(a_type, B_type)
pois2_tree3 = right_tree_constructor(a_type, B_type)
pois2_poly = TreePolynomial([pois2_tree1, pois2_tree2, pois2_tree3], [-1, 1, -1])
pois2_rel = GroebnerRelation(pois2_poly, 1, 'Pois-2')

pois3_tree1 = left_tree_constructor(B_type, b_type)
pois3_tree2 = right_tree_constructor(b_type, B_type)
pois3_tree3 = perm_left_tree_constructor(b_type, B_type)
pois3_poly = TreePolynomial([pois3_tree1, pois3_tree2, pois3_tree3], [-1, 1, 1])
pois3_rel = GroebnerRelation(pois3_poly, 0, 'Pois-3')

pois4_tree1 = right_tree_constructor(B_type, b_type)
pois4_tree2 = perm_left_tree_constructor(a_type, B_type)
pois4_tree3 = left_tree_constructor(b_type, B_type)
pois4_poly = TreePolynomial([pois4_tree1, pois4_tree2, pois4_tree3], [1, -1, -1])
pois4_rel = GroebnerRelation(pois4_poly, 2, 'Pois-4')

pois5_tree1 = perm_left_tree_constructor(B_type, b_type)
pois5_tree2 = right_tree_constructor(b_type, B_type)
pois5_tree3 = left_tree_constructor(b_type, B_type)
pois5_poly = TreePolynomial([pois5_tree1, pois5_tree2, pois5_tree3], [-1, -1, 1])
pois5_rel = GroebnerRelation(pois5_poly, 0, 'Pois-5')

pois6_tree1 = left_tree_constructor(B_type, a_type)
pois6_tree2 = perm_left_tree_constructor(a_type, B_type)
pois6_tree3 = right_tree_constructor(a_type, B_type)
pois6_poly = TreePolynomial([pois6_tree1, pois6_tree2, pois6_tree3], [-1, 1, 1])
pois6_rel = GroebnerRelation(pois6_poly, 0, 'Pois-6')

pois = GroebnerBasis([pois1_rel, pois2_rel, pois3_rel, pois4_rel, pois5_rel, pois6_rel])


basis = GroebnerBasis()
basis.merge_bases(arel)
basis.merge_bases(lie)
basis.merge_bases(pois)

quadraticity_check(basis, 'Poisson_log.tex', full_s_list=True)
