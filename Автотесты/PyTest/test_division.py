from division import division
import pytest

rtg = [(10, 5, 2),
       (20, 2, 10),
       (10, 2, 5),
       (30, -3, -10),
       (5, 2, 2.5),
       ]


@pytest.mark.parametrize('a, b, result', rtg)
def test_div_good(a, b, result):
    assert division(a, b) == result


@pytest.mark.parametrize('a, b, error', [
    (10, 0, ZeroDivisionError),
    (10, '2', TypeError)
])
def test_div_zero(a, b, error):
    with pytest.raises(error):
        division(a, b)
