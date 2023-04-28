import json

# Initialize an empty list to store JSON objects
json_objects = []

def create_json_object(doc_name, id):
    return {
        "id": f"{doc_name}_{id}",
        "conversations": []
    }

def add_conversation(json_object, question, answer):
    json_object["conversations"].append(question)
    json_object["conversations"].append(answer)

def main(doc_name, id, question, answer):
    json_object = create_json_object(doc_name, id)
    add_conversation(json_object, question, answer)
    json_objects.append(json_object)
    return json_object

if __name__ == "__main__":
    doc_name = "osan3-happy-org"
    id = "1"
    question = "Your question here"
    answer = "Your answer here"
    json_object = main(doc_name, id, question, answer)

    question = "Your question here"
    answer = "Your 2nd answer here"
    add_conversation(json_object, question, answer)

    id = "2"
    question = "Your question here"
    answer = "Your answer here"
    json_object = main(doc_name, id, question, answer)

    question = "Your question here"
    answer = "Your 2nd answer here"
    add_conversation(json_object, question, answer)

    print(json.dumps(json_objects, indent=2))