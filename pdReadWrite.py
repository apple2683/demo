import pandas as pd
#~~~~~~~~~~~~~~~~~~~~~Pandas数据读取（excel）与写入（csv）(单个Sheet)~~~~~~~~~~~~~~~~~~~~#
# df=pd.read_excel('pyexcel\\2017年级.xlsx',sheet_name=2,header=0,index_col=None)
# print(df) #df 原始数据
# print('*'*60,"\n")
# #填充空值NaN(inplace = True让源数据发生改变)
# df.fillna(value='缺考',inplace = True)
# #分数处理
# def EditScore(data):
#     v=[]
#     for i in data:
#         if type(i)==float:
#             i=int(round(i,0))
#         if i=='缺':
#             i='缺考'
#         if i=='及':
#             i='及格'
#         v.append(i)
#     return v
#
# df.分数=EditScore(df.分数) #修改后的分数列替换原来列
# print(df)
#
# #写入csv文件，index=None（行索引不写入），encoding='utf-8_sig'（解决excel打开csv乱码）
# # mode='a'(追加的方式写入),header=None(不写入列索引)
# df.to_csv('pycsv\\2017年级.csv',index=False,encoding='utf-8_sig',mode='a')
# print('总共 ' + str(df.shape[0]) + ' 条记录')
# print('Success')

#~~~~~~~~~~~~~~~~~~~~~Pandas数据读取（excel）与写入（csv）(多个Sheet)~~~~~~~~~~~~~~~~~~~~#
import pandas as pd
df=pd.read_excel('2017年级成绩数据.xlsx',sheet_name=0,header=0,index_col=None)
print(df,type(df)) #为了便于观察，打印出原始数据
print('*'*60,"\n") #用*符号隔开
#分数处理
def EditScore(data):
    v=[]
    for i in data:
        if type(i)==float:
            i=int(round(i,0))
        if i=='缺':
            i='缺考'
        if i=='及':
            i='及格'
        v.append(i)
    return v

num=0
for i in df.values():
    i.fillna(value='缺考',inplace = True)
    i.分数=EditScore(i.分数)
    print(i) #为了便于观察，打印出处理过后的数据
    num=num+i['姓名'].count() #统计条数
    # i.to_csv('2017年级成绩数据.csv',index=None,header=None,encoding='utf-8_sig',mode='a')
print('总共 ' + str(num) + ' 条记录')
