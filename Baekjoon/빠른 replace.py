def frep(s : str, f : str, rep : str = ''):
    st, f, lf = [], list(f), len(f)
    for i in s:
        st.append(i)
        if st[-lf:] == f:
            for _ in range(lf): st.pop()
            st.append(rep)
    return ''.join(st)

'''
스택 사용해서 만든 빠른 replace 함수

s(문자열) 문자열
f(문자열) 패턴
rep(문자열) 바꿀 문자열 (기본 = "")


rep 쓸 필요 없으면 (rep == "") 매개변수 rep지우고 8번줄(st.append) 부분도 삭제
(그러면 백준 9935번 38860 KB, 272 ms 로 통과 가능)
'''

# 예제
print(frep('q222222', '2')) # q
