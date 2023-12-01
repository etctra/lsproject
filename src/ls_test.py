import unittest
from ls import custom_ls

class TestCustomLS(unittest.TestCase):
    def test_custom_ls_without_rev(self):
        output = custom_ls()

        expected_output = "file1\nfile2\nfile3\n"
        self.assertEqual(output, expected_output)

    def test_custom_ls_with_rev(self):
        output = custom_ls(["--rev"])

        expected_output = "1elif\n2elif\n3elif\n"
        self.assertEqual(output, expected_output)

if __name__ == '__main__':
    unittest.main()
