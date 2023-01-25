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

    TEST(project, N1)
    {
        project myFile;
        std::string non_existing_file("fake_text.txt");
        {
            std::ifstream checkStream(non_existing_file);
            ASSERT_EQ(1, checkStream.is_open());
        }
        if (myFile.is_open())
        {
            EXPECT_THROW(myFile.func_read_line_string1(), std::runtime_error);
        }
    }

    TEST(project, N2)
    {
    }

    TEST(project, N3)
    {
    }

    TEST(project, N4)
    {
    }

    TEST(project, N5)
    {
    }

    TEST(project, N6)
    {
    }

    TEST(project, N7)
    {
    }