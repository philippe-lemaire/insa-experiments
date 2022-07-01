from time import time


def timer(func):
    def wrapper(*args, **kwargs):
        # on note l'heure avant d'exécuter la fonction
        t1 = time()
        # on exécute la fonction avec ses arguments et on stocke sa valeur de sortie
        value = func(*args, **kwargs)
        # on note l'heure après l'exécution de la fonction
        t2 = time()

        print(f"{func.__name__}({args[0]}) exécutée en {t2 - t1} secondes.")
        # notre fonction wrapper renvoie la valeur de sortie de la fonction "emballée"
        return value
    # on renvoie la fonction "emballée" dans le wrapper
    return wrapper


def simple_sum(n):
    """Renvoie la somme des nombres de 1 à n en sommant range(1, n+1)."""
    return sum(range(1, n + 1))


def gaussian_sum(n):
    """Calcule la somme de 1 à n, avec la technique utilisée par Gauss en primaire."""
    return (n * (n + 1)) // 2


print(simple_sum(100))
print(gaussian_sum(100))
