# created by: Dennis Kwong
# cost: 2.00 cat food

import re


class Cat:
    def __init__(self, cat):
        self.cat = cat
        self.ability = cat["ability"]
        self.alias = cat["alias"]
        self.cost = cat["cost"]
        self.description = cat["description"]
        self.effect = cat["effect"]
        self.form = cat["form"]
        self.name = cat["name"]
        self.rarity_index = cat["rarity_index"]
        self.rarity_pct = cat["rarity_pct"]
        self.rarity_total = cat["rarity_total"]
        self.rarity = cat["rarity"]
        self.target = cat["target"]

    def get_ability(self, search=None):
        """
        return list of abilities or abilities that match search regex
        :param str search: optional regex search string
        :return: list of abilities
        :rtype: list
        """
        if search:
            result = list()
            for ability in self.ability:
                matches = re.search(search, ability, re.IGNORECASE)
                if matches:
                    result.append(ability)
        else:
            result = self.ability
        return result

    def get_ability_effect(self, search=None):
        """
        return list of abilities|effects or abilities|effects that match search regex
        :param str search: optional regex search string
        :return: list of abilities or effects
        :rtype: list
        """
        if search:
            result = self.get_ability(search) + self.get_effect(search)
        else:
            result = self.ability + self.effect
        return result

    def get_alias(self):
        return self.alias

    def get_cost(self):
        return self.cost

    def get_description(self):
        return self.description

    def get_effect(self, search=None):
        """
        return list of effects or effects that match search regex
        :param str search: optional regex search string
        :return: list of effects
        :rtype: list
        """
        if search:
            result = list()
            for effect in self.effect:
                matches = re.search(search, effect, re.IGNORECASE)
                if matches:
                    result.append(effect)
        else:
            result = self.effect
        return result

    def get_form(self):
        return self.form

    def get_name(self):
        return self.name

    def get_rarity(self):
        return self.rarity

    def get_rarity_index(self):
        return self.rarity_index

    def get_rarity_pct(self):
        return self.rarity_pct

    def get_rarity_total(self):
        return self.rarity_total

    def get_target(self, search=None):
        """
        return list of targets or targets that match search regex
        :param str search: optional regex search string
        :return: list of targets
        :rtype: list
        """
        if search:
            result = list()
            for target in self.target:
                matches = re.search(search, target, re.IGNORECASE)
                if matches:
                    result.append(target)
        else:
            result = self.target
        return result
