class Stack(object):

    def __init__(self, input_list=None):
        self._stack = []
        self._size = 0
        if input_list and type(input_list) == list:
            self._stack.extend(input_list)
            self._size += len(input_list)
        if input_list and type(input_list) != list:
            raise TypeError("input_list is not of type list")
            

    def push(self, element):
        try:
            self._stack.append(element)
            self._size += 1
            return True
        except IndexError as e:
            raise IndexError


    def pop(self):
        to_return = self._stack.pop()
        self._size -= 1
        return to_return


    def peek(self):
        return self._stack[self._size - 1]


    def __len__(self):
        return self.size()

    def size(self):
        return self._size


    def __str__(self) -> str:
        return f"{self._stack}"


    def __repr__(self) -> str:
        return f"<BasicCollections.stack.Stack object {self._stack}>"

