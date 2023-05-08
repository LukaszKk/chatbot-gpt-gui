import openai


class Chatbot:
    API_KEY = "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"

    def __init__(self):
        openai.api_key = Chatbot.API_KEY

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
