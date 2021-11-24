from read_file import read_from_file


def test_read_from_file():
    test_data = ['one\n', 'two\n', 'three']
    assert test_data == read_from_file('data.txt')


def test_read_from_file2():
    test_data = ['one\n', 'two\n', 'three']
    assert test_data == read_from_file('data.txt')