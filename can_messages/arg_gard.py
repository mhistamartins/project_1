import sys  # include <sys>
from os import makedirs,path
from argparse import ArgumentParser # #include <argparse> \n using namespace argparse
#from our_informator import Info

if __name__ == "__main__":
#    print(f'OUR NAME = {__name__}, BUT INFOR NAME IS {info.def_magic()}')

    arg_parser = ArgumentParser(description="This script read json file and generates C++ lass (header and source files)")

    arg_parser.add_argument("-i","--input",action="store",
                            help="Specify a path to read signals.json"
                            , required=True)
    arg_parser.add_argument("-o","--output_dir",action="store",
                            help="output dir", default="./output")
    
    arguments = arg_parser.parse_args()

    print(f' input file = {arguments.input}')
    print(f' output dir = {arguments.output_dir}')

    makedirs( arguments.output_dir )
    include_path = path.join(arguments.output_dir , "include", "can_messages")
    makedirs(include_path )
    src_path = path.join(arguments.output_dir , "src")
    makedirs(src_path)

