class Solution:
    def romanToInt(self, s: int) -> str:
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
            "M" : 1_000,
            "_V": 5_000,
            "_X": 10_000,
            "_L": 50_000,
            "_C": 100_000,
            "_D": 500_000,
            "_M": 1_000_000
        }
        final_str = ""
        roman_num_list = list(ROMAN_NUMS_DICT.keys())
        roman_num_list.reverse()
        
        for roman_num in roman_num_list:
            while (s // ROMAN_NUMS_DICT[roman_num] > 0):
                final_str += roman_num
                s -= ROMAN_NUMS_DICT[roman_num]
        
        return final_str
        # while s != "":
        #     for roman_num in roman_num_list:
        #         if s.startswith(roman_num):
        #             total += ROMAN_NUMS_DICT[roman_num]
        #             s = s[len(roman_num)::]
        # return total
    
solution1 = Solution()
print(solution1.romanToInt(3_133_257))
