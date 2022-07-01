# 10 Trucs et Astuces Python 
Bonjour à tous ! Dans cette vidéo je vais vous montrer 10 trucs et astuces simples pour améliorer la qualité et la lisibilité de votre code Python. C'est parti.

## 1. Utiliser un opérateur ternaire

Parfois on veut créer une variable avec une valeur ou une autre selon une condition.

> Ouvrir avec gvim ~/code/python-experiments/1.ternary_operators.py

Typiquement, on ferait quelque-chose comme ça, avec un bloc `if` suivi d'un bloc `else`.

Mais avec un opérateur ternaire ce serait beaucoup plus concis et élégant

> changer à partir de `if`

    x = 1 if condition else 0
## 2. Utiliser underscore pour séparer les paquets de chiffres dans les grands nombres¶
Quand on saisit un grand nombre, cela peut devenir difficile à lire : 

> ouvrir avec gvim 2.big_numbers.py

 Mais saviez-vous que vous pouvez utiliser des undescores _ pour séparer les milliers, millions ? C'est sans impact sur le code : 

> insérer les underscores

Alternativement, vous pouvez utiliser la notation scientifique, mais vous obtiendrez des `float` :

> remplacer les valeurs numériques par `1e10` et `1e7`

## 3. Utiliser un `context manager` pour gérer les ressources
👇 Téléchargeons un petit fichier texte pour les besoins de notre exemple :

> ouvrir avec gvim 3.context_manager.py

Il est fréquent d'ouvrir un fichier, de lire son contenu, puis de le fermer pour libérer la ressource, ainsi :


Mais si on oublie de le fermer, ou si il y a une erreur entre le moment où on ouvre le fichier et le moment où on le ferme, cela peut poser problème.

💡 La solution, utiliser un gestionnaire de contexte with ainsi, qui garantit que le fichier sera fermé automatiquement à l'issue du bloc indenté.

Changer le code à partir de `file = ` en

    with open(filename) as file:
        words = file.read().splitlines()

## 4. Itération avec indices grâce à `enumerate`

Prenons une petite liste de prénoms.

> ouvrir 4.enumerate.py

Il y a plusieurs manières possibles de la traverser, plus ou moins idiomatiques :

> montrer la traversée avec une boucle `while i < len(names)`

☝️ Traverser la liste avec un `while` oblige à gérer soit même l’incrémentation de la variable qui contient l'indice.

> montrer l'itération avec `for i in range(len(names))`

☝️ Traverser la liste avec un `for i in range(len(iterable))` a le bénéfice d'incrémenter la variable d'indice automatiquement, mais c’est un peu long à taper et manque de simplicité.

> montrer l'itération pythonique `for name in names`

☝️ Cette itération directe sur les éléments est la forme pythonique, simple et élégante. 

Mais parfois, on veut quand même avoir l'indice pour les besoins de notre algorithme…

> montrer l'ajout d'une variable i dans la boucle
    i = 0
    for name in names:
        print(f"{i}: {name}")
        i = i + 1

☝️ Alors on pourrait imaginer combiner l’itération directe et la gestion d'un indice comme ici, mais c'est un peu maladroit…

 > montrer l'usage d'enumerate

💡 Le moyen le plus propre est d'utiliser la fonction enumerate sur notre itérable (ici une liste), et d'itérer dessus avec 2 variables : la première tiendra l'indice, la seconde les éléments de l'itérable que l'on traverse.

## 5. Itérer sur plusieurs listes en même temps avec `zip()`
Cette fois, nous allons avoir 2 listes. On souhaite itérer sur les deux en parallèle.

👇 On pourrait le faire avec un indice sur un `range` de la longueur de l'une ou l'autre, mais encore une fois, c'est un peu fastidieux :

> montrer `for i in range(len(first_names)):`…

👇 On pourrait utiliser enumerate pour itérer directement sur une liste, et utiliser l'index donné par enumerate pour aller chercher les éléments dans l'autre liste, mais c’est un peu tordu.

> montrer `for i, first in enumerate(first_names):`

💡 Mais en réalité, pour traverser directement 2 ou plusieurs itérables, le plus simple, c’est d’utiliser zip pour les réunir, et itérer sur le zip, avec autant de variables d'itération que d’itérables :

> montrer `for first, last in zip(first_names, last_names):`

## 6. Dépaqueter des valeurs
Quand on a plusieurs valeurs dans un tuple à droite d'une assignation, on peut directement les assigner à plusieurs variables, en les séparant par des virgules, comme ceci :

> ouvrir 6.tuple_unpacking.py

👇 Si l'une des valeur ne nous intéresse pas pour la suite, la convention est de l'assigner à une variable appelée `_`. Votre IDE ne vous reprochera plus d'avoir assigné une variable et de ne pas l'avoir utilisée ensuite, si elle est nommée ainsi :

> remplacer b par _ et retirer le print(b)

👇 Si on a plus de noms de variables que de valeurs à dépaqueter, on obtient une `ValueError` :

> montrer `a, b, c = (1, 2)`

👇 Si on a plus de valeurs à dépaqueter que de noms de variables, là aussi, une ValueError nous attend :

> montrer `a, b, c = (1, 2, 3, 4, 5)`

👇 Mais dans ce cas là, on peut aussi dire à Python de mettre toutes les valeurs qui restent à dépaqueter dans une seule variable, qui contiendra une liste, juste avec une petite étoile `*` :

montrer `a, b, *c = (1, 2, 3, 4, 5)`

👇 la variable qui récupère le trop-plein de valeurs n’a pas à être la dernière de l'assignation :

montrer `a, b, *c, d = (1, 2, 3, 4, 5, 6)`

## 7. Extraire et fixer des attributs dans une instance

Ici nous allons parler un peu de programmation orientée objet.

Imaginez que vous ayez une classe très simple, et très vide.

> ouvrir 7.set_attr_get_attr.py

Vous pourriez ajoutre des attributs à votre instance `person` ainsi :

> montrer l'ajout d'attributs 

    person.first = "Sadi"
	person.last = "Carnot"

et les extraire ainsi :

	print(person.first)
	print(person.last)

Mais si les noms des attributs étaient dans une variable, vous seriez coincé·e.

> montrer 

    class Person:
        pass


    person = Person()

    first_key = "first"
    first_val = "Sadi"


💡 C’est là qu’interviennent les fonctions `setattr` (set attribute) et `getattr` (get attribute) :

> montrer
    setattr(person, first_key, first_val)
	person.first

    first = getattr(person, first_key)
    
Pour lire un attribut dont le nom est dans une variable :

> montrer

	first = getattr(person, first_key)
    print(first)

## 8. Faire saisir des mots de passe en toute sécurité

Parfois un script a besoin de vous faire saisir un mot de passe, par exemple pour vous identifier à un service.

On peut demander à l'utilisateur du script de saisir le mot de passe, mais si on le fait avec la fonction classique `input`, le problème est que le mot de passe apparaît à l'écran, ce qui n'est pas idéal quand d’autres personnes peuvent voir l'écran.

> ouvrir `8.getpass.py`

💡 Pour cela, il suffit d'utiliser `getpass.getpass()` qui fonctionne comme `input()` mais cache le mot de passe saisi :

> importer `from getpass import getpass` et remplacer l’`input` sur le mot de passe par un `getpass`

## 9. Décorateurs

Parfois on se rend compte que l'on a besoin d'ajouter un comportement commun à plusieurs fonctions ou méthodes.

Par exemple, pour enregistrer un fichier "journal" qui traque les appels passés à une fonction, ou bien si l’on souhaite simplement chronométrer deux algorithmes pour les comparer.

On pourrait ajouter la logique qui assure le chronométrage dans la définition de chaque fonction, mais ce serait répéter de la logique qui devrait être définie en un seul lieu.

C’est là qu’interviennent les décorateurs.

Imaginons que je veuille comparer les performances de ces deux fonctions, qui toutes les deux renvoient la somme des entiers entre `1` et `n`.

> ouvrir 9.decorators.py

Pour mesurer le temps pris par chaque fonction, il suffit de récupérer l’heure avant l'exécution, puis après l'exécution, et de calculer la différence.

Nous allons écrire une fonction appelée un décorateur. Elle va prendre une fonction, et nous la renvoyer modifiée avec le comportement de chronométrage.

>




