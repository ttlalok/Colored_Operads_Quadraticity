# Colored_Operads Project
This project implements a rewriting system for colored operads, 
following the article [Gröbner Bases for Coloured Operads](https://arxiv.org/abs/2008.05295).

The main purpose of this project is the following:  
given
a set of quadratic relations in a colored shuffle operad with the chosen
leading terms, compute all
non-trivial S-polynomials.  
If there are no such polynomials, the set of quadratic
relations forms a Groebner basis for the operad.

## Workflow

We assume that the operad is presented through generators and relations.

### Step 1
Create a new file, add import statement:

        from quadraticity import *
        from tree_constructor import *
The `quadraticity` module implements the proposed functionality. 

The `tree_constructor` module is a helper module for easier tree construction.

### Step 2
Declare the generators of the operad. This is done by creating an object of class
`TypeOfObject`:

        a_type = TypeOfVertex('a', [0, 0], 0)
The first argument is the label of the operation (its name), a string.

The second argument is the list containing the colors of the inputs of the operation.

The third argument is the color of the output of the operation.

### Step 3
Declare the relations of the operad. 

First, create all the trees constituting the relation:

        com1_tree1 = left_tree_constructor(a_type, a_type)
        com1_tree2 = perm_left_tree_constructor(a_type, a_type)
        
Second, create a tree polynomial, specifying the coefficients:

        com1_poly = TreePolynomial([com1_tree1, com1_tree2], [1, -1])

Third, create a `GroebnerRelation` object by specifying the index of the leading term, and
giving the relation a name.

        com1_rel = GroebnerRelation(com1_poly, 1, 'Com1')

We recommend to group the relations coming from the same symmetric relation together
in a single `GroebnerBasis` object. The result may look something like this:

        com1_tree1 = left_tree_constructor(a_type, a_type)
        com1_tree2 = perm_left_tree_constructor(a_type, a_type)
        com1_poly = TreePolynomial([com1_tree1, com1_tree2], [1, -1])
        com1_rel = GroebnerRelation(com1_poly, 1, 'Com1')
        
        com2_tree1 = left_tree_constructor(a_type, a_type)
        com2_tree2 = right_tree_constructor(a_type, a_type)
        com2_poly = TreePolynomial([com2_tree1, com2_tree2], [1, -1])
        com2_rel = GroebnerRelation(com2_poly, 1, 'Com2')
        
        com = GroebnerBasis([com1_rel, com2_rel])
        
### Step 4

Create a blank `GroebnerBasis` object. Merge all the `GroebnerBasis` object of the relations with it:

        basis = GroebnerBasis()
        basis.merge_bases(com)
        basis.merge_bases(lie)
        basis.merge_bases(leib)

The main function:

        quadraticity_check(basis, 'OperadName_log.tex')

This function returns `True` if the basis has no non-trivial S-polynomials.
It also keeps the log of all reductions performed, and S-polynomials found, writing it
in the file `'OperadName_log.tex'`. The log file is a LaTeX file.

If the optional argument `full_s_list` is set to `True`, the program will add the whole
list of S-polynomials to the log file.

### **Warning**
The `quadraticity_check` function **overwrites** the log file, so it's better to 
create a separate file just to serve as a log file.

### Examples

Please consult the examples of operads in the **Operads** folder.

### Author
Vladislav Kharitonov.
