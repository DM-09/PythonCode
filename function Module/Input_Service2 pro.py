def type_service2(word, types='int'):
    if types == 'str':
        str(word)
    else:
        try:
            if types == 'int' and int(word):
                return int(word)
        except ValueError:
            return str(word)


def input_service2(sentence, error_msg='error', types='int'):
    while True:
        i = input(str(sentence))

        if i == '1':
            return type_service2(i, types)
        elif i == '2':
            return type_service2(i, types)
        else:
            print(error_msg)
