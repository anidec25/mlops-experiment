from apple import calculate_total_apples

def test_calculate_total_apples():
    assert calculate_total_apples(5, 10) == 50


def test_empty_basket():
    assert calculate_total_apples(0, 10) == 0


def test_single_basket():
    assert calculate_total_apples(1, 10) == 10