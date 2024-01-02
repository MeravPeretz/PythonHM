import pytest
from lesson2 import main


@pytest.mark.parametrize('num , result',[(12,[2,3,5,7,11]),('a',[1,2]),(-9,[0])])
def test_prime(num,result):
    assert main.find_prims(num) == result

@pytest.mark.parametrize('l , result',[([2,3,5,7,11],[2,3,5,7,11]),('a',[1,2]),([-9,8,3,4],[-9,3,4,8])])
def test_sort(l,result):
    assert main.sort_list(l) == result

@pytest.mark.parametrize('s , result',[("1+2", 3), ('a', 3), ("2*(9+5)", 28)])
def test_exp(s, result):
    assert main.calculate_expretion(s) == result