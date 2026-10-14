# Варіант 9: loyalty_points
# Виконав: Поворознюк Даніїл

def loyalty_points(amount: float | int, is_member: bool = False) -> int:
    """
    Обчислює кількість балів лояльності.
    За кожні повні 20 грн нараховується 1 бал.
    Якщо is_member=True, кількість балів подвоюється.
    При amount < 0 виникає помилка ValueError.
    """
    if amount < 0:
        raise ValueError("Сума покупки не може бути від'ємною")

    base_points = int(amount // 20)

    if is_member:
        return base_points * 2

    return base_points
