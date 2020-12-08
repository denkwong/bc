from os import path
import sys
import unittest
sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))
from bc import Bc


class TestBC(unittest.TestCase):
    test_file = "bc.json"
    bc = Bc(test_file)

    def test_ability(self):
        cat = None
        cats = self.bc.find_ability("Strengthen")
        cats = self.bc.find_ability("Single Attack", cats)
        for cat in cats:
            if cat.name == "Sayaka Cat":
                break
        self.assertEqual("Sayaka Cat", cat.name)
        self.assertIn("Strengthen", cat.ability)
        self.assertIn("Single Attack", cat.ability)

    def test_ability_effect(self):
        # search for ability and effect
        cat = None
        cats = self.bc.find_ability_effect("Area Attack")
        cats = self.bc.find_ability_effect("Knockback", cats)
        for cat in cats:
            if cat.name == "Mizli":
                break
        self.assertEqual("Mizli", cat.name)
        self.assertIn("Area Attack", cat.ability)
        self.assertIn("Knockback", cat.effect)

    def test_cost_down(self):
        # test cat with multiple costs
        cat = None
        cats = self.bc.find_cost("1050")
        cats = self.bc.find_cost("1020", cats)
        for cat in cats:
            if cat.name == "Chill Cat":
                break
        self.assertEqual("Chill Cat", cat.name)
        self.assertIn("Area Attack", cat.ability)
        self.assertListEqual(["Wheel Cat", "Solar Cat"], cat.alias)
        self.assertListEqual([1050, 1020], cat.cost)
        self.assertEqual("An evolved Cat who is always calm and collected at the office. "
                         "Massive area damage to Aliens.", cat.description)
        self.assertIn("Massive Damage", cat.effect)
        self.assertEqual("True", cat.form)
        self.assertEqual("Rare", cat.rarity)
        self.assertIn("Alien", cat.target)

    def test_cost_equal(self):
        cat = None
        cats = self.bc.find_cost("=150")
        for cat in cats:
            if cat.name == "Eraser Cat":
                break
        self.assertEqual("Eraser Cat", cat.name)
        self.assertEqual(150, cat.cost)

        cats = self.bc.find_cost("==150", cats)
        for cat in cats:
            if cat.name == "Eraser Cat":
                break
        self.assertEqual("Eraser Cat", cat.name)
        self.assertEqual(150, cat.cost)

    def test_cost_greater_than(self):
        cats = self.bc.find_cost(">7500")
        self.assertListEqual([], cats)

        cat = None
        cats = self.bc.find_cost(">7499")
        for cat in cats:
            if cat.name == "Killer Cat":
                break
        self.assertEqual("Killer Cat", cat.name)
        self.assertEqual(7500, cat.cost)

    def test_cost_greater_than_or_equals(self):
        cat = None
        cats = self.bc.find_cost(">=7500")
        for cat in cats:
            if cat.name == "Killer Cat":
                break
        self.assertEqual("Killer Cat", cat.name)
        self.assertEqual(7500, cat.cost)

        cats = self.bc.find_cost(">=7499", cats)
        for cat in cats:
            if cat.name == "Killer Cat":
                break
        self.assertEqual("Killer Cat", cat.name)
        self.assertEqual(7500, cat.cost)

    def test_cost_less_than(self):
        cats = self.bc.find_cost("<45")
        self.assertListEqual([], cats)

        cat = None
        cats = self.bc.find_cost("<46")
        for cat in cats:
            if cat.name == "Li'l Mohawk Cat":
                break
        self.assertEqual("Li'l Mohawk Cat", cat.name)
        self.assertEqual(45, cat.cost)

    def test_cost_less_than_or_equals(self):
        cat = None
        cats = self.bc.find_cost("<=45")
        for cat in cats:
            if cat.name == "Li'l Mohawk Cat":
                break
        self.assertEqual("Li'l Mohawk Cat", cat.name)
        self.assertEqual(45, cat.cost)

        cats = self.bc.find_cost("<=46")
        for cat in cats:
            if cat.name == "Li'l Mohawk Cat":
                break
        self.assertEqual("Li'l Mohawk Cat", cat.name)
        self.assertEqual(45, cat.cost)

    def test_description(self):
        cat = None
        cats = self.bc.find_description("Brilliant Bow can grant")
        cats = self.bc.find_description("watch your mouth", cats)
        for cat in cats:
            if cat.name == "Megaphrodite":
                break
        self.assertEqual("Megaphrodite", cat.name)

    def test_effect(self):
        cat = None
        cats = self.bc.find_effect("Freeze")
        cats = self.bc.find_effect("Resistant", cats)
        for cat in cats:
            if cat.name == "Tourist Cat":
                break
        self.assertEqual("Tourist Cat", cat.name)
        self.assertIn("Freeze", cat.effect)
        self.assertIn("Resistant", cat.effect)

    def test_form(self):
        # test normal cat where index, rarity_pct, and rarity_total is unlikely to change.
        cat = None
        cats = self.bc.find_form("Normal")
        cats = self.bc.find_form("Normal", cats)
        for cat in cats:
            if cat.name == "Cat":
                break
        self.assertEqual("Cat", cat.name)
        self.assertEqual("Normal", cat.rarity)
        self.assertEqual(1, cat.rarity_index)
        self.assertEqual(0.1111111111111111, cat.rarity_pct)
        self.assertEqual(9, cat.rarity_total)

    def test_name(self):
        cat = None
        cats = self.bc.find_name("thief cat")
        cats = self.bc.find_name("phantom", cats)
        for cat in cats:
            if cat.name == "Phantom Thief Cat":
                break
        self.assertEqual("Phantom Thief Cat", cat.name)
        self.assertListEqual(["Extra Money", "Single Attack"], cat.ability)
        self.assertListEqual(["Thief Cat", "Goemon Cat"], cat.alias)
        self.assertEqual(495, cat.cost)
        self.assertEqual("Moves too fast. Still steals the same. Has a large treasure collection now. "
                         "More money earned when defeating an enemy.", cat.description)
        self.assertIn("", cat.effect)
        self.assertEqual("Evolved", cat.form)
        self.assertEqual("Rare", cat.rarity)
        self.assertIsInstance(cat.rarity_index, int)
        self.assertIsInstance(cat.rarity_pct, float)
        self.assertIsInstance(cat.rarity_total, int)
        self.assertIn("", cat.target)

    def test_rarity(self):
        # test legend cat
        cat = None
        cats = self.bc.find_rarity("Legend")
        cats = self.bc.find_rarity("Legend", cats)
        for cat in cats:
            if cat.name == "True Kyosaka Nanaho":
                break
        self.assertEqual("True Kyosaka Nanaho", cat.name)
        self.assertEqual("Legend", cat.rarity)
        self.assertEqual("Evolved", cat.form)
        self.assertEqual(4050, cat.cost)
        self.assertListEqual(["Metal"], cat.target)

    def test_talent_ability(self):
        cat = None
        cats = self.bc.find_ability("Resist Wave")
        cats = self.bc.find_ability("Single Attack", cats)
        for cat in cats:
            if cat.name == "Balrog Cat":
                break
        self.assertEqual("Balrog Cat", cat.name)
        self.assertIn("Resist Wave", cat.ability)
        self.assertIn("Single Attack", cat.ability)
        self.assertGreater(cat.talents["Resist Wave"], 0)

    def test_talent_attack_up(self):
        # Attack Up talent becomes Strengthen ability
        cat = None
        cats = self.bc.find_name("Goemon Cat")
        for cat in cats:
            if cat.name == "Goemon Cat":
                break
        self.assertEqual("Goemon Cat", cat.name)
        self.assertIn("Strengthen", cat.ability)
        self.assertGreater(cat.talents["Attack Up"], 0)

    def test_talent_curse_immunity(self):
        # Curse Immunity talent becomes Immune to Curse ability
        cat = None
        cats = self.bc.find_ability("Immune to Curse")
        for cat in cats:
            if cat.name == "Octopus Cat":
                break
        self.assertEqual("Octopus Cat", cat.name)
        self.assertIn("Immune to Curse", cat.ability)
        self.assertGreater(cat.talents["Curse Immunity"], 0)

    def test_talent_effect(self):
        cat = None
        cats = self.bc.find_name("Almighty Aphrodite")
        for cat in cats:
            if cat.name == "Almighty Aphrodite":
                break
        self.assertEqual("Almighty Aphrodite", cat.name)
        self.assertIn("Slow", cat.effect)
        self.assertGreater(cat.talents["Slow"], 0)

    def test_talent_money_up(self):
        # Money Up talent becomes Extra Money ability
        cat = None
        cats = self.bc.find_ability("Extra Money")
        for cat in cats:
            if cat.name == "Can Can Cat":
                break
        self.assertEqual("Can Can Cat", cat.name)
        self.assertIn("Extra Money", cat.ability)
        self.assertGreater(cat.talents["Money Up"], 0)

    def test_talent_resist(self):
        cat = None
        cats = self.bc.find_ability("Resist Wave")
        for cat in cats:
            if cat.name == "Balrog Cat":
                break
        self.assertEqual("Balrog Cat", cat.name)
        self.assertIn("Resist Wave", cat.ability)
        self.assertGreater(cat.talents["Resist Wave"], 0)

    def test_talent_survives(self):
        # Survives talent becomes Survive ability
        cat = None
        cats = self.bc.find_ability("Survive")
        for cat in cats:
            if cat.name == "Sanzo Cat":
                break
        self.assertEqual("Sanzo Cat", cat.name)
        self.assertIn("Survive", cat.ability)
        self.assertGreater(cat.talents["Survives"], 0)

    def test_talent_target(self):
        # Target Angel talent adds Angel to target list
        cat = None
        cats = self.bc.find_target("Angel")
        for cat in cats:
            if cat.name == "Sanzo Cat":
                break
        self.assertEqual("Sanzo Cat", cat.name)
        self.assertIn("Angel", cat.target)
        self.assertGreater(cat.talents["Target Angel"], 0)

    def test_target(self):
        cat = None
        cats = self.bc.find_target("Relic")
        cats = self.bc.find_target("Zombie", cats)
        cats = self.bc.find_target("Alien", cats)
        for cat in cats:
            if cat.name == "Cyberpunk Cat":
                break
        self.assertEqual("Cyberpunk Cat", cat.name)
        self.assertEqual("Super", cat.rarity)
        self.assertIn("Relic", cat.target)
        self.assertIn("Zombie", cat.target)
        self.assertIn("Alien", cat.target)

    def test_target_traitless(self):
        cat = None
        cats = self.bc.find_target("traitless")
        for cat in cats:
            if cat.name == "Shadow Gao":
                break
        self.assertEqual("Shadow Gao", cat.name)

    def test_target_rarity_ability(self):
        cats = self.bc.find_target("Red")
        cats = self.bc.find_rarity("Uber", cats)
        cats = self.bc.find_ability("Immune to Weaken", cats)
        for cat in cats:
            self.assertIn("Red", cat.target)
            self.assertEqual("Uber", cat.rarity)
            self.assertIn("Immune to Weaken", cat.ability)

    def test_wildcard(self):
        cat = None
        cats = self.bc.find_description("honor")
        cats = self.bc.find_description("executioner.*treacherous", cats)
        for cat in cats:
            if cat.name == "Hell Sentinel Emma":
                break
        self.assertEqual("Hell Sentinel Emma", cat.name)


if __name__ == "__main__":
    unittest.main()
