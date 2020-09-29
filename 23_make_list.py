
import json

def make_list (list=[]):

    return f"make_list({list})\n{json.dumps(list)}"

print(make_list([12,"hello",45]))