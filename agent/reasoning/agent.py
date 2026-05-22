from openai import OpenAI

client = OpenAI(api_key="YOUR_OPENAI_API_KEY")

def process_request(user_text):
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a healthcare assistant."},
            {"role": "user", "content": user_text}
        ]
    )

    return response.choices[0].message.content
