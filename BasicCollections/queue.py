class Queue(object):

    def __init__(self, input_list=None):
        self.queue = []
        self._size = 0
        if input_list and type(input_list) == list:
            self.queue.extend(input_list)
            self._size += len(input_list)
        if input_list and type(input_list) != list:
            raise TypeError("input_list is not of type list")

    
    def enqueue(self, element: object) -> bool:
        try:
            self.queue.append(element)
            self._size += 1
            return True
        except Exception as e:
            return False

    def dequeue(self) -> object:
        toReturn = self.queue.pop(0)
        self._size -= 1
        return toReturn

    def size(self):
        return self._size

    def peek_start(self) -> object:
        if self.size() > 0:
            return self.queue[0]
        else:
            raise IndexError
    
    def peek_end(self) -> object:
        if self.size() > 0:
            return self.queue[self.size() - 1]
        else:
            raise IndexError

    def __str__(self) -> str:
        return f"{self.queue}"


    def __repr__(self) -> str:
        return f"<BasicCollections.queue.Queue object {self.queue}>"

