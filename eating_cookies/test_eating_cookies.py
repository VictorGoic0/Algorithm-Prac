import unittest
from eating_cookies import eating_cookies

class Test(unittest.TestCase):

  def test_eating_cookies_small_n(self):
    cache = {0: 1, 1: 1, 2: 2, 3: 4, 4: 7}
    self.assertEqual(eating_cookies(0, cache), 1)
    self.assertEqual(eating_cookies(1, cache), 1)
    self.assertEqual(eating_cookies(2, cache), 2)
    self.assertEqual(eating_cookies(5, cache), 13)
    self.assertEqual(eating_cookies(10, cache), 274)

  def test_eating_cookies_large_n(self):
    cache = {0: 1, 1: 1, 2: 2, 3: 4, 4: 7}
    self.assertEqual(eating_cookies(50, cache), 10562230626642)
    self.assertEqual(eating_cookies(100, cache), 180396380815100901214157639)
    self.assertEqual(eating_cookies(500, cache), 1306186569702186634983475450062372018715120191391192207156664343051610913971927959744519676992404852130396504615663042713312314219527)


if __name__ == '__main__':
  unittest.main()
