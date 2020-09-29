
def list_merge_sort(list):



    if len(list) > 1:

        mid = len(list) // 2

        L = list[ :mid ]
        R = list[ mid: ]

        list_merge_sort(L)
        list_merge_sort(R)

        i = j = k = 0

        while i < len(L) and j < len(R):

            if L[i] < R[j]:

                list[k] = L[i]
                i+=1
            else:
                list[k] = R[j]
                j+=1
            k+=1

        while i < len(L):

            list[k] = L[i]
            i+=1
            k+=1

        while j < len(R):

            list[k] = R[j]
            j+=1
            k+=1


    new_list = []
    for num in list:
        new_list.insert( 0 , num)


    unique_list = []
    for i in new_list:
        if i not in unique_list:
            unique_list.append(i)

    return unique_list


list = [50,75,60,55,60,98,50,23]

print(f"list_merge_sort({list})")
print(list_merge_sort(list))

