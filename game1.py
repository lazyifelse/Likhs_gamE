"""
WORK FLOW OF THE PROJECT:

1)USER WILL CHOOSE ROCK PAPER OR SCISSOR
2)COMPUTER WILL CHOOSE RANDOMLY 
3)RESULT WILL BE PRINTED 

CASES:
A-ROCK
ROCK-ROCK=TIE             
ROCK-PAPER=OUT        
ROCK-SCISSOR =WIN


B-PAPER
PAPER-ROCK=WIN
PAPER-PAPER=TIE           
PAPER-SCISSOR =OUT


C-SCISSOR
SCISSOR-ROCK=OUT
SCISSOR-PAPER=WIN
SCISSOR-SCISSOR=TIE        
"""
import random

Item_list = ["ROCK", "PAPER", "SCISSOR"]

print("🎮 Welcome to the ROCK PAPER SCISSOR Game! GOOD LUCK! 🍀")
USER_CHOICE = input("👉 Enter your choice (ROCK, PAPER, SCISSOR): ").strip().upper()

if USER_CHOICE not in Item_list:
    print("❌ Invalid input! Please enter ROCK, PAPER, or SCISSOR.\n💡 Created by LIKHITH")
else:
    COMPUTER_CHOICE = random.choice(Item_list)
    print(f"🧍 You chose: {USER_CHOICE} \n🖥️ Computer chose: {COMPUTER_CHOICE}")

    if USER_CHOICE == COMPUTER_CHOICE:
        print("🤝 It's a Tie! Same choice by both players.\n✨ Created by LIKHITH")

    elif USER_CHOICE == "ROCK":
        if COMPUTER_CHOICE == "SCISSOR":
            print("💥 ROCK smashes SCISSOR!\n🎉 Congratulations, you won!\n✨ Created by LIKHITH")
        else:
            print("📄 PAPER covers ROCK.\n😢 Oops, you lost. Better luck next time!\n✨ Created by LIKHITH")

    elif USER_CHOICE == "PAPER":
        if COMPUTER_CHOICE == "ROCK":
            print("📄 PAPER covers ROCK.\n🎉 Congratulations, you won!\n✨ Created by LIKHITH")
        else:
            print("✂️ SCISSOR cuts PAPER.\n😢 Oops, you lost. Better luck next time!\n✨ Created by LIKHITH")

    elif USER_CHOICE == "SCISSOR":
        if COMPUTER_CHOICE == "PAPER":
            print("✂️ SCISSOR cuts PAPER.\n🎉 Congratulations, you won!\n✨ Created by LIKHITH")
        else:
            print("💥 ROCK smashes SCISSOR.\n😢 Oops, you lost. Better luck next time!\n✨ Created by LIKHITH")
