#!/usr/bin/env python

# created by: Dennis Kwong
# cost: 1.12 cat food

import json
import re


class BattleCats:
    def __init__(self):
        with open ("battle_cats.json", "r") as fh:
            self.all_cats = json.load(fh)

    def find_cat(self, cat_name):
        """
        print the cat class, relative position and all forms of the cat
        :param str cat_name: name of cat to search for
        :return: None
        """
        r = re.compile(cat_name, re.IGNORECASE)
        for cat_class, cats in self.all_cats.items():
            i = 0
            for cat in cats:
                matches = filter(r.search, cat[1:])
                if matches:
                    print("{0} - {1}".format(cat_name, self._format_cat_info(cat_class, i)))
                i += 1

    def find_cat_cost(self, cost):
        """
        print the cats that match the specified cost
        :param str cost: exact cost to search for
        :return: None
        """
        for cat_class, cats in self.all_cats.items():
            i = 0
            for cat in cats:
                if cost in cat[0]:
                    print("{0} - {1}".format(cost, self._format_cat_info(cat_class, i)))
                i += 1

    def _format_cat_info(self, cat_class, index):
        """
        return a displayable string of class, relative position and cat names
        :param cat_class: name of cat class
        :param index: array position of the cat in the class
        :return: string formatted for display with appropriate padding
        """
        cat_count = len(self.all_cats[cat_class])
        _class = "{0},".format(cat_class)
        position = "({0}/{1})".format(index + 1, cat_count)
        percentage = "{0}%".format((index + 1) * 100 / cat_count)
        cats = "({0})".format(", ".join(self.all_cats[cat_class][index][1:]))
        # return "{0} {1} {2} {3}".format(_class.ljust(16), position.rjust(5), percentage.rjust(7), cats)
        return "{0}, {1} {2} {3}".format(cats, _class, percentage, position)

    def cat_count(self):
        """
        show counts for each cat class
        :return: None
        """
        for cat_class, cats in self.all_cats.items():
            print("{0}: {1}".format(cat_class, len(cats)))


if __name__ == "__main__":
    bc = BattleCats()

    bc.find_cat("mighty")
    print("")
    bc.find_cat("brave")
    print("")
    bc.find_cat("titan cat")
    print("")
    bc.find_cat("Masked Yulala")
    print("")
    bc.find_cat("mas")
    print("")
    bc.find_cat("Karin Nekozuka")
    print("")
    bc.find_cat("gao")
    print("")
    bc.find_cat_cost("75")
    print("")
    bc.find_cat_cost("750")
    print("")
    bc.cat_count()

"""
'wargod'
- rare cat
  - 3/45, (x wargod | immortal x)
  - 4/45, (y wargod | immortal y)
- super rare cat
  - 15/20, (wargodcat)

./find_cat.py "mas"
'mas' - Special Cat, 9/45, (Kung Fu Cat | Drunken Master Cat | Dancer Cat)
'mas' - Special Cat, 44/45, (Hermit Cat | Grandmaster Cat)
'mas' - Special Cat, 45/45, (Masked Yulala | Mystic Yulala)
'mas' - Rare Cat, 1/64, (Pogo cat | Masai cat | Jiangshi cat)
'mas' - Rare Cat, 13/64, (Swordsman Cat | Sword Master Cat | Elemental Duelist Cat)
'mas' - Rare Cat, 26/64, (Reindeer Fish Cat | Sashimi Cat | Xmas Pudding Cat)
'mas' - Rare Cat, 35/64, (Kung Fu Cat X | Drunken Master Cat X | Iron Claw X)
'mas' - Rare Cat, 47/64, (Clockwork Cat | Puppetmaster Cat)
'mas' - Uber Rare Cat, 8/45, (Date Masamune | Wargod Masamune | Immortal Masamune)


./find_cat.py "mas"
'mas'
- Special Cat
  - 9/45, (Kung Fu Cat | Drunken Master Cat | Dancer Cat)
  - 44/45, (Hermit Cat | Grandmaster Cat)
  - 45/45, (Masked Yulala | Mystic Yulala)
- Rare Cat
  - 1/64, (Pogo cat | Masai cat | Jiangshi cat)
  - 13/64, (Swordsman Cat | Sword Master Cat | Elemental Duelist Cat)
  - 26/64, (Reindeer Fish Cat | Sashimi Cat | Xmas Pudding Cat)
  - 35/64, (Kung Fu Cat X | Drunken Master Cat X | Iron Claw X)
  - 47/64, (Clockwork Cat | Puppetmaster Cat)
- Uber Rare Cat
  - 8/45, (Date Masamune | Wargod Masamune | Immortal Masamune)

todo: return a structure of matches.  determine padding based on results.
"""
