
import parseur
import solveur
import utils

equation = input("enter votre equation")
elements = utils.equation_to_list(equation) # elements est la liste qui contient l'equation


index1 = int(parseur.start_parentheses_index(elements))
index2 = int(parseur.end_parentheses_index(elements))
expresion_simp = solveur.simp_parenthesis(parseur.start_parentheses_index(elements),elements)
print(expresion_simp)
reponse = solveur.res_equation(expresion_simp)
print(reponse)
print(index1,index2)
print(elements)
elements = utils.replace(elements, index1, index2, reponse)
print(elements)



