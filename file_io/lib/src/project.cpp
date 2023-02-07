#include "project.h"
#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <iterator>

using namespace std;

FileWork::FileWork(const std::string &FileName) : FileName(FileName) {}

bool FileWork::open()
{
    bool status = false;
    Files.open(FileName, ios::out | ios::in | ios::app);
    File.open(FileName, ios::out | ios::in | ios::app);
    if (Files.is_open() && File.is_open())
    {
        std::cout << "File is opened" << std::endl;

        status = true;
    }
    return false;
}

void FileWork::func_write_line_string(const std::string &write)
{
    Files.open(FileName);
    Files << "writing this line of code to file" << std::endl;
}

std::string FileWork::func_read_line_string()
{
    string data[1];
    int num;
    std::cout << "specify line of file:" << std::endl;
    cin >> num;
    for (int i = 0; i < num; i++)
    {
        getline(File, data[0]);
    }
    return data[0];
}

std::vector<std::string> FileWork::read_container()
{
    std::vector<std::string> vec;
    std::string str;
    while (getline(File, str))
    {
        vec.push_back(str);
    }
    return vec;
}

void FileWork::write_container(const std::vector<std::string> &writecont)
{
    for (const auto &write : writecont)
    {
        Files << write << std::endl;
    }
}

void FileWork::close()
{
    File.close();
    Files.close();
}