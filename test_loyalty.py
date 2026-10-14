import pytest
from loyalty import loyalty_points


def test_loyalty_points_happy_path_guest():
    # AAA: Arrange, Act, Assert
    amount = 20
    is_member = False

    result = loyalty_points(amount, is_member)

    assert result == 1


def test_loyalty_points_happy_path_member():
    amount = 40
    is_member = True

    result = loyalty_points(amount, is_member)

    assert result == 4


def test_loyalty_points_negative_amount_raises_error():
    with pytest.raises(ValueError, match="Сума покупки не може бути від'ємною"):
        loyalty_points(-10, False)


def test_loyalty_points_boundary_below_twenty():
    # Межа: 19 грн дає 0 балів
    assert loyalty_points(19, False) == 0


def test_loyalty_points_zero_amount():
    # Додатковий випадок: 0 грн
    assert loyalty_points(0, True) == 0
