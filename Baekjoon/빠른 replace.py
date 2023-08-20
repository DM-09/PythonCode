def frep(s : str, f : str, rep : str = '', c : int = 0):
    co, st, f = 0, [], list(f)
    for i in s:
        st.append(i)
        if st[-len(f):] == f:
            exec("st.pop();"*len(f))
            st.append(rep)
            co += 1
            if co == c: rep = ''.join(f)
    return ''.join(st)

'''
s(문자열) 문자열
f(문자열) 패턴
rep(문자열) 바꿀 문자열 (기본 = '')
c(정수) 바꿀 횟수 (기본 = 전부)
'''

# 예제
print(frep('q22323', '2', '!', 2))
# q!!323
