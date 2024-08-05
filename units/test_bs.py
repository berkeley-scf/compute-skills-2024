import pytest
import binary_search as bs

def test_search_found():
    assert bs.search([3,7,9,13,17,203,205],3) == 0
    assert bs.search([3,7,9,13,17,203,205],13) == 3
    assert bs.search([3,7,9,13,17,203,205],17) == 4
    assert bs.search([3,7,9,13,17,203,205],205) == 6
    assert bs.search(['a','b','d','z'],'z') == 3


def test_search_notfound():
    assert bs.search([3,7,9,13,17,203,205],-7) == -1
    assert bs.search([3,7,9,13,17,203,205],5) == -1
    assert bs.search([3,7,9,13,17,203,205],25) == -1


def test_bad_input():
    with pytest.raises(TypeError):
        bs.search([3,7,9,13,17,203,205], "hi")
    with pytest.raises(TypeError):
        bs.search_fix(['a','c','d'], 300)
    
