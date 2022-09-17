def type_service(word, types='str'):
    if type(word).__name__ == types:
        return 'true'
    else:
        try:
            if types == "int" and int(word):
                return 'true'
        except ValueError:
            return 'false'
            
  '''
  Description:
  Argument: word = str, types = class type(str)
  설명: 입력 받은 단어가 원하는 타입(문자열, 정수 등)이라면 'true'를 반환, 아니면 'false'를 반환 한다.
  인자: word=문자열, types=클래스 타입(문자열),
  '''
