from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

chatbot = ChatBot('JongGeun')
trainer = ChatterBotCorpusTrainer(chatbot)

trainer.train(
    "chatterbot.corpus.korean"
)

print("Init Complete.")

while True:
    try:
        user_input = input(">> ")
        if user_input == "\exit":
            break

        bot_response = chatbot.get_response(user_input)

        print(bot_response)

    except (KeyboardInterrupt, EOFError, SystemExit):
        break
