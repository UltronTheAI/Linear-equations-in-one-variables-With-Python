def Get_X(eq):
    res = eq.replace('1', '').replace(
        '2', '').replace('3', '').replace('4', '').replace('5', '').replace('6', '').replace('7', '').replace('8', '').replace('9', '').replace('0', '').replace('+', '').replace('-', '').replace('*', '').replace('/', '').replace('=', '')
    res = len(res)
    return res

def solve(eq):
    res = eq.replace(' ', '') #.split('=')
    x = 1
    
    x = Get_X(res)
    res = res.split('=')
    
    one = res[0]
    two = res[1]
    
    o1 = list(one)
    
    v = ''
    ns = ''
    gx = 0
    gpass = 0 
    for i in o1:
        if gpass == 0:
            if i == 'x':
                gx = 1
            if gx == 1:
                if i == 'x':
                    pass
                if i == '+':
                    v = '+'
                    ns += '-'
                    gpass = 0
                if i == '-':
                    v = '-'
                    ns += '+'
                if i == '*':
                    v = '*'
                    ns += '/'
                if i == '/':
                    v = '/'
                    ns += '*'
                else: ns += i.replace('x', '')
        # gpass = 0
        else: pass
        if gpass > 0:
            gpass -= 1
        # print(ns)
    ls = []
    exec('''
ls.append(''' + res[1] + ns + ''')  
         ''')            
    return ls[0] / x

#   Linear equations in one variables String pass to a function
print(solve('x + 2 = 7'))
