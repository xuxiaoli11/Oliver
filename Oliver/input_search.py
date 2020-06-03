def main(file, a):
    file = open('Oliver\\'+file, 'r')
    wordCounts = {}    # 先建立一个空的字典，用来存储单词 和相应出现的频次
    for line in file:
        line_process(line.lower(), wordCounts)  # 对于每一行都进行处理，调用lineprocess()函数，参数就是从file文件读取的一行
        items0 = list(wordCounts.items())       # 把字典中的键值对存成列表，形如：["word":"data"]
        items = [[x, y] for (y, x) in items0]     # 将列表中的键值对换一下顺序，方便进行单词频次的排序 就变成了["data":"word"]
        items.sort()            # sort()函数对每个单词出现的频次按从小到大进行排序
    # a = input("please input a word:\n")
    if a in wordCounts:
        print(wordCounts[a])
        return wordCounts[a]
    else:
        print("no this word")
        return wordCounts == 0


def line_process(line, wordCounts):
    for ch in line:   # 对于每一行中的每一个字符 对于其中的特殊字符需要进行替换操作
        if ch in "~@#$%^&*()_-+=<>?/,.:;{}[]|\'""":
            line = line.replace(ch, "")
    words = line.split()  # 替换掉特殊字符以后 对每一行去掉空行操作,也就是每一行实际的单词数量
    for word in words:
        if word in wordCounts:
            wordCounts[word] += 1
        else:
            wordCounts[word] = 1


# main('a.txt', 'love')
