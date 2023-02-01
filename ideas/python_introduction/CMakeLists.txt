#create cmakelist in folder where your pyscript is running(canmessages)
#target name could be any variable
add_custom_target(
    generate_sources_from_json
    COMMAND "python3" "classwork.py"  #change filename/path later
    WORKING_DIRECTORY ${CMAKE_CURRENT_SOURCE_DIR}
)

set(CAN_INCLUDE_DIR
                "${CMAKE_CURRENT_SOURCE_DIR}/output/include"
                PARENT_SCOPE)
set(CAN_SOURCES
            ${CMAKE_CURRENT_SOURCE_DIR}/output/src/CAN_min_signals.cpp
            PARENT_SCOPE)