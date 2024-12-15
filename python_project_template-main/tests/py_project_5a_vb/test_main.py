import webbrowser
from test_data_loader import get_rockets, get_engines, get_agencies

rockets = get_rockets()

def show_main_menu():
    print("1. Voir la liste des fusées")
    print("5. Quitter")
    choice = input("Entrez votre choix : ")
    if choice == '1':
        show_rockets_list()
    elif choice == '5':
        exit()
    else:
        print("Choix invalide, réessayez.")
        show_main_menu()

def show_rockets_list():
    print("\nListe des fusées :")
    for i, rocket in enumerate(rockets, 1):
        print(f"{i}. {rocket['name']}")
    choice = input("\nEntrez le numéro de la fusée pour plus d'informations ou 'q' pour revenir au menu principal : ")
    if choice.lower() == 'q':
        show_main_menu()
    else:
        try:
            rocket = rockets[int(choice) - 1]
            show_rocket_details(rocket)
        except (ValueError, IndexError):
            print("Choix invalide.")
            show_rockets_list()

def show_rocket_details(rocket):
    print(f"\nNom : {rocket['name']}")
    print(f"Moteur : {rocket['engine']}")
    print(f"Hauteur : {rocket['height']}")
    print(f"Diamètre : {rocket['diameter']}")
    print(f"Nombre d'étages : {rocket['stages']}")
    print(f"Nombre de lancements : {rocket['launches']}")
    print(f"Date de création : {rocket['creation_date']}")
    print(f"Active : {'Oui' if rocket['active'] else 'Non'}")
    print(f"Type d'ergol : {rocket['propellant_type']}")
    print(f"Charge utile maximale : {rocket['payload_mass']}")
    redirect = input("\nVoulez-vous voir la page Wikipédia de cette fusée ? (oui/non) : ")
    if redirect.lower() == 'oui':
        webbrowser.open(rocket['wikipedia_url'])
    show_main_menu()

show_main_menu()

    

