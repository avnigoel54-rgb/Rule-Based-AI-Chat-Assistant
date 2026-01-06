import time
import datetime
print()

current_hour = datetime.datetime.now().hour

name=input("Enter your name: ")
print()

if 5<=current_hour<=12:
    print("Good Morning ",name,"!",sep="")
elif 12<current_hour<=16:
    print("Good Afternoon ",name,"!",sep="")
elif 16<current_hour<=20:
    print("Good Evening ",name,"!",sep="")
else:
    print("Good Night ",name,"!",sep="")
print()
time.sleep(0.75)

print("Hello My friend! I am your Chat buddy.")
time.sleep(0.75)
print("I am here to assist you with anything you need.")
time.sleep(0.6)
print("Ask me basic questions..")
time.sleep(0.5)
print("Type 'exit' to end the chat.")
print()
time.sleep(0.5)

d={
    "Hi":"Hello! How can I assist you today?",
    "How are you?":"I'm very fine, thank you! How about you?",
    "What is your name?":"I am your friendly Chatbot.",
    "Motivate me":"Believe in yourself! You are capable of amazing things.",
    "Tell me a joke":"Why don't scientists trust atoms? Because they make up everything!",
    "I am feeling sad":"I'm sorry to hear that. Remember, it's okay to feel sad sometimes. Take a deep breath and know that things will get better.",
    "I am also good":"That's great to hear! If you need any assistance, feel free to ask.",
    "Thank you":"You're welcome! If you have any more questions, just ask.",
    "Good joke":"Thank you! I'm glad you liked it."
}

while(1):
    user_input=input("You: ")
    print()

    if "exit" in user_input.lower():
        time.sleep(0.5)
        print("Chatbot: It was nice chatting with you! Goodbye!")
        print()
        break

    elif user_input in d:
        time.sleep(0.5)
        print("Chatbot:",d[user_input])
        print()

    else:
        time.sleep(0.5)
        print("Chatbot: I'm sorry, I don't have an answer for that. Can you ask something else?")
        print()