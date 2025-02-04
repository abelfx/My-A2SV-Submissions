# Problem: Masking Personal Information - https://leetcode.com/problems/masking-personal-information/description/?envType=problem-list-v2&envId=string

class Solution:
    def maskPII(self, s: str) -> str:
        

        result = ""

        if s[-1].isalpha():
            l, r = s.lower().split("@")
            result += l[0]
            result += "*****"
            result += l[-1]
            result += "@"
            result += r

        elif(s[-1].isdigit() or s[-2].isdigit()):
            clean_numbers = ""
            for i in s:
                if(i.isdigit()):
                    clean_numbers += i
            if(len(clean_numbers) == 10):
                result += "***-***-"
            elif(len(clean_numbers) == 11):
                result += "+*-***-***-"
            elif(len(clean_numbers) == 12):
                result += "+**-***-***-"
            elif(len(clean_numbers) == 13):
                result += "+***-***-***-"

            result += clean_numbers[-4:]
                
        
        return result

            
        


     

       
        
    


        
       

        