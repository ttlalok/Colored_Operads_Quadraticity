from quadraticity import *
from itertools import combinations

#
# class QPVertex:
#     def __init__(self, input, output, isABC):
#         self.label = None
#         self.input = input
#         self.output = output
#
#         self.compositionInputGreater = input[0] > input[1]
#         self.compositionOutputGreater = output[1] > output[0]
#
#         self.isABC = isABC
#         self.isXYZ = not self.isABC
#         if self.isABC:
#             oup = min(output)
#             if oup > max(input):
#                 self.label = 'a'
#             elif oup < min(input):
#                 self.label = 'c'
#             else:
#                 self.label = 'b'
#         if self.isXYZ:
#             inp = min(input)
#             if inp > max(output):
#                 self.label = 'x'
#             elif inp < min(output):
#                 self.label = 'z'
#             else:
#                 self.label = 'y'
#
#     def get_composition_leaf(self):
#         if self.isABC:
#             if self.label == 'a':
#                 if self.compositionInputGreater:
#                     return 2
#                 else:
#                     return 1
#             elif self.label == 'b':
#                 if self.compositionInputGreater:
#                     return 3
#                 else:
#                     return 1
#             elif self.label == 'c':
#                 if self.compositionInputGreater:
#                     return 3
#                 else:
#                     return 2
#         if self.isXYZ:
#             if self.label == 'x':
#                 if self.compositionOutputGreater:
#                     return 2
#                 else:
#                     return 1
#             elif self.label == 'y':
#                 if self.compositionOutputGreater:
#                     return 3
#                 else:
#                     return 1
#             elif self.label == 'z':
#                 if self.compositionOutputGreater:
#                     return 3
#                 else:
#                     return 2
#
#
#
#
#
#         # self.minLeaf = min(min)
#         # for inp in input:
#         #     if not isinstance(inp, QPVertex):
#         #         if inp < self.minLeaf:
#         #             self.minLeaf = inp
#         # for oup in output:
#         #     if not isinstance(oup, QPVertex):
#         #         if oup < self.minLeaf:
#         #             self.minLeaf = oup
#
#
# class QPTree:
#     def __init__(self, input, output):
#         topLeavesProper = [input[0], input[1], output[0]]
#         self.topLeaves = topLeavesProper
#         self.topFreeOutput = output[0]
#         minTopLeaf = min(topLeavesProper)
#         maxTopLeaf = max(topLeavesProper)
#
#         botLeavesProper = [input[2], output[1], output[2]]
#         self.botLeaves = botLeavesProper
#         self.botFreeInput = input[2]
#         minBotLeaf = min(botLeavesProper)
#         maxBotLeaf = max(botLeavesProper)
#
#         self.topIsRoot = maxTopLeaf > maxBotLeaf
#         self.botIsRoot = maxBotLeaf > maxTopLeaf
#
#         self.topIsABC = max(output[0], maxBotLeaf) > max(input[0], input[1])
#         self.botIsABC = max(output[1], output[2]) > max(input[2], maxTopLeaf)
#
#         #self.topVer = QPVertex([input[0], input[1]], [output[0], min(botLeavesProper)], topIsABC)
#         #self.botVer = QPVertex([min(topLeavesProper), input[2]], [output[1], output[2]], botIsABC)
#
#         self.sign = 1
#
#     def get_top_label(self):
#         if self.topIsABC:
#             if self.topFreeOutput == max(self.topLeaves):
#                 return 'a'
#             if self.topFreeOutput == min(self.topLeaves):
#                 return 'c'
#             else:
#                 return 'b'
#         else:
#             if
#
#     def get_comp_slot(self):
#         if self.topIsRoot:
#             return self.topVer.get_composition_leaf()
#         if self.botIsRoot:
#             return self.botVer.get_composition_leaf()
#
#     def get_permutation(self):
#         if self.topIsRoot:
#             nonRootVer = self.botVer
#             rootVer = self.topVer
#             nonRootLeaves = self.botLeaves
#             rootLeaves = self.topLeaves
#         if self.botIsRoot:
#             nonRootVer = self.topVer
#             rootVer = self.botVer
#             nonRootLeaves = self.topLeaves
#             rootLeaves = self.botLeaves
#         slot = self.get_comp_slot()
#         result_list = list()
#         sorted_root_leaves = sorted(rootLeaves)
#         rootLeaf0 = sorted_root_leaves[0]
#         rootLeaf1 = sorted_root_leaves[1]
#         if slot == 1:
#             result_list.extend(sorted(nonRootLeaves))
#             result_list.append(rootLeaf0)
#             result_list.append(rootLeaf1)
#         if slot == 2:
#             result_list.append(rootLeaf0)
#             result_list.extend(sorted(nonRootLeaves))
#             result_list.append(rootLeaf1)
#         if slot == 3:
#             result_list.append(rootLeaf0)
#             result_list.append(rootLeaf1)
#             result_list.extend(sorted(nonRootLeaves))
#         return result_list
#
#
#     def get_decomposition(self):
#         print(self.topVer.label, self.botVer.label, self.get_comp_slot(), self.get_permutation())
#
#
# tr1 = QPTree([6, 3, 1], [4, 2, 5])
# tr1.get_decomposition()
#
# tr2 = QPTree([1, 3, 6], [4, 2, 5])
# tr2.get_decomposition()

gen_dict = {
    'a': TypeOfVertex('a', [0, 0, 1], 1),
    'b': TypeOfVertex('b', [0, 1, 0], 1),
    'c': TypeOfVertex('c', [1, 0, 0], 1),
    'x': TypeOfVertex('x', [1, 1, 0], 0),
    'y': TypeOfVertex('y', [1, 0, 1], 0),
    'z': TypeOfVertex('z', [0, 1, 1], 0)
}


class QPLeaf:
    def __init__(self, color, numbers):
        self.color = color  # 0 for input, 1 for output
        self.numbers = sorted(numbers)
        self.min = min(numbers)
        self.max = max(numbers)

        self.is_root = False

    def is_proper_leaf(self):
        return len(self.numbers) == 1 and not self.is_root


class QPVertex:
    def __init__(self, leaves):
        self.leaves = leaves
        self.inputs = [leaf for leaf in leaves if leaf.color == 0]
        self.outputs = [leaf for leaf in leaves if leaf.color == 1]

        self.proper_min = min([leaf.min for leaf in leaves if leaf.is_proper_leaf()])
        self.proper_max = max([leaf.max for leaf in leaves if leaf.is_proper_leaf()])

        self.max_leaf = sorted(self.leaves, key=lambda x: x.max)[-1]
        self.max_leaf.is_root = True

        self.isABC = None
        self.type = None
        self.set_type()

    def set_type(self):
        self.max_leaf = sorted(self.leaves, key=lambda x: x.max)[-1]
        non_root_leaves = [leaf for leaf in self.leaves if leaf != self.max_leaf]
        sorted_leaves = sorted(non_root_leaves, key=lambda x: x.min)
        color_mask = [leaf.color for leaf in sorted_leaves]
        if self.max_leaf.color == 0:
            self.isABC = False
            if color_mask == [1, 1, 0]:
                self.type = 'x'
            if color_mask == [1, 0, 1]:
                self.type = 'y'
            if color_mask == [0, 1, 1]:
                self.type = 'z'
        if self.max_leaf.color == 1:
            self.isABC = True
            if color_mask == [0, 0, 1]:
                self.type = 'a'
            if color_mask == [0, 1, 0]:
                self.type = 'b'
            if color_mask == [1, 0, 0]:
                self.type = 'c'
        assert (self.type is not None)


class QPTree:
    def __init__(self, inputs, outputs):
        topNumbers = [inputs[0], inputs[1], outputs[0]]
        botNumbers = [inputs[2], outputs[1], outputs[2]]

        topLeaves = [QPLeaf(0, [inputs[0]]),
                     QPLeaf(0, [inputs[1]]),
                     QPLeaf(1, [outputs[0]]),
                     QPLeaf(1, botNumbers)]
        self.topVer = QPVertex(topLeaves)

        botLeaves = [QPLeaf(0, topNumbers),
                     QPLeaf(0, [inputs[2]]),
                     QPLeaf(1, [outputs[1]]),
                     QPLeaf(1, [outputs[2]])]
        self.botVer = QPVertex(botLeaves)

        if self.botVer.proper_max > self.topVer.proper_max:
            self.rootVer = self.botVer
            self.nonRootVer = self.topVer
        else:
            self.rootVer = self.topVer
            self.nonRootVer = self.botVer

    def get_comp_slot(self):
        comp_number = min([leaf.min for leaf in self.rootVer.leaves if not leaf.is_proper_leaf()])
        list_of_mins = sorted([leaf.min for leaf in self.rootVer.leaves])
        return 1 + list_of_mins.index(comp_number)

    def get_permutation(self):
        rootLeaves = [leaf.min for leaf in self.rootVer.leaves if leaf.is_proper_leaf()]
        nonRootLeaves = [leaf.min for leaf in self.nonRootVer.leaves if leaf.is_proper_leaf()]
        slot = self.get_comp_slot()
        result_list = list()
        sorted_root_leaves = sorted(rootLeaves)
        rootLeaf0 = sorted_root_leaves[0]
        rootLeaf1 = sorted_root_leaves[1]
        if slot == 1:
            result_list.extend(sorted(nonRootLeaves))
            result_list.append(rootLeaf0)
            result_list.append(rootLeaf1)
        if slot == 2:
            result_list.append(rootLeaf0)
            result_list.extend(sorted(nonRootLeaves))
            result_list.append(rootLeaf1)
        if slot == 3:
            result_list.append(rootLeaf0)
            result_list.append(rootLeaf1)
            result_list.extend(sorted(nonRootLeaves))
        return result_list

    def get_decomposition(self):
        #print(self.topVer.type, self.botVer.type, self.get_comp_slot(), Permutation(*self.get_permutation()))
        return [self.nonRootVer.type, self.rootVer.type, self.get_comp_slot(), Permutation(*self.get_permutation())]


# tr1 = QPTree([6, 3, 1], [4, 2, 5])
# tr1.get_decomposition() #y z 1 [1, 2, 5, 3, 4]
#
# tr2 = QPTree([1, 3, 6], [4, 2, 5])
# tr2.get_decomposition() #a z 1 [1, 3, 4, 2, 5]


def generate_QP_relation(inp, oup):
    relation = []
    rel_name = "INP: " + str(inp) + " OUT: " + str(oup)
    trees = []
    signs = []
    for sigma in Permutation.group(3):

        if sigma.is_odd:
            sign = -1
        else:
            sign = 1
        for tau in Permutation.group(3):
            signs.append(sign)
            qp_tree = QPTree(sigma.permute(inp), tau.permute(oup))
            top_label, bot_label, slot, perm = qp_tree.get_decomposition()
            tree = graft(gen_dict[bot_label].create_corolla(), gen_dict[top_label].create_corolla(), slot, perm)
            trees.append(tree)
    poly = TreePolynomial(trees, signs)
    rel = GroebnerRelation(poly, 0, rel_name)
    return rel


generate_QP_relation((6, 3, 1), (4, 2, 5))
six_numbers = set(range(1, 7))
relations = []
for inp in combinations(six_numbers, 3):
    oup = tuple([x for x in six_numbers if x not in inp])
    relations.append(generate_QP_relation(inp, oup))

QP = GroebnerBasis(relations)
quadraticity_check(QP, "QuadraticPoisson_log.tex")


