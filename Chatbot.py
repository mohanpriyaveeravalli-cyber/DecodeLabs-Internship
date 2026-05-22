from datetime import datetime

print("=" * 60)
print("🤖 Welcome to DecodeLabs Smart AI Chatbot")
print("Type 'bye' anytime to exit.")
print("=" * 60)

# Taking User Name
user_name = input("Before we start, what's your name? : ")

print(f"\nBot: Nice to meet you, {user_name}! 😊")

# Greeting words
greetings = [
    "hi",
    "hello",
    "hey",
    "hlo",
    "bro",
    "buddy",
    "sup"
]

# Main Chat Loop
while True:

    user = input(f"\n{user_name}: ").lower().strip()

    # Exit Condition
    if user == "bye":
        print(f"Bot: Goodbye {user_name}! Best of luck 🚀")
        break

    # Greeting Detection
    elif user in greetings:
        print("Bot: Hello! Nice to chat with you 😊")

    # AI Information
    elif "ai" in user or "artificial intelligence" in user:
        print("Bot: AI stands for Artificial Intelligence.")
        print("Bot: AI helps machines think and solve problems.")

    # Python Information
    elif "python" in user:
        print("Bot: Python is a powerful and beginner-friendly programming language.")

    # Chatbot Name
    elif "your name" in user:
        print("Bot: I am DecodeLabs Smart Assistant 🤖")

    # Time Feature
    elif "time" in user:
        current_time = datetime.now().strftime("%H:%M:%S")
        print("Bot: Current time is:", current_time)

    # Date Feature
    elif "date" in user:
        current_date = datetime.now().strftime("%d-%m-%Y")
        print("Bot: Today's date is:", current_date)

    # Joke Feature
    elif "joke" in user:
        print("Bot: Why did the computer go to therapy?")
        print("Bot: Because it had too many bugs 😂")

    # Motivation Feature
    elif "motivate" in user:
        print("Bot: Every expert was once a beginner. Keep going 🚀")

    # Sad Mood
    elif "sad" in user or "upset" in user:
        print("Bot: Don't worry. Better days are coming 🌸")

    # Happy Mood
    elif "happy" in user:
        print("Bot: That's wonderful to hear 😄")

    # Thank You
    elif "thank" in user:
        print("Bot: You're welcome 😊")

    # Internship Information
    elif "internship" in user:
        print("Bot: DecodeLabs internship helps students gain practical experience.")

    # Default Response
    else:
        print("Bot: Hmm... I don't understand that yet.")
        print("Bot: Please try another question.")
      
