import names
from random import *
from print_dict import pd
from print_dict import format_dict
import sortedict
from time import sleep

mode = input('W or R? ')
mode = mode.lower()
system = {}
time = ''

if mode == 'w':
    full = ''
    file = open('NT.txt','w')
    amount = int(input('class amount? '))
    for clas in range(amount):
        clas += 1
        print(f'**{clas}')
        full += f'**{clas}' + '\n'
        for i in range(randint(27,32)):
            if randint(1,2) == 1:
                full += names.get_full_name(gender='male') + '\n'
            else:
                full += names.get_full_name(gender='female') + '\n'
    print(full)
    file.write(full)
    file.close()
    print('DONE')

if mode == 'r':
    file = open('NT.txt','r')
    inside = str(file.read()).split('\n')
    school = inside
    for line in school:
        if line.startswith('**'):
            system[str(line[2:])] = {}
            time = line[2:]
        elif line == '':
            pass
        else:
            system[time][str(line)] = 'O'
    #{klasse{name}}
    #pd(system)
    newsys = {}
    for a in system:
        #print(a + '**')
        newlist = sorted(system[a])
        newsys[str(a)] = {}
        for b in newlist:
            newsys[str(a)][str(b)] = 'O'
    #pd(newsys)
    system = {}
    for clas in newsys:
        last = ''
        #print(str(len(newsys[clas])) + '----------------')
        #print(newsys[clas])
        #print(len(newsys[clas])%2)
        #print('--------------')
        if len(newsys[clas]) % 2 == 0:
            newlist = sorted(newsys[clas])
            for i in range(int(len(newsys[clas]) / 2)):
                i += 1
                a = i
                #print(f'{i}/{len(newsys[clas])}/{int(len(newsys[clas]) / 2)}: {newlist[a - 1]}')
                newsys[clas][newlist[a - 1]] = 'A'
            #print('-_-_--_-_--__--___----------------')
            for b in range(int(len(newsys[clas]) / 2)):
                b += 1 + a
                #print(f'{b}/{len(newsys[clas])}/{int(len(newsys[clas]) / 2)}: {newlist[b - 1]}')
                newsys[clas][newlist[b - 1]] = 'B'

        else:
            newlist = sorted(newsys[clas])
            last = newlist[-1]
            #print(f'last ============================================= {last}')
            #print(f'{len(newsys[clas])}/{int(len(newsys[clas]) / 2)}')
            for i in range(int(len(newsys[clas]) / 2)):
                i += 1
                a = i
                #print(f'{i}/{len(newsys[clas])}/{int(len(newsys[clas]) / 2)}: {newlist[a-1]}')
                newsys[clas][newlist[a - 1]] = 'A'
            #print('-_-_--_-_--__--___----------------')
            for b in range(int(len(newsys[clas]) / 2)):
                b += 1 + a
                #print(f'{b}/{len(newsys[clas])}/{int(len(newsys[clas]) / 2)}: {newlist[b-1]}')
                newsys[clas][newlist[b-1]] = 'B'
            newsys[clas][last] = 'B'

    for clasA in range(int(len(newsys)/2)+1):
        classlist = sorted(newsys)
        clasAs = classlist[clasA]
        for membA in newsys[clasAs]:
            for clasB in range(int(len(newsys)/2)):
                clasB += int(len(newsys)/2)
                clasBs = classlist[clasB]
                for membB in newsys[clasBs]:
                    if membA.split(' ')[1] == membB.split(' ')[1]:
                        print(f'WARNING! {membB};{clasBs} and {membA};{clasAs}')
    #sleep(2)
    pd(newsys)
    file.close()
    file = open('NT.txt','w')
    #file.write(str(str(str(newsys).replace('{','{\n')).replace('}','\n}').replace(',',',\n\t')))
    file.write(format_dict(newsys))
    file.close()
