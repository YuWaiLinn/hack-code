import unittest


class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        dict_roman = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        n_list = [dict_roman[c] for c in s]
        t = 0
        i = 0
        while (i < len(n_list)):
            s1 = n_list[i]
            s2 = 0
            x = 0
            if i < len(n_list) - 1:
                s2 = n_list[i + 1]
            if(s1 < s2):
                x = s2 - s1
                i += 1
            else:
                x = s1
            t += x
            i += 1
        return t


class TestMethods(unittest.TestCase):

    def test_1(self):
        self.assertEqual(Solution().romanToInt("III"), 3)
    def test_2(self):
        self.assertEqual(Solution().romanToInt("LVIII"), 58)
    def test_3(self):
        self.assertEqual(Solution().romanToInt("MCMXCIV"), 1994)
