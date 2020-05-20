fil = open('IN.txt','r',encoding='utf-8')

lines = fil.readlines()
i=0
for line in lines:
    print(i)
    i+=1
    #print(line)
    line = line.split(',')[0]
    line = line.replace(' ','')
    line = line.lower()
    names = line+'\n'
    line = names
    if names[0]=='a':
        with open('a.txt','a+',encoding='utf-8') as f:
            f.write(line.replace(' ',','))
    elif names[0]=='b':
        with open('b.txt','a+',encoding='utf-8') as f:
            f.write(line.replace(' ',','))
    elif names[0]=='c':
        with open('c.txt','a+',encoding='utf-8') as f:
            f.write(line.replace(' ',','))
    elif names[0]=='d':
        with open('d.txt','a+',encoding='utf-8') as f:
            f.write(line.replace(' ',','))
    elif names[0]=='e':
        with open('e.txt','a+',encoding='utf-8') as f:
            f.write(line.replace(' ',','))
    elif names[0]=='f':
        with open('f.txt','a+',encoding='utf-8') as f:
            f.write(line.replace(' ',','))
    elif names[0]=='g':
        with open('g.txt','a+',encoding='utf-8') as f:
            f.write(line.replace(' ',','))
    elif names[0]=='h':
        with open('h.txt','a+',encoding='utf-8') as f:
            f.write(line.replace(' ',','))
    elif names[0]=='i':
        with open('i.txt','a+',encoding='utf-8') as f:
            f.write(line.replace(' ',','))
    elif names[0]=='j':
        with open('j.txt','a+',encoding='utf-8') as f:
            f.write(line.replace(' ',','))
    elif names[0]=='k':
        with open('k.txt','a+',encoding='utf-8') as f:
            f.write(line.replace(' ',','))
    elif names[0]=='l':
        with open('l.txt','a+',encoding='utf-8') as f:
            f.write(line.replace(' ',','))
    elif names[0]=='m':
        with open('m.txt','a+',encoding='utf-8') as f:
            f.write(line.replace(' ',','))
    elif names[0]=='n':
        with open('n.txt','a+',encoding='utf-8') as f:
            f.write(line.replace(' ',','))
    elif names[0]=='o':
        with open('o.txt','a+',encoding='utf-8') as f:
            f.write(line.replace(' ',','))
    elif names[0]=='p':
        with open('p.txt','a+',encoding='utf-8') as f:
            f.write(line.replace(' ',','))
    elif names[0]=='q':
        with open('q.txt','a+',encoding='utf-8') as f:
            f.write(line.replace(' ',','))
    elif names[0]=='r':
        with open('r.txt','a+',encoding='utf-8') as f:
            f.write(line.replace(' ',','))
    elif names[0]=='s':
        with open('s.txt','a+',encoding='utf-8') as f:
            f.write(line.replace(' ',','))
    elif names[0]=='t':
        with open('t.txt','a+',encoding='utf-8') as f:
            f.write(line.replace(' ',','))
    elif names[0]=='u':
        with open('u.txt','a+',encoding='utf-8') as f:
            f.write(line.replace(' ',','))
    elif names[0]=='v':
        with open('v.txt','a+',encoding='utf-8') as f:
            f.write(line.replace(' ',','))
    elif names[0]=='w':
        with open('w.txt','a+',encoding='utf-8') as f:
            f.write(line.replace(' ',','))
    elif names[0]=='x':
        with open('x.txt','a+',encoding='utf-8') as f:
            f.write(line.replace(' ',','))
    elif names[0]=='y':
        with open('y.txt','a+',encoding='utf-8') as f:
            f.write(line.replace(' ',','))
    elif names[0]=='z':
        with open('z.txt','a+',encoding='utf-8') as f:
            f.write(line.replace(' ',','))