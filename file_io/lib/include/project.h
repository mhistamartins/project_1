#ifndef PROJECT_H
#define PROJECT_H
#include <iostream>
#include <string>
#include <fstream>
#include <vector>

class FileWork
{
private:
    std::string FileName;
    std::ofstream Files;
    std::ifstream File;

public:
    explicit FileWork(const std::string &FileName);

    bool open();
    void func_write_line_string(const std::string &write);
    std::string func_read_line_string();
    std::vector<std::string> read_container();
    void write_container(const std::vector<std::string> &writecont);

    void close();

    ~FileWork() {}
};
#endif