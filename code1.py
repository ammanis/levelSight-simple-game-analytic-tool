import time

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

# Function to get player stats
def get_player_stats(username):
    if username in player_data:
        stats = player_data[username]['levels']
        for level, data in stats.items():
            print(f"Level {level}:")
            print(f"  Time Spent: {data['time_spent']:.2f} seconds")
            print(f"  Failures: {data['failures']}")
    else:
        print("No data found for the given username.")

# Example usage
username = "Player1"
start_level(username, 1)
time.sleep(2)  # Simulate time spent in level
end_level(username, 1)
record_failure(username, 1)
record_failure(username, 1)

get_player_stats(username)
