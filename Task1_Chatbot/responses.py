import random

def get_response(user_input):

    greetings = ["hello", "hi", "hey"]
    thanks = ["thanks", "thank you"]
    goodbye = ["bye", "goodbye"]

    if any(word in user_input for word in greetings):
        return random.choice([
            "Hello! How can I help you?",
            "Hi there! Nice to meet you.",
            "Hey! What can I do for you today?"
        ])

    elif "how are you" in user_input:
        return "I'm doing well! Thanks for asking."

    elif "your name" in user_input:
        return "I am a rule-based chatbot created for the CODSOFT AI Internship."

    elif "ai" in user_input:
        return "Artificial Intelligence allows machines to simulate human intelligence."

    elif "python" in user_input:
        return "Python is a popular programming language used in AI and Data Science."

    elif any(word in user_input for word in thanks):
        return "You're welcome!"

    elif any(word in user_input for word in goodbye):
        return "Goodbye! Have a great day."

    else:
        return "Sorry, I didn't understand that."