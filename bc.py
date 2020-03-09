# created by: Dennis Kwong
# cost: 2.00 cat food

import json
import logging
import re
from cat import Cat


class InputError(Exception):
    def __init__(self, message):
        self.logger = logging.getLogger("bc")
        self.logger.error(message)
        print(message)


class Bc:
    def __init__(self, input_file):
        """
        open input_file and load into self.cats.
        :param str input_file: input file to process
        """
        self.logger = logging.getLogger("bc")
        with open(input_file, "r") as fh:
            self.json_cats = json.load(fh)
            self.cats = list()
            self.load_cats()

    def find_ability(self, ability, cats=None):
        """
        find cat with ability
        :param str ability: name of ability, can be regex
        :param list cats: optional list of Cats to search
        :return: list of Cats
        :rtype: list
        """
        result = list()
        if cats is None:
            cats = self.cats
        for cat in cats:
            matches = cat.get_ability(ability)
            if matches:
                result.append(cat)
        return result

    def find_ability_effect(self, ability_effect, cats=None):
        """
        find cat with ability or effect
        :param str ability_effect: name of ability or effect, can be regex
        :param list cats: optional list of Cats to search
        :return: list of Cats
        :rtype: list
        """
        result = set()
        for cat in self.find_ability(ability_effect, cats):
            result.add(cat)
        for cat in self.find_effect(ability_effect, cats):
            result.add(cat)
        return list(result)

    def find_cat(self, name, cats=None):
        """
        find cat with name
        :param str name: name of cat, can be regex
        :param list cats: optional list of Cats to search
        :return: list of Cats
        :rtype: list
        """
        result = list()
        if cats is None:
            cats = self.cats
        for cat in cats:
            cat_name = cat.get_name()
            matches = re.search(name, cat_name, re.IGNORECASE)
            if matches:
                result.append(cat)
        return result

    def find_cost(self, cost, cats=None):
        """
        find cost of cat, also supports operators <, <=, >=, >
        :param int or str cost: examples supported: 75, ">= 75", "< 1000"
        :param list cats: optional list of Cats to search
        :return: list of Cats
        :rtype: list
        """
        operator = "=="
        cost = cost.strip()
        if cats is None:
            cats = self.cats

        matches = re.match("(=|==|<|<=|>=|>) *(\d+)$", cost)
        if matches:
            operator = matches.group(1)
            cost = matches.group(2)

            if operator == "=":
                operator = "=="
        else:
            matches = re.match("^\d+$", cost)
            if matches:
                cost = matches.group(0)
            else:
                raise InputError("Invalid cost: {0}".format(cost))

        result = self._find_cost(int(cost), operator, cats)
        return result

    def _find_cost(self, cost, operator, cats):
        """
        helper method that handles cost search with supported operators
        :param int cost: cost of Cat
        :param str operator: integer equality / inequality operators
        :param list cats: list of Cats to search
        :return: list of Cats matching the search criteria
        :rtype: list
        """
        if operator in ("<", "<=", "==", ">=", ">"):
            result = list()
            for cat in cats:
                cat_costs = cat.get_cost()
                if isinstance(cat_costs, int):
                    cat_costs = [cat_costs]
                for cat_cost in cat_costs:
                    if eval("{0} {1} {2}".format(cat_cost, operator, cost)):
                        result.append(cat)
            return result
        else:
            print("Operator {0} is not supported.".format(operator))

    def find_description(self, description, cats=None):
        """
        find cat with description
        :param str description: description to search for, can be regex
        :param list cats: optional list of Cats to search
        :return: list of Cats
        :rtype: list
        """
        result = list()
        if cats is None:
            cats = self.cats
        for cat in cats:
            matches = cat.get_description(description)
            if matches:
                result.append(cat)
        return result

    def find_effect(self, effect, cats=None):
        """
        find cat with effect
        :param str effect: name of effect, can be regex
        :param list cats: optional list of Cats to search
        :return: list of Cats
        :rtype: list
        """
        result = list()
        if cats is None:
            cats = self.cats
        for cat in cats:
            matches = cat.get_effect(effect)
            if matches:
                result.append(cat)
        return result

    def find_form(self, form, cats=None):
        """
        find cat with form
        :param str form: name of form, can be regex
        :param list cats: optional list of Cats to search
        :return: list of Cats
        :rtype: list
        """
        result = list()
        if cats is None:
            cats = self.cats
        for cat in cats:
            matches = cat.get_form(form)
            if matches:
                result.append(cat)
        return result

    def find_rarity(self, rarity, cats=None):
        """
        return a list of cats that match specified rarity
        :param str rarity: normal, special, rare, super, uber
        :param list cats: optional list of Cats to search
        :return: list of Cats that match rarity
        :rtype: list
        """
        result = list()
        if cats is None:
            cats = self.cats
        for cat in cats:
            matches = re.search(rarity, cat.get_rarity(), re.IGNORECASE)
            if matches:
                result.append(cat)
        return result

    def find_target(self, target, cats=None):
        """
        return a list of cats with the specified target
        :param str target: case-insensitive Black, Floating, etc.
        :param list cats: optional list of Cats to search
        :return: list of Cats that match target
        :rtype: list
        """
        result = list()
        if cats is None:
            cats = self.cats
        for cat in cats:
            matches = cat.get_target(target)
            if matches:
                result.append(cat)
        return result

    def list_cats(self):
        """
        Print list of cat names with rarity (n), (sp), (r), (sr), (u)
        :return: None
        """
        rarity_map = {
            "Normal": "n",
            "Special": "sp",
            "Rare": "r",
            "Super": "sr",
            "Uber": "u"
         }
        for cat in self.cats:
            rarity = cat.get_rarity()
            name = cat.get_name()
            rarity_pct = cat.get_rarity_pct()
            print("{0} ({1}) {2}%".format(name, rarity_map[rarity], int(rarity_pct * 100)))

    def load_cats(self):
        """
        read cats from bc.json, create Cat objects and load them into self.cats.
        :return: None
        """
        for cat in self.json_cats["cats"]:
            self.cats.append(Cat(cat))
