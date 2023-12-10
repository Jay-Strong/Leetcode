class Solution:        
    def isValid(self, s: str) -> bool:
        num_open_parenth = 0
        num_closed_parenth = 0
        num_open_square = 0
        num_closed_square = 0
        num_open_curley = 0
        num_closed_curley = 0       
        for c in s:
            if c == "(":
                num_open_parenth += 1
            if c == ")":
                num_closed_parenth += 1
            if c == "{":
                num_open_curley += 1
            if c == "}":
                num_closed_curley += 1
            if c == "[":
                num_open_square += 1
            if c == "]":
                num_closed_square += 1
            
        return (
            (num_open_parenth == num_closed_parenth) 
            and (num_open_curley == num_closed_curley) 
            and (num_open_square == num_closed_square)
        )

if __name__ == "__main__":
    s = "([)]"
    print(Solution().isValid(s))