#ifndef FILE_IO_H
#define FILE_IO_H

#include <string>
#include <vector>

class File_IO
{
public:
    explicit File_IO(std::string filename);
    std::string readLine();
    std::vector<std::string> readLines();
    void writeLine(std::string data_line);
    void writeLines(std::vector<std::string> data);

private:
    std::string m_filename;
};

#endif // FILE_IO_H