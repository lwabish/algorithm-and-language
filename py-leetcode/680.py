import unittest


def main(s):
    def judge(s, adjuest):
        head, tail = 0, len(s) - 1
        while head < tail:
            if s[head] == s[tail]:
                head += 1
                tail -= 1
                continue
            elif adjuest:
                return judge(s[head+1:tail+1], False) or judge(s[head:tail], False)
            else:
                return False
        return True
    return judge(s, True)


class Test(unittest.TestCase):
    def test_main(self):
        self.assertTrue(main("abca"))
        self.assertTrue(main("aba"))
        self.assertEqual(main("abacctaba"), True)
        self.assertEqual(main('abd'), False)
        self.assertEqual(main("eeccccbebaeeabebccceea"), False)
        self.assertEqual(main('cuucu'), True)


if __name__ == '__main__':
    unittest.main(exit=False)
