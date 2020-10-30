print("""
Given an expression string exp, write a program to examine whether the pairs
and the orders of “{“, “}”, “(“, “)”, “[“, “]” are correct in exp.

    Input: exp = “[()]{}{[()()]()}” 
    Output: Balanced

    Input: exp = “[(])” 
    Output: Not Balanced    
""")

from re import sub

def is_balanced(expr): 
    s = []
    open_list = '([{'
    close_list = ')]}'
    
    for i in expr:
        if i in open_list: 
            s.append(i)            
            
        elif i in close_list:
            pos = close_list.index(i)
            
            if len(s) > 0 and s[-1] == open_list[pos]:
                s.pop()                
            else: 
                return False
            
    return True if not s else False

  
# Driver Code 
if __name__ == "__main__": 
    expr = input("enter string: ")
    
    print("method 1: Balanced" if is_balanced(expr) else "Not Balanced")
    


