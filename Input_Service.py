def input_service(sentence, types='str', error_msg='error'):
    while True:
        i = input(sentence)

        if type(i).__name__ == types:
            return i
        else:
            try:
                if types == "int" and int(i):
                    return int(i)
            except ValueError:
                print(error_msg)
      
  
  '''
  Description: A function that outputs a message and prompts you until the type 
  you want is not the type you want (string, integer, etc.)

  Argument: sentence = str, types = class type, error_msg = str

  설명: 입력받은 문자가 원하는 타입(문자열, 정수 등)이 아니라면 메시지를 출력하고 
  원하는 타입이 나올 때까지 묻는 함수

  인자: sentence는 문자열, types=클래스 타입, error_msg = 문자열
  '''


