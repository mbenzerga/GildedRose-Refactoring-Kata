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


@pytest.mark.parametrize(
    "name", ["foo", "Aged Brie", "Backstage passes to a TAFKAL80ETC concert", "Sulfuras, Hand of Ragnaros"]
)
def test_error_if_quality_is_negative(name):
    items = [Item(name=name, sell_in=0, quality=-1)]
    with pytest.raises(ValueError):
        GildedRose(items)


@pytest.mark.parametrize(
    "name", ["foo", "Aged Brie", "Backstage passes to a TAFKAL80ETC concert", "Sulfuras, Hand of Ragnaros"]
)
def test_item_quality_does_not_exceed_50(name):
    items = [Item(name=name, sell_in=0, quality=51)]
    with pytest.raises(ValueError):
        GildedRose(items)


@pytest.mark.parametrize("sell_in, quality", [(1, 1), (3, 5), (8, 12)])
def test_Aged_Brie_quality_increases_if_quality_is_less_than_50(sell_in, quality):
    items = [Item(name="Aged Brie", sell_in=sell_in, quality=quality)]
    gilded_rose = GildedRose(items)
    gilded_rose.update_quality()
    assert items[0].name == "Aged Brie"
    assert items[0].sell_in == sell_in - 1
    assert items[0].quality == quality + 1


@pytest.mark.parametrize("sell_in", [-1, 0, 1, 5])
def test_Aged_Brie_quality_does_not_exceed_50(sell_in):
    items = [Item(name="Aged Brie", sell_in=sell_in, quality=50)]
    gilded_rose = GildedRose(items)
    gilded_rose.update_quality()
    assert items[0].name == "Aged Brie"
    assert items[0].sell_in == sell_in - 1
    assert items[0].quality == 50


def test_Aged_Brie_quality_increases_twice_as_fast_if_sell_in_is_negative():
    items = [Item(name="Aged Brie", sell_in=0, quality=10)]
    gilded_rose = GildedRose(items)
    gilded_rose.update_quality()
    assert items[0].name == "Aged Brie"
    assert items[0].sell_in == -1
    assert items[0].quality == 12
    gilded_rose.update_quality()
    assert items[0].name == "Aged Brie"
    assert items[0].sell_in == -2
    assert items[0].quality == 14


@pytest.mark.parametrize("sell_in, quality", [(1, 1), (3, 5), (8, 12), (17, 50)])
def test_Sulfuras_quality_and_sell_in_remain_constant(sell_in, quality):
    items = [Item(name="Sulfuras, Hand of Ragnaros", sell_in=sell_in, quality=quality)]
    gilded_rose = GildedRose(items)
    gilded_rose.update_quality()
    assert items[0].name == "Sulfuras, Hand of Ragnaros"
    assert items[0].sell_in == sell_in
    assert items[0].quality == quality
    gilded_rose.update_quality()
    assert items[0].name == "Sulfuras, Hand of Ragnaros"
    assert items[0].sell_in == sell_in
    assert items[0].quality == quality
