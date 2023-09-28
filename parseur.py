

"""
# parseur : analyse l'equation
# la classe contient des methodes 'ckeck' qui definissent quel operateur mathematique utiliser
# la classe contient des methodes 'start' qui indique où doit commencer la resolution de l'equation
"""
def check_parenthese(expr_list):
    """

    :param expr_list:
    :return:
    """
    if "(" in expr_list:
        return 1   # Renvoie l'index du nombre après la parenthèse ouverte
    else:
        return -1  # Aucune parenthèse ouverte n'a été trouvée
def check_exposant(expr_list):
    """

    :param expr_list:
    :return:
    """
    if "^" in expr_list:
        return 2   # Renvoie l'index du nombre après l'exposant
    else:
        return -1  # Aucun exposant n'a été trouvé

def check_multiplication(expr_list):
    """

    :param expr_list:
    :return:
    """
    if "*" in expr_list:
        return 3   # Renvoie l'index multiplication
    else:
        return -1  # Aucune multiplication n'a été trouvée

def check_division(expr_list):
    """

    :param expr_list:
    :return:
    """
    if "/" in expr_list:
        return 4   # Renvoie l'index du nombre après la division
    else:
        return -1  # Aucune division n'a été trouvée

def check_addition(expr_list):
    """
    :param expr_list:
    :return:
    """
    if "+" in expr_list:
        return 5
    else:
        return -1  # Aucune addition n'a été trouvée

def check_subtraction(expr_list):
    """
    :param expr_list: equation a analyser
    :return: valeur 6 pour indiquer au soleur qui devras faire une soustraction avec les nombres suivants
    """
    if "-" in expr_list:
        return 6
    else:
        return -1  # Aucune soustraction n'a été trouvée
def start_parentheses_index(expr_list):
    """
    :param expr_list:
    :return:
    """
    reversed_list = expr_list[::-1]  # Inverse la liste
    if "(" in reversed_list:
        return len(expr_list) - 1 - reversed_list.index("(")  # Renvoie l'index de la parenthèse ouverte dans la liste d'origine
    else:
        return -1  # Aucune parenthèse ouverte n'a été trouvée
def end_parentheses_index(expr_list):
    """
    :param expr_list:
    :return:
    """
    if ")" in expr_list:
        return expr_list.index(")") # Renvoie l'index de la parenthèse ouverte dans la liste d'origine
    else:
        return -1  # Aucune parenthèse ouverte n'a été trouvée
def start_exposant_index(expr_list):
    if "^" in expr_list:
        return expr_list.index("^")   # Renvoie l'index du nombre après l'exposant
    else:
        return -1  # Aucun exposant n'a été trouvé

def start_multiplication_index(expr_list):
    """
    cette functions retourne l'index ou se trouve l'operateur
    :param expr_list:
    :return:
    """
    if "*" in expr_list:
        return expr_list.index("*")   # Renvoie l'index du nombre après la multiplication
    else:
        return -1  # Aucune multiplication n'a été trouvée

def start_division_index(expr_list):
    if "/" in expr_list:
        return expr_list.index("/")   # Renvoie l'index du nombre après la division
    else:
        return -1  # Aucune division n'a été trouvée

def start_addition_index(expr_list):
    if "+" in expr_list:
        return expr_list.index("+")   # Renvoie l'index du nombre après l'addition
    else:
        return -1  # Aucune addition n'a été trouvée

def start_subtraction_index(expr_list):
    if "-" in expr_list:
        return expr_list.index("-")   # Renvoie l'index du nombre après la soustraction
    else:
        return -1  # Aucune soustraction n'a été trouvée

