# Problem: Print Words Vertically - https://leetcode.com/problems/print-words-vertically/description/

class Solution:
    def printVertically(self, s: str) -> List[str]:

        lst=s.split()

        

        max_var=0
        
        max_var=max(len(word) for word in lst)

        # full_lst = []
        

        # for i in lst:
           
        #     if len(i) < max_var:
        #         sp = max_var - len(i)
        #         i+=" "*sp
        #         full_lst.append(i)
       
        #     else:
        #         full_lst.append(i)

            
        
        # print(full_lst)

        result=["" for i in range(max_var) ]

        space = 0        
        for i in range(len(lst)):
                for j in range(len(lst[i])):
                        result[j]+=lst[i][j]
                        space +=1
                for k in range(space, len(result)):
                    result[k] += " "

                space = 0

               
        for i in range(len(result)):
            result[i]=result[i].rstrip()
        
        
        return (result)

        

        



                

        

                
      
        # return(result)
                



        