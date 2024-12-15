import json

def load_data(file_name):
    """
    Charge les données depuis un fichier JSON.
    """
    with open(file_name, 'r') as f:
        return json.load(f)

def get_rockets():
    return load_data('database/rockets.json')

def get_engines():
    return load_data('database/engines.json')

def get_agencies():
    return load_data('database/agencies.json')


