
import json


def write_output(filename, data):
    with open(filename, "w") as file_fd:
        file_fd.writelines(data)


def gen_include_guard_class_decl_ctor(json_filename):
    top = []  # include guard, class declaration and constructor
    bottom = ""  # ending of include guard

    json_name_upper = json_filename.upper()
    include_guard_name = f'HEADER_{json_name_upper}_H'

    top.append(f'#ifndef {include_guard_name}')
    top.append(f'#define {include_guard_name}')
    top.append('\n')
    top.append(f'class CAN_{json_filename} {{')
    top.append('    public:')
    top.append(f'        CAN_{json_filename}();')

    bottom = ['};', f'#endif //{include_guard_name}']
    return top, bottom


def generate_setter_h(signal_name, signal_type, signal_length, signal_comment):
    buffer = "\n"
    buffer = f'\t/*\n\tset {signal_comment}\n\t */'
    buffer += f'\n\tstd::string set_{signal_name}({signal_type} newValue);'
    return buffer


def generate_getter_h(signal_comment, signal_name):
    buffer = ""
    buffer += f'\t/*\n\t get_{signal_comment}\n\t */'
    buffer += f'\n\tstd:: string get_{signal_name}();\n\t '
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
        set_prototype = generate_setter_h(signal_name, signal_type, signal_length, signal_comment)
        content.append(set_prototype)
        
    return content


def generate_private_fields(json_dict):
    content = []
    data_type = "unint8_t"
    content.append(f'\n\t {data_type} m_startMsgID;')
    for element in json_dict["signals"]:
        content.append(f'\t {data_type} m_{element["name"]}GetMsgID;')
        content.append(f'\t {data_type} m_{element["name"]}SetMsgID;')

    return content


def generate_header(json_filename, json_dict):
    output = []

    header_top, header_bottom = gen_include_guard_class_decl_ctor(json_filename)
    output += header_top
    output += generate_get_set_functions(json_dict)
    output.append('\n\tprivate:')
    output += generate_private_fields(json_dict)

    output += header_bottom  # output = output + header_bottom
    return output


def write_header_file(filename, data):
    if filename is None or filename == "":
        return
    with open(filename, 'w') as file_fP:
        file_fP.writelines(data)


def gen_incl_guard_src(json_filename):
    top = []
    bottom = ""

    json_filename_lower = json_filename.lower()
    m_startMsgId = 0x100
    start_msg_id = "m_startMsgId"

    top.append(f'#include "can_messages/{json_filename_lower}.h" ')
    top.append(f'#include <sstream>')
    top.append(f'\nCAN_{json_filename_lower}::CAN_{json_filename_lower}() {{')
    top.append(f'\t{start_msg_id};')
    top.append(f'\tm_temperatureGetMsgId = {start_msg_id} + 2 ;')
    top.append(f'\tm_temperatureSetMsgId = {start_msg_id} + 2 + 1;')
    top.append(f'\tm_humidityGetMsgId = {start_msg_id} + 4')
    top.append(f'\tm_humiditySetMsgId = {start_msg_id} + 4 + 1 ;\n')

    bottom = ['}']

    return top, bottom


def generate_source(json_filename, json_dict):
    output = []
    
    
    header_top, header_bottom = gen_incl_guard_src(json_filename)
    output += header_top
    output += header_bottom

    return output



if __name__ == "__main__":
    input_filename = "min_signals.json"
    filename_h = "/Users/aboycandream/dev/project_1/project_1/can_messages/output/include/can_messages/CAN_min_signals.h"
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


   