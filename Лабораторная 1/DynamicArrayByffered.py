from ctypes import py_object as po


class DynamicArray:
    def __init__(self, initial_buffer: int = 10):
        if not isinstance(initial_buffer, int):
            raise TypeError("Изначальный буфер должен быть типа int")
        self.self_size = 0  # current number of user's elements
        self.size = initial_buffer  # default number of elements of buffer
        self.buf = (self.size * po)()  # create a buffer

    def __setitem__(self, i, value):
        if not isinstance(i, int):
            raise TypeError("Индекс должен быть типа int")
        if i > self.self_size - 1 or abs(i) > self.self_size:
            raise ValueError("Введен несуществующий индекс")
        if i < 0:
            i = self.self_size - i
        self.buf[i] = value
        return value  # Скажите, пожалуйста, зачем возвращать что-либо этим методом? Мы ведь просто меняем ей атрибут.

    def __getitem__(self, i):
        if not isinstance(i, int):
            raise TypeError("Индекс должен быть типа int")
        if i > self.self_size - 1 or abs(i) > self.self_size:
            raise ValueError("Введен несуществующий индекс")
        if i < 0:
            i = self.self_size - i
        return self.buf[i]

    def append(self, value):
        self.self_size += 1
        if self.self_size > self.size:
            self.size += 10
            dest = (self.size * po)()
            for i in range(self.self_size-1):
                dest[i] = self.buf[i]
            self.buf = dest
        self.buf[self.self_size-1] = value

    def pop(self, index):
        if not isinstance(index, int):
            raise TypeError("Индекс должен быть типа int")
        if index > self.self_size - 1 or abs(index) > self.self_size:
            raise ValueError("Введен несуществующий индекс")
        if index == -1 or index == self.self_size-1:
            self.buf[self.self_size-1] = po
        else:
            for i in range(index, self.self_size-1):
                self.buf[i] = self.buf[i+1]
        self.buf[self.self_size - 1] = po
        self.self_size -= 1

    def inser(self, index, value):
        if not isinstance(index, int):
            raise TypeError("Индекс должен быть типа int")
        if index > self.self_size - 1 or abs(index) > self.self_size:
            raise ValueError("Введен несуществующий индекс")
        self.self_size += 1
        if self.self_size > self.size:
            self.size += 10
            dest = (self.size * po)()
            for i in range(self.self_size - 1):
                dest[i] = self.buf[i]
            self.buf = dest
        if index == -1 or index == self.self_size-2:
            self.buf[self.self_size-1] = self.buf[self.self_size-2]
            self.buf[self.self_size-2] = value
        else:
            if index < 0:  # Немного смутила логика вставки по отрицательному индексу, потому что если мы вставляем по
                # положительному, то обратиться к нему можем по тому же самому индексу, а вот с отрицательными значени-
                # ями так не работает. Нормально ли это?
                index = self.self_size + index - 1
            for i in range(self.self_size-1, index, -1):
                self.buf[i] = self.buf[i-1]
            self.buf[index] = value


if __name__ == '__main__':
    # create plain array in python:
    # size = 10
    # data = (size * po)()  # array of objects with fixed size
    # # print(data) # <__main__.py_object_Array_10 object at 0x000001F60DF50740>
    # for i in range(size):
    #     data[i] = i*2
    # for i in range(size):
    #     print(data[i])

    # create dynamic array that handles varying size
    array = DynamicArray()
    array.append(123)
    array.append(4)
    array.append("p")
    array.append("p")
    array.pop(0)
    # print("array:", array[0], array[1], array[2])
    array.inser(2, 321)
    array.pop(-1)
    array.append(13)

    print("array:", array[0], array[1], array[2], array[3])
    # p1 = array.__getitem__(1)
    # array.__setitem__(0, 5)
    # p = array[10]
    # p = array[-1]
    # array[20] = 6
    # p = array[1]
    # array[0] = 6
    # array[10] = 6
    # p = array[10]
    # array[11] = 6

