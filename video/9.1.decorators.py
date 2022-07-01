def simple_sum(n):
    """Renvoie la somme des nombres de 1 à n en sommant range(1, n+1)."""
    return sum(range(1, n + 1))


def gaussian_sum(n):
    """Calcule la somme de 1 à n, avec la technique utilisée par Gauss en primaire."""
    return (n * (n + 1)) // 2


print(simple_sum(100))
print(gaussian_sum(100))
