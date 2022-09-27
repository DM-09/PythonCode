def input_service2(sentence, error_msg='error'):
    while True:
        i = input(str(sentence))

        if i == "1":
            return i
        elif i == '2':
            return i
        else:
            print(error_msg)


'''
설명: 특정 값만 반환(기본값: 1,2)
인자: sentence = 문자열(물어볼 말), error_msg = 문자열(에러 메시지)
'''
