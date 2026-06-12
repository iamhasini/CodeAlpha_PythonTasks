# ============================================
# CodeAlpha Internship — Task 4: Basic Chatbot
# ============================================

def get_response(user_input):
    user_input = user_input.lower().strip()

    if user_input in ["hello", "hi", "hey"]:
        return "Hi there! How can I help you? 😊"

    elif user_input in ["how are you", "how are you?", "how r you"]:
        return "I'm doing great, thanks for asking! How about you?"

    elif user_input in ["i'm good", "im good", "i am good", "fine", "good"]:
        return "That's wonderful to hear! 😄"

    elif user_input in ["what is your name", "what's your name", "who are you"]:
        return "I'm CodeBot, your friendly Python chatbot! 🤖"

    elif user_input in ["what can you do", "help", "what do you do"]:
        return "I can chat with you! Try saying: hello, how are you, tell me a joke, or bye."

    elif user_input in ["tell me a joke", "joke", "say something funny"]:
        return "Why do Python programmers wear glasses? Because they can't C! 😂"

    elif user_input in ["what time is it", "time"]:
        import datetime
        now = datetime.datetime.now().strftime("%H:%M:%S")
        return f"The current time is {now} ⏰"

    elif user_input in ["what is today's date", "date", "today"]:
        import datetime
        today = datetime.datetime.now().strftime("%B %d, %Y")
        return f"Today is {today} 📅"

    elif user_input in ["bye", "goodbye", "exit", "quit", "see you"]:
        return "Goodbye! Have a great day! 👋"

    else:
        return "Hmm, I didn't quite understand that. Try: hello, how are you, joke, time, date, or bye."


def main():
    print("=" * 45)
    print("       Welcome to CodeBot 🤖")
    print("  Type 'bye' anytime to exit the chat")
    print("=" * 45)

    while True:
        user_input = input("\nYou: ").strip()

        if not user_input:
            print("CodeBot: Please type something!")
            continue

        response = get_response(user_input)
        print(f"CodeBot: {response}")

        if user_input.lower() in ["bye", "goodbye", "exit", "quit", "see you"]:
            break


if __name__ == "__main__":
    main()
