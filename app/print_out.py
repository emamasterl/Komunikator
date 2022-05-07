import json

def print_out(question, response):
    intents_data = {}
    intents_data["tag"] =["{}".format(response)]
    intents_data["patterns"] = ["{}".format(question)]
    intents_data["responses"] = [""]
    intents_data["codex"] = [""]

    fileName=r'app/intents2.json'
    with open(fileName, 'r',encoding="utf8") as fp:
        data = json.load(fp)

    data['intents'].append(intents_data)                 

    with open(fileName, 'w',encoding="utf8") as fp:
        json.dump(data, fp, ensure_ascii=False ,indent=2)