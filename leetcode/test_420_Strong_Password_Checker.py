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
            undeletable1 = 0
            undeletable2 = 0
            i = 0
            while i < pass_len:
                pc = password[i]
                repeating = pc + pc + pc
                if password[i:i+3] == repeating:
                    if i+4 < pass_len and password[i+3: i+5] == pc + pc:
                        undeletable2 += 1
                    elif i+3 < pass_len and password[i+3] == pc:
                        undeletable1 += 1
                    count += 1
                    i += 3
                else:
                    i += 1

            return count, undeletable1, undeletable2

        rule1_res = rule1(password)
        rule2_res, undeletable1, undeletable2 = rule2(password)
        res1 = rule1_res > 0
        res2 = rule2_res > 0

        # It has at least 6 characters and at most 20 characters.
        add = 0
        delete = 0
        if pass_len < 6:
            add = 6 - pass_len
        if pass_len > 20:
            delete = pass_len - 20
        must_change1 = 0
        must_change2 = 0

        # add, change
        if res1:
            if(rule1_res > add):
                must_change1 = rule1_res - add

        # add, delete(optional), change
        if res2:
            can_overwrite = add + must_change1
            deletable = rule2_res - (undeletable1 + undeletable2)

            if delete < deletable:
                can_overwrite += delete
            else:
                can_overwrite += deletable

                can_overwrite_x = 0
                if undeletable1:
                    can_overwrite_x = min(undeletable1, ((delete - deletable)//2))
                    if can_overwrite_x > 0:
                        can_overwrite += can_overwrite_x

                if undeletable2:
                    can_overwrite_x = min(undeletable2, ((delete - deletable - (can_overwrite_x * 2))//3))
                    if can_overwrite_x > 0:
                        can_overwrite += can_overwrite_x

            if rule2_res > can_overwrite:
                must_change2 = rule2_res - can_overwrite

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
