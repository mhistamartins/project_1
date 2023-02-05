#include <gtest/gtest.h>
#include "project.h"
#include <fstream>

/* List of Test cases to implement:
1. Read Line From file, which doesn't exist,'
   throws an Exception
2. Read Lines (all content) From file,
   which doesn't exist, throws an Exception
3. Write Line to file, which doesn't exist, should create a file
4. Write Lines (all content) to file,
   which doesn't exist, should create a file
5. If file exists,
   Write Line to file should <...> (1 -> append OR 2-> override)
6. If file exists, Write Lines (all content)
   to file should <...> (1 -> append OR 2-> override)
7. if a user provided an empty string
   for filename -> throw an exception.
8. When we have finished to use File_IO component,
   the file should be closed. ( we can open it via C/C++ functions)
9. After "read" functions (if file doesn't exist) file should not exist.
*/