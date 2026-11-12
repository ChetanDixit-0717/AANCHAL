
from chatbot.chatbot import get_chatbot_response


def main():

    question = "Why is nutrition important for children?"

    response = get_chatbot_response(question)

    print("\nUser:", question)
    print("\nAANCHAL:", response)


if __name__ == "__main__":
    main()
