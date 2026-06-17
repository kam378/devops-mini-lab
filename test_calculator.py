from calculator import calculate_area, subtract

def test_area():
    assert calculate_area(5, 4) == 20
def test_subtract():
    assert subtract(10, 4) == 6 