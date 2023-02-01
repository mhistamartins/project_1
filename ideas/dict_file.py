
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
    buffer = "\n //some comment \n"
    buffer += f'\tstd::string set_{signal_name}({signal_type} newValue);'
    return buffer


def generate_get_set_functions(json_dict):
    content = []
    for signal in json_dict["signals"]:
        signal_name = signal["name"]
        signal_type = signal["type"]
        signal_length = signal["length"]
        signal_comment = signal["comment"]
        set_prototype = generate_setter_h(signal_name, signal_type, signal_length, signal_comment)
        content.append(set_prototype)
    return content


def generate_private_fields(json_dict):
    content = []
    return content


def generate_header(json_filename, json_dict):
    output = []

    header_top, header_bottom = gen_include_guard_class_decl_ctor(json_filename)
    output += header_top

    # fill in with more code...
    output += generate_get_set_functions(json_dict)
    output.append('    private:')
    output += generate_private_fields(json_dict)

    output += header_bottom  # output = output + header_bottom
    return output


def generate_source(json_filename, json_dict):
    return []


if __name__ == "__main__":
    input_filename = "min_signals.json"
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
    # TODO: create a string with filename for a header
    # TODO: create a string with filename for a source file
