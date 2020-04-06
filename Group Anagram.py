






strs=["eat", "tea", "tan", "ate", "nat", "bat"]
sorted_input = [''.join(sorted(item)) for item in strs]

map={}

for i in range(0,len(sorted_input)):
    if sorted_input[i] not in map:
        map[sorted_input[i]]=[strs[i]]
    else:
        map[sorted_input[i]].append(strs[i])

print(list(map.values()))


















# input=["eat", "tea", "tan", "ate", "nat", "bat"]
# sorted_input = [''.join(sorted(item)) for item in input]
# print(sorted_input)
# set_words=list(set(sorted_input))
# answer=[]
# print(set_words)
#
#
#
#
#
# for item in range(0,len(set_words)):
#     answer.append([])
#     for iitem in range(0,len(input)):
#         if sorted_input[iitem] == set_words[item]:
#             answer[item].append(input[iitem])
#
# print(answer)
