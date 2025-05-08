import openai
from config import get_openai_api_key, Model
from datetime import datetime


class ChatBot:
    def __init__(self):
        self.client = openai.OpenAI(api_key=get_openai_api_key())
        self.history = []

    def chat(self, prompt, system_message="You are a helpful assistant."):
        messages = [
            {"role": "system", "content": system_message},
            *self.history,
            {"role": "user", "content": prompt},
        ]

        response = self.client.chat.completions.create(
            model=Model, messages=messages, temperature=0.7
        )
        return response.choices[0].message.content

    def run(self):
        print("AI Chatbot activated! Type 'quit' to exit.")
        while True:
            user_input = input("You: ")
            if user_input.lower() == "quit":
                break

            # Persona switching
            if "pirate" in user_input.lower():
                system_msg = "You are a pirate from the Caribbean. Say 'Arrr!' often."
            else:
                system_msg = "You are a helpful assistant."

            response = self.chat(user_input, system_msg)
            print(f"Bot: {response}")

            # Update history
            self.history.extend(
                [
                    {"role": "user", "content": user_input},
                    {"role": "assistant", "content": response},
                ]
            )


if __name__ == "__main__":
    bot = ChatBot()
    bot.run()
