#include "project.h"
#include <iostream>
#include <string>
#include <vector>
#include <fstream>
#include <iterator>

using namespace std;

int main(int argc, char *argv[])
{
    project network;

    fstream myFile;
    myFile.open("TextFile.txt", ios::out);
    if (myFile.is_open())
    {
        cout << "File has been opened\n";
    }
    else if (!myFile.is_open())
    {
        myFile.open("TextFile.txt", ios::out);
        std::cout << "File does not exist. New file created.";
    }

    network.write_container();
    network.func_write_line_string();
    // network.func_read_line_string1();
    network.read_container();

    myFile.close();

    return 0;
}