import input_search
import file_open

file_list = list(file_open.file_open('Oliver'))
a = input("please input a word:\n")
i = 0
for i in range(len(file_list)):
    input_search.main(file_list[i], a)


