import json

def json_dict(filename):
    buffer = []
    if filename is None or filename == "":
        return buffer
    with open(filename, 'r') as json_file:
        buffer = json_file.readlines()
        return buffer
  

def write_list(filename, list_of_strings):
    if filename is None or filename == "":
        return
    with open(filename, 'w') as file_fP:
        file_fP.writelines(list_of_strings)


def generate_headerfile(class_name, signal_name, signal_type, value_type, signal_comment):
    output_data = ""
    output_data += '\t/*\tget {}\n\t*/' .format(signal_comment)
    output_data += "\n\*\tstd::string get_{}(); \n" .format(signal_name)
    output_data += '\t/*\n\tset {}\n\t*/' .format(signal_comment)
    output_data += "\n\tstd::string set:{}({} {}); \n " .format(signal_name, signal_type, value_type)

    return output_data


def create_headerfile():

    header_file_path = "project_1/can_messages/output/include/can_messages/CAN_min_signals.h"
    header_file = open(header_file, "w")

    ifndef_def = "#ifndef SIGNALS_H"
    define = "#define SIGNALS_H"
    endif = "#endif /* SIGNALS_H */\n"
    include = "#include<sstream>"
    header_file.write("{}\n{}\n\n".format(ifndef_def, define))
    header_file.write("{}\n\n" .format(include))
    class_can = 'class CAN_min_signals\n{'
    public = '\npublic:\n'
    private = '\nprivate:\n'
    constructor = '\tCAN_min_signals();\n'
    header_file.write(class_can + public)
    header_file.write(constructor)
    for signal_element in json_dict["signals"]:
        print(signal_element["name"])
        formatted_string = f'{signal_element["type"]} and {signal_element["length"]}'
        print(formatted_string)
        print(signal_element["comment"])
        header_file.write(generate_headerfile
            ("CAN_messages", signal_element["name"], signal_element["type"], "newValue", signal_element["comment"]))
             
        header_file.write("};\n" + endif)
        header_file.close()

if __name__ == "__main__":

    content = json_dict('min_signals.json')
    for Line in content:
        print(Line, end='')
    print()

    write_list("MyList", content)

    output = generate_headerfile("CAN_min_signals", "temperature", "float", "new value", "the ambient temperature")
    print(output)

    create_headerfile()
