class Solution:        
    def isValid(self, s: str) -> bool:
        if s == "" or len(s) == 1 or s[0] == ")" or s[0] == "]" or s[0] == "}":
            return False
        
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

        if (num_open_parenth == num_closed_parenth) and (num_open_curley == num_closed_curley) and (num_open_square == num_closed_square):
            i = 0
            for i in range(i, len(s)):
                if s[i] == "(":
                    for i in range(i + 1, len(s)):
                        if s[i] == ")":
                            i += 1
                            continue
                elif s[i] == "[":
                    for i in range(i + 1, len(s)):
                        if s[i] == "]":
                            i += 1
                            continue
                elif s[i] == "{":
                    for i in range(i + 1, len(s)):
                        if s[i] == "}":
                            i += 1
                            continue
            return True
        return False

if __name__ == "__main__":
    s = "([)]"
    print(Solution().isValid(s))