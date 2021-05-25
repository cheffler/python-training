# default is to read only
# with open('13_file_io/test.txt', mode='r') as my_file:
#     print(my_file.readlines())

# r+ is read and write
# r+ will write at cursor 0 (start and overwrite)
# r+ requires file to be there
# w is write and will create file
# a is append
with open('13_file_io/test.txt', mode='a') as my_file:
    text = my_file.write(':)\n')
    print(text)
