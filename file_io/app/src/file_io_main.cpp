#include "project.h"
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
    std::vector<std::string> Inputs;
    std::string Input;
    std::cout << "Enter the Lines to be written in the file:" << std::endl;
    std::getline(std::cin >> ws, Input);
    Inputs.push_back(Input);
    for (int i = 0; i < Inputs.size(); i++)
        std::cout << "Strings: \n"
                  << Inputs[i] << std::endl;

   
    std::vector<std::string> ReadContainer = project_fileio.read_container();
    for (const auto &str : Inputs)
    {
        std::cout << str << std::endl;

    }

    project_fileio.close();

    return 0;
}