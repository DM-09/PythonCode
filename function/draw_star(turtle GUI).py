import turtle as t # import turtle Gui

t.shape("turtle")


def draw_star(length, num=3, num2=2, color='black'): # function code
    if num > 2 and num2 > 1 and num & num2 != 0 and num != num2:
        t.pencolor(color)
        t.circle(length, 360 * num2, num)
    else:
        boolean = True
        while boolean:
            num2 += 1
            if num % num2 != 0:
                boolean = False
                print(num2)
        draw_star(length, num, num2, color)


draw_star(100, 5, 2, 'skyblue') # use function(example)

t.done() # keep screen

'''
설명: 정n각별을 그려주는 함수(turtle Gui와 호환)
인자: length = 길이(정수), num = 각의 개수(정수), num2 = 소수(정수), color = 색상(문자열)

# 아직 미완성
# It's not finished yet
'''
