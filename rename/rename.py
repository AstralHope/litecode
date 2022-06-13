# -*- coding: utf-8 -*-
import os
# path=input('输入文件路径（以/结尾）')
old = []
new = []
pwd = os.getcwd()
path_old =pwd + os.sep  + 'old'
path_new =pwd + os.sep  + 'new'
f = open(pwd + os.sep +'old.txt')
for line in f:
	old.append(line.strip())
f.close()
f = open(pwd + os.sep +'new.txt')
for line in f:
	new.append(line.strip())
f.close()
# print(a)
# print(b)
for i in range(len(old)):
	oldname=path_old+ os.sep + old[i]   # os.
	if os.path.isfile(oldname):
		#设置新文件名
		newname=path_new + os.sep + new[i]
		os.rename(oldname,newname)   #用os模块中的rename方法对文件改名
		print("已找到",old[i],"移至",newname)
	else:
		print("没找到",old[i])
print("重命名完成！")
	