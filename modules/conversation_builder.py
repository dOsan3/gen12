# conversation_builder.py
import json

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
