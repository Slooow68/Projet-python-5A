import webbrowser
from test_data_loader import get_rockets, get_engines, get_agencies

rockets = get_rockets()

def show_rockets_list():
    print("\nListe des fusées :")
    for i, rocket in enumerate(rockets, 1):
        print(f"{i}. {rocket['name']}")

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
    
show_rocket_details(rockets['Falcon 9'])
