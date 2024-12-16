import matplotlib.pyplot as plt

def plot_agency_rocket_count(rockets, agencies):
    """
    Displays a pie chart with the number of rockets by space agency.
    """
    # Counting the number of rockets by agency
    agency_counts = {agency['name']: 0 for agency in agencies}
    for rocket in rockets:
        agency_name = rocket['agency']
        if agency_name in agency_counts:
            agency_counts[agency_name] += 1

    # Preparing data for charting
    labels = list(agency_counts.keys())
    sizes = list(agency_counts.values())

    # Pie chart creation
    plt.figure(figsize=(8, 8))
    plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140)
    plt.title("Répartition des fusées par agence spatiale")
    plt.axis('equal')  # make it a perfect circle
    plt.show()

def plot_top_rocket_by_launches(rockets):
    """
    Displays a histogram with the top 5 rockets with the highest number of launches
    """
    # Sort rockets by number of launches
    rockets_sorted = sorted(rockets, key=lambda x: x['launches'], reverse=True)
    top_5_rockets = rockets_sorted[:5]
    
    # Prepare the data for the histogram
    names = [rocket['name'] for rocket in top_5_rockets]
    launches = [rocket['launches'] for rocket in top_5_rockets]

    # Histogram creation
    plt.figure(figsize=(10, 6))
    plt.barh(names, launches, color='skyblue')
    plt.xlabel("Nombre de lancements")
    plt.title("Top 5 des fusées avec le plus grand nombre de lancements")
    plt.gca().invert_yaxis()  # Pour que le plus grand soit en haut
    plt.show()

def plot_top_rocket_by_payload(rockets):
    """
    Displays a graph with the top 5 rockets with the highest payload capacity.
    
    """
    # Sort rockets by payload mass
    rockets_sorted = sorted(rockets, key=lambda x: x['payload_mass'], reverse=True)
    top_5_rockets = rockets_sorted[:5]

    # Prepare the data for the histogram
    names = [rocket['name'] for rocket in top_5_rockets]
    payloads = [rocket['payload_mass'] for rocket in top_5_rockets]

    # Histogram creation
    plt.figure(figsize=(10, 6))
    plt.barh(names, payloads, color='red')
    plt.xlabel("Capacité de payload (kg)")
    plt.title("Top 5 des fusées avec la plus grande capacité de payload")
    plt.gca().invert_yaxis()  # So that the biggest capacity is on top
    plt.show()
    print(payloads)

def calculate_statistics(rockets, engines, agencies):
    """
    Calculates statistics for rockets, engines and agencies.
    """
    rocket_count = len(rockets)
    engine_count = len(engines)
    agency_count = len(agencies)

    # Engines statistics
    reusable_engines = sum(1 for engine in engines if engine['reusable'])
    non_reusable_engines = engine_count - reusable_engines

    return {
        'rocket_count': rocket_count,
        'engine_count': engine_count,
        'agency_count': agency_count,
        'reusable_engines': reusable_engines,
        'non_reusable_engines': non_reusable_engines
    }