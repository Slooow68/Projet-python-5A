import matplotlib.pyplot as plt

def plot_agency_rocket_count(rockets, agencies, ax):
    """
    Displays a pie chart with the number of rockets by space agency.
    """
    # Ensure all agencies in rockets are accounted for in the agency list
    agency_names_in_rockets = [rocket['agency'] for rocket in rockets]
    
    # Initialize agency counts for every agency in the agencies list
    agency_counts = {agency['name']: 0 for agency in agencies}
    
    # Count rockets for each agency
    for agency_name in agency_names_in_rockets:
        if agency_name in agency_counts:  # Only count valid agencies
            agency_counts[agency_name] += 1
        else:
            print(f"Warning: Agency '{agency_name}' not found in agencies list.")

    # Add any agencies from the agencies list that are not in rockets
    for agency in agencies:
        if agency['name'] not in agency_counts:
            agency_counts[agency['name']] = 0

    # Preparing data for charting
    labels = list(agency_counts.keys())
    sizes = list(agency_counts.values())

    # Pie chart creation
    ax.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140)
    ax.set_title("Répartition des fusées par agence spatiale")
    ax.axis('equal')  # Make it a perfect circle


def plot_top_rocket_by_launches(rockets, ax):
    """
    Displays a histogram with the top 5 rockets with the highest number of launches.
    """
    # Sort rockets by number of launches
    rockets_sorted = sorted(rockets, key=lambda x: x['launches'], reverse=True)
    top_5_rockets = rockets_sorted[:5]
    
    # Prepare the data for the histogram
    names = [rocket['name'] for rocket in top_5_rockets]
    launches = [rocket['launches'] for rocket in top_5_rockets]

    # Histogram creation
    ax.barh(names, launches, color='skyblue')
    ax.invert_yaxis()  # For top-to-bottom ordering
    ax.set_xlabel("Nombre de lancements")
    ax.set_title("Top 5 des fusées avec le plus grand nombre de lancements")

def plot_top_rocket_by_payload(rockets, ax):
    """
    Displays a graph with the top 5 rockets with the highest payload capacity.
    """
    # Clean and convert payload_mass to float, and filter out invalid entries
    valid_rockets = []
    for rocket in rockets:
        try:
            payload = float(rocket['payload_mass'].replace(' kg', '').replace(',', ''))
            if payload > 0:  # Only keep rockets with a valid payload greater than 0
                rocket['payload_mass'] = payload
                valid_rockets.append(rocket)
        except (ValueError, AttributeError):
            continue  # Skip rockets with invalid payload_mass

    # Sort rockets by payload mass (ascending order)
    rockets_sorted = sorted(valid_rockets, key=lambda x: x['payload_mass'], reverse=True)
    top_5_rockets = rockets_sorted[:5]  # Get top 5 rockets with the highest payloads

    # Prepare the data for the histogram
    names = [rocket['name'] for rocket in top_5_rockets]
    payloads = [rocket['payload_mass'] for rocket in top_5_rockets]

    # Histogram creation
    ax.barh(names, payloads, color='red')
    ax.invert_yaxis()  # So that the rocket with the highest capacity is on top
    ax.set_xlabel("Capacité de payload (kg)")
    ax.set_title("Top 5 des fusées avec la plus grande capacité de payload")

    # Set x-axis to start from 0
    ax.set_xlim(0, max(payloads) * 1.1)  # Adding a margin to the max payload for better visualization


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

def show_statistics(rockets, engines, agencies):
    stats = calculate_statistics(rockets, engines, agencies)
    print("\n--- Statistiques ---")
    print(f"Nombre de fusées : {stats['rocket_count']}")
    print(f"Nombre de moteurs : {stats['engine_count']}")
    print(f"Nombre d'agences spatiales : {stats['agency_count']}")
    print(f"Moteurs réutilisables : {stats['reusable_engines']}")
    print(f"Moteurs non réutilisables : {stats['non_reusable_engines']}")

    # Create subplots for displaying multiple charts in one figure
    fig, axes = plt.subplots(1, 3, figsize=(18, 6))

    # Plot each graph on a separate subplot
    plot_agency_rocket_count(rockets, agencies, axes[0])
    plot_top_rocket_by_launches(rockets, axes[1])
    plot_top_rocket_by_payload(rockets, axes[2])

    plt.tight_layout()  # To make sure the graphs don't overlap
    plt.show()  # Display the figure with all the plots
