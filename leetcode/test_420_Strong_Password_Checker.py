import unittest


class Solution(object):
    def strongPasswordChecker(self, password):
        """
        :type password: str
        :rtype: int
        """
        pass_len = len(password)

        def rule1(password):
            # It contains at least one lowercase letter, at least one uppercase letter, and at least one digit.
            no_digit = [pc for pc in password if pc not in '0123456789']
            is_upper = len([pc for pc in no_digit if pc.isupper()]) > 0
            is_lower = len([pc for pc in no_digit if not pc.isupper()]) > 0
            is_digit = len([pc for pc in password if pc in '0123456789']) > 0
            return 3 - len([res for res in [is_upper, is_lower, is_digit] if res])

        def rule2(password):
            # It does not contain three repeating characters in a row (i.e., "...aaa..." is weak, but "...aa...a..." is strong, assuming other conditions are met).
            count = 0
            replaceable_by_2 = 0
            replaceable_by_3 = 0
            i = 0
            while i < pass_len:
                pc = password[i]
                repeating = pc + pc + pc
                if password[i:i+3] == repeating:
                    if i+4 < pass_len and password[i+3: i+5] == pc + pc:
                        replaceable_by_3 += 1
                    elif i+3 < pass_len and password[i+3] == pc:
                        replaceable_by_2 += 1
                    count += 1
                    i += 3
                else:
                    i += 1

            return count, replaceable_by_2, replaceable_by_3

        rule1_res = rule1(password)
        rule2_res, replaceable_by_2, replaceable_by_3 = rule2(password)

        # It has at least 6 characters and at most 20 characters.
        add = max(6 - pass_len, 0)
        delete = max(pass_len - 20, 0)
        must_change1 = max(rule1_res - add, 0)

        # replaceable by : add, delete(optional), change
        # replace by del
        replaceable_by_del = min(delete, (rule2_res - (replaceable_by_2 + replaceable_by_3)))
        remian_delete = max(delete - replaceable_by_del, 0)
        replaceable_by_del_1 = min(delete, min(remian_delete // 2, replaceable_by_2))
        remian_delete =  max(remian_delete - (replaceable_by_del_1 * 2), 0)
        replaceable_by_del += replaceable_by_del_1
        replaceable_by_del = min(delete, replaceable_by_del + min((remian_delete // 3, replaceable_by_3)))
        must_change2 = max(rule2_res - add - must_change1 - replaceable_by_del, 0)

        return add + delete + must_change1 + must_change2

class TestMethods(unittest.TestCase):
    def test_1(self):
        self.assertEqual(Solution().strongPasswordChecker("a"), 5)
        self.assertEqual(Solution().strongPasswordChecker("aA1"), 3)
        self.assertEqual(Solution().strongPasswordChecker("1337C0d3"), 0)

    def test_2(self):
        self.assertEqual(Solution().strongPasswordChecker("abc"), 3)
        self.assertEqual(Solution().strongPasswordChecker("abccc"), 2)
        self.assertEqual(Solution().strongPasswordChecker("acccc"), 2)
        self.assertEqual(Solution().strongPasswordChecker("aaa"), 3)
        self.assertEqual(Solution().strongPasswordChecker("aaaa"), 2)
        self.assertEqual(Solution().strongPasswordChecker("aaaaaa"), 2)
        self.assertEqual(Solution().strongPasswordChecker("aaaaaaA1"), 2)
        self.assertEqual(Solution().strongPasswordChecker("aaaaaaaaaaaaaaaaaaA1"),6)
        self.assertEqual(Solution().strongPasswordChecker("aaaaaaaaaaaaaaaaaaaA1"),7)
        self.assertEqual(Solution().strongPasswordChecker("aaBaaBaaBaaBaaBaaBA1"),0)
        self.assertEqual(Solution().strongPasswordChecker("aaabbbaaabbbaaabbbaA1"), 6)
        self.assertEqual(Solution().strongPasswordChecker("abcdefghijklbbbaaaaaaaA1"), 5)
        self.assertEqual(Solution().strongPasswordChecker("abcdefghijklbbaaBaA1"), 0)
        self.assertEqual(Solution().strongPasswordChecker("abcdefghijklbbbaaaaaaaaaaA1"), 8)
        self.assertEqual(Solution().strongPasswordChecker("abcdefghijklbbaaEaA1"), 0)
        self.assertEqual(Solution().strongPasswordChecker("aaAA11"), 0)
        self.assertEqual(Solution().strongPasswordChecker("ABABABABABABABABABAB1"), 2)
        self.assertEqual(Solution().strongPasswordChecker("A1234567890aaabbbbccccc"), 4)
        self.assertEqual(Solution().strongPasswordChecker("FFFFFFFFFFFFFFF11111111111111111111AAA"), 23)
        self.assertEqual(Solution().strongPasswordChecker("FF11a11a11a11a11a1AA"), 0)
        self.assertEqual(Solution().strongPasswordChecker("1111111111"), 3)
        self.assertEqual(Solution().strongPasswordChecker("aaaaaaaAAAAAA6666bbbbaaaaaaABBC"), 13)
        self.assertEqual(Solution().strongPasswordChecker("aaAA5AA66bbaa7aaABBC"), 0)
