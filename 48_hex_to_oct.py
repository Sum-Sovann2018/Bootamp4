
import json
def Hex_to_oct(hex):

    print(f"Hex_to_oct({json.dumps(hex)})")
    try:
        return oct(int(hex, 16))[2:]
    except:
        return "This is not an hexa-decimal number"

print(Hex_to_oct("2b9"))