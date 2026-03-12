from responses import get_response

print("Welcome to the Rule-Based Chatbot")
print("Type 'bye' to exit\n")

while True:
    user_input = input("You: ").lower()

    if user_input == "bye":
        print("Bot: Goodbye!")
        break

    response = get_response(user_input)
    print("Bot:", response) 