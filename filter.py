# -*- coding: utf-8 -*-
import re
class Filter:

	def __init__(self, nick_name):
		self.nick_name = nick_name

	def get_result(self):	
		file_name = "../py/musiclog.log"
		f = file(file_name, 'r')
		txt = f.read()
		f.close()
		cura = '^.*' + self.nick_name + '\s(.*$)'
		pattern = re.compile(cura, re.M)
		res = re.findall(pattern, txt)
		l = ('\n').join(res)
		print len(l)
		return l 
if __name__ == "__main__":
	filter = Filter("wode")
	print filter.get_result()
