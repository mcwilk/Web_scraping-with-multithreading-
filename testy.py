import unittest
import skrypt
import watki


class TestSkrypt(unittest.TestCase):


    def test_path_function(self):
        """
            Test method to check if function's output is not equals to 0.
        """

        result = watki.path_function('adresy_url.txt')
        self.assertEqual(type(result), str)


    def test_file_reader(self):
        """
            Test method to check if function's output is in 'list' type.
        """

        result = watki.file_reader('adresy_url.txt')
        self.assertEqual(type(result), list)
    

    def test_main(self):
        """
            Test method to check if function's output is not empty list.
        """

        result = watki.main()
        self.assertNotEqual(len(result), 0)


    def test_html_tags(self):
        """
            Test method to check if function's output is in 'list' type.
        """

        result = skrypt.html_tags()
        self.assertEqual(type(result), list)
    

if __name__ == '__main__':
    unittest.main()
