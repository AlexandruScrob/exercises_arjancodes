from pay.order import LineItem


def test_line_item_default() -> None:
    line_item = LineItem("test", 100)
    assert line_item.total == 100


def test_line_item() -> None:
    line_item = LineItem("Test", 200, 5)
    assert line_item.total == 1000
