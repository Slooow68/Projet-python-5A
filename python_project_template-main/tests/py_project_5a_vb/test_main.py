import webbrowser
from test_data_loader import get_rockets, get_engines, get_agencies

rockets = get_rockets()
engines = get_engines()
agencies = get_agencies()

def show_main_menu():
    print("1. Voir la liste des fusées")
    print("2. Voir la liste des moteurs")
    print("3. Voir la liste des agences spatiales")
    print("5. Quitter")
    choice = input("Entrez votre choix : ")
    if choice == '1':
        show_rockets_list()
    elif choice == '2':
        show_engines_list()
    elif choice == '3':
        show_agencies_list()
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

def show_engines_list():
    print("\nListe des moteurs :")
    for i, engine in enumerate(engines, 1):
        print(f"{i}. {engine['name']}")
    choice = input("\nEntrez le numéro du moteur pour plus d'informations ou 'q' pour revenir au menu principal : ")
    if choice.lower() == 'q':
        show_main_menu()
    else:
        try:
            engine = engines[int(choice) - 1]
            show_engine_details(engine)
        except (ValueError, IndexError):
            print("Choix invalide.")
            show_engines_list()
        
def show_engine_details(engine):
    print(f"\nNom du moteur : {engine['name']}")
    print(f"Fusées associées : {', '.join(engine['rockets'])}")
    print(f"Poussée : {engine['thrust']}")
    print(f"Réallumable : {'Oui' if engine['reusable'] else 'Non'}")
    print(f"Type d'ergol : {engine['propellant_type']}")
    print(f"Hauteur : {engine['height']}")
    print(f"Cycle : {engine['cycle']}")
    redirect = input("\nVoulez-vous voir la page Wikipédia de ce moteur ? (oui/non) : ")
    if redirect.lower() == 'oui':
        webbrowser.open(engine['wikipedia_url'])
    show_main_menu()

def show_agencies_list():
    print("\nListe des agences spatiales :")
    for i, agency in enumerate(agencies, 1):
        print(f"{i}. {agency['name']}")
    choice = input("\nEntrez le numéro de l'agence pour plus d'informations ou 'q' pour revenir au menu principal : ")
    if choice.lower() == 'q':
        show_main_menu()
    else:
        try:
            agency = agencies[int(choice) - 1]
            show_agency_details(agency)
        except (ValueError, IndexError):
            print("Choix invalide.")
            show_agencies_list()

def show_agency_details(agency):
    print(f"\nNom : {agency['name']}")
    print(f"Date de création : {agency['creation_date']}")
    print(f"Pays d'origine : {agency['country']}")
    print(f"Type : {agency['type']}")
    print(f"PDG actuel : {agency['ceo']}")
    redirect = input("\nVoulez-vous voir la page Wikipédia de cette agence ? (oui/non) : ")
    if redirect.lower() == 'oui':
        webbrowser.open(agency['wikipedia_url'])
    show_main_menu()

show_main_menu()

    

