```python
import random
from datetime import datetime

def chatbot_response(message):
    message = message.lower().strip()

    if any(word in message for word in ["hello", "hi", "hey"]):
        return random.choice([
            "Hello! How can I help you?",
            "Hi there! Nice to meet you.",
            "Hey! What would you like to talk about?"
        ])

    elif "your name" in message:
        return "I am PyBot, your Python chatbot!"

    elif "how are you" in message:
        return "I'm doing great! Thanks for asking."

    elif "time" in message:
        return "The current time is " + datetime.now().strftime("%I:%M %p")

    elif "date" in message:
        return "Today's date is " + datetime.now().strftime("%d-%m-%Y")

    elif "joke" in message:
        return random.choice([
            "Why do programmers prefer dark mode? Because light attracts bugs!",
            "Why was the Python programmer confused? Because life had too many loops!",
            "Why do Python programmers wear glasses? Because they cannot C!"
        ])

    elif "python" in message:
        return "Python is a popular programming language used in AI, automation, and web development."

    elif "help" in message:
        return "You can ask me about my name, the time, the date, Python, or a joke."

    elif any(word in message for word in ["bye", "goodbye", "exit"]):
        return "Goodbye! Keep learning Python. See you again!"

    else:
        return "I'm not sure how to answer that yet. Type 'help' to see what I can do."


def start_chatbot():
    print("=" * 40)
    print("       WELCOME TO PYBOT 🤖")
    print("=" * 40)
    print("Type 'help' to see what I can do.")
    print("Type 'bye' to end the conversation.\n")

    while True:
        user_message = input("You: ")
        response = chatbot_response(user_message)

        print("PyBot:", response)

        if any(word in user_message.lower().strip().split()
               for word in ["bye", "goodbye", "exit"]):
            break


if __name__ == "__main__":
    start_chatbot()
```
