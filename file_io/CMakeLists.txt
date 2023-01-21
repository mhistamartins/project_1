cmake_minimum_required(VERSION 3.10)

project(project CXX)

#tells to CMake to search for header files in lib/include folder
include_directories(lib/include)

set(sourcesLib lib/src/project.cpp)
set(sourcesApp app/src/test.cpp)


#we are telling to cmake to build a library from source code
add_library(project_file_lib ${sourcesLib})

#it is our poor application
add_executable(projectApp ${sourcesApp})

#link our library to an executable file
target_link_libraries(projectApp project_file_lib)


# GoogleTest requires at least C++14
#include CMake module to be able to download GoogleTest code.
include(FetchContent)

# Declare git repo and tag to fetch:
FetchContent_Declare(
  googletest
  GIT_REPOSITORY https://github.com/google/googletest.git
  GIT_TAG        release-1.12.0
)

# For Windows: Prevent overriding the parent project's compiler/linker settings
set(gtest_force_shared_crt ON CACHE BOOL "" FORCE)

#Download or check that googletest is downloaded:
FetchContent_MakeAvailable(googletest)

add_executable(lib_ut_tests lib/ut/gtest.cpp)
target_link_libraries(lib_ut_tests gtest gtest_main)
