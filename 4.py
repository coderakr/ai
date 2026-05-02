# chatbot 

def chatbot():
    print("Chatbot: Hello! Welcome to our store support.")
    print("Type 'exit' to end the chat.\n")

    while True:
        user_input = input("You: ").lower()

        if user_input == "exit":
            print("Chatbot: Thank you! Have a great day ")
            break

        elif "hello" in user_input or "hi" in user_input:
            print("Chatbot: Hello! How can I help you?")

        elif "order" in user_input and "status" in user_input:
            print("Chatbot: Please provide your Order ID to check the status.")

        elif "return" in user_input:
            print("Chatbot: You can return items within 7 days of delivery.")

        elif "refund" in user_input:
            print("Chatbot: Refunds are processed within 3-5 business days.")

        elif "delivery" in user_input:
            print("Chatbot: Delivery usually takes 3-7 working days.")

        elif "time" in user_input or "hours" in user_input:
            print("Chatbot: Our store is open from 9 AM to 9 PM.")

        elif "contact" in user_input:
            print("Chatbot: You can contact us at support@example.com.")

        else:
            print("Chatbot: Sorry, I didn't understand that. Can you rephrase?")


# ---------------- Main ----------------
chatbot()
