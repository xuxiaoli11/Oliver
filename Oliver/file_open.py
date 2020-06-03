import input_search
import os


def file_open(filename):
    # for root, dirs, files in os.walk(filename):
    #     for dir in dirs:
    #         print(os.path.join(root, dir))
    return os.listdir(filename)
    # print(filename_list)

# a = input("please input a word:\n")
# file = open("count_word.txt", 'r')
# input_search.main(file, a)

# print(ss)


print(file_open('Oliver'))
