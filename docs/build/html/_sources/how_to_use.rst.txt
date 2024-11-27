How to Use LevelSight
=====================

Step 1: Prepare Game Logs
--------------------------
- Collect player activity logs from your game.
- Ensure the logs are in `.csv` or `.json` format with the following fields:
  
  - `Level ID`
  - `Time Spent`
  - `Success/Failure Status`

Step 2: Load Data
-----------------
- Use the provided `upload` functionality to import the logs into **LevelSight**:

  .. code:: bash

      python levelsight.py --upload game_logs.csv

Step 3: Analyze Data
--------------------
- Generate insights by running the `analyze` command:

  .. code:: bash

      python levelsight.py --analyze

- View key matrices such as:
  
  - Levels completed
  - Time spent per level
  - Failure points

Step 4: Visualize Insights
--------------------------
- Open the visualization dashboard to review player behavior trends:

  .. code:: bash

      python levelsight.py --dashboard

Step 5: Export Data
-------------------
- Export processed insights for external analysis:

  .. code:: bash

      python levelsight.py --export output.csv
