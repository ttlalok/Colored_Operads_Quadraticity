"""
This file computes S-polynomials for two Groebner relations
"""

from groebner_basis import *
from overlapping import get_list_of_gammas


def shuffles(n):
    result = []
    for perm in Permutation.group(n):
        L = list(perm.permute(list(range(1, 6))))
        if L[0] == 1:
            result.append(Permutation(*L))
    return result


def get_s_polys(relation1, relation2):
    """
    :param relation1: Groebner relation 1
    :param relation2: Groebner relation 2
    :return: (list of S-polys, list of small common multiples)
    """
    result = []
    gammas = []
    lt1 = relation1.lt
    lc1 = relation1.lt_coeff
    lt2 = relation2.lt
    lc2 = relation2.lt_coeff

    # lt1 = small tree, lt2 = big tree
    list_of_gammas = get_list_of_gammas(lt1, lt2)
    for gamma in list_of_gammas:
        for sh in shuffles(gamma.arity):
            candidate = gamma.relabel_leaves_by_permutation(sh)
            if candidate.is_shuffle_tree() and candidate.is_divisible_by(lt1) and candidate.is_divisible_by(lt2):
                print('Gamma found: ', candidate)
                # computing actual S-pol:
                seq_in_1 = get_seq_of_m(candidate, candidate.find_subtree(lt1))
                seq_in_2 = get_seq_of_m(candidate, candidate.find_subtree(lt2))
                s_pol = seq_in_1.apply_to_poly(relation1.poly) - ((lc1 / lc2) * seq_in_2.apply_to_poly(relation2.poly))
                if s_pol and s_pol not in result and -s_pol not in result:
                    result.append(s_pol)
                    gammas.append(candidate)

    # lt2 = small tree, lt1 = big tree
    list_of_gammas = get_list_of_gammas(lt2, lt1)
    for gamma in list_of_gammas:
        for sh in shuffles(gamma.arity):
            candidate = gamma.relabel_leaves_by_permutation(sh)
            if candidate.is_shuffle_tree() and candidate.is_divisible_by(lt1) and candidate.is_divisible_by(lt2):
                print('Gamma found: ', candidate)
                # computing actual S-pol:
                seq_in_1 = get_seq_of_m(candidate, candidate.find_subtree(lt1))
                seq_in_2 = get_seq_of_m(candidate, candidate.find_subtree(lt2))
                s_pol = seq_in_1.apply_to_poly(relation1.poly) - ((lc1 / lc2) * seq_in_2.apply_to_poly(relation2.poly))
                if s_pol and s_pol not in result and -s_pol not in result:
                    result.append(s_pol)
                    gammas.append(candidate)
    print('S-polys computed:', *result)
    return result, gammas
