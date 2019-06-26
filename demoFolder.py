
#获取文件夹/文件名路径、创建文件夹、查看文件夹内容
import os

print('【获取指定路径的文件、文件大小】')
path='E:\\demo\\test\\17计算机期末成绩.csv' #指定路径
print(os.path.dirname(path)) #获取文件夹
print(os.path.basename(path)) #获取文件名
print(os.path.getsize(path)) #获取文件大小
print('--'*20)
print('\n')


print('【获取指定文件夹、查看文件夹内容】')
path1='E:\\demo\\test\\' #指定文件夹
print(os.listdir(path1)) #查看文件夹内容
print('--'*20)
print('\n')

print('【获取当前文件目录、查看文件夹内容】')
path2=os.getcwd() #获取当前文件目录
print(path2)
print(os.listdir(path2)) ##遍查看文件夹内容
print(__file__) #获取当前文件路径
print('--'*20)
print('\n')


print('【分割路径、分割后缀名】')
path5='E:\\demo\\test\\17计算机期末成绩.csv'
print(os.path.split(path5)) #分割当前路径的文件夹和文件
print(os.path.splitext(path5)) #分割文件后缀
print('--'*20)
print('\n')

print('【判断文件夹/文件是否存在】')
path3='E:\\demo\\test\\'
print(os.path.exists(path3)) #判断文件夹/文件是否存在，存在返回True
path4='E:\\demo\\test\\111.csv'
print(os.path.exists(path4)) #判断文件夹/文件是否存在，存在返回True
print('--'*20)
print('\n')


print('【创建新目录】')
#os.makedirs('data\\123\\abc') #创建新的文件夹（包含所有必要的中间文件夹），当文件夹存在时报错
print('--'*20)
print('\n')
