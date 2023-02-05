import json

def write_output(filename, data):
    with open(filename, "w") as file_fd:
        file_fd.writelines(data)


def gen_include_guard_class_decl_ctor(json_filename):
    top = []
    bottom = "" 

    json_name_upper = json_filename.upper()
    include_guard_name = f'HEADER_{json_name_upper}_H'

    top.append(f'#ifndef {include_guard_name}\n')
    top.append(f'#define {include_guard_name}')
    top.append(f'\n#include <string>')
    top.append('\n\n')
    top.append(f'class CAN_{json_filename} {{\n')
    top.append('\tpublic:\n')
    top.append(f'\t\tCAN_{json_filename}();')

    bottom = ['};\n', f'#endif //{include_guard_name}']
    return top, bottom


def generate_setter_h(signal_name, signal_type, signal_length, signal_comment):
    buffer = "\n"
    buffer = f'\t\t/*\n\t\tset {signal_comment}\n\t\t*/'
    buffer += f'\n\t\tstd::string set_{signal_name}({signal_type} newValue);'
    return buffer


def generate_getter_h(signal_comment, signal_name):
    buffer = "\n"
    buffer += f'\t\t/*\n\t\t get_{signal_comment}\n\t\t*/'
    buffer += f'\n\t\tstd::string get_{signal_name}();\n'
    return buffer


def generate_get_set_functions(json_dict):
    content = []
    temp = []
    for signal in json_dict["signals"]:
        signal_name = signal["name"]
        signal_type = signal["type"]
        signal_length = signal["length"]
        signal_comment = signal["comment"]
        get_prototype = generate_getter_h(signal_comment, signal_name)
        content.append(get_prototype)
        set_prototype = generate_setter_h(
            signal_name, signal_type, signal_length, signal_comment)
        content.append(set_prototype)

    return content


def generate_private_fields(json_dict):
    content = []
    data_type = "uint8_t"
    content.append(f'\n\t\t{data_type} m_startMsgID;\n')
    for element in json_dict["signals"]:
        content.append(f'\t\t{data_type} m_{element["name"]}GetMsgID;\n')
        content.append(f'\t\t{data_type} m_{element["name"]}SetMsgID;\n')

    return content


def generate_header(json_filename, json_dict):
    output = []

    header_top, header_bottom = gen_include_guard_class_decl_ctor(
        json_filename)
    output += header_top
    output += generate_get_set_functions(json_dict)
    output.append('\n\tprivate:')
    output += generate_private_fields(json_dict)

    output += header_bottom
    return output


def write_header_file(filename, data):
    if filename is None or filename == "":
        return
    with open(filename, 'w') as file_fP:
        file_fP.writelines(data)

#back here
def gen_incl_guard_src(json_filename):
    top = []
    bottom = ""

    json_filename_lower = json_filename.lower()
    start_msg_id = "m_startMsgId"
    data_id = json_dict["id"]
    top.append(f'#include "../include/can_messages/CAN_{json_filename_lower}.h"\n')
    top.append(f'#include <sstream>\n\n')
    top.append(f'CAN_{json_filename_lower}::CAN_{json_filename_lower}() {{\n')
    top.append(f'\t{start_msg_id} = {data_id};\n')
    num = len(list(json_dict["signals"]))
    i = 2
    for element in json_dict["signals"]:
        elem_name = element["name"]
        top.append(f'\tm_{elem_name}GetMsgId = {start_msg_id} + {i}; \n')
        top.append(f'\tm_{elem_name}SetMsgId = {start_msg_id} + {i} + 1;\n')
        i += 2
    top.append(f'}}\n')

    for element in json_dict["signals"]:
        elem_name = element["name"]
        elem_type = element["type"]
        elem_len = element["length"]
        top.append(f'std::string CAN_{json_filename_lower}::get_{elem_name}() {{\n')
        top.append(f'\tstd::stringstream sstream; \n')
        top.append(f'\tsstream << "{{\\"ID\\": " << m_{elem_name}GetMsgId\n')
        top.append(f'\t\t\t<< ", \\"length\\":0 "\n')
        top.append(f'\t\t\t<< ", \\"value\\": \\"\\" }}";\n')
        top.append(f'\treturn sstream.str();\n')
        top.append(f'}}\n')
        top.append(f'std::string CAN_{json_filename_lower}::set_{elem_name}({elem_type} newValue) {{\n')
        top.append(f'\tstd::stringstream sstream;\n')
        top.append(f'\tsstream << "{{\\"ID\\": " << m_{elem_name}GetMsgId\n')
        top.append(f'\t\t\t<< ", \\"length\\":{elem_len} "\n')
        top.append(f'\t\t\t<< ", \\"value\\":\\""\n')
        top.append(f'\t\t\t<< ", \\"value\\":\\""\n')
        top.append(f'\t\t\t<< newValue\n')
        top.append(f'\t\t\t<< \"}}";\n')
        top.append(f'\treturn sstream.str();\n')
        top.append(f'}}\n')

    return top, bottom


def generate_source(json_filename, json_dict):
    output = []

    header_top, header_bottom = gen_incl_guard_src(json_filename)
    output += header_top
    output += header_bottom

    return output


def write_src_file(filename, data):
    if filename is None or filename == "":
        return
    with open(filename, 'w') as file_fP:
        file_fP.writelines(data)


if __name__ == "__main__":
    input_filename = "min_signals.json"
    filename_h = "/Users/aboycandream/dev/project_1/project_1/can_messages/output/include/can_messages/CAN_min_signals.h"
    filename_s = "/Users/aboycandream/dev/project_1/project_1/can_messages/output/src/min_signals.cpp"
    json_dict = {}
    with open(input_filename) as file_fd:
        json_raw_content = file_fd.read()
        json_dict = json.loads(json_raw_content)
    print(json_dict)
    json_filename = input_filename.replace(".json", "")
    print(json_filename)

    header_content = generate_header(json_filename, json_dict)
    for element in header_content:
        print(element)

    print("\n")

    source_content = generate_source(json_filename, json_dict)
    for data in source_content:
        print(data)

write_header_file(filename_h, header_content)
write_src_file(filename_s, source_content)
