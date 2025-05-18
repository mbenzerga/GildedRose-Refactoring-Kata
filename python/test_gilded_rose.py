import pytest

from gilded_rose import Item, GildedRose


def test_item_sell_in_decreases_but_not_quality_if_sell_in_is_0():
    items = [Item(name="foo", sell_in=0, quality=0)]
    gilded_rose = GildedRose(items)
    gilded_rose.update_quality()
    assert items[0].name == "foo"
    assert items[0].sell_in == -1
    assert items[0].quality == 0


@pytest.mark.parametrize("sell_in, quality", [(1, 1), (3, 5), (8, 12)])
def test_item_sell_in_and_quality_decrease_if_sell_in_is_positive(sell_in, quality):
    items = [Item(name="foo", sell_in=sell_in, quality=quality)]
    gilded_rose = GildedRose(items)
    gilded_rose.update_quality()
    assert items[0].name == "foo"
    assert items[0].sell_in == sell_in - 1
    assert items[0].quality == quality - 1
