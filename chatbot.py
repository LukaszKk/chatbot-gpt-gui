import os
import openai


class Chatbot:
    def __init__(self):
        openai.api_key = os.environ.get("OPENAI_API_KEY")

    def get_response(self, user_input):
        return openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {'role': 'user', 'content': user_input}
            ],
            temperature=0.5
        ).choices[0].message.content


if __name__ == "__main__":
    chatbot = Chatbot()
    response = chatbot.get_response("Write a joke about birds.")
    print(response)
