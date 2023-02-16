import pytest
import subprocess
from os import path

inputfile_content="""
set temperature 50
"""
expected_read_content="""
{
    "cmds " : [ 
		{"ID": 103, "length":10 , "value": " 72.43" }
	]
}
"""
def test_mc():
    input_filename="input.txt"
    output_filename = "output.txt"
    print(inputfile_content)

    with open(input_filename , "w") as fd:
        fd.write(inputfile_content)

    mc_filename = path.join(path.curdir, "../..", "build/main_component/main_component")

    mc_process = subprocess.run(
        args=[mc_filename, input_filename, output_filename],
        capture_output = True
    )
    captured_output = mc_process.stdout.decode()
    print(captured_output)

    read_output = ""
    with open(output_filename) as fd:
        read_output = fd.read()

    print(f'_{read_output}_')
    print(f'_{expected_read_content}_')

    assert read_output == expected_read_content