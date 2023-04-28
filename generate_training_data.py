# 1. generate_answers: mock response with two questions and answers from file in correct form.
# 2. expand_answers: mock up up with several answers (some relevant and some non-diverse, too).

def generate_training_data(file_content):
    prompt = "Generate diverse questions and answers useful for training an LLM on the following: " + file_content
    #questions_and_answers = generate_answers(prompt)
    # To be replaced with `generate_answers` output
    questions_and_answers =
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

    expanded_questions_and_answers = expand_answers(questions_and_answers)
    save(expanded_questions_and_answers)

def expand_answers(questions_and_answers):
    training_data = []
    # "What is the purpose of the Osan3 Alpha Program?"
    # How much will Happy Org sponsor for the chatbot development?
    for i, qa_pair in enumerate(questions_and_answers):
        #question = qa_pair["question"]
        # To be replaced with `generate_answers` output
        question = "What is the purpose of the Osan3 Alpha Program?"
        # ["a1", "a2", ...]
        more_answers = generate_more_answers(question)

        for answer in more_answers:
            training_data.append(create_training_data_entry(i, question, answer))

    return training_data

def create_training_data_entry(id, question, answer):
    return {
        "id": f"identity_{id}",
        "conversations": [
            {
                "from": "human",
                "value": question
            },
            {
                "from": "gpt",
                "value": answer
            }
        ]
    }

def save(expanded_questions_and_answers):
    # Save the expanded questions and answers to a file in the desired format
    with open("training_data.json", "w") as f:
        json.dump(expanded_questions_and_answers, f)
