class Solution:
    def romanToInt(self, s: str) -> int:
        ROMAN_NUMS_DICT = {
            "I" : 1,
            "IV": 4, 
            "V" : 5,
            "IX": 9,
            "X" : 10,
            "XL": 40,
            "L" : 50,
            "XC": 90,
            "C" : 100,
            "CD": 400,
            "D" : 500,
            "CM": 900,
            "M" : 1000
        }
        total = 0
        roman_num_list = list(ROMAN_NUMS_DICT.keys())
        roman_num_list.reverse()
        while s != "":
            for roman_num in roman_num_list:
                if s.startswith(roman_num):
                    total += ROMAN_NUMS_DICT[roman_num]
                    s = s[len(roman_num)::]
        return total
    
solution1 = Solution()
print(solution1.romanToInt("IV"))