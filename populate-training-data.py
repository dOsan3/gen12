import json

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
    print(json.dumps(json_object, indent=2))

if __name__ == "__main__":
    doc_name = "osan3-happy-org"  # Replace with the desired document name
    id = "your_id_here"          # Replace with the desired ID value
    question = "Your question here"  # Replace with the desired question
    answer = "Your answer here"      # Replace with the desired answer
    main(doc_name, id, question, answer)