#include "project_1/file_io/lib/include/project.h"
#include <iostream>
#include <string>
#include <vector>
#include <fstream>
#include <iterator>

using namespace std;

int main(int argc, char *argv[])
{
    FileWork project_fileio("TextFile.txt");

    project_fileio.open();

    std::string write;
    std::cout << "Enter line of strings: ";
    std::getline(std::cin, write);

    project_fileio.func_write_line_string(write);
    project_fileio.func_read_line_string();

    std::vector<std::string> ReadContainer = project_fileio.read_container();

    return 0;
}