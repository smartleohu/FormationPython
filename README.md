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
