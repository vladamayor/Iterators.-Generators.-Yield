import copy
import types

class FlatIterator:

    def __init__(self, list_of_list):
        self.list_of_list = copy.deepcopy(list_of_list)

    def __iter__(self):
        self.count_el = 0
        self.amount_el = len(self.list_of_list)
        return self

    def __next__(self):

        if len(self.list_of_list[self.count_el]) == 0:
            self.count_el += 1
            if self.count_el == self.amount_el:
                raise StopIteration
            
        return self.list_of_list[self.count_el].pop(0)



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


def flat_generator(list_of_lists):

    count_el = 0
    while count_el < len(list_of_lists):
        for el in list_of_lists[count_el]:
            yield el
        count_el += 1


def test_2():

    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    for flat_iterator_item, check_item in zip(
            flat_generator(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):

        assert flat_iterator_item == check_item

    assert list(flat_generator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]

    assert isinstance(flat_generator(list_of_lists_1), types.GeneratorType)


if __name__ == '__main__':
    test_2()
    