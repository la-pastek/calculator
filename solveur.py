
import parseur
# le solveur resous les equations
# la classe contient des functions 'res & simp' qui resous/simplie les equations
def simp_parenthesis(index_start, express_list):
    """
    cette function renvoie une list de l'equation se trouvant dans les parentheses
    :param index_start: indique l'endroit ou se trouve le debut de la parenthese ou si il ya une parenthese
    :param express_list: l'equation d'origine
    :return: l'equation a resoudre
    """
    equa_list = []

    if index_start != -1:
        # print("Oui, il y a une parenthèse")
        count_open_parentheses = 1  # Compteur pour suivre les parenthèses ouvertes
        while count_open_parentheses > 0:
            index_start += 1
            if express_list[index_start] == "(":
                count_open_parentheses += 1
            elif express_list[index_start] == ")":
                count_open_parentheses -= 1
            if count_open_parentheses > 0:
                equa_list.append(express_list[index_start])
        # print("Équation à l'intérieur des parenthèses :", equa_list)
    return equa_list

def res_equation(equation_list):
    """
    cette function retourne la reponse d'une equation
    :param equation_list: l'equation SIMPLIFIE fournie par 'equal_inside_parenthesis'
    :return: la reponse se trouvant dans la parenthese ou  l'equation simplifier
    """
    Larepo = equation_list

    while len(Larepo) > 1:
        print("ok")
        operateur_multi = parseur.check_multiplication(Larepo)
        operateur_div = parseur.check_division(Larepo)
        operateur_add = parseur.check_addition(Larepo)
        if 3 == operateur_multi: # multiplcation
            while operateur_multi == 3:
                start_index = parseur.start_multiplication_index(Larepo)
                if start_index - 1 >= 0 and start_index + 1 < len(equation_list):
                    entier1 = float(equation_list[start_index - 1])
                    entier2 = float(equation_list[start_index + 1])
                    reponse = entier1 * entier2
                    Larepo = modifier_liste(Larepo, parseur.start_multiplication_index(equation_list), str(reponse))
                    operateur_multi = parseur.check_multiplication(Larepo)
        elif 4 == operateur_div: # disvion
            while operateur_div == 4:
                start_index = parseur.start_division_index(Larepo)
                if start_index - 1 >= 0 and start_index + 1 < len(equation_list):
                    entier1 = float(equation_list[start_index - 1])
                    entier2 = float(equation_list[start_index + 1])
                    reponse = entier1 / entier2
                    Larepo = modifier_liste(Larepo, parseur.start_division_index(Larepo), str(reponse))
                    operateur_div = parseur.check_division(Larepo)
        elif 5 == operateur_add: # addition
            while operateur_add == 5:
                start_index = parseur.start_addition_index(Larepo)
                if start_index - 1 >= 0 and start_index + 1 < len(equation_list):
                    entier1 = float(equation_list[start_index - 1])
                    entier2 = float(equation_list[start_index + 1])
                    reponse = entier1 + entier2
                    Larepo = modifier_liste(Larepo, parseur.start_addition_index(Larepo), str(reponse))
                    operateur_add = parseur.check_addition(Larepo)
    return Larepo



def modifier_liste(liste, index, nombre):
    """
    Modifie l'equation en fonction de son étape
    :param liste: est l'equation simplifier sans parenthese
    :param index: l'endroit ou se trouve l'operateur
    :param nombre: la reponse qu resoit la methodes "res_equation"
    :return: une nouvelle equation sans l'operation qui
    """
    list = liste
    if index >= 1 and index + 1 < len(list):
        del list[index - 1:index + 2]  # Supprime les éléments à l'index-1, index, et index+1
        list.insert(index - 1, nombre)  # Insère le nombre à l'index-1
        return list
    else:
        print("Index en dehors des limites de la liste")

