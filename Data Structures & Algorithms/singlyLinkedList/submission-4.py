class LinkedList:

    class __Node:
        def __init__(self, item, next=None):
            self.item = item
            self.next = next

    
    def __init__(self):
        self.size = 0
        self.first = self.__Node(None, None)
        self.last = self.first
    
    def get(self, index: int) -> int:
        if self.size < index+1:
            return -1
        else:
            cursor = self.first.next
            for i in range(index):
                cursor = cursor.next
            print(cursor.item)
            return cursor.item

    def insertHead(self, val: int) -> None:
        node = self.__Node(val, None)
        node.next = self.first.next
        self.first.next = node
        self.size += 1
        if self.size == 1:
            self.last = self.first.next
        print(self.getValues())

    def insertTail(self, val: int) -> None:
        node = self.__Node(val, None)
        self.last.next = node
        self.last = node
        self.size += 1
        print(self.getValues())

    def remove(self, index: int) -> bool:
        if self.size < index+1:
            return False
        cursor = self.first
        for i in range(index):
            cursor = cursor.next
        
        cursor.next = cursor.next.next
        if cursor.next is None:
            self.last = cursor
        self.size -= 1
        return True

    def getValues(self) -> List[int]:
        o_list = []
        cursor = self.first
        while cursor.next is not None:
            cursor = cursor.next
            o_list.append(cursor.item)

        return o_list
        
