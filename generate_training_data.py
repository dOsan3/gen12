# example.py
import json
import conversation_builder as cb

doc_name = "osan3-happy-org"
id = "1"
question = "Your question here"
answer = "Your answer here"
json_object = cb.main(doc_name, id, question, answer)

question = "Your question here"
answer = "Your 2nd answer here"
cb.add_conversation(json_object, question, answer)

id = "2"
question = "Your question here"
answer = "Your answer here"
json_object = cb.main(doc_name, id, question, answer)

question = "Your question here"
answer = "Your 2nd answer here"
cb.add_conversation(json_object, question, answer)

print(json.dumps(cb.json_objects, indent=2))