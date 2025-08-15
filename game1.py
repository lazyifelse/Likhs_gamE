import random

while True:
    
    Item_list = ["ROCK", "PAPER", "SCISSOR"]
    
    user_score = 0
    computer_score = 0
    tie_count = 0

    print("🎮 Welcome to the ROCK PAPER SCISSOR Game! GOOD LUCK! 🍀")
    USER_CHOICE = input("👉 Enter your choice (ROCK, PAPER, SCISSOR): ").strip().upper()

    if USER_CHOICE not in Item_list:
        print("❌ Invalid input! Please enter ROCK, PAPER, or SCISSOR.\n💡 Created by LRH")
    else:
        COMPUTER_CHOICE = random.choice(Item_list)
        print(f"🧍 You chose: {USER_CHOICE} \n🖥️ Computer chose: {COMPUTER_CHOICE}")

        if USER_CHOICE == COMPUTER_CHOICE:
            print("🤝 It's a Tie! Same choice by both players.\n✨ Created by LRH")
            tie_count += 1


        elif USER_CHOICE == "ROCK":
            if COMPUTER_CHOICE == "SCISSOR":
                print("💥 ROCK smashes SCISSOR!\n🎉 Congratulations, you won!\n✨ Created by LRH")
                user_score += 1

            else:
                print("📄 PAPER covers ROCK.\n😢 Oops, you lost. Better luck next time!\n✨ Created by LRH")
                computer_score += 1


        elif USER_CHOICE == "PAPER":
            if COMPUTER_CHOICE == "ROCK":
                print("📄 PAPER covers ROCK.\n🎉 Congratulations, you won!\n✨ Created by LRH")
                user_score += 1

            else:
                print("✂️ SCISSOR cuts PAPER.\n😢 Oops, you lost. Better luck next time!\n✨ Created by LRH")
                computer_score += 1


        elif USER_CHOICE == "SCISSOR":
            if COMPUTER_CHOICE == "PAPER":
                print("✂️ SCISSOR cuts PAPER.\n🎉 Congratulations, you won!\n✨ Created by LRH")
                user_score += 1

            else:
                print("💥 ROCK smashes SCISSOR.\n😢 Oops, you lost. Better luck next time!\n✨ Created by LRH")
                computer_score += 1


    print(f"\n📊 Scoreboard: You: {user_score} | Computer: {computer_score} | Ties: {tie_count}")

    play_again = input("Do you want to play again? (yes/no): ").strip().lower()
    if play_again not in ["yes", "y"]:
        print("👋 Thanks for playing! \n✨ Created by LRH")
        break
