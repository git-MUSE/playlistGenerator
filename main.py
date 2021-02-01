import os

mus= os.listdir(path='.')

with open('test.m3u', 'w') as file:
    file.write(r'#EXTM3U'+'\n')

    for i in mus:
        if i=='test.m3u' or i=='main.py':
            #to compile the file, replace 'main.py' to 'main.exe'
            pass
        else:
            file.write(r'#EXTINF:1,'+i+'\n')
            file.write(i+'\n'+'\n')

os.startfile('test.m3u')










