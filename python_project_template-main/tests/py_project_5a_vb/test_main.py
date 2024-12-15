from test_data_loader import get_rockets, get_engines, get_agencies

rockets = get_rockets()

def show_rockets_list():
    print("\nListe des fusées :")
    for i, rocket in enumerate(rockets, 1):
        print(f"{i}. {rocket['name']}")

show_rockets_list()