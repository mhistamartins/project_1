CMAKE_MINIMUM_REQUIRED(VERSION 3.10)

PROJECT(PoC) #proof of concept 
set(CMAKE_CXX_STANDARD 17)

add_subdirectory(file_io)
add_subdirectory(can_messages)

message(STATUS "Generated Include path = ${CAN_INCLUDE_DIR}),sources= ${CAN_SOURCES}")

add_subdirectory(main_component)