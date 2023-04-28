import json

# Store all JSON objects in a dictionary with 'doc_name-id' keys
json_objects = {}

def create_json_object(doc_name, id):
    return {
        "id": f"{doc_name}_{id}",
        "conversations": []
    }

def add_conversation(doc_name, id, question, answer):
    key = f"{doc_name}_{id}"
    if key not in json_objects:
        json_objects[key] = create_json_object(doc_name, id)
    json_objects[key]["conversations"].append(question)
    json_objects[key]["conversations"].append(answer)

def main(doc_name, id, question, answer):
    add_conversation(doc_name, id, question, answer)

if __name__ == "__main__":
    doc_name = "osan3-happy-org"  # Replace with the desired document name
    id = "1"          # Replace with the desired ID value
    question = "Your question here"  # Replace with the desired question
    answer = "Your answer here"      # Replace with the desired answer
    main(doc_name, id, question, answer)
    question = "Your question here"  # Replace with the desired question
    answer = "Your 2nd answer here"      # Replace with the desired answer
    main(doc_name, id, question, answer)


    doc_name = "osan3-happy-org"  # Replace with the desired document name
    id = "2"          # Replace with the desired ID value
    question = "Your question here"  # Replace with the desired question
    answer = "Your answer here"      # Replace with the desired answer
    main(doc_name, id, question, answer)
    question = "Your question here"  # Replace with the desired question
    answer = "Your 2nd answer here"      # Replace with the desired answer
    main(doc_name, id, question, answer)

    print(json.dumps(json_objects, indent=2))