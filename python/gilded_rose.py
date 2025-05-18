# -*- coding: utf-8 -*-


class GildedRose(object):

    def __init__(self, items):
        self.items = items

        for item in self.items:
            self.validate_item(item)

    def validate_item(self, item):
        if item.quality < 0:
            raise ValueError("Quality cannot be negative")
        if item.name == "Sulfuras, Hand of Ragnaros" and item.quality != 80:
            raise ValueError("Sulfuras quality must be 80")
        if item.quality > 50 and item.name != "Sulfuras, Hand of Ragnaros":
            raise ValueError("Quality cannot exceed 50")

    def update_quality(self):
        for item in self.items:
            # decrease quality for normal items
            self.decrease_quality_of_normal_item(item)

            # increase quality for Aged Brie or Backstage passes
            self.increase_quality_of_Aged_Brie(item)
            self.increase_quality_of_Backstage_passes(item)

            # double decrease quality for Conjured items
            self.decrease_quality_of_Conjured(item)

            # decrease sell_in
            self.decrease_sell_in(item)

    def decrease_quality_of_normal_item(self, item):
        if self.is_normal(item) and item.quality > 0:
            item.quality = item.quality - 1 - int(item.sell_in <= 0)

    def increase_quality_of_Aged_Brie(self, item):
        if item.name == "Aged Brie" and item.quality < 50:
            item.quality = item.quality + 1 + int(item.sell_in <= 0)

    def increase_quality_of_Backstage_passes(self, item):
        if item.name == "Backstage passes to a TAFKAL80ETC concert" and item.quality < 50:
            if item.sell_in > 10:
                item.quality = item.quality + 1
            elif item.sell_in in range(6, 11):
                item.quality = item.quality + 2
            elif item.sell_in in range(1, 6):
                item.quality = item.quality + 3
            else:
                item.quality = 0

    def decrease_quality_of_Conjured(self, item):
        if item.name.startswith("Conjured") and item.quality > 0:
            item.quality = item.quality - 2 - 2 * int(item.sell_in <= 0)

    @staticmethod
    def decrease_sell_in(item):
        # decrease sell_in
        if item.name != "Sulfuras, Hand of Ragnaros":
            item.sell_in = item.sell_in - 1

    def is_normal(self, item):
        # check if item is normal
        return (
            item.name not in ["Aged Brie", "Backstage passes to a TAFKAL80ETC concert", "Sulfuras, Hand of Ragnaros"]
            and item.name.startswith("Conjured") is False
        )


class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)
