# -*- coding: utf-8 -*-


class GildedRose(object):

    def __init__(self, items):
        self.items = items

        for item in self.items:
            if item.quality < 0:
                raise ValueError("Quality cannot be negative")
            if item.quality > 50:
                raise ValueError("Quality cannot exceed 50")

    @staticmethod
    def decrease_sell_in(item):
        # decrease sell_in
        if item.name != "Sulfuras, Hand of Ragnaros":
            item.sell_in = item.sell_in - 1

    def is_normal(self, item):
        # check if item is normal
        return item.name not in ["Aged Brie", "Backstage passes to a TAFKAL80ETC concert", "Sulfuras, Hand of Ragnaros"]

    def decrease_quality_of_normal_item(self, item):
        if item.quality > 0:
            item.quality = item.quality - 1

    def update_quality(self):
        for item in self.items:
            # decrease quality for normal items
            if self.is_normal(item):
                self.decrease_quality_of_normal_item(item)
            # increase quality for Aged Brie or Backstage passes
            else:
                if item.quality < 50:
                    item.quality = item.quality + 1
                    if item.name == "Backstage passes to a TAFKAL80ETC concert":
                        if item.sell_in < 11:
                            if item.quality < 50:
                                item.quality = item.quality + 1
                        if item.sell_in < 6:
                            if item.quality < 50:
                                item.quality = item.quality + 1

            self.decrease_sell_in(item)

            # decrease quality when sell_in is negative
            if item.sell_in < 0:
                if item.name != "Aged Brie":
                    if item.name != "Backstage passes to a TAFKAL80ETC concert":
                        if item.quality > 0:
                            if item.name != "Sulfuras, Hand of Ragnaros":
                                item.quality = item.quality - 1
                    else:
                        item.quality = item.quality - item.quality
                else:
                    if item.quality < 50:
                        item.quality = item.quality + 1


class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)
