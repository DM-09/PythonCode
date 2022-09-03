def input_service(sentence, types='str', error_msg='error'):
    while True:
        i = input(sentence)

        if type(i).__name__ == types:
            return  i
    
        print(error_msg)
      
  
  # input_service 설명: 입력받은 문자가 원하는 타입(문자열, 정수 등)이 아니라면 메시지를 출력하고 워하는 타입이 나올 때까지 묻는 함수
