#include "project.h"
#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <iterator>

using namespace std;

project::project() {}

project::~project() {}

void project::open()
{
    fstream myFile;
    myFile.open("TextFile.txt", ios::out);
    if (myFile.is_open())
    {
        cout << "File has been opened\n";
    }
    else if (!myFile.is_open())
    {
        std::cout << "File does not exist. New file created.";
    }
}

void project::close()
{
    fstream myFile;
    myFile.close();
    std::cout << "File is closed" << std::endl;
}

int project::func_read_line_string1(void)
{
    ifstream file;

    string filename;
    int line_number;

    cout << "Please enter Filename: ";
    cin >> filename;

    cout << "Line: ";

    cin >> line_number;

    if (line_number <= 0)
    {
        cout << "Line number must be >= 1" << endl;

        return 1;
    }

    file.open(filename);

    if (file.fail())
    {
        cout << "File failed to open." << endl;
        return 1;
    }

    int current_line = 0;
    string line;

    while (!file.eof())
    {
        current_line++;

        getline(file, line);

        if (current_line == line_number)
            break;
    }
    if (current_line < line_number)
    {
        cout << "Line not found!" << endl;
        cout << "File contains " << current_line;
        cout << " lines total." << endl;
    }

    else
        cout << "Line: " << line << endl;

    file.close();

    return 0;
}

int project::func_write_line_string()
{
    ofstream myfile("TextFile.txt");
    if (myfile.is_open())
    {
        myfile << "This is a line.\n";
    }
    else
        cout << "Unable to open file\n";

    return 0;
}

int project::read_container()
{
    std::ifstream file("TextFile.txt");

    std::vector<std::string> v;

    std::string str;
    while (file >> str) // keep reading until we run out
    {
        v.push_back(str);
    }

    copy(v.begin(), v.end(), ostream_iterator<string>(cout, " "));
    std::cout << "\n";

    return 0;
}

void project::write_container()
{
    vector<string> myvector;
    string str;

    cout << "Please enter strings: \n";
    getline(cin, str);
    myvector.push_back(str);

    for (int i = 0; i < myvector.size(); i++)
    {
        cout << "Your strings are: \n"
             << myvector[i] << endl;
    }
}