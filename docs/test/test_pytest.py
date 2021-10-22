import pytest

# Single test case
def test_sorted():
    assert sorted([4, 2, 1, 3]) == [1, 2, 3, 4]

# Test fixture
@pytest.fixture
def dict_list():
    return [
        dict(a='a', b=3),
        dict(a='c', b=1),
        dict(a='b', b=2),
    ]

def test_sorted__key_example_1(dict_list):
    assert sorted(dict_list, key=lambda dicts: dicts['a']) == [
        dict(a='a', b=3),
        dict(a='b', b=2),
        dict(a='c', b=1),
    ]

def test_sorted__key_example_2(dict_list):
    assert sorted(dict_list, key=lambda dicts: dicts['b']) == [
        dict(a='c', b=1),
        dict(a='b', b=2),
        dict(a='a', b=3),
    ]
    
# Test parameterisation
@pytest.mark.parametrize('input,expected', [
    ([2, 1], [1, 2]),
    ('zasdqw', list('adqswz')),
])
def test_examples(input, expected):
    actual = sorted(input)
    assert actual == expected
