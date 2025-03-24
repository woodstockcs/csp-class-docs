import random

def roll_die():
    """Roll a 6-sided die and return the result."""
    return random.randint(1, 6)

def get_player_choice():
    """Get and validate player's choice to roll or hold."""
    while True:
        choice = input("Roll or hold? (r/h): ").lower()
        if choice in ['r', 'h']:
            return choice
        print("Invalid input. Please enter 'r' to roll or 'h' to hold.")

def process_roll(roll, turn_score, turn_rolls):
    """Process the result of a die roll and update turn information."""
    turn_rolls.append(roll)
    print(f"You rolled: {roll}")
    
    if roll == 1:
        print("Oops! You rolled a 1 and lost your turn points!")
        return 0, True  # Return 0 points and True for end turn
    else:
        new_turn_score = turn_score + roll
        print(f"Turn total: {new_turn_score}")
        return new_turn_score, False  # Return new score and False for continue turn

def process_turn(score, target_score):
    """Process a single turn of the game."""
    turn_score = 0
    turn_rolls = []  # List to store rolls for this turn
    
    print(f"\nYour score: {score}")
    
    while True:
        choice = get_player_choice()
        
        if choice == 'h':
            print(f"You held with {turn_score} points. New total: {score + turn_score}")
            return turn_score, turn_rolls
        
        # Player chose to roll
        roll = roll_die()
        turn_score, end_turn = process_roll(roll, turn_score, turn_rolls)
        
        if end_turn:
            return 0, turn_rolls
            
        # Check if player won with this roll
        if score + turn_score >= target_score:
            print(f"You reached {score + turn_score} points and won the game!")
            return turn_score, turn_rolls

def calculate_turn_score(turn_rolls):
    """Calculate the score for a turn based on its roll history."""
    if 1 in turn_rolls:
        return 0
    return sum(turn_rolls)

def find_highest_scoring_turn(rolls_history):
    """Find the highest scoring turn and its details."""
    if not rolls_history:
        return 0, []
    
    turn_scores = [calculate_turn_score(turn) for turn in rolls_history]
    highest_score = max(turn_scores)
    highest_turn_index = turn_scores.index(highest_score)
    highest_turn_rolls = rolls_history[highest_turn_index]
    
    return highest_score, highest_turn_rolls

def find_most_common_roll(rolls_history):
    """Find the most frequently rolled number."""
    all_rolls = [roll for turn in rolls_history for roll in turn]
    if not all_rolls:
        return None, 0
    
    # Count occurrences of each possible roll (1-6)
    roll_counts = [all_rolls.count(i) for i in range(1, 7)]
    most_common = roll_counts.index(max(roll_counts)) + 1
    count = max(roll_counts)
    
    return most_common, count

def display_statistics(rolls_history):
    """Display game statistics based on roll history."""
    print("\n=== GAME STATISTICS ===")
    
    # Calculate basic statistics
    total_turns = len(rolls_history)
    total_rolls = sum(len(turn) for turn in rolls_history)
    
    print(f"Total turns played: {total_turns}")
    print(f"Total dice rolls: {total_rolls}")
    
    # Find and display highest scoring turn
    highest_score, highest_turn_rolls = find_highest_scoring_turn(rolls_history)
    print(f"Highest scoring turn: {highest_score} points")
    print(f"Rolls in highest turn: {highest_turn_rolls}")
    
    # Find and display most common roll
    most_common, count = find_most_common_roll(rolls_history)
    if most_common:
        print(f"Most common roll: {most_common} (appeared {count} times)")

def play_game():
    """Play a single-player version of the Game of Pig."""
    score = 0
    target_score = 50
    rolls_history = []  # List to store all rolls made during the game
    
    print("=== GAME OF PIG (SINGLE PLAYER) ===")
    print(f"Try to reach {target_score} points!")
    print("If you roll a 1, you lose all points for that turn.")
    print("Type 'r' to roll or 'h' to hold and add points to your score.")
    
    while score < target_score:
        turn_score, turn_rolls = process_turn(score, target_score)
        score += turn_score
        rolls_history.append(turn_rolls)
        
        if score >= target_score:
            break
    
    # Analyze and display game statistics
    display_statistics(rolls_history)

if __name__ == "__main__":
    play_game()