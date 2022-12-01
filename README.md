# Optimal_matching

Projet de programmation linéaire avec Gurobi en Python.

Implémentation du critère de Wald et du Min Max Regret

## Installations requises
Les bibliothèques utilisés sont disponibles dans ``requirements.txt``.

Pour les télécharger :

```
pip3 install -r requirements.txt
```

## Commandes

- ``lib.py``

    Exécuter les fonctions des différents problèmes linéaires:
    ```
    python3 lib.py <nom fonction> <taille matrice> <borne inférieure> <borne supérieure>
    ```
    Exemple pour éxécuter la fonction ``question_1`` pour une matrice d'utilités aléatoire de taille 5 qui prend ses valeurs dans [0,20]:
    ```
    python3 lib.py question_1 5 0 20
    ```
    Pour donner des matrices particulières à ces fonctions, le faire dans ``main.py``

- ``perf.py``

    Exécuter un test de performance sur une des fonctions de ``lib.py``
    ```
    python3 perf.py <nom fonction> <borne inf> <borne sup> <iterations par point> <taille limite> <pas>
    ```
    Exemple pour faire un test de performance de ``question_1`` pour la taille N allant de 5 à 100 par pas de 5 avec une moyenne sur 10 itérations pour des utilités dans [0,20]:
    ```
    python3 perf.py question_1 0 20 10 100 5
    ```

## Fonctions disponibles

- ``question_1``: Maximise la satisfaction moyenne
- ``question_4``: Maximise la satisfaction de l'entité la moins satisfaite avec reste pour prendre en compte la satisfaction globale
- ``question_5``: Minimise le plus grand regret


Se référer au ``rendu.pdf`` pour la définition formelle de ces fonctions

