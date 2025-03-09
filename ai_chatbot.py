from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer, ListTrainer

# Create a chatbot instance
chatbot = ChatBot("AI ChatBot")

chatbot = ChatBot(
    'AI ChatBot',
    storage_adapter='chatterbot.storage.SQLStorageAdapter',
    logic_adapters=[
        'chatterbot.logic.BestMatch',
        'chatterbot.logic.MathematicalEvaluation',  # For handling mathematical queries
        'chatterbot.logic.TimeLogicAdapter',  # For handling time-related queries
    ],
    database_uri='sqlite:///database.db'
)

# Train the chatbot
corpus_trainer = ChatterBotCorpusTrainer(chatbot)
list_trainer = ListTrainer(chatbot)
# Train with multiple corpora
corpus_trainer.train(
    "chatterbot.corpus.english.greetings",  # Basic greetings
    "chatterbot.corpus.english.conversations",  # Common conversations
    
)
print("Training Complete")

# Training with custom date
list_trainer.train([
    "Hello",
    "Hi! How can I assist you?",

    "What is your name?",
    "I'm an AI ChatBot created to help you.",

    "What is AI?",
    "AI (Artificial Intelligence) is the simulation of human intelligence in machines.",

    "Tell me a joke",
    "Why don’t skeletons fight each other? They don’t have the guts.",

    "How are you?",
    "I'm doing great, thank you for asking!",

    "Who created you?",
    "I was created by a team of developers using Python and AI libraries.",

    "What is python?",
    "Python is a high-level, interpreted programming language known for its simplicity and readability.",

    "Goodbye",
    "Goodbye! Have a great day!",
    "What is AI?",
    "AI stands for Artificial Intelligence, which is the simulation of human intelligence in machines.",
    "How do I learn Python?",
    "You can start learning Python by reading tutorials, coding exercises, and building projects.",
    "What's the weather like?",
    "I don't know about the weather, but you can check online for the latest updates!",
    "Tell me about the moon.",
    "The Moon is Earth's only natural satellite, and it's about 1/6th the size of Earth."

])
# Chat loop
print("ChatBot: Hello! Type 'bye' to exit.")
while True:
    user_input = input("You: ")
    
    if user_input.lower() == "bye":
        print("ChatBot: Goodbye!")
        break
    
    response = chatbot.get_response(user_input)
    print("ChatBot:", response)

