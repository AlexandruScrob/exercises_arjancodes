from typing import Iterable, Protocol
from item import Item


def decrease_item_quality(item: Item, amount: int = 1) -> None:
    item.quality = max(0, item.quality - amount)


def increase_item_quality(item: Item, amount: int = 1, max_quality: int = 50) -> None:
    item.quality = min(max_quality, item.quality + amount)


# Item types
AGED_BRIE = "Aged Brie"
BACKSTAGE_PASSES = "Backstage passes to a TAFKAL80ETC concert"
SULFURAS = "Sulfuras, Hand of Ragnaros"
CONJURED = "Conjured Mana Cake"


class ItemUpdater(Protocol):
    def update_quality(self, item: Item):
        ...

    def update_sell_in(self, item: Item):
        ...


class DefaultItemUpdater:
    def update_quality(self, item: Item) -> None:
        decrease_item_quality(item)
        if item.sell_in < 0:
            decrease_item_quality(item)

    def update_sell_in(self, item: Item) -> None:
        item.sell_in = item.sell_in - 1


class AgedBriedUpdater(DefaultItemUpdater):
    def update_quality(self, item: Item) -> None:
        increase_item_quality(item)
        if item.sell_in < 0:
            increase_item_quality(item)


class BackstagePassesUpdater(DefaultItemUpdater):
    def update_quality(self, item: Item) -> None:
        increase_item_quality(item)
        if item.sell_in < 10:
            increase_item_quality(item)
        if item.sell_in < 5:
            increase_item_quality(item)
        if item.sell_in < 0:
            item.quality = 0


class SulfurasUpdater(DefaultItemUpdater):
    def update_quality(self, item: Item):
        pass

    def update_sell_in(self, item: Item):
        pass


class ConjuredUpdater(DefaultItemUpdater):
    def update_quality(self, item: Item) -> None:
        decrease_item_quality(item, 2)
        if item.sell_in < 0:
            decrease_item_quality(item, 2)


ITEM_UPDATERS: dict[str, ItemUpdater] = {
    AGED_BRIE: AgedBriedUpdater(),
    BACKSTAGE_PASSES: BackstagePassesUpdater(),
    SULFURAS: SulfurasUpdater(),
    CONJURED: ConjuredUpdater(),
}


def update_quality(items: Iterable[Item]):
    for item in items:
        update_quality_single(item)


def update_quality_single(item: Item):
    item_updater = ITEM_UPDATERS.get(item.name, DefaultItemUpdater())
    item_updater.update_sell_in(item)
    item_updater.update_quality(item)
