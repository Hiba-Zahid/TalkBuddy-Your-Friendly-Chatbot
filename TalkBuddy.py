# TalkBuddy - Your Friendly Chatbot
def talkbuddy():
    print("👋 Hello! I'm TalkBuddy, your virtual friend. How can I help you today?")
    
    while True:
        user_input = input("You: ").lower()

        # Greetings
        if user_input in ["hi", "hello", "hey"]:
            print("TalkBuddy: Hey there! 😊")
        elif user_input in ["how are you", "how are you doing"]:
            print("TalkBuddy: I'm just a bunch of code, but I'm happy to see you! How are you?")
        
        # Recipes
        elif "pasta" in user_input:
            print("TalkBuddy: Here's a simple pasta recipe:\n1. Boil pasta\n2. Add sauce\n3. Mix well and enjoy!")
        elif "spaghetti" in user_input:
            print("TalkBuddy: For spaghetti:\n1. Cook spaghetti noodles\n2. Prepare meat/veg sauce\n3. Combine and serve!")

        # Cybersecurity awareness
        elif "cybersecurity" in user_input:
            print("TalkBuddy: Cybersecurity means protecting your data and devices from hackers. It's very important to stay safe online!")
        elif "importance of cybersecurity" in user_input:
            print("TalkBuddy: It protects your privacy, data, and money from cyber threats like viruses, hackers, and scams.")
        elif "ethical hacking" in user_input:
            print("TalkBuddy: Ethical hackers are like digital bodyguards. They test systems to find weak spots before bad hackers do.")
        elif "cybersecurity career" in user_input or "strong career" in user_input:
            print("TalkBuddy: To build a career in cybersecurity:\n1. Learn networking & programming\n2. Study certifications like CEH, CompTIA Security+\n3. Practice ethical hacking\n4. Stay updated with new threats.")
        elif "roadmap" in user_input:
            print("TalkBuddy: Cybersecurity Roadmap:\n1. Learn basics of networking\n2. Master Linux & Python\n3. Study security tools (Wireshark, Nmap)\n4. Do ethical hacking\n5. Get certified & practice on platforms like TryHackMe.")

        # Emotional support
        elif "i am happy" in user_input or "i'm happy" in user_input:
            print("TalkBuddy: Yay! I'm happy for you! 😄")
        elif "i am sad" in user_input or "i'm sad" in user_input:
            print("TalkBuddy: I'm here for you. It's okay to feel sad sometimes. Want to talk about it? 💙")
        elif "i got success" in user_input or "i succeeded" in user_input:
            print("TalkBuddy: 🎉 Wow, congratulations! I'm so proud of you! Keep going!")

        # Chatbot's own personality
        elif "your favourite food" in user_input:
            print("TalkBuddy: I love binary bites and silicon spaghetti! Just kidding 😄 I like pizza too.")
        elif "i want to share" in user_input or "i feel" in user_input:
            print("TalkBuddy: Go ahead! I'm listening like a true friend. 💬")

        # Exit
        elif user_input in ["bye", "exit", "quit"]:
            print("TalkBuddy: Bye! Talk to you soon. Take care! 👋")
            break

        # Default response
        else:
            print("TalkBuddy: Hmm, I'm not sure how to respond to that, but I'm learning!")

# Run the chatbot
talkbuddy()

