try:
    f = open('simple.txt','r')
    f.write('Teste write')
except Exception as inst:
    print(dir(inst))
    print('type\t:',type(inst))
    print('errorno\t:',inst.errno)
    print('filename:',inst.filename)
    print('strerror:',inst.strerror)
    print('args\t:',inst.args)
    print('inst\t:',inst)
else:
    print('SUCESS')
    f.close()

