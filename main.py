import time

# Simulate a simple game state using global variables, representing "memory"
player_health = 100
player_score = 0
game_over = False
game_round = 1

print("--- Simulating a Simple Game ---")
print("Initial State: Health={}, Score={}".format(player_health, player_score))
print("--------------------------------")

while not game_over:
    print(f"\n--- Round {game_round} ---")
    
    # Simulate game events affecting "memory" variables
    player_health -= 10 # Player takes damage
    player_score += 50  # Player gains score

    print(f"Current State: Health={player_health}, Score={player_score}")

    # --- SIMULATED REVERSE ENGINEERING / MEMORY MANIPULATION ---
    # This section demonstrates how an external process (or a "cheat engine")
    # might find and modify a value in the program's "memory" (here, a variable).
    # In a real scenario, this would involve attaching to another process and finding
    # the memory address of these variables, then writing new values to them.
    
    if game_round == 3:
        print("\n[REVERSE ENGINEERING INTERVENTION DETECTED]")
        print(f"  * A 'cheat' is attempting to modify player_health from {player_health}...")
        player_health = 100 # Restore health to max, simulating a health cheat
        print(f"  * player_health successfully set to {player_health}!")
    
    if game_round == 5:
        print("\n[REVERSE ENGINEERING INTERVENTION DETECTED]")
        print(f"  * A 'cheat' is attempting to modify player_score from {player_score}...")
        player_score = 99999 # Set score to a very high value, simulating a score cheat
        print(f"  * player_score successfully set to {player_score}!")
    # --- END SIMULATED REVERSE ENGINEERING ---

    if player_health <= 0:
        game_over = True
        print("\nGAME OVER! Your health dropped to 0.")
    
    game_round += 1
    time.sleep(1) # Pause for a second to simulate real-time game

print("\n--- Game Ended ---")
print(f"Final Score: {player_score}")
print("------------------")
