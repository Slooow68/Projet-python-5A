import json
import os

def load_data(file_name):
    """
    Charge les données depuis un fichier JSON.
    """
    # Obtenir le chemin absolu du répertoire contenant le fichier test_data_loader.py
    current_dir = os.path.dirname(os.path.abspath(__file__))
    # Construire le chemin absolu vers le fichier JSON dans le dossier database
    full_path = os.path.join(current_dir, '..', '..', 'database', file_name)

    print(f"Trying to open: {full_path}")  # Debugging print pour vérifier le chemin

    # Charger les données
    with open(full_path, 'r') as f:
        return json.load(f)

def get_rockets():
    """
    Retourne les données des fusées.
    """
    return load_data('rockets.json')

def get_engines():
    return load_data('engines.json')

def get_agencies():
    return load_data('agencies.json')


