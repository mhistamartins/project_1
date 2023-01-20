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

   network.open();

   // network.write_container();
   //network.read_container();
   network.func_write_line_string();
   network.func_read_line_string1();

   network.close();

   return 0;
}