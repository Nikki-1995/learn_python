s = 'From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'
lists=s.split('@')
print(lists)
name=lists[1].split(' ')
print(name[0])
