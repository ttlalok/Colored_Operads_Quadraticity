"""
This is the main file. It answers the question whether the given Groebner basis has non-trivial S-polynomials.
"""

import sys
from itertools import product, combinations

from groebner_basis import *
from s_poly import get_s_polys


def quadraticity_check(basis, log_file_name='quadraticity_log.tex', full_s_list=False):
    """
    WARNING: The function OVERWRITES the file log_file_name.

    :param basis: Groebner basis
    :param log_file_name: The name of of .tex file, where the log of all performed reduction will be kept.
                          The file is overwritten.
                          The name of the file should end in .tex .
    :param full_s_list: Boolean. If TRUE the full list of S-polynomials will be computed.
                                 If FALSE the program will stop after finding the first non-trivial S-polynomial.
    :return: quadraticity value (TRUE if basis has no non-trivial S-polynomials) and a list of S-polynomials found.
             If full_s_list is FALSE, the list will contain only the first non-trivial S-polynomial found.
    """

    log = ['\\documentclass[11pt]{amsart} \n \n \\begin{document} \n \n', 'The shuffle operad has the following relations: \n',
           basis.basis_to_latex(), '\n \n \n List of reductions: \n \n']

    s_dict = dict()
    print('Quadraticity check')
    quadratic = True
    for relation1, relation2 in combinations(basis.relations, 2):
        print('Computing S-poly\'s for ' + relation1.label + ' and ' + relation2.label)
        s_polys, gammas = get_s_polys(relation1, relation2)
        for i, poly in enumerate(s_polys):
            log.append(
                '\\begin{align*} \n' + '& \\text{Reducing S-polynomial for relations ' + relation1.label + ' and ' + relation2.label + ':} \\\\ \n')
            log.append('& \\gamma = ' + tree_to_latex(gammas[i]) + ' \\\\ \n')
            log.append('& \\text{Reduction}: \\\\')
            s_poly_after_reduction = basis.reduce_poly(poly, log)
            log.append('\\end{align*} \n \n')
            if s_poly_after_reduction:
                if not full_s_list:
                    print('NON ZERO S-pol FOUND: ', poly)
                    print('for ', relation1.label, ' and ', relation2.label)
                    quadratic = False

                    lbl = relation1.label + ' ' + relation2.label
                    s_dict[lbl] = [s_poly_after_reduction]

                    break
                else:
                    lbl = relation1.label + ' ' + relation2.label
                    if lbl in s_dict:
                        if s_poly_after_reduction not in s_dict[lbl]:
                            s_dict[lbl].append(s_poly_after_reduction)
                    else:
                        s_dict[lbl] = [s_poly_after_reduction]
        if not quadratic:
            print('NOT QUADRATIC')
            break
        print('\n')

    quadratic = not s_dict
    log.append('\n Quadratic: ')
    log.append(str(quadratic))

    if s_dict:
        log.append('\n \n S-polynomials found: \n')
        for label, spoly_list in s_dict.items():
            log.append('\\begin{align*} \n')
            for spoly in spoly_list:
                log.append('& \\text{S-polynomial for relations ' + label + ':} \\\\ \n')
                log.append('&' + poly_to_latex(spoly) + ' \\\\ \n')
            log.append('\\end{align*}')

    log.append('\n \\end{document}')

    log_text = ''
    for item in log:
        log_text += item

    old_target = sys.stdout
    sys.stdout = open(log_file_name, 'w')
    print(log_text)
    sys.stdout = old_target

    print('QUADRATIC:', quadratic)
    return quadratic, s_dict
