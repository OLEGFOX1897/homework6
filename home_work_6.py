#Task 2 Написать программу, которая будет считать введенное выражение типа 2+2*3
# Мои допущения: 
# 1. Не читает отрицательное число в скобках, к примеру (-7)
# 2. В скобках выполняется одно действие

inp_mem='-89+73+(45/0)*1.2' # тут вводится исходное значение
inp_mem=inp_mem.replace(' ','')
inp_mem_in=inp_mem


def LR_digit(ind_sign, inp_mem):
    """ Модуль возвращает в кортеже левое, правое число относительно входном индекса математич знака,
    а так же их левый и правый индексы во входном выражении"""
    ind=ind_sign
    while True:
        ind+=1
        if ind<=len(inp_mem)-1:
            if inp_mem[ind].isdigit()==0 and inp_mem[ind]!='.':
                right_dig_ind=ind-1
                break
        elif ind>len(inp_mem)-1:
            right_dig_ind=len(inp_mem)-1
            break
    ind=ind_sign
    while True:
        ind-=1
        if ind==0 and inp_mem[ind].isdigit()==1:
            left_dig_ind=0
            break
        elif inp_mem[0]=='-' and ind==0:
            left_dig_ind=0
            break
        elif not inp_mem[ind].isdigit() and inp_mem[ind]!='.':
            left_dig_ind=ind+1
            break
    return inp_mem[left_dig_ind:ind_sign], inp_mem[ind_sign+1:right_dig_ind+1], left_dig_ind, right_dig_ind 

def calc_mem(inp_mem):
    while True:
        if inp_mem.find('/0')!=-1:
                    print(inp_mem.find('/0'))
                    print('Делить на ноль нельзя. Исправьте выражение.')
                    break
        elif '--' in inp_mem:
            inp_mem=inp_mem.replace('--','+')
        elif '+-' in inp_mem:
            inp_mem=inp_mem.replace('+-','-')
        elif'(' and ')' in inp_mem:
            list_no_dig=[x for x in inp_mem[inp_mem.find('(')+1: inp_mem.find(')')] if not x.isdigit()] # находит математ знак в скобках
            inp_mem=new_mem(inp_mem.find(list_no_dig[0],inp_mem.find('(')), inp_mem, list_no_dig[0], 1)
        elif '*' in inp_mem:
                inp_mem=new_mem(inp_mem.find('*'), inp_mem,'*', 0)
        elif '/' in inp_mem:
                inp_mem=new_mem(inp_mem.find('/'), inp_mem,'/', 0)
        elif inp_mem.find('-',1)>0 or inp_mem.find('+',1)>0:
                list_ind_s_min=[x for x in range(1,len(inp_mem)-1) if inp_mem[x]=='+' or inp_mem[x]=='-'] # создает лист с индексами всех (+) и (-) 
                # не включая самый первый
                ind_sign=list_ind_s_min[0] #индекс знака
                sign=inp_mem[ind_sign] #знак в выражении + или -
                inp_mem=new_mem(ind_sign, inp_mem, sign, 0)
        else: break
    return inp_mem
         
def new_mem(ind_sign, inp_mem, a:str, b):
    '''Модуль возвращает новое математическое выражение после выполненого одного математ действия'''
    tut_LR_dig=LR_digit(ind_sign,inp_mem)
    if a=='*':
        new_dig=float(tut_LR_dig[0])*float(tut_LR_dig[1])
    elif a=='/':
        new_dig=float(tut_LR_dig[0])/float(tut_LR_dig[1])
    elif a=='-':
        new_dig=float(tut_LR_dig[0])-float(tut_LR_dig[1])
    elif a=='+':
        new_dig=float(tut_LR_dig[0])+float(tut_LR_dig[1])
    if b==0:    
        inp_mem=inp_mem[0:tut_LR_dig[2]]+str(new_dig)+inp_mem[tut_LR_dig[3]+1:len(inp_mem)]
    else:
        inp_mem=inp_mem[0:tut_LR_dig[2]-1]+str(new_dig)+inp_mem[tut_LR_dig[3]+2:len(inp_mem)]
    return inp_mem
print(f'{inp_mem_in}={calc_mem(inp_mem)}')
        



    
    




    
    
