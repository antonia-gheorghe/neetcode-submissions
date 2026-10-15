class Solution:
    def isopposite(self, a:str, b:str):
        if (a == "(" and b == ")") or (a == "[" and b == "]") or (a == "{" and b == "}"):
            return True
        else:
            return False 
    
    def isopening(self, a:str):
        if a == "(" or a == "[" or a == "{":
            return True
        else:
            return False 

    def isValid(self, s: str) -> bool:

        stack = []
        i = 0

        while i<len(s):

            ch = s[i]

            if self.isopening(ch):
                stack.append(ch)
            else: 
                if stack and self.isopposite(stack[-1], ch):
                    stack.pop()
                else:
                    return False   
            i +=1 

        if not stack: 
            return True
        else:
            return False 


        