#include "project.h"
#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <iterator>

using namespace std;

FileWork::FileWork(const std::string &FileName) : FileName(FileName) {}

bool FileWork::open(bool to_write = false)
{
    bool status = false;
    if (to_write)
    {
        // output stream
        Files.open(FileName, ios::out); // optionally -> add a flag ios::app
        if (Files.is_open())
        {
            std::cout << "File is opened" << std::endl;
            status = true;
        }
    }
    else
    {
        // input stream
        File.open(FileName, ios::in);
        if (File.is_open())
        {
            std::cout << "File is opened" << std::endl;
            status = true;
        }
    }
    return status;
}

void FileWork::func_write_line_string(const std::string &write)
{
    open(true);
    Files << "writing this line of code to file" << std::endl;
}

std::string FileWork::func_read_line_string()
{
    open(false);
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
    open(false);
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
    open(true);
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