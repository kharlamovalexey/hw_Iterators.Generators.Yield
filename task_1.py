class FlatIterator:

    def __init__(self, list_of_list):
        self.list_ = list_of_list
        self.i = 0
        self.j = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.j < len(self.list_[self.i]):
            item = self.list_[self.i][self.j]
            self.j += 1
        else:
            self.i += 1
            self.j = 0
            if self.i == len(self.list_):
                raise StopIteration
            item = self.list_[self.i][self.j]
            self.j += 1
        return item
            


def test_1():

    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    for flat_iterator_item, check_item in zip(
            FlatIterator(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):

        assert flat_iterator_item == check_item

    assert list(FlatIterator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]


if __name__ == '__main__':
    test_1()
