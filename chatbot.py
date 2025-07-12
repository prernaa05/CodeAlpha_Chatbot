
def chatbot():
    print("Chatbot: Hello! I'm your friendly chatbot. Type 'bye' to exit.")
    
    while True:
        user_input = input("You: ").lower().strip()

        if user_input in ['hello', 'hi', 'hey']:
            print("Chatbot: Hi there! How can I help you?")
        
        elif user_input in ['how are you', 'how are you doing']:
            print("Chatbot: I'm fine, thanks! How about you?")
        
        elif user_input in ['i am fine', 'i am good', 'i am okay']:
            print("Chatbot: Glad to hear that!")
        
        elif user_input in ['bye', 'exit', 'goodbye']:
            print("Chatbot: Goodbye! Have a great day!")
            break

        elif user_input == '':
            print("Chatbot: Please type something.")
        
        else:
            print("Chatbot: Sorry, I don't understand that yet.")

# Run the chatbot
if __name__ == "__main__":
    chatbot()
