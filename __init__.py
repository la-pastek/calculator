
import parseur
import solveur
import utils

equation = input("enter votre equation attention de bien rentrer votre equation car ce code respecte a la lettre la regles PEMDAS")
elements = utils.equation_to_list(equation) # elements est la liste qui contient l'equation
i = 3
while i > 1:
    index1 = int(parseur.start_parentheses_index(elements))
    index2 = int(parseur.end_parentheses_index(elements))
    expression_simp = solveur.simp_parenthesis(parseur.start_parentheses_index(elements),elements)

    reponse = solveur.res_equation(expression_simp)
    elements = utils.replace(elements, index1, index2, reponse)
    print(elements)
    i = i-1




