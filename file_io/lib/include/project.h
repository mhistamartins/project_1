#ifndef PROJECT_H
#define PROJECT_H
#include <iostream>

class project
{

    public:
        project();  // constructor definition
        ~project(); // destructor definition

        void open();
        void close();

        int func_read_line_string1();
        int func_write_line_string();
        int read_container();
        void write_container();
};
#endif