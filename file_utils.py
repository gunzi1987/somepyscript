# -*-coding: utf-8 -*-


__author__ = 'lifenghua'


import os
import shutil

#复制文件
#@param src_filename:要cp的文件绝对路径
#@param dst_dir:目标文件夹
def copy_file(src_filename, dst_dir):
	if (not os.path.exists(dst_dir)) or (not os.path.isdir(dst_dir)):
		return
	if (not os.path.exists(src_filename)) or (not os.path.isfile(src_filename)):
		return
	bn = os.path.basename(src_filename)
	dst_filename = os.path.join(dst_dir, bn)
	shutil.copy2(src_filename, dst_filename)

#复制文件
#@param src_filename:要cp的文件绝对路径
#@param dst_filename:目标文件
def copy_file_to_file(src_filename, dst_filename):
	if (not os.path.exists(src_filename)) or (not os.path.isfile(src_filename)):
		return
	shutil.copy2(src_filename, dst_filename)

#复制文件夹
#@param src:原始文件件
#@param dst:目标文件夹
def copy_dir(src, dst):
	names = os.listdir(src)
	if not os.path.isdir(dst):
		os.makedirs(dst)

	for name in names:
		src_name = os.path.join(src, name)
		dst_name = os.path.join(dst, name)
		if os.path.isdir(src_name):
			copy_dir(src_name, dst_name)
		else:
			if os.path.isdir(dst_name):
				os.rmdir(dst_name)
			elif os.path.isfile(dst_name):
				os.remove(dst_name)
			shutil.copy2(src_name, dst_name)


#删除文件夹
#@param dst_dir:要删除的文件夹绝对路径
def del_dir(dst_dir):
	if (os.path.exists(dst_dir)) and (os.path.isdir(dst_dir)):
		shutil.rmtree(dst_dir)


#删除文件
#@param filename:要删除的文件绝对路径
def del_file(filename):
	if (os.path.exists(filename)) and (os.path.isfile(filename)):
		os.remove(filename)


#创建文件夹
#@param dst_dir:文件夹绝对路径
def mk_dir(dst_dir):
	if (not os.path.exists(dst_dir)) or (not os.path.isdir(dst_dir)):
		os.makedirs(dst_dir)
