f=open('mbox.txt','r')
comp_names={}
for i in f:
    if i.startswith('From'):
        line=i.split('@')
        name=(line[1].split(' ')[0])
        if name in comp_names:
            comp_names[name]+=1
        else: 
            comp_names[name]=1
for (p,k) in comp_names.items():
    print(p,':',k)  


f.close()          