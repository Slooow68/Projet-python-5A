import matplotlib.pyplot as plt

def plot_agency_rocket_count(rockets, agencies):
    """
    Affiche un camembert avec le nombre de fusées par agence spatiale.
    """
    # Comptage du nombre de fusées par agence
    agency_counts = {agency['name']: 0 for agency in agencies}
    for rocket in rockets:
        agency_name = rocket['agency']
        if agency_name in agency_counts:
            agency_counts[agency_name] += 1

    # Préparation des données pour le graphique
    labels = list(agency_counts.keys())
    sizes = list(agency_counts.values())

    # Création du graphique en camembert
    plt.figure(figsize=(8, 8))
    plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140)
    plt.title("Répartition des fusées par agence spatiale")
    plt.axis('equal')  # Assure un cercle parfait
    plt.show()

def plot_top_rocket_by_launches(rockets):
    """
    Affiche un histogramme avec le top 5 des fusées ayant le plus grand nombre de lancements.
    """
    # Trier les fusées par nombre de lancements
    rockets_sorted = sorted(rockets, key=lambda x: x['launches'], reverse=True)
    top_5_rockets = rockets_sorted[:5]
    
    # Préparer les données pour l'histogramme
    names = [rocket['name'] for rocket in top_5_rockets]
    launches = [rocket['launches'] for rocket in top_5_rockets]

    # Création de l'histogramme
    plt.figure(figsize=(10, 6))
    plt.barh(names, launches, color='skyblue')
    plt.xlabel("Nombre de lancements")
    plt.title("Top 5 des fusées avec le plus grand nombre de lancements")
    plt.gca().invert_yaxis()  # Pour que le plus grand soit en haut
    plt.show()

def plot_top_rocket_by_payload(rockets):
    """
    Affiche un graphique avec le top 5 des fusées ayant la plus grande capacité de payload.
    
    """
    # Trier les fusées par capacité de charge utile (payload mass)
    rockets_sorted = sorted(rockets, key=lambda x: x['payload_mass'], reverse=True)
    top_5_rockets = rockets_sorted[:5]

    # Préparer les données pour l'histogramme
    names = [rocket['name'] for rocket in top_5_rockets]
    payloads = [rocket['payload_mass'] for rocket in top_5_rockets]

    # Création de l'histogramme
    plt.figure(figsize=(10, 6))
    plt.barh(names, payloads, color='salmon')
    plt.xlabel("Capacité de payload (kg)")
    plt.title("Top 5 des fusées avec la plus grande capacité de payload")
    plt.gca().invert_yaxis()  # Pour que le plus grand soit en haut
    plt.show()

def calculate_statistics(rockets, engines, agencies):
    """Calcul les statistiques pour les fusées, moteurs et agences."""
    rocket_count = len(rockets)
    engine_count = len(engines)
    agency_count = len(agencies)

    # Calcul du nombre total de lancements
    total_launches = sum(rocket['launches'] for rocket in rockets)

    # Statistiques sur les moteurs
    reusable_engines = sum(1 for engine in engines if engine['reusable'])
    non_reusable_engines = engine_count - reusable_engines

    return {
        'rocket_count': rocket_count,
        'engine_count': engine_count,
        'agency_count': agency_count,
        'total_launches': total_launches,
        'reusable_engines': reusable_engines,
        'non_reusable_engines': non_reusable_engines
    }
