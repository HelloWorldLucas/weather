#!/usr/bin/env python
# -*- coding: utf-8 -*-

def parse_to_utf8(ucode):
	if not ucode :
		return ""
	if isinstance(ucode, unicode):
		ucode.encode('utf-8')
	else:
		ucode = ""
	return ucode

if __name__ == "__main__":
	print parse_to_utf8(u"ok")
	print parse_to_utf8('wrong')
	print parse_to_utf8(u"周五")