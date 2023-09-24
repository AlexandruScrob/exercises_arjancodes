from gilded_rose import (
    Item,
    update_quality,
)

SULFURAS = "Sulfuras, Hand of Ragnaros"


def test_item_sulfuras_sell_in_doesnt_decrease():
    item = Item(SULFURAS, 0, 0)
    update_quality([item])
    assert 0 == item.sell_in


def test_item_sulfuras_quality_doesnt_decrease():
    item = Item(SULFURAS, 0, 0)
    update_quality([item])
    assert 0 == item.quality
