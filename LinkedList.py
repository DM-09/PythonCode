class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        head = Node('head')

        self.head = head
        self.tail = head
        self.len = 0

    def go(self, ind):
        cur = self.head.next
        for i in range(ind):
            cur = cur.next

        return cur

    def toList(self):
        l, cur = [], self.head.next
        for i in range(self.len):
            l.append(cur.data)
            cur = cur.next

        return l

    def __str__(self):
        return str(self.toList())

    def get(self, ind):
        return self.go(ind).data

    def append(self, data):
        new = Node(data)
        self.tail.next = new
        self.tail = new
        self.len += 1

    def pop(self):
        tail = self.go(self.len - 2)
        cur = self.tail.data

        tail.next = None
        self.tail = tail
        self.len -= 1
        return cur

    def insert(self, ind, data):
        new = Node(data)

        if ind == 0:
            hnext = self.head.next
            self.head.next = new
            new.next = hnext
        else:
            go = self.go(ind - 1)
            next = self.go(ind)

            go.next = new
            new.next = next

        self.len += 1

    def remove(self, ind):
        go = self.go(ind - 1)
        next = self.go(ind + 1)
        go.next = next

        self.len -= 1

'''
[시용 방법]
# *모든 명령어에는 head가 포함되지 않음

l = LinkedList() # 정의

l.append('값') # 맨 뒤에 값을 추가함
l.insert(인덱스, '값') # 특정 인덱스에 값을 추가함 | 인덱스 : int
l.get(인덱스) # 특정 인덱스의 값을 가져옴 | 인덱스 : int
l.pop() # 맨 뒤에 값을 삭제하고 반환함
l.remove(인덱스) # 특정 인덱스의 값을 삭제함 | 인덱스 : int
l.toList() # list 자료형으로 변환함

l.len # 길이(값이 몇 개 있나) *head는 포함되지 않음
print(l) # list 형식으로 출력함
'''
