from functions.get_files_info import get_files_info
from functions.get_file_content import get_file_content
from functions.write_file import write_file

def TestGetFilesInfo():

    print("Result for current directory")
    result = get_files_info("calculator", ".")
    print(result)

    print("Result for 'pkg' directory")
    result = get_files_info("calculator", "pkg")
    print(result)

    print("Result for '/bin' directory")
    result = get_files_info("calculator", "/bin")
    print(result)

    print("Result for parent directory")
    result = get_files_info("calculator", "../")
    print(result)

def TestGetFileContent():

    print("Contents of main.py file:")
    result = get_file_content("calculator", "main.py")
    print(result)
    print("=========================================================")

    print("Contents of pkg/calculator.py file:")
    result = get_file_content("calculator", "pkg/calculator.py")
    print(result)
    print("=========================================================")

    print("Contents of /bin/cat file:")
    result = get_file_content("calculator", "/bin/cat")
    print(result)
    print("=========================================================")

def TestWriteFile():
    print("Attempting to write to lorem.txt file:")
    result = write_file("calculator", "lorem.txt", "wait, this isn't lorem ipsum")
    print(result)
    print("=========================================================")

    print("Attempting to write to pkg/morelorem.txt file:")
    result = write_file("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet")
    print(result)
    print("=========================================================")

    print("Attempting to write to /tmp/temp.txt file:")
    result = write_file("calculator", "/tmp/temp.txt", "this should not be allowed")
    print(result)
    print("=========================================================")


if __name__ == "__main__":
    #TestGetFilesInfo()
    #TestGetFileContent()
    TestWriteFile()