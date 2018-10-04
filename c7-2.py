#!/usr/bin/python3
#-*-coding:UTF-8-*-

other={'城市':'北京','爱好':'编程'}
def personinfo(name,number,**kw):
    print('名称',name,'学号:',number,'其他:',kw)
    pass
personinfo('',1002,城市=other['城市'],爱好=other['爱好'])