
import json
def fun_split (list=[]):

    new_list = list.split()

    return f"fun_split({list})\n{json.dumps(new_list)}"

print(fun_split("Hello world welcome to Python"))