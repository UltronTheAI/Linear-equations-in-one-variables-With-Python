def RemoveNumFromX(x):
    # res = x.split('=')[1]
    res2 = x.split(' ')
    fx = 0
    fx2 = 0
    calc = []
    calc2 = []
    
    for i in range(0, len(res2)):
        data = res2[i]
        if 'x' in data:
            if fx == 0:
                d2 = data.replace('x', '')
                if d2 == '':
                    d2 = 1
                else: d2 = int(d2)
                fx2 += d2
            else: 
                pn1 = ''
                pn2 = ''
                try:
                    bres2 = res2[i - 1]
                    if bres2 == '+':
                        pn1 = '-'
                    if bres2 == '-':
                        pn1 = '+'
                    if bres2 == '*':
                        pn1 = '/'
                    if bres2 == '/':
                        pn1 = '*'
                    
                except: pass
                try:
                    bres2 = res2[i + 1]
                    if bres2 == '+':
                        pn2 = '-'
                    if bres2 == '-':
                        pn2 = '+'
                    if bres2 == '*':
                        pn2 = '/'
                    if bres2 == '/':
                        pn2 = '*'

                except:
                    pass
                
                if pn1 == '-' or pn1 == '+' or pn1 == '/' or pn1 == '*':
                    
                    if data.replace('x', '') == '':
                        data = '1'
                    num = int(data.replace('x', ''))
                    if pn1 == '-':
                        fx2 -= num
                    if pn1 == '+':
                        fx2 += num
                    if pn1 == '/':
                        fx2 /= num
                    if pn1 == '*':
                        fx2 *= num
        if data == '=': fx = 2
        else:
            if fx == 0:
                if 'x' in data or '-' in data or '+' in data or '*' in data or '/' in data: pass
                else:
                    pn3 = ''
                    pn4 = ''
                    try:
                        pn33 = res2[i - 1]
                        # print(pn3)
                        if pn33 == '-':
                            pn3 = '+'
                            # print('yes')
                        if pn33 == '+':
                            pn3 = '-'
                        if pn33 == '/':
                            pn3 = '*'
                        if pn33 == '*':
                            pn3 = '/'
                        else: pass
                        # print(pn3)

                    except:
                        pass
                    try:
                        pn4 = res2[i + 1]

                    except:
                        pass
                    calc.append(pn3 + data)
            if fx == 2:
                if 'x' in data or '-' in data or '+' in data or '*' in data or '/' in data:
                    pass
                else:
                    pn3 = ''
                    pn4 = ''
                    try:
                        pn3 = res2[i - 1]
                        if pn3 == '=': pn3 = ''
                        # print(pn3)
                        # else:
                            # pass
                        # print(pn3)

                    except:
                        pass
                    try:
                        pn4 = res2[i + 1]

                    except:
                        pass
                    calc2.append(pn3 + data)
    fffs = ''
    for ci in calc2:
        fffs += ci
    for ci in calc:
        fffs += ci
    
    rtx = []
    exec('''
rtx.append(''' + fffs + ''')
         ''')
    
   
    res567 = rtx[0]
    
    if fx2 == 0:
        fx2 = 1
    return res567 / fx2

def solve(eq):
    res = eq
    x = 0
    xs = RemoveNumFromX(eq.replace(' ', '').replace(
        '-', ' - ').replace('+', ' + ').replace('/', ' / ').replace('*', ' * ').replace('=', ' = '))
    
    return xs


#   Linear equations in one variables String pass to a function
print(solve('5x - 3 = 7 - 5x'))

