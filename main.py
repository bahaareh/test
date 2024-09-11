from dotenv import load_dotenv
import openai
import os

# Load environment variables from .env file
load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")

def ask_gpt(question):
    response = openai.Completion.create(
      engine="text-davinci-003",  # Choose the GPT engine
      prompt=question,
      max_tokens=150
    )
    return response.choices[0].text.strip()

if __name__ == "__main__":
    question = input("Ask me anything: ")
    answer = ask_gpt(question)
    print(f"GPT: {answer}")
