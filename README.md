# Space Data Visualization Tool

A Python-based project to visualize data related to space exploration, including rockets, rocket engines, and space agencies. The project provides users with detailed information about these entities and statistical visualizations. Users can interact with the program through a terminal menu, which offers intuitive options for navigation.

# Features
Rocket Details:

* View a list of rockets and their detailed specifications, such as height, diameter, number of stages, launch history, and payload capacity.
* Option to visit the rocket's Wikipedia page directly from the terminal.

Engine Details:

* Explore a list of rocket engines and their properties, including thrust, reusability, propellant type, and cycle type.
* Direct links to engine Wikipedia pages.

Space Agency Information:

* Learn about space agencies, including their founding date, country of origin, type (government or private), and current CEO.
* Access agency Wikipedia pages for more information.

Statistical Visualizations:

* Number of rockets per space agency (pie chart).
* Top 5 rockets with the most launches (bar chart).
* Top 5 rockets with the highest payload capacity (bar chart).

# Installation
**Prerequisites**

**Python 3.11** or higher.

The following Python libraries are required:
* matplotlib
* os (standard library)
* webbrowser (standard library)

**Steps**
* Clone the repository:

```

git clone https://github.com/your-repo/space-data-visualization.git
cd space-data-visualization
```

* Ensure the required dependencies are installed:

```
pip install matplotlib
```
* The database folder (database) must include three JSON files:

  - rockets.json — Data about rockets.
  - engines.json — Data about engines.
  - agencies.json — Data about space agencies.


# How to Use
**Run the main program:**

``` 
python main.py
```

* The terminal menu will appear with the following options:

  - View rocket data.
  - View engine data.
  - View space agency data.
  - Access statistics and visualizations.

* Follow the prompts to navigate through the menu and explore data or statistics.

* Choose "yes" when prompted to open the Wikipedia page of a selected rocket, engine, or agency in your default browser.

Project Structure
```

space-data-visualization/
├── database/
│   ├── rockets.json           # Rockets data
│   ├── engines.json           # Engines data
│   └── agencies.json          # Space agencies data
├── src/
│   ├── main.py                # Main program with menu
│   ├── data_loader.py         # Data loading utility
│   └── statistics.py          # Statistics and visualizations
├── test/
│   ├── test_main.py           # Main program with menu
│   ├── test_data_loader.py    # Data loading utility
│   └── test_statistics.py     # Statistics and visualizations
├── docs/                      #documentation folder
├── pyproject.toml             #useful infos about the project
├── Some projects setup files
└── README.md                  # Project documentation
```
# Statistical Features
  * **Pie Chart:** Displays the distribution of rockets by their respective space agencies.
  * **Bar Charts:**
        - Top 5 rockets with the highest number of launches.
        - Top 5 rockets with the greatest payload capacity.

These visualizations are generated using **Matplotlib.**

# Contact
For questions or suggestions, feel free to contact:

Email: **victor.blatz@estaca.eu**
GitHub: **Slooow68**
