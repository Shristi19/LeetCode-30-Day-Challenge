int_list=[-2,-1,-3]


def logic(int_list):
    max_far=int_list[0]
    max_ending=int_list[0]
    for i in range(1,len(int_list)):
        max_ending=max(max_ending+int_list[i],int_list[i])
        max_far=max(max_far,max_ending)
    return max_far

print(logic(int_list))
