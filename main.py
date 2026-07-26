import os
import json
import sys
from typing import Any
from dotenv import load_dotenv
from prompts import system_prompt
from call_function import available_functions, function_map, call_function

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
    parser.add_argument("--verbose", action="store_true", help="Enable verbose mode")

    args = parser.parse_args()
    user_prompt = args.user_prompt
    verbose = args.verbose



    #AI Block
    client = OpenAI(
        base_url="https://openrouter.ai/api/v1",
        api_key=api_key
    )

    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_prompt},
    ]

    #LOOK AT THIS, this was for type checker later in printing block
    response = None
    
    #available_functions was list of dict json, schema. so this was used to satisfy type checker
    tools_parameter: Any = available_functions
    def call_llm():
        return client.chat.completions.create(
            model= "openrouter/free",
            messages= messages,
            temperature = 0.0,
            tools = tools_parameter
        )

    for call in range(20):
        if call == 19:
            sys.exit(1)
        response = call_llm()
        if response.usage is None or not response.usage.prompt_tokens:
            raise RuntimeError

        message = response.choices[0].message
        messages.append(message)
        if message.tool_calls:
            for tool_call in message.tool_calls:
                result_message = call_function(tool_call, verbose)
                if not result_message.get("content"):
                    raise Exception("function_result return None")
                if verbose:
                    print(f"-> {result_message['content']}")
                messages.append(result_message)
        else:
            break

    

    #Printing Blo
    if response is None:
        raise RuntimeError("Loop never ran")
    if response.usage is None:
        raise RuntimeError("The metadata of prompts and completions tokens is None")
    final_content = response.choices[0].message.content or "Done executing tool calls."
    print(f"""
    User prompt: {user_prompt}.
    Prompt tokens: {response.usage.prompt_tokens}
    Response tokens: {response.usage.completion_tokens}
    Final Response:
    {final_content}
    """)


if __name__ == "__main__":
    main()
