# Calcul par commande
C’est un fichier de commande avec une instruction par ligne basé sur le 
principe de la polonaise inverse 
(https://fr.wikipedia.org/wiki/Notation_polonaise_inverse). 
Nous supporterons uniquement les flottants avec une expression par ligne, 
le séparateur étant l’espace. 

## Commandes supportées : 

- \# commentaire 
- +, -, *, / : les 4 opérations 
- ^ : la puissance 
- CEIL : l'arrondi vers le haut
- COS, SIN, TAN, ACOS, ASIN, ATAN : fonctions trigonométriques 
- LN, LOG, EXP : fonctions logarithmiques (LN pour logarithme népérien, 
et LOG pour le logarithme décimal) 
- ABS : valeur absolue 
- DUP : duplique le dernier élément dans la pile 
- DROP : supprime le dernier élément dans la pile 
- SWAP : échange les 2 dernières valeurs 

## Exemples de programme : 
- Calcul simple :
    2 5 + DUP * 
    Résultat : 49 
- Calcul complexe : 
    12 0.5 SIN * 36 0.5 COS * + ABS LOG 

Par exemple, le fichier à lire est : “samples/1.txt” 


1. Utiliser le console en Pycharm et le notebook chez Jupyter lab pour commencer les manipulations arithmétiques sur les nombres. Afficher les résultats par print.  

2. Interpréter les manipulations mathématiques en notation polonaise inverse, et verse versa.  

3. Utiliser la liste pour créer une pile. Pousser les éléments en notation polonaise inverse dans une liste.  

4. Définir 3 fonctions pour mettre en œuvre les manipulations logiques : DUP, DROP, SWAP. 

5. Distinguer deux types d’opérateurs : unitaires et binaires pour les manipulations.  

6. Définir les fonctions lambda (anonymes) pour les opérateurs. 

7. Définir deux foncteurs : fct1 et fct2 pour prendre en argument d’entrée tous ces opérateurs de fonction lambda. 

8. Créer un dictionnaire COMMANDS pour faire la correspondance entre les noms des opérateurs et ses définitions en foncteur.  

9. Définir la fonction interpreter(text : str) pour interpréter un texte en chaîne de  caractères pour calculer le résultat. 

10. Utiliser IF et ELIF 

11. Réfléchir à une autre solution (NOTA : avoir des ‘if/elif’ en cascade n’est ni lisible ni simplement extensible ni maintenable dans le temps) 

12. Lire le fichier “sample/1.txt” en extrayant les textes non commentaires ligne par ligne pour appliquer la fonction interpreter avant d’imprimer les résultats. Par ailleurs, enrichir interpreter avec l’argument d’entrée line_number pour indiquer les erreurs des lignes textuelles dans le fichier au cas où. 

13. Parcourir le dossier “sample” pour manipuler tous les fichiers .txt dedans. 

14. Écrire un décorateur pour mesurer le temps d’exécution d’une fonction. Et si on le fait avec context manager ? 

15. Encapsuler des fonctionnalités en classes 

    Le constructeur 

    Les propriétés 

    Les méthodes : objet, classe et statique 

    Organiser les différents modules dans le projet avec docstring 

    Réaliser les tests unitaires 
