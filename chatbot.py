import os
from openai import OpenAI
from dotenv import load_dotenv

# Carga tu clave de API desde el archivo .env
load_dotenv()
client = OpenAI(api_key=os.getenv("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"))

def chat():
    print("🤖 Chatbot IA (escribe 'salir' para terminar)\n")
    conversation = []

    while True:
        user_input = input("Tú: ")
        if user_input.lower() == "salir":
            break

        conversation.append({"role": "user", "content": user_input})

        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=conversation
        )

        bot_reply = response.choices[0].message.content
        print("Bot:", bot_reply)
        conversation.append({"role": "assistant", "content": bot_reply})

if __name__ == "__main__":
    chat()
