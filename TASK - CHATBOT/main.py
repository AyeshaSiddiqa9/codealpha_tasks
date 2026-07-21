def get_bot_response(user_message):
    user_message=user_message.lower()
    greet=["hi","hello","hey"]
    positive_words=["good","great","fine","well","awesome","excellent","happy"]
    negative_words = ["bad","sad","tired","upset","angry"]
    # greeting
    if user_message in greet:
        return "Hello! How can I help you today?"
    
    # how are you
    elif user_message in ["how are you","how are you?"]:
        return "I'm fine, thanks! what about you?"
    
    #negative user reply
    elif ("not good" in user_message or
          "not fine" in user_message or
          "not well" in user_message or
          not set(negative_words).isdisjoint(user_message.split())):
        return "I'm sorry to hear that. I hope things get better."

    #positive user reply
    elif not set(positive_words).isdisjoint(user_message.split()):
        return "Happy to hear that!"

    # thank you
    elif user_message in ["thank you", "thanks", "thankyou"]:
        return "You're welcome! I'm always happy to help."

    # Bot name
    elif user_message in ["what is your name", "what is your name?"]:
        return "I'm PyBot, your simple Python chatbot."

    # Who created you
    elif user_message in ["who created you", "who made you", "who developed you"]:
        return "I was created as a Python internship project."

    # Help
    elif user_message == "help":
        return ("You can try saying:\n"
                "- hello\n"
                "- how are you\n"
                "- thank you\n"
                "- what is your name\n"
                "- who created you\n"
                "- bye")

    # bye
    elif user_message in ["bye","goodbye"]:
        return "Goodbye! Have a great day!"

    # default response
    else:
        return "I'm sorry, I don't understand that"
def start_chatbot():
    print("=" * 45)
    print("Welcome to PyBot!")
    print("A Simple Rule-Based Chatbot")
    print("Type 'help' to see available commands.")
    print("Type 'bye' or 'goodbye' to exit.")
    print("=" * 45)
    while True:
        user_input=input("You:").lower().strip()
        response=get_bot_response(user_input)
        print(f"Chatbot: {response}")
        if user_input in ["bye","goodbye"]:
            break
start_chatbot()
    
