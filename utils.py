
import re
def equation_to_list(equation):
    # Utilisation d'une expression régulière pour diviser l'équation en éléments
    elements = re.findall(r'[\d.]+|[\+\-\*/\(\)]', equation)

    # Supprimer les espaces vides des éléments
    elements = [e.strip() for e in elements if e.strip()]
    return elements

def replace(input_list, index1, index2, reponse):
    """
    :param input_list: l'equation initiale
    :param index1: debut de la 1er parenthse
    :param index2: fin de la parenthse
    :param replacement_number: reponse
    :return:
    """
    new_list =list()
    if index1 < 0 or index2 < 0 or index1 >= len(input_list) or index2 >= len(input_list):
        raise IndexError("Indices hors de la plage valide")

    for i in range(index1):
        new_list.append(input_list[i])
    new_list.append(reponse[0]) # il ne faut pas oublier de rajouter la fin de l'equation

    return new_list
