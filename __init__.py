import sympy as sp

import sympy as sp
import parseur
import solveur
def equation_to_list(equation):
    try:
        # Crée une liste pour stocker les éléments de l'équation
        elements_list = []

        # Parcourt l'expression analysée
        for i in range(len(equation)):
            elements_list.append(equation[i])
        return elements_list

    except sp.SympifyError:
        # En cas d'erreur d'analyse de l'équation
        return None

equation = input("enter votre equation")
elements = equation_to_list(equation) # elements est la liste qui contient l'equation

print(elements)
print(parseur.start_parentheses_index(elements))
expresion_simp = solveur.simp_parenthesis(parseur.start_parentheses_index(elements),elements)
print(expresion_simp)
reponse = solveur.res_equation(expresion_simp)
print(reponse)



