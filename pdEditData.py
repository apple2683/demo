

import pandas as pd
#~~~~~~~~~~~~~~~~~~~~~Pandas读取数据(单个Sheet)~~~~~~~~~~~~~~~~~~~~#

df=pd.read_excel('pyexcel\\2017年级.xlsx',sheet_name=0,header=0,index_col=None)
print(df,"\n",type(df)) #df 原始数据
print('*'*60,"\n")

df1=df.copy()
df2=df1.fillna(value='ok')
print(df2)
# print(df.loc[0,'分数'],type(df.loc[0,'分数']))
# data={}
# for i in df.values:
#     if type(i[3])==float:
#         i[3]=int(round(i[3],0))
#     data.append(i)
#
#
# pop={'班级':data[0],'学期':data[1]}
# print(data[0],type(data))
# df.to_csv('pycsv\\2017年级.csv',index=0,header=1,encoding='utf-8_sig',na_rep='缺考')

# dfcsv=pd.read_csv('pycsv\\2017年级.csv',header=0)
# print(dfcsv,"\n",type(dfcsv))
















#~~~~~~~~~~~~~~~~~~~~~Pandas读取数据(多个Sheet)~~~~~~~~~~~~~~~~~~~~#
# df=pd.read_excel('pyexcel\\2017年级.xlsx',sheet_name=None,header=0,index_col=None)
# print(df,"\n",type(df)) #df 原始数据
# print('*'*60,"\n")
#
#
# for k,i in df.items():
#     print(i,type(i))
#     i.to_csv('pycsv\\2017年级.csv',index=0,header=1,encoding='utf-8_sig',na_rep='缺考',float_format='%.2f')
# # #
# dfcsv=pd.read_csv('pycsv\\2017年级.csv',header=0)
# print(dfcsv,"\n",type(dfcsv))
# print('*'*60,"\n")









# print('*'*30,type(df))
# df=df.fillna(value='缺考')
# df=df.replace('陈林峰', '林欣')

# for i in df.values:
#     if type(i[3])==float:
#         i[3]=int(round(i[3],0))
#     print(i)
# print(df.分数)
# for i in df.values:
#     i[3]=int(round(i[3],0))
#     print(i[3],type(i[3]))

# print(df)
# print(df.分数.dtype)
# print(df.分数.round(0))










#**********以下有用***************#
def EditScore(v):
    v=v.fillna(value='缺考')
    for i in v.values:
        if type(i[3])==float:
            i[3]=int(round(i[3],0))
        # print(i)
    return i

# def ToCSV():
#     #excel多个sheet数据写入1个csv文件，不含标题
#     io='pyexcel\\2017年级.xlsx'
#     df=pd.read_excel(io,sheet_name=None,header=0,index_col=None)
#
#     num=0
#     for k,v in df.items():
#         v=v.fillna(value='缺考')
#         if type(v.分数)==float:
#             print('ok')
#         print(v.分数)
#         print(v)
#         num=len(v.index)+num
#         # v.to_csv('pycsv\\2017年级.csv',index=False,header=False,encoding='utf-8_sig',mode='a')
#     print('总共' + str(num) + '条记录')
# ToCSV()
