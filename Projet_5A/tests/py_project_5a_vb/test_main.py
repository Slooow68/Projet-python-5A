import webbrowser
import matplotlib.pyplot as plt
from test_data_loader import get_rockets, get_engines, get_agencies
from test_statistics import calculate_statistics, plot_agency_rocket_count, plot_top_rocket_by_launches, plot_top_rocket_by_payload

"""
Collect the data from the database
"""
rockets = get_rockets()
engines = get_engines()
agencies = get_agencies()

"""
Main menu 
User can choose what he want to see between the rockets, engines, space agencies & some statistics from the database
"""
def show_main_menu():
    print("1. Voir la liste des fusées")
    print("2. Voir la liste des moteurs")
    print("3. Voir la liste des agences spatiales")
    print("4. Voir les statistiques")
    print("5. Quitter")
    choice = input("Entrez votre choix : ")
    if choice == '1':
        show_rockets_list()
    elif choice == '2':
        show_engines_list()
    elif choice == '3':
        show_agencies_list()
    elif choice == '4':
        show_statistics()
    elif choice == '5':
        exit()
    else:
        print("Choix invalide, réessayez.")
        show_main_menu()

"""
Show the rocket list (names)
User can select a rocket to get more details about it

"""

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



"""
Show the rocket detail from the rockets.json data
Name, engine, height, diameter, nb of stages, nb of launches, the creation date, still in activity ?, ergol type, payload mass
The user can also choose to see the wikipedia website of the rocket. It will open it in his web browser
"""
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
        webbrowser.open(rocket['wikipedia_url']) #open the website in the user web browser
    show_main_menu() #back to the main menu



"""
Show the engine list as the rocket list 
"""
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




"""
Show the engine details as the rocket details
Name, associated rocket, thrust, can start multiple times ?, ergol type, height and cycle type
User can choose to see the wikipedia website 
"""
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



"""
Show the agencies list 
"""
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



"""
Show the agency details as the rocket details
Name, creation date, country,type (government or private), actual CEO
User can choose to see the wikipedia website 
"""
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



"""
Showcase some statistics :
nb of rockets, nb of engines, nb of agencies, nb of reusable engine, nb of no-reusable engines
plot some statistics :
- nb of rocket for each agencies
"""

def show_statistics():
    stats = calculate_statistics(rockets, engines, agencies)
    print("\n--- Statistiques ---")
    print(f"Nombre de fusées : {stats['rocket_count']}")
    print(f"Nombre de moteurs : {stats['engine_count']}")
    print(f"Nombre d'agences spatiales : {stats['agency_count']}")
    print(f"Moteurs réutilisables : {stats['reusable_engines']}")
    print(f"Moteurs non réutilisables : {stats['non_reusable_engines']}")

    # Créer des sous-graphes pour afficher plusieurs graphiques dans une seule figure
    fig, axes = plt.subplots(1, 3, figsize=(18, 6))

    # Placer chaque graphique sur un sous-graphique distinct
    plot_agency_rocket_count(rockets, agencies, axes[0])
    plot_top_rocket_by_launches(rockets, axes[1])
    plot_top_rocket_by_payload(rockets, axes[2])

    plt.tight_layout()  # Pour ajuster l'espacement entre les graphiques
    plt.show()  # Afficher la figure avec tous les graphiques
    show_main_menu()


"""
Main programm 
"""
show_main_menu()

    

