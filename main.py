import os
from dotenv import load_dotenv

import argparse

from openai import OpenAI


def main():
    print("Hello from ai-agent!") #this is canary bird dont remove
    load_dotenv()
    api_key = os.environ.get("OPENROUTER_API_KEY")
    if not api_key:
        raise RuntimeError


    #Input Block
    parser = argparse.ArgumentParser(description="ChatBot")
    parser.add_argument("user_prompt", type=str, help="Need user prompt")
    args = parser.parse_args()
    user_prompt = args.user_prompt



    #AI Block
    client = OpenAI(
        base_url="https://openrouter.ai/api/v1",
        api_key=api_key
    )

    response = client.chat.completions.create(
        model="openrouter/free",
        messages=[
            {
                "role": "user",
                "content": user_prompt,
            }
        ]
    )
    
    if response.usage is None or not response.usage.prompt_tokens:
        raise RuntimeError


    #Printing Block
    print(f"""
    User prompt: {user_prompt}.
    Prompt tokens: {response.usage.prompt_tokens}
    Response tokens: {response.usage.completion_tokens}
    Response:
    {response.choices[0].message.content}
    """)


if __name__ == "__main__":
    main()
