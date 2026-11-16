class Solution:
    def digitSum(self, s: str, k: int) -> str:
        while len(s)>k:
            l=[]
            if len(s)%k==0 :
                a= int(len(s)/k)
            else :
                a=(len(s)//k)+1
            c=0
            d=k
            for i in range(a):
                l.append(s[c:d])
                c+=k
                d+=k
            l1=[]
            for i in l:
                sum=0
                for j in i:
                    sum+=int(j)
                l1.append(str(sum))
            s="".join(l1)
        else:
            return s
