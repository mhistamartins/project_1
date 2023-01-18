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
