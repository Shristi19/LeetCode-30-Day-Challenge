arr = [1,1,2]

dict_hash={}

for item in arr:
     if item not in dict_hash:
         dict_hash[item] =1

     else:
         dict_hash[item] += 1
count=0

for k,v in dict_hash.items():
    if k+1 in dict_hash:
       value_of_k = dict_hash[k]
       value_of_k_plus = dict_hash[k+1]
       if value_of_k_plus == value_of_k:
           count += value_of_k_plus
       elif value_of_k_plus < value_of_k:
          count += value_of_k
       else:
           count += min(value_of_k,value_of_k_plus)

print(count)
