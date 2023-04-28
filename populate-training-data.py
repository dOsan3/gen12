import json

def create_json_object(doc_name, id):
    return {
        "id": f"{doc_name}_{id}",
        "conversations": []
    }

def main(doc_name, id):
    json_object = create_json_object(doc_name, id)
    print(json.dumps(json_object, indent=2))

if __name__ == "__main__":
    doc_name = "osan3-happy-org"  # Replace with the desired document name
    id = "1"          # Replace with the desired ID value
    main(doc_name, id)