def calculate_score(participant):
    # Calculate the score for a participant based on the given points for each food
    return participant['chickenwings'] * 5 + participant['hamburgers'] * 3 + participant['hotdogs'] * 2

def scoreboard(participants):
    # Calculate the score for each participant and create a scoreboard
    scoreboard = []
    for participant in participants:
        score = calculate_score(participant)
        scoreboard.append({'name': participant['name'], 'score': score})
    
    # Sort the scoreboard by score (descending) and name (ascending)
    scoreboard.sort(key=lambda x: (-x['score'], x['name']))
    return scoreboard

# Example 
participants = [
    {'name': "Habanero Hillary", 'chickenwings': 5, 'hamburgers': 17, 'hotdogs': 11},
    {'name': "Big Bob", 'chickenwings': 20, 'hamburgers': 4, 'hotdogs': 11}
]

result = scoreboard(participants)
print(result)
