#读取文件有四种方法
'''
1.read()
2.readline()
3.readlies()
4.循环文件
'''
#（改方法保险，效率高，内存小）
print('【读取文件】')
with open ('test\\17计算机期末成绩.csv','r',encoding='UTF-8') as file:
    for i in file:
        print(i)

print('--'*20)
print('\n')

#（改方法保险，效率高，内存小）
print('【写入追加文件】')
txt=['18计算机','201704','林想','60','hhah']
with open ('test\\17计算机期末成绩.csv','a',encoding='UTF-8') as file:
    file.write(join(txt))
    for i in file:
        print(i)

print('--'*20)
print('\n')
