from simple import add, isleap, mypro
def test_add_one():
    assert 30 == add(10,20)
    assert 120 == add(50,70)

def test_add_two():
    assert 110 == add(90,20)
    assert 110 == add(50,60)

def test_leap_one():
    assert False == isleap(2006)

def test_leap_two():
    assert False == isleap(2015)

def test_pro_one():
    assert 200 == mypro(10,20)
    assert 350 == mypro(50,70)

def test_pro_two():
    assert 700 == mypro(10,70)
    assert 800 == mypro(40,20)