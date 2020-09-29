
def mean_of_list(list):

    sum = 0
    count = 0

    for i in list:
        sum += i
        count += 1

    print(f"mean_of_list({list})")
    return sum/count

print(mean_of_list([50,10,62,32]))