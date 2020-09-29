
def slice_list(list,num):

    print(f"slice_list({list},{num})\n")

    list = list[num : -num]

    return list

print(slice_list([50,10,62,32,64,78,90],2))
