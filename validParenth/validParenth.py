class Solution:        
    def isValid(self, s: str) -> bool:
        """
        1. On an open paranthesis put a value in an array/stack
        2. On a close pop the latest from the stack and check its the correct type, if not return false
        3. If a close comes through and the stack is empty, return false, else return true
        4. Once through the entire string, if the stack has anything remaining on it return false

        Helpful Hints
        
        array.append(value) <- puts it at the end of the "stack"
        array.pop(-1) <- takes the newest value, removes it from the list, returns its value

        if array: <- True if a value, False if not

        """
        parenthesis_queue = []
        
        CLOSE_DICT = {"{": "}", "[": "]", "(": ")"}

        for char in s:
            if char in CLOSE_DICT.keys():
                parenthesis_queue.append(char)
                continue
            
            if not parenthesis_queue:
                return False

            if CLOSE_DICT[parenthesis_queue.pop(-1)] != char:
                return False
            
        if parenthesis_queue:
            return False

        return True

if __name__ == "__main__":
    s = "{[]}"
    print(Solution().isValid(s))
# py .\validParenth.py
    # ==========================================================================================================================
    # class Solution:        
    # def isValid(self, s: str) -> bool:
    #     """
    #     1. On an open paranthesis put a value in an array/stack
    #     2. On a close pop the latest from the stack and check its the correct type, if not return false
    #     3. If a close comes through and the stack is empty, return false, else return true
    #     4. Once through the entire string, if the stack has anything remaining on it return false

    #     Helpful Hints
        
    #     array.append(value) <- puts it at the end of the "stack"
    #     array.pop(-1) <- takes the newest value, removes it from the list, returns its value

    #     if array: <- True if a value, False if not

    #     """
    #     parenthesis_queue = []
    #     i = 0
    #     for i in range(i, len(s)):
    #         if s[i] == "(" or s[i] == "[" or s[i] == "{":
    #             parenthesis_queue.append(s[i])
    #             continue
            
    #         if not parenthesis_queue:
    #             return False

    #         if s[i] == ")":
    #             temp = parenthesis_queue.pop(-1)
    #             if temp != "(":
    #                 return False
            
    #         if s[i] == "]":
    #             temp = parenthesis_queue.pop(-1)
    #             if temp != "[":
    #                 return False
            
    #         if s[i] == "}":
    #             temp = parenthesis_queue.pop(-1)
    #             if temp != "{":
    #                 return False

            
    #     if parenthesis_queue:
    #         return False

    #     return True
    # py .\validParenth\validParenth.py