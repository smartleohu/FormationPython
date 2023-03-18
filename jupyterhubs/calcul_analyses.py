# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.14.5
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

# !pip install jupytext --upgrade
# !jupytext --to py ./calcul_analyses.ipynb

import sys
sys.version_info

# # Notation
# https://fr.wikipedia.org/wiki/Notation_polonaise_inverse

# ***
# $\mathbf{\text{Noatition Polonaise Inverse}}$<br>
# ***

# ![CPT-RPN](CPT-RPN-example1.png)

# ### exo1: 
# Utiliser le console en Pycharm et le notebook chez Jupyter lab pour commencer les manipulations arithmétiques sur les nombres. Afficher les résultats par print.  

# - +, -, *, / : les 4 opérations 
# - ^ : la puissance 
# - CEIL : l'arrondi vers le haut
# - COS, SIN, TAN, ACOS, ASIN, ATAN : fonctions trigonométriques 
# - LN, LOG, EXP : fonctions logarithmiques (LN pour logarithme népérien, et LOG pour le logarithme décimal) 

import math

10**3

math.log(1)

math.log10(10)

math.exp(0)

math.cos(0)

math.cos(math.pi)

round(math.degrees(math.asin(0.5)),2)

# 2 5 + DUP * 

a, b = 2, 5

c = a + b

c_bis = c

c * c_bis

# 12 0.5 SIN * 36 0.5 COS * + ABS LOG 

a, b = 12, 0.5

c = math.sin(b) * a

d, e = 36, 0.5

f = math.cos(e) * d + c
f

g = abs(f)
g

math.log(g)

math.fabs(-21)

abs(-21)

abs(-21.5)

math.ceil(-21.5)

# ### Exo2:
# Interpréter les manipulations mathématiques en notation polonaise inverse, et verse versa.  

# 1.&emsp;exemple $$\frac{sin(\frac{3\times \pi}{4})}{\frac{3\times \pi}{4}}$$

# 3 pi * 4 / DUP SIN SWAP / 

# ### Exo3:
# Utiliser la liste pour créer une pile. Pousser les éléments en notation polonaise inverse dans une liste.  

text1 = '2 5 + DUP *'
text1

elements =  text1.split()
elements

elements.pop()

elements

elements.append('*')

elements

elements.pop(0)

elements

elements.insert(0, '2')

elements

elements.pop(5)
elements

elements =  text1.split()
elements.pop(4)

elements + ['*']

elements =  text1.split()
elements.pop()

elements.extend(['*'])

elements

elements =  text1.split()
elements.reverse()

elements

reversed(elements)

sorted(elements)

elements

elements.sort()

elements

elements.remove('DUP')

elements

elements.remove('DUP')

stack1 =  text1.split()
stack1

# ### Exo4
# Définir 3 fonctions pour mettre en œuvre les manipulations logiques : DUP, DROP, SWAP. 

stack_org = ['2', '5']
stack_org


def dup(stack):
    stack.append(stack[-1])
stack_copy = stack_org.copy()
dup(stack_copy)
print(f"DUP sur {stack_org} est {stack_copy}")


def drop(stack):
    stack.pop()
stack_copy = stack_org.copy()
drop(stack_copy)
print(f"DROP sur {stack_org} est {stack_copy}")


def swap(stack):
    x, y = stack.pop(), stack.pop()
    stack.append(x)
    stack.append(y)
stack_copy = stack_org.copy()
swap(stack_copy)
print(f"SWAP sur {stack_org} est {stack_copy}")

# ### Exo5
# Distinguer deux types d’opérateurs : unitaires et binaires pour les manipulations.  

# \+ \- * / sont unitaires

# ### Exo6 
# Définir les fonctions lambda (anonymes) pour les opérateurs. 

(lambda x, y: x + y)(10, 3)

(lambda x, y: x - y)(10, 3)

(lambda x, y: x * y)(10, 3)

(lambda x, y: x / y)(10, 3)

(lambda x, y: x ** y)(10, 3)

# ### Exo7
# Définir deux foncteurs : fct1 et fct2 pour prendre en argument d’entrée tous ces opérateurs de fonction lambda. 

stack_org = [2, 10]
stack_org


# +
def fct1(fct):
    def _fct(stack):
        stack.append(fct(stack.pop()))

    return _fct

stack_cpy = stack_org.copy()
print(fct1(math.log10)(stack_cpy))
print(f"appliquer log10 sur stack_org est {stack_cpy}")


# +
def fct2(fct):
    def _fct(stack):
        y, x = stack.pop(), stack.pop()
        stack.append(fct(x, y))

    return _fct

stack_cpy = stack_org.copy()
print(fct2(lambda x, y: x ** y)(stack_cpy))
print(f"appliquer POWER sur {stack_org} est {stack_cpy}")
# -

# ### Exo8
# Créer un dictionnaire COMMANDS pour faire la correspondance entre les noms des opérateurs et ses définitions en foncteur.  

from pprint import pprint

# +
COMMANDS = {'+': fct2(lambda x, y: x + y),
            '-': fct2(lambda x, y: x - y),
            '*': fct2(lambda x, y: x * y),
            '/': fct2(lambda x, y: x / y),
            '^': fct2(lambda x, y: x ** y),
            'COS': fct1(math.cos),
            'SIN': fct1(math.sin),
            'TAN': fct1(math.tan),
            'ACOS': fct1(math.acos),
            'ASIN': fct1(math.asin),
            "CEIL": fct1(math.ceil),
            'ATAN': fct1(math.atan),
            'LN': fct1(math.log),
            'LOG': fct1(math.log10),
            'EXP': fct1(math.exp),
            'ABS': fct1(math.fabs),
            'DUP': dup,
            'SWAP': swap,
            'DROP': drop,
            }

pprint(COMMANDS)
# -

stack_org = [2, 1]
stack_org

for operator, fct in COMMANDS.items():
    stack_cpy = stack_org.copy()
    fct(stack_cpy)
    print(f"appliquer {operator} sur {stack_org} est {stack_cpy}")


# ### Exo9
# Définir la fonction interpreter(text : str) pour interpréter un texte en chaîne de  caractères pour calculer le résultat. 
# ##### a. Utiliser IF et ELIF 

def interpreter(text: str, line_number: int = 0):
    # decompose
    stack = []
    commands = text.split()

    # execute commands
    for command in commands:
        # is it a number?
        if str(command[-1]).replace('.', '').isdigit():
            stack.append(float(command))
            continue
        elif command in COMMANDS:
            fct = COMMANDS[command]
        else:
            print(
                F"ERROR: [line={line_number}]: unknown error on executing "
                F"'{command}' witch stack {stack}")
            return

        if command in ('+', '-', '*', '/'):
            if len(stack) > 1:
                fct(stack)
        elif len(stack) > 0:
            fct(stack)
        else:
            print(
                F"ERROR: [line={line_number}]: unknown error on executing "
                F"'{command}' witch stack {stack}")
            return

    return stack


text_1 = '3 3.14 * 4 / DUP SIN SWAP /'
stack_1 = interpreter(text_1)
print(stack_1)

text_2 = '3 pi * 4 / DUP SIN SWAP /'
stack_2 = interpreter(text_2)
print(stack_2)

text_3 = '3 SIN /'
stack_3 = interpreter(text_3)
print(stack_3)

text_3 = '3 0 /'
stack_3 = interpreter(text_3)
print(stack_3)


#
# ##### b. Réfléchir à une autre solution (N.B. : avoir des ‘if/elif’ en cascade n’est ni lisible ni simplement extensible ni maintenable dans le temps) 

def interpreter(text: str, line_number: int = 0):
    # decompose
    stack = []
    commands = text.split()

    # execute commands
    for command in commands:
        # is it a number?
        try:
            stack.append(float(command))
            continue
        except ValueError:
            pass

        # is it a command?
        try:
            fct = COMMANDS[command]
        except KeyError:
            print(F"ERROR[line={line_number}]: invalid command '{command}'")
            return

        # compute
        try:
            fct(stack)
        except Exception as e:
            print(
                F"ERROR {e}: [line={line_number}]: unknown error on executing "
                F"'{command}' witch stack {stack}")
            return

    return stack


text_1 = '3 3.14 * 4 / DUP SIN SWAP /'
stack_1 = interpreter(text_1)
print(stack_1)

text_2 = '3 pi * 4 / DUP SIN SWAP /'
stack_2 = interpreter(text_2)
print(stack_2)

text_3 = '3 SIN /'
stack_3 = interpreter(text_3)
print(stack_3)

text_3 = '3 0 /'
stack_3 = interpreter(text_3)
print(stack_3)

# ### Exo10
# Lire le fichier “sample/1.txt” en extrayant les textes non commentaires ligne par ligne pour appliquer la fonction interpreter avant d’imprimer les résultats. Par ailleurs, enrichir interpreter avec l’argument d’entrée line_number pour indiquer les erreurs des lignes textuelles dans le fichier au cas où. 

from pathlib import Path
def read_file(filename: Path):
    with open(filename, "r") as file:
        for line_number, line in enumerate(file, 1):
            # treat blank/comment lines
            line = line.strip()
            if 0 == len(line) or "#" == line[0]:
                continue

            # interpret
            result = interpreter(line, line_number)
            print(result)


fp = Path.cwd().parents[0] / 'samples' / '1.txt'
fp

read_file(fp)


# ### Exo11
# Parcourir le dossier “sample” pour manipuler tous les fichiers .txt dedans. 

def read_files(f_dir: Path):
    for fp in sorted(f_dir.glob('*.txt')):
        print(fp)
        read_file(fp)


file_dir = Path.cwd().parents[0] / 'samples'
file_dir

read_files(file_dir)

# ### Exo12
# Érire un décorateur pour mesurer le temps d’exécution d’une fonction. 

import time
def timing(func):
    """
    Mesure le temps d'exécution d'une fonction.
    """
    def wrapper(*args, **kwargs):
        """
        wrapper dans timing
        :param args: 
        :param kwargs: 
        :return: 
        """
        start_time = time.perf_counter()
        func(*args, **kwargs)
        end_time = time.perf_counter()
        print(f"Durée d'exécution : {end_time - start_time :1.3f}s")

    return wrapper


# +
@timing
def pause(t):
    """
    Pause 
    :param t: seconde
    :return:
    """
    print("Début ...")
    time.sleep(t)  # Pause de t secondes
    print("Fin !")
    
pause(t=2)
# -

pprint(pause.__doc__)

import functools


def timing(func):
    """
    Mesure le temps d'exécution d'une fonction.
    """
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        """
        wrapper dans timing
        :param args: 
        :param kwargs: 
        :return: 
        """
        start_time = time.perf_counter()
        func(*args, **kwargs)
        end_time = time.perf_counter()
        print(f"Durée d'exécution : {end_time - start_time :1.3f}s")

    return wrapper


@timing
def pause(t):
    """
    Pause 
    :param t: seconde
    :return:
    """
    print("Début ...")
    time.sleep(t)  # Pause de t secondes
    print("Fin !")



pprint(pause.__doc__)

# ### Exo12-bis
# Et si on le fait avec context manager ? 

# +
import datetime
import functools
import time
from typing import Callable


class EvaluationTime:
    def __init__(self, fct_name):
        self._fct_name = fct_name
        self._init_time = datetime.datetime.now()

    def __enter__(self):
        print(f"Started: {self._fct_name} at {self._init_time}")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print(f"Finished: {self._fct_name} in "
              f"{datetime.datetime.now() - self._init_time}")


def timing(fct: Callable):
    @functools.wraps(fct)
    def fct_wrapper(*args, **kwargs):
        with EvaluationTime(fct.__qualname__):
            return fct(*args, **kwargs)

    return fct_wrapper


# -

@timing
def pause(t: float):
    """
    Pause function
    :param t: second
    :return:
    """
    print("Begin ...")
    time.sleep(t)  # Pause de t secondes
    print("End!")


pause(t=2)


