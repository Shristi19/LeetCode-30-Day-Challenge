class Solution:
    def isHappy(self, n: int) -> bool:
        set_s=set()
        if n==1:
            return True
        else:
            set_s.add(n)
            while n !=1:
                n = get_digits_inalist(n)
                if n not in set_s:
                    set_s.add(n)
                    continue
                elif n in set_s:
                    return False
        return True




def get_digits_inalist(num):
    string_num=list(str(num))
    liist=list(map(int,string_num))
    sum=0
    for items in liist:
        sum=sum + (items**2)
    return sum






