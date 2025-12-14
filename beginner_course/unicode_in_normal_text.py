s = input()
s1 = ''
code = ''
flag = False

if '[' not in s:
    print(s)
else:
    for i in range(len(s)):
        if s[i] in '0123456789':
            flag = True
        if flag:
            if len(code)<4:
                    code += s[i]
            else:
                    code = int(code)
                    s1 += chr(code)
                    code = ''
        if s[i] ==']':
            flag = False
        if s[i]!='[' and  s[i]!=']' and s[i]!='-' and s[i]!='u' and s[i].isdigit()!=True:
            s1 += s[i]
        elif s[i]=='[' or s[i]==']' or s[i]=='-' or s[i]=='u':
            if (i>0 and (s[i-1]==']' and s[i]=='-')) or (i < len(s) - 1 and (s[i+1]=='[' and s[i]=='-')):
                s1 += s[i]
            if s[i]=='u' and s[i-1].isalpha()==True:
                s1 += s[i]
            else:
                continue         
    print(s1)