
from collections import Counter
import operator
import json

def list_count(list):

    if len(list)==0:

        print("TOTAL: 0")
        return []

    else:
        c = Counter(list)
        ans = []

        for key in c:

            ans.append((key,c[key]))

        print(f"list_count({json.dumps(list)})")
        print("TOTAL: %d"%sum(c.values()))

        ans.sort(key = operator.itemgetter(0))

        return ans

print(list_count(["a","b","b","c","c","c","c","d","d","e","e","e"]))