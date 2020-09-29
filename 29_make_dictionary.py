

def make_dictionary(list,tuple):

    dict = {}
    for i,j in zip(list,tuple):
        dict[i] = j

    print(f"\nmake_dictionary({list},{tuple})\n")
    return dict

print(make_dictionary([50,10,62],("Borey","Thirak","Dane")))