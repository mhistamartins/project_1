def list_example():
    #how to define a list:
    #variable_name = [ enumerate elements ]
    list_v1 = [ 1, 2, 3.142, "a string", "five"]
    print(list_v1)

    #list.append to add element to the lis
    #list.pop(element_position) to remove element from the lis
    #list.remove() TO remove element equal to a specific line

#dictionary is a set of key : value 
def dict_example():
    dict_v1 = { "key1":"value1" , "key2": 12, 35 : "value3"}
    print(dict_v1)
    for key_elem in dict_v1:
        print(f'key_elem = {key_elem} contains {dict_v1[key_elem]} ')



if __name__ == "__main__":
    #list_example()
    dict_example()
