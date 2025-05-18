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


def test_item_quality_decreases_twice_as_fast_if_sell_in_is_negative():
    items = [Item(name="foo", sell_in=0, quality=10)]
    gilded_rose = GildedRose(items)
    gilded_rose.update_quality()
    assert items[0].name == "foo"
    assert items[0].sell_in == -1
    assert items[0].quality == 8
    gilded_rose.update_quality()
    assert items[0].name == "foo"
    assert items[0].sell_in == -2
    assert items[0].quality == 6


@pytest.mark.parametrize("sell_in", list(range(-2, 3)))
def test_item_quality_remains_0_if_quality_is_0(sell_in):
    items = [Item(name="foo", sell_in=sell_in, quality=0)]
    gilded_rose = GildedRose(items)
    gilded_rose.update_quality()
    assert items[0].name == "foo"
    assert items[0].sell_in == sell_in - 1
    assert items[0].quality == 0


def test_error_if_quality_is_negative():
    items = [Item(name="foo", sell_in=0, quality=-1)]
    with pytest.raises(ValueError):
        GildedRose(items)


def test_item_quality_does_not_exceed_50():
    items = [Item(name="foo", sell_in=0, quality=51)]
    with pytest.raises(ValueError):
        GildedRose(items)


def test_Aged_Brie_quality_increases_if_quality_is_less_than_50():
    items = [Item(name="Aged Brie", sell_in=10, quality=20)]
    gilded_rose = GildedRose(items)
    gilded_rose.update_quality()
    assert items[0].name == "Aged Brie"
    assert items[0].sell_in == 9
    assert items[0].quality == 21
