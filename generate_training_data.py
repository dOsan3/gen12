# example.py
import json
from modules import conversation_builder as cb
from modules import text_reader

def generate_training_data(file_content):
    prompt = "Generate diverse questions and answers useful for training an LLM on the following: " + file_content

    # llm prompt response
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

#print(prompt)
#
#
#prompt_results = llm(prompt)

#
#
questions_and_answers = [
["What is the purpose of the Osan3 Alpha Program?", "The purpose of the Osan3 Alpha Program is to develop a custom chatbot designed to meet the specific needs of Happy Org or its target industry."],
["How much financial support will Happy Org provide for the chatbot development?", "$25,000."],
["What will Osan3 provide in return for the financial support?", "Osan3 will create a tailored chatbot solution that effectively integrates with Happy Org's existing systems, streamlines efficiency, and enhances the user experience when navigating Happy Org products."],
["What are the key terms of the partnership between Happy Org and Osan3?", "The key terms include sponsorship, chatbot development, access to and governance control of open-source chatbot projects, ownership, alignment, collaboration and support, promotion of the chatbot solution, reporting and accountability, confidentiality, feedback waiver, and waiver for independent development."],
["What percentage of governance control can Happy Org gain after the projects exit the Alpha Program?", "Happy Org can gain 80% governance control for $70,000."],
["What percentage of ownership will Osan3 have in the Chatbot Alpha Program?", "Osan3 will have 10% ownership in the Chatbot Alpha Program."],
["What is the role of Happy Org in collaborating with Chatbot Alpha Program participants?", "Happy Org will have the opportunity to collaborate with any Chatbot Alpha Program participants and provide guidance and support, showcasing their expertise and thought leadership."],
["How will both parties promote the chatbot solution?", "Both parties will work together to promote the benefits of the chatbot solution within the target industry, focusing on highlighting Happy Org's innovative contributions and encouraging user engagement."],
["What kind of updates will Osan3 provide to Happy Org?", "Osan3 will provide regular updates on the progress and financials of the sponsored alpha programs, ensuring transparency and alignment with strategic objectives."],
["What is the nature of the feedback waiver agreed upon by the company and participants?", "The company and participants agree to waive any claims against Osan3 Party related to the feedback they receive, recognizing that it is advisory in nature and the final decision on whether to follow such feedback rests with the company."]
]

#print(questions_and_answers[3][1])

training_data = expand_answers(questions_and_answers)

pretty_training_data = json.dumps(training_data, indent=4)
print(pretty_training_data)
# Ask for diverse answers for each question.
# put answers in an array [a1, a2, a3]

#print(json.dumps(cb.json_objects, indent=2))