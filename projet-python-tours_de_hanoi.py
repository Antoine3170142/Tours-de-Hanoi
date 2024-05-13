"""
Code de Antoine NICOLAS TP4
"""

def initHanoi(n):
    # Crée une liste de trois éléments : la première tour avec des disques de 1 à n, les deux autres tours vides
    return [list(range(n, 0, -1)), [], []]

def afficheHanoi(tours):
    # Trouve la hauteur maximale parmi les tours
    max_height = max(len(tour) for tour in tours)
    
    # Affiche les tours en alignant les éléments avec les numéros de ligne
    for i in range(max_height - 1, -1, -1):
        # Crée une chaîne de caractères pour chaque niveau des tours
        # Si le niveau actuel est supérieur à la hauteur de la tour, affiche un espace pour ce niveau
        # Sinon, affiche l'élément de la tour correspondante
        row = ' '.join(str(tour[i]) if i < len(tour) else ' ' for tour in tours)
        # Affiche la ligne en ajoutant un espace supplémentaire pour l'alignement
        print(f"{' '.join(row):<4}")  # Affichage avec une largeur de 4 caractères pour aligner les colonnes
    
    # Affiche les indices des tours
    print('[0] [1] [2]')

def joueHanoi(tours):
    while tours[0] or tours[1]:  # Continue tant que les deux premières tours ne sont pas vides
        afficheHanoi(tours)  # Affiche les tours actuelles
        source = int(input("Source : "))  # Demande à l'utilisateur le numéro de la tour source
        destination = int(input("Destination : "))  # Demande à l'utilisateur le numéro de la tour destination

        # Vérifie si les numéros de tour saisis sont valides
        if 0 <= source < 3 and 0 <= destination < 3:
            # Vérifie si la tour source n'est pas vide
            if not tours[source]:
                print("La tour source est vide. Veuillez choisir une autre tour.")
                continue
            # Vérifie si le déplacement est valide et effectue le déplacement des disques
            elif not tours[destination] or tours[destination][-1] > tours[source][-1]:
                tours[destination].append(tours[source].pop())
            else:
                print("Erreur de saisie ou coup non permis")
        else:
            print("Les numéros de tour sont incorrects.")

def bougeHanoi(tours, n, depuisTour, versTour):
    if n == 1:
        tours[versTour].append(tours[depuisTour].pop())  # Déplace un disque de la tour source vers la tour destination
        afficheHanoi(tours)  # Affiche les tours après le déplacement
        return

    tour_transit = 3 - depuisTour - versTour  # Détermine la tour de transit
    bougeHanoi(tours, n - 1, depuisTour, tour_transit)  # Déplace n-1 disques de depuisTour à la tour de transit
    tours[versTour].append(tours[depuisTour].pop())  # Déplace un disque de depuisTour vers versTour
    afficheHanoi(tours)  # Affiche les tours après le déplacement
    bougeHanoi(tours, n - 1, tour_transit, versTour)  # Déplace n-1 disques de la tour de transit vers versTour

# Test des fonctions
tours_initiaux = initHanoi(4)
joueHanoi([[3, 2, 1], [], []])
