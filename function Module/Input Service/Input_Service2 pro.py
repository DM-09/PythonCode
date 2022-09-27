def type_service2(word, types='int'):
    if types == 'str':
        str(word)
    else:
        try:
            if types == 'int' and int(word):
                return int(word)
        except ValueError:
            return str(word)


def input_service2(sentence, error_msg='error', max_num='2', types='int'):
    while True:
        i = input(str(sentence))

        if i <= max_num:
            return type_service2(i, types)
        else:
            print(error_msg)


'''
설명: 최댓값보다 같거나 작으면 설정한 타입으로 바꿔줌
'''
