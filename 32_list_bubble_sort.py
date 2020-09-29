def list_bubble_sort(list):

    print(f"list_bubble_sort({list})")

    new_list = list

    for i in range(len(new_list)-1, 0, -1):

        for num in range(i):

            if new_list[num] > new_list[num + 1]:

                temp = new_list[num]

                new_list[num] = new_list[num + 1]
                new_list[num + 1] = temp

    return new_list

print(list_bubble_sort([50,75,60,55,98,23]))
