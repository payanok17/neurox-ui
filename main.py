import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

def chat(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are NeuroX, personal AI of Kevin Payano."},
            {"role": "user", "content": prompt}
        ]
    )
    return response.choices[0].message.content.strip()

if __name__ == "__main__":
    prompt = input("Say something: ")
    print(chat(prompt))
