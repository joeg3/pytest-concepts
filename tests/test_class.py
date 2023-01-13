from src.rectangle import Rectangle

def test_calc_area():
    r = Rectangle(3,4)
    assert 12 == r.calculate_area()