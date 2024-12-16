Modules Overview
================

The project consists of the following key modules:

**main.py**

- Manages the main program and user interface.
- Provides options to view data, statistics, and visualizations.

**data_loader.py**

- Handles loading of JSON data from the `database/` directory.
- Functions:
  
  - `get_rockets()`: Loads data from `rockets.json`.
  - `get_engines()`: Loads data from `engines.json`.
  - `get_agencies()`: Loads data from `agencies.json`.

**statistics.py**

- Generates statistics and visualizations using `matplotlib`.
- Functions:
  
  - `calculate_statistics()`: Computes key statistics.
  - `plot_agency_rocket_count()`: Displays a pie chart of rockets by agency.
  - `plot_top_rocket_by_launches()`: Displays a bar chart of rockets by launch count.
  - `plot_top_rocket_by_payload()`: Displays a bar chart of rockets by payload.