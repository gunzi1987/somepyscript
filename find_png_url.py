# -*-coding: utf-8 -*-

import os
import sys
import codecs


PNG_LIST = []
PNG_EXT = ".png"
DST_DIR = ''

def trversal_png_dir(abs_path):
	if os.path.isfile(abs_path):
		suffix = os.path.splitext(abs_path)[1]
		if suffix==PNG_EXT:
			PNG_LIST.append(abs_path.replace(DST_DIR, ''))
	else:
		for f in os.listdir(abs_path):
			child_abs_path = os.path.join(abs_path, f)
			trversal_png_dir(child_abs_path)
			

def save_png_fielanem(save_filename):
	save_files = codecs.open(save_filename, "w", "utf-8")
	for name in PNG_LIST:
		save_files.write(name+'\n')
	save_files.close()

if len(sys.argv) >= 1:
	DST_DIR = os.getcwd()
	trversal_png_dir(DST_DIR)
	save_png_fielanem(os.path.join(DST_DIR, 'png_filename.txt'))