import random
# 1) Welcome the player
print("🎯 Welcome to the WHY-BECAUSE Game! \n✨ Created by LRH")
# 2) Rules and directions 
rules = """
📜 RULES & HOW TO PLAY:
1. There will be exactly 2 groups.
2. Group 1 players will write WHY questions.
3. Group 2 players will write BECAUSE answers.
4. Each player can only write one sentence during their turn.
5. Questions and answers should be creative, funny, or unexpected.
6. After all inputs are collected, the computer will shuffle and randomly match questions with answers.
7. The mismatched pairs will be read aloud for laughs!
"""
print(rules)


# Ask organiser about group sizes
group1_size = int(input("Organiser, enter number of players in Group 1: "))
group2_size = int(input("Organiser, enter number of players in Group 2: "))

print("\n📜 RULES:")
print("1. Group 1 will enter 'WHY' questions.")
print("2. Group 2 will enter 'BECAUSE' answers.")
print("3. Answers will later be shuffled and matched for fun.\n")

# Collect WHY questions from Group 1
why_questions = []
print("🔹 Group 1: Enter your WHY questions.")
for i in range(group1_size):
    question = input(f"Player {i+1} from Group 1, enter a WHY question: ")
    why_questions.append(question)

# Collect BECAUSE answers from Group 2
because_answers = []
print("\n🔹 Group 2: Enter your BECAUSE answers.")
for i in range(group2_size):
    answer = input(f"Player {i+1} from Group 2, enter a BECAUSE answer: ")
    because_answers.append(answer)

# Show what was collected (just to verify)
print("\n✅ Data collected:")
print("WHY Questions:", why_questions)
print("BECAUSE Answers:", because_answers)

# Shuffle answers
random.shuffle(because_answers)

# Combine and print
print("\n🤣 HERE ARE YOUR WHY-BECAUSE COMBOS:\n")
pairs = min(len(why_questions), len(because_answers))
for i in range(pairs):
    print(f"{why_questions[i]}")
    print(f"{because_answers[i]}")
    print("-" * 40)     