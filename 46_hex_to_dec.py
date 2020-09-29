import json
def hex_to_dec(hex):

    print(f"hex_to_dec({json.dumps(hex)})")
    try:
        return int(hex, 16)

    except:
        return "This is not an hexa-decimal number"

print(hex_to_dec("BA1"))