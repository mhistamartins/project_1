#working with files
def read_file(filename):
    buffer = []  
    #first check that filename is not empty
    if filename is None or filename =="":
        return buffer #if filename is none or empty, then return empty list
    file_obj = open(filename, "r")  #we open a file, r is for read
    buffer = file_obj.readlines()  #readlines help to read the list of all the contents
    file_obj.close()
    return buffer

def read_file_improved(filename):
    buffer = []
    if filename is None or filename =="":
        return buffer
    with open(filename, 'r') as obj_file:
        buffer = obj_file.readlines()
        return buffer


#function to write a file
def write_file(filename, data_to_write):
    if filename is None or filename == "":
        return
    #we open a file to write (and override the contect incase if the file doesnt exist)
    write_file_obj = open(filename, 'w')
    write_file_obj.writelines(data_to_write)
    write_file_obj.close()


if __name__== "__main__":
    content = read_file("RandomFile.txt")
    #print("------------")
    #print(content)
    print("------------")
    for line in content:
        print(line)
    print("------------")

    content = read_file_improved("Improved_randomfile.txt")
    for Line in content:
        print(Line)
   

    print("...............")

    write_file("anotherRandomfile.txt", content)
    print("Everything is done now")

