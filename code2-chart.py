import time
import matplotlib.pyplot as plt

# Sample data storage
player_data = {}

# Function to start tracking a level
def start_level(username, level):
    if username not in player_data:
        player_data[username] = {'levels': {}}
    
    if level not in player_data[username]['levels']:
        player_data[username]['levels'][level] = {'time_spent': 0, 'failures': 0}
    
    player_data[username]['levels'][level]['start_time'] = time.time()

# Function to end tracking a level
def end_level(username, level):
    if username in player_data and level in player_data[username]['levels']:
        start_time = player_data[username]['levels'][level].pop('start_time', None)
        if start_time:
            time_spent = time.time() - start_time
            player_data[username]['levels'][level]['time_spent'] += time_spent

# Function to record a failure
def record_failure(username, level):
    if username in player_data and level in player_data[username]['levels']:
        player_data[username]['levels'][level]['failures'] += 1

# Function to visualize player stats
def visualize_player_stats(username):
    if username in player_data:
        stats = player_data[username]['levels']
        levels = list(stats.keys())
        time_spent = [data['time_spent'] for data in stats.values()]
        failures = [data['failures'] for data in stats.values()]
        
        # Create bar chart
        x = range(len(levels))
        plt.figure(figsize=(10, 6))

        plt.bar(x, time_spent, width=0.4, label='Time Spent (s)', align='center', alpha=0.7)
        plt.bar(x, failures, width=0.4, label='Failures', align='edge', color='orange', alpha=0.7)

        plt.xlabel('Levels')
        plt.ylabel('Metrics')
        plt.title(f"Player Stats for {username}")
        plt.xticks(x, [f"Level {lvl}" for lvl in levels])
        plt.legend()

        plt.tight_layout()
        plt.show()
    else:
        print("No data found for the given username.")

# Example usage
username = "Player1"
start_level(username, 1)
time.sleep(3)  # Simulate time spent in level
end_level(username, 1)
record_failure(username, 1)
record_failure(username, 1)

start_level(username, 2)
time.sleep(5)  # Simulate time spent in another level
end_level(username, 2)
record_failure(username, 2)

# Visualize stats
visualize_player_stats(username)
