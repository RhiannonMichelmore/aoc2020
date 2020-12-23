import sys

class Node:
    def __init__(self,p=None,n=None,data=None,lt=None):
        self.prev = p
        self.next = n
        self.data = data
        self.less_than = lt
    def __repr__(self):
        return 'Node'
    def __str__(self):
        s = 'Data: ' + str(self.data) + ' LT: '
        if self.less_than == None:
            s += 'None'
        else:
            s += str(self.less_than.data)
        return s

def print_list(head):
    print(head)
    head_data = head.data
    current = head
    while not current.next.data == head_data:
        current = current.next
        print(current)

def print_string_answer(head):
    current = head
    started = False
    s = ''
    while True:
        if started == True and current.data == 0:
            break
        elif started == False and current.data == 0:
            started = True
        elif started == True:
            s += str(current.data+1)
        current = current.next
    print(s)

def print_after(head):
    current = head
    while True:
        if current.data == 0:
            break
        current = current.next
    cup1 = current.next.data + 1
    cup2 = current.next.next.data + 1
    print(cup1*cup2)

def main(in_string):
    ring = list(map(int,list(in_string)))
    ring = [r-1 for r in ring]

    small_head = Node(None,None,ring[0])
    current = small_head
    for i in range(1,len(ring)):
        current.next = Node(current,None,ring[i])
        current = current.next

    small_tail = current

    list_len = 1_000_000

    for i in range(9,list_len):
        current.next = Node(current,None,i)
        current = current.next

    big_head = small_tail.next

    # last one is tail
    big_tail = current

    # link small back in loop
    small_head.prev = small_tail
    small_tail.next = small_head

    head_outer = small_head
    for i in range(len(ring)):
        head_inner = head_outer.next
        for j in range(len(ring)-1):
            if head_inner.data == head_outer.data-1:
                head_outer.less_than = head_inner
                break
            head_inner = head_inner.next
        head_outer = head_outer.next

    #get node 0 and node 8
    tmp = small_head
    node0 = None
    node8 = None
    while node0 == None or node8 == None:
        if tmp.data == 0:
            node0 = tmp
        elif tmp.data == 8:
            node8 = tmp
        tmp = tmp.next

    big_head.less_than = node8
    tmp = big_head.next
    while True:
        if not tmp.data == list_len-1:
            tmp.less_than = tmp.prev
            tmp = tmp.next
        else:
            tmp.less_than = tmp.prev
            node0.less_than = tmp
            tmp.next = small_head
            small_head.prev = tmp
            break

    # relink small_tail to big_head
    # relink big_tail to small_head
    small_tail.next = big_head
    big_head.prev = small_tail

    print('list constructed')
    head = small_head

    for i in range(10_000_000):
        # get the head of the 3 values up next
        three_head = head.next
        # get the place we should relink
        three_tail = three_head.next.next
        # relink the head to skip the next 3
        head.next = three_tail.next

        vals = [three_head.data,three_head.next.data,three_head.next.next.data]

        dest = head.less_than
        while dest.data in vals:
            dest = dest.less_than

        after = dest.next
        dest.next = three_head
        three_tail.next = after
        head = head.next

    print_after(head)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print('No input found.')
    else:
        with open(sys.argv[1],'r') as f:
            in_string = f.read().strip()
            main(in_string)
