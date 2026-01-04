class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        from copy import deepcopy
        def f(x):
            if len(x)==1:
                return [x]
            else:
                s=[]
                for i in range(len(x)):
                    l=deepcopy(x)
                    a=l.pop(i)
                    m=f(l)
                    for j in m:
                        j.append(a)
                    s+=m
                return s
        return f(nums)



