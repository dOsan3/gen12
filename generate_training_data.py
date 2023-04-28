# example.py
import json
from modules import conversation_builder as cb

def generate_training_data(file_content):
    prompt = "Generate diverse questions and answers useful for training an LLM on the following: " + file_content

    questions_and_answers = [
        {
            "id": "osan3-happy-org_1",
            "conversations": [
                {
                    "from": "human",
                    "value": "What is the purpose of the Osan3 Alpha Program?"
                },
                {
                    "from": "gpt",
                    "value": "The Osan3 Alpha Program aims to develop a custom chatbot for Happy Org or its target industry. The chatbot will integrate with Happy Org's existing systems, improve efficiency, and enhance the user experience when navigating Happy Org products."
                },
                {
                    "from": "human",
                    "value": "How much will Happy Org sponsor for the chatbot development?"
                },
                {
                    "from": "gpt",
                    "value": "The feedback waiver acknowledges that feedback received from Osan3 is advisory in nature and the final decision on whether to follow it rests with the company."
                }
            ]
        }
    ]


file_content = "Osan3 LOI"
prompt = "Generate diverse questions and answers useful for training an LLM on the following: " + file_content


print(json.dumps(cb.json_objects, indent=2))