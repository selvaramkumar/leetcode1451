from collections import OrderedDict
class Solution:
    def arrangeWords(self, text: str) -> str:
        temp=text.split(" ")
        dict1={}
        for i in temp:
            if  not len(i) in dict1:
                dict1[len(i)]=i
            else :
                dict1[len(i)]=dict1[len(i)]+" "+i
        res=""   
        dict2=OrderedDict(sorted(dict1.items()))
        count=0
        for key,value in dict2.items():
            if count>=1:
                res=res+" "+value[0].lower() + value[1:]
                count=count+1
            else:
                res=res+value[0].upper() + value[1:]
                count=count+1 
        return res
s=Solution()
str1="Keep calm and code on"
print(s.arrangeWords(str1))        
        