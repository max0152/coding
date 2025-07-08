import unittest
from unittest.mock import patch
import io
class math:
  @staticmethod
  def fac(n):
    if n == 0:
        return 1
    f = 1
    while n > 1:
        f *= n
        n -= 1
    return f

  @staticmethod
  def step(base, exponent):
    result = base ** exponent
    print(result)

  @staticmethod
  def form(n):
    return n + 1
    
class TestMathMethods(unittest.TestCase):

    def test_fac(self):
        self.assertEqual(math.fac(0), 1)
        self.assertEqual(math.fac(5), 120)

    def test_step(self):
        with patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:
            math.step(2, 3)
            self.assertIn('8', mock_stdout.getvalue())

        with patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:
            math.step(10, 2)
            self.assertIn('100', mock_stdout.getvalue())

    def test_form(self):
        self.assertEqual(math.form(4), 5)
        self.assertEqual(math.form(-10), -9)

if __name__ == '__main__':
    unittest.main()
