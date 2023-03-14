class Heap(object):

    def __init__(self, input_list=None):
        self._heap = [None]
        self._size = 0
        if input_list and type(input_list) == list:
            self._heap.extend(input_list)
            self._size += len(input_list)
        if input_list and type(input_list) != list:
            raise TypeError("input_list is not of type list")
        self._heapify()


    def _heapify(self) -> list:
        start_ind = self._size // 2
        while start_ind != 0:
            self._subheap(start_ind)
            start_ind -= 1

    def size(self):
        return self._size

    def add(self, element):
        self._heap.append(element)
        self._size += 1
        ind = self.size() // 2
        while ind != 0:
            self._subheap(ind)
            ind //= 2

    def peek(self):
        if self.size() > 1:
            return self._heap[1]
        else:
            raise IndexError

    def pop(self):
        if self.size() == 0:
            raise IndexError
        to_return = self._heap[1]
        reassign = self._heap.pop()
        self._size -= 1
        if self._size > 0:
            self._heap[1] = reassign
            self._subheap(1)
        return to_return

    def _subheap(self, ind) -> bool:
        # print("==============================")
        # print(ind)
        # print(self._heap)
        left_ind = ind * 2
        right_ind = (ind * 2) + 1
        if left_ind > self.size():
            return True
        if right_ind > self.size() and self._heap[ind] >= self._heap[left_ind]:
            return True
        elif right_ind > self.size() and self._heap[ind] < self._heap[left_ind]:
            right_ind = left_ind
        if self._heap[ind] >= max(self._heap[left_ind], self._heap[right_ind]):
            return True
        else:
            max_index = left_ind if self._heap[left_ind] >= self._heap[right_ind] else right_ind
            temp = self._heap[ind]
            self._heap[ind] = self._heap[max_index]
            self._heap[max_index] = temp
            # print(f"swapper {max_index} and {ind}")
            # print(self._heap)
            # print("==============================")
            return self._subheap(max_index)

        