# -*- coding: utf-8 -*-
"""
Created on Tue Jan 30 16:18:41 2018

@author: xuanxuan
"""
# 首先来写如何统计一个英文文本中单词出现的频率（非自己独立完成）


def main():
    file = open("count_word.txt", 'r')
    wordCounts = {}    # 先建立一个空的字典，用来存储单词 和相应出现的频次
    count = 10         # 显示前多少条（按照单词出现频次从高到低）
    for line in file:
        lineprocess(line.lower(), wordCounts)  # 对于每一行都进行处理，调用lineprocess()函数，参数就是从file文件读取的一行
        items0 = list(wordCounts.items())       # 把字典中的键值对存成列表，形如：["word":"data"]
        items = [[x, y] for (y, x) in items0]     # 将列表中的键值对换一下顺序，方便进行单词频次的排序 就变成了["data":"word"]
        items.sort()            # sort()函数对每个单词出现的频次按从小到大进行排序

    for i in range(len(items)-1, len(items)-count-1, -1):   # 上一步进行排序之后 对items中的元素从后面开始遍历 也就是先访问频次多的单词
            print(items[i][1]+"\t"+str(items[i][0]))


def lineprocess(line, wordCounts):
    for ch in line:   # 对于每一行中的每一个字符 对于其中的特殊字符需要进行替换操作
        if ch in "~@#$%^&*()_-+=<>?/,.:;{}[]|\'""":
            line = line.replace(ch, "")
    words = line.split()  # 替换掉特殊字符以后 对每一行去掉空行操作,也就是每一行实际的单词数量
    print(len(words))
    for word in words:
        if word in wordCounts:
            wordCounts[word] += 1
        else:
            wordCounts[word] = 1

    # 这个函数执行完成之后整篇文章里每个单词出现的频次都已经统计好了


main()