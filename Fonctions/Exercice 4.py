def décorateur(nb):
    for i in range(nb):
        def décorée(nb):
            return nb

    return décorée(nb)

print(décorateur (3))


