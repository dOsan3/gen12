import json
import os
import openai
from modules import conversation_builder as cb
from modules import text_reader

def generate_training_data(prompt):
    # Call the OpenAI GPT-3 API
    with open("openai_api_key", "r") as key_file:
        openai_api_key = key_file.read().strip()

    os.environ["OPENAI_API_KEY"] = openai_api_key
    openai.api_key = os.getenv("OPENAI_API_KEY")

    questions_and_answer = openai.Completion.create(
      model="text-davinci-003",
      prompt=prompt
      temperature=0.7,
      max_tokens=256,
      top_p=1,
      frequency_penalty=0,
      presence_penalty=0
    )

    # Get the generated questions and answers
    questions_and_answers = response.choices[0].text.strip()

    # Process the generated questions and answers
    # You may need to adjust this code to match the format returned by GPT-3
    return json.loads(questions_and_answers)


def expand_answers(questions_and_answers):
    # "What is the purpose of the Osan3 Alpha Program?"
    # How much will Happy Org sponsor for the chatbot development?
    doc_name = "osan3-happy-org"
    train_data = []
    # llm prompt response, 'generate more diverse answers from this question' and put the answers in the form ```["answer1, answer2, ...]```
    more_answers = ["a1", "a2", "a3"]
    for i, qa_pair in enumerate(questions_and_answers):
        id = i
        question = qa_pair[0]
        answer = qa_pair[1]
        training_data_json = cb.main(doc_name, id, question, answer)
        for answer in more_answers:
          cb.add_conversation(training_data_json, question, answer)
        train_data.append(training_data_json)
    return train_data

############## Start
json_objects = []
file_name = 'loi-osan3-happy-org.txt'
file_content = text_reader.read_text_file(file_name)

### Load prompt with file content
form = "\
```[  [question, answer],  [question, answer]   ]```"
prompt = "Generate diverse questions and answers in a json list, where each question answer pair is also a list, in the example form " + form + " based on the follwoing content: ```" + file_content + "```"

questions_and_answers = generate_training_data(prompt)

#print(questions_and_answers[3][1])

training_data = expand_answers(questions_and_answers)

pretty_training_data = json.dumps(training_data, indent=4)
print(pretty_training_data)
# Ask for diverse answers for each question.
# put answers in an array [a1, a2, a3]

#print(json.dumps(cb.json_objects, indent=2))