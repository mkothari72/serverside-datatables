import json

f=open('json_resp.json')

data=json.load(f)

# print(type(data))
# print(data)
# context_dict=data.pop("context")
# length=data.pop("length")
# selector_dict=data.pop("selector")
# ajax_dict=data.pop("ajax")
del data["context"]
del data["length"]
del data["selector"]
del data["ajax"]
# print(data)
v = [dict(zip(data,t)) for t in zip(*data.values())]
print(context_dict)
