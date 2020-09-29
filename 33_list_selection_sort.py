
def list_selection_sort(list):

    new_list = []

    print(f"list_selection_sort({list})")

    for num in range(len(list)):

        min_num = num

        for i in range( num + 1, len(list)):

            if list[ min_num] > list[i]:

                min_num = i

        list[ num ], list[ min_num ] = list[ min_num ], list[ num ]

        new_list = list

    return new_list

print(list_selection_sort([50,75,60,55,98,23]))
