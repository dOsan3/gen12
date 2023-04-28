# example.py
import json
from modules import conversation_builder as cb
from modules import text_reader

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
############## Start

json_objects = []
file_name = 'loi-osan3-happy-org.txt'
file_content = text_reader.read_text_file(file_name)

### Load prompt with file content
form = "\
```[[Example question, Example answer],[Example question 2, Example answer 2]]```"
prompt = "Generate diverse questions and answers in the form " + form + " based on the follwoing content: ```" + file_content + "```"

print(prompt)
#
#
##prompt_results = llm(prompt)
#
#
#print(json.dumps(cb.json_objects, indent=2))