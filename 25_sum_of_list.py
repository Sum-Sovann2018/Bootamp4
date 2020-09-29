
def sum_of_list(list=[]):

    print(f"\nSum_of_list({list})\n")
    return sum(int(i) for i in (list))



print(sum_of_list([20,15,10,30]))
