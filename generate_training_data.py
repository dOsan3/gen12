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
        question = "What is the purpose of the Osan3 Alpha Program?"
        # To be replaced with `generate_more_answers` output
        more_answers = generate_more_answers(question)
        more_answers = [
            "The purpose of the Osan3 Alpha Program is to develop a custom chatbot designed to meet the specific needs of Happy Org or its target industry. The program aims to create a tailored solution that effectively integrates with Happy Org's existing systems, streamlines efficiency, and enhances the user experience when navigating Happy Org products. By partnering with Happy Org, Osan3 also seeks to foster innovation and collaboration, ultimately promoting the benefits of the chatbot solution within the target industry.",
            "The purpose of the Osan3 Alpha Program is to foster the development of custom chatbot solutions tailored to meet the specific needs of organizations, like Happy Org, or their target industries. The program aims to create innovative, effective, and user-friendly chatbot systems that integrate seamlessly with the existing systems of the participating organizations, streamline efficiency, and enhance user experience when navigating their products. Through partnerships, sponsorships, and collaboration, the Osan3 Alpha Program seeks to drive innovation and growth in chatbot technology and applications, while promoting the benefits of these solutions within the target industries.",
            "The purpose of the Osan3 Alpha Program is to foster the development of innovative chatbot solutions tailored to meet the specific needs of Happy Org or its target industry. By providing financial support and collaborating with Osan3, Happy Org aims to create a custom chatbot that effectively integrates with its existing systems, streamlines efficiency, and enhances the user experience when navigating Happy Org products. Through the program, both parties will work together to promote the benefits of the chatbot solution within the target industry, positioning Happy Org as an industry innovator and encouraging user engagement.",
            "The purpose of the Osan3 Alpha Program is to foster the development of innovative chatbot solutions tailored to meet the specific needs of Happy Org or its target industry. By providing financial support and collaborating with Osan3, Happy Org aims to create a custom chatbot that effectively integrates with its current systems, streamlines efficiency, and enhances the user experience when navigating Happy Org products. Through the program, both parties will work together to promote the benefits of the chatbot solution within the target industry, positioning Happy Org as an industry innovator and encouraging user engagement."
         ]

        for answer in more_answers:
            training_data.append(create_training_data_entry(i, question, answer))

    return training_data
    # To be replaced with results from for loop above results in training_data
    return {
      "id": "osan3-happy-org_1",
      "conversations": [
        {
        "from": "human",
        "value": "What is the purpose of the Osan3 Alpha Program?"
        },
        {
        "from": "gpt",
        "value": "The purpose of the Osan3 Alpha Program is to develop a custom chatbot designed to meet the specific needs of Happy Org or its target industry. The program aims to create a tailored solution that effectively integrates with Happy Org's existing systems, streamlines efficiency, and enhances the user experience when navigating Happy Org products. By partnering with Happy Org, Osan3 also seeks to foster innovation and collaboration, ultimately promoting the benefits of the chatbot solution within the target industry.",
        },
        {
        "from": "human",
        "value": "What is the purpose of the Osan3 Alpha Program?"
        },
        {
        "from": "gpt",
        "value": "The purpose of the Osan3 Alpha Program is to foster the development of custom chatbot solutions tailored to meet the specific needs of organizations, like Happy Org, or their target industries. The program aims to create innovative, effective, and user-friendly chatbot systems that integrate seamlessly with the existing systems of the participating organizations, streamline efficiency, and enhance user experience when navigating their products. Through partnerships, sponsorships, and collaboration, the Osan3 Alpha Program seeks to drive innovation and growth in chatbot technology and applications, while promoting the benefits of these solutions within the target industries.",
        },
        {
        "from": "human",
        "value": "What is the purpose of the Osan3 Alpha Program?"
        },
        {
        "from": "gpt",
        "value": "The purpose of the Osan3 Alpha Program is to foster the development of innovative chatbot solutions tailored to meet the specific needs of Happy Org or its target industry. By providing financial support and collaborating with Osan3, Happy Org aims to create a custom chatbot that effectively integrates with its current systems, streamlines efficiency, and enhances the user experience when navigating Happy Org products. Through the program, both parties will work together to promote the benefits of the chatbot solution within the target industry, positioning Happy Org as an industry innovator and encouraging user engagement."
        },
      ]
    }

def create_training_data_entry(id, question, answer):
    return {
        "id": f"osan3-happy-org_{id}",
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
