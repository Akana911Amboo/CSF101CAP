#########################################
# Name: Tashi Tobden
# Course: 1 Electrical Engineering
# Student no. : 02230083
#########################################
# References
# YouTube: https://youtu.be/LpZmZs2_BC4?si=SxvYGCRSv_TGRYV4
# Tutorial: How to Easily Read Files in Python (Text, CSV, JSON)
# YouTube: https://youtu.be/ZYFug798Tcw?si=w4Aba-eVDWV1A1km
# Linkedin: Working with file input and output - Python Tutorial From the course: Programming Foundations: Beyond the Fundamentals
# CSF101 Unit Guides and Notes
#########################################
# Solution
# The total score is : 49483
# Put your number here:
# input_3_cap1.txt
#########################################

# Read the input.txt file
def read_input():
    input_data = []
    with open('C:/Users/homeb/OneDrive/Desktop/main csf/CSF101CAP/CSF101CAP/input_3_cap1.txt', 'r') as file:
        file_data = file.readlines()
        for line in file_data:
            # Remove leading/trailing whitespaces and split the line into a list of values
            values = line.strip().split()
            input_data.append((values[0], values[1]))
    return input_data
# code for the calculations of the score
def calculate_score(input_data):
    scores = {'A': 1, 'B': 2, 'C': 3}
    outcomes = {'X': 0, 'Y': 3, 'Z': 6}    # store keys and values in a list
    total_score = 0

    for opponent_move, outcome in input_data:
        player_move = None
        # Conditional statement used  to give proper instructions 
        if outcome == 'X':  # you need to lose
            if opponent_move == 'A':  # Opponent chooses Rock
                player_move = 'C'  # You choose Scissor
            elif opponent_move == 'B':  # Opponent chooses Paper
                player_move = 'A'  # You choose Rock
            elif opponent_move == 'C':  # Opponent chooses Scissors
                player_move = 'B'  # You choose Paper
        elif outcome == 'Y':  # you need to draw
            player_move = opponent_move  # You choose the same as opponent
        elif outcome == 'Z':  # you need to win
            if opponent_move == 'A':  # Opponent chooses Rock
                player_move = 'B'  # You choose Paper
            elif opponent_move == 'B':  # Opponent chooses Paper
                player_move = 'C'  # You choose Scissor
            elif opponent_move == 'C':  # Opponent chooses Scissors
                player_move = 'A'  # You choose Rock

        player_score = scores[player_move] + outcomes[outcome]
        total_score += player_score 

    return total_score

# Call the functions
input_data = read_input()
final_score = calculate_score(input_data)
print(f"Total Score: {final_score}")
