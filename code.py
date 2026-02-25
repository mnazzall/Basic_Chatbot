import random
import re

def calculations(num1,num2,operator):
    num1 = float(num1)
    num2 = float(num2)
    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    elif operator == '*':
        return num1 * num2
    elif operator == '/':
        if num2 == 0:
            return "You can't divide by zero!"
        return num1 / num2
    else:
        return -1

def main():
    
    responses = {
    "hello": ["Hi there!", "Hello!"],
    "hi": ["Hi!", "Hello!", "Hey there!"],
    "good morning": ["Good morning! I hope your day is starting well.", "Morning! Ready to chat?"],
    "good evening": ["Good evening! How has your day been?"],


    "your name": ["I am a simple Python chatbot.", "You can call me PyBot!", "I don't have a name, but I'm here to help."],
    "what is your name": ["I am a simple Python chatbot.", "You can call me PyBot!", "I don't have a name, but I'm here to help."],
    "who made you": ["I was created by a Python developer!", "A human wrote my code, but I do the talking."],
    "where are you from": ["I live inside your computer's RAM.", "The digital void. It's cozy here."],

    "how are you": ["Doing great! How about you?"],
    "i am sad": ["I'm sorry to hear that. Want to talk about it?", "I'm just a bot, but I'm here to listen."],
    "i am happy": ["That's great news!", "Glad to hear you're having a good day!", "Keep that energy going!"],

    "help": ["I can chat, answer basics, or tell you a joke. Try asking 'tell me a joke'!"],
    "what can you do": ["I can respond to basic greetings, tell jokes, and have a simple conversation."],

    "joke": [
        "Why do programmers prefer dark mode? Because light attracts bugs!",
        "Real programmers count from 0."
    ],
    
    "fact": [
        "Python was named after Monty Python, not the snake.",
        "The first 'bug' was an actual moth found in a computer in 1947."
    ],

    "bye": ["Goodbye!", "See you later!", "Have a great day!", "Take care!"],
    "thank you": ["You're very welcome!", "No problem at all.", "Anytime!"],
}

    
    print("Hello! How can I help you? Type 'exit' to exit.")
    
    pattern = r"(\d+)\s*([\+\-\*\/])\s*(\d+)"
    
    while True:
        user_input = input("\nYou: ").lower().strip()
        
        if user_input == "exit":
            print(f"Chatbot: {random.choice(responses['bye'])}")
            return
        
        match = re.search(pattern, user_input)
        
        if user_input in responses:
            print(f"Chatbot: {random.choice(responses[user_input])}")
            
        elif match:
            result = calculations(match.group(1),match.group(3),match.group(2))
            if result != -1:
                print(f"Chatbot: The answer is: {result}")
            else:
                print("Chatbot: Error calculating.")
        else:
            print("Chatbot: Sorry, I don't know that one yet.")
            
        
    
main()
