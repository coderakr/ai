# Simple Chatbot for Customer Interaction Application

print("===================================")
print(" Welcome to Customer Support Bot ")
print("===================================")

while True:
    print("\nHow can I help you?")
    print("1. Product Information")
    print("2. Order Status")
    print("3. Complaint Registration")
    print("4. Exit")

    choice = input("Enter your choice: ")

    # Product Information
    if choice == '1':
        product = input("Enter product name: ")
        print(product, "is available in stock.")
        print("Price: Rs. 500")

    # Order Status
    elif choice == '2':
        order_id = input("Enter Order ID: ")
        print("Order", order_id, "has been shipped successfully.")

    # Complaint Registration
    elif choice == '3':
        complaint = input("Enter your complaint: ")
        print("Your complaint has been registered.")
        print("We will contact you soon.")

    # Exit
    elif choice == '4':
        print("Thank you for using Customer Support Bot!")
        break

    # Invalid Choice
    else:
        print("Invalid choice! Please try again.")