#include "project.h"
#include <vector>
#include <stdexcept>
#include <fstream>

File_IO::File_IO(std::string filename)
{
    m_filename = filename;
}

std::string File_IO::readLine()
{
    std::string content;

    /* open file using m_filename variable*/
    // read operation
    // close file

    return content;
}

std::vector<std::string> File_IO::readLines()
{
    std::vector<std::string> content;

    const int buffer_size = 256;
    std::ifstream input_stream(m_filename);
    if (input_stream.is_open())
    {
        while (input_stream.good())
        {
            char buffer[buffer_size] = {0};

            input_stream.getline(buffer, buffer_size - 1);
            content.emplace_back(buffer);
        }
    }

    input_stream.close();

    return content;
}

void File_IO::writeLine(std::string data_line)
{
    /* open file using m_filename variable*/

    // write operation

    // close file
}

void File_IO::writeLines(std::vector<std::string> data)
{
    std::ofstream output_stream(m_filename, std::ios::out);
    if (output_stream.is_open())
    {
        for (std::string eachLine : data)
        {
            output_stream << eachLine << std::endl;
        }
    }

    output_stream.close();
    // close file
}