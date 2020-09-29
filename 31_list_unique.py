
def list_unique(list):

    unique_list = []

    for i in list:
        if i not in unique_list:
            unique_list.append(i)

    return f"list_unique({list})\n{unique_list}"

print(list_unique([50,60,25,65,25,60]))