import unittest
from functions.get_files_info import get_files_info

class TestGetFilesInfo(unittest.TestCase):
    def test_working_directory(self):
        print(get_files_info("calculator", "."))

    def test_child_directory(self):
        print(get_files_info("calculator", "pkg"))

    def test_error_outside_directory(self):
        print(get_files_info("calculator", "/bin"))

    def test_parent_directory(self):
        print(get_files_info("calculator", "../"))



if __name__ == "__main__":
    unittest.main()