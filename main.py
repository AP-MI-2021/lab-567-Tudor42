# problema 2
"""
Un program pentru gestionarea unui inventar dintr-o instituție.

Cerinte:
    1. Adăugare / ștergere / modificare obiect: se efectuează pe bază de
        număr de inventar / ID. Un obiect conține: ID, nume, descriere
        (nenule), preț achiziție, locație (exact `4` caractere).
    2. Mutarea tuturor obiectelor dintr-o locație în alta.
    3. Concatenarea unui string citit la toate descrierile obiectelor cu
        prețul mai mare decât o valoare citită.
    4. Determinarea celui mai mare preț pentru fiecare locație.
    5. Ordonarea obiectelor crescător după prețul de achiziție.
    6. Afișarea sumelor prețurilor pentru fiecare locație.
    7. Undo.
"""
import UserInterface.ui as ui
import Tests.run_tests as test


def main():
    test.run_tests()
    ui.run()


if __name__ == "__main__":
    main()
