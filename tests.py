import unittest
from tiny import Tiny

t = Tiny('5SX0TEjkR1mLOw8Gvq2VyJxIFhgCAYidrclDWaM3so9bfzZpuUenKtP74QNH6B')

class TinyTest(unittest.TestCase):

    def test_generation(self):
        test_code = t.generate_set()
        self.assertTrue(len(test_code) == 62)

    def test_encode(self):
        self.assertEqual(t.encode(5), 'E')
        self.assertEqual(t.encode(126), 'XX')

    def test_decode(self):
        self.assertEqual(t.decode('E'), 5)
        self.assertEqual(t.decode('XX'), 126)

if __name__ == '__main__':
    unittest.main()
