import time


def multiply_table(n, _min = 1, _max = 10):
    print(f"Table de multiplication par : {n}")
    for i in range(_min, _max + 1):
        result = i * n
        print(f"{i} x {n} = {result}")
        time.sleep(1)


entry = int (input("Tu souhaites faire la table de multiplication par : "))
_min = int(input("Avec quel nombre souhaites tu commencer la table de multiplication? : "))
_max = int(input('Avec quel nombre souhaites tu terminer la table de multiplication? : '))

if _min > _max:
    print("Erreur : la valeur de debut ne peut pas être supérieur à la valeur de fin !")
elif _min == _max:
    print("Erreur : la valeur de debut ne peut pas être supérieur à la valeur de fin !")
else:
    multiply_table(entry, _min, _max)

print('Fin !')
