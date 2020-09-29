
def search_in_tuple(tuple,num):

    if num in tuple:
        print(f"search_in_tuple({tuple},{num})")
        return f"Element found at Index:{tuple.index(num)}"

    else:
        print(f"search_in_tuple({tuple},{num})")
        return f"Element not found in the tuple"


print(search_in_tuple((20,15,10,30),10))
