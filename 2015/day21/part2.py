import itertools
import math
import re
from collections import namedtuple
from typing import Dict, List

Item = namedtuple('Item', ['cost', 'damage', 'armor'])
Character = namedtuple('Character', ['hitpoints', 'damage', 'armor'])

item_shop: Dict[str, List[Item]] = {
	category.split(':')[0]: [Item(*map(int, re.findall(r'\s(\d+)', line))) for line in category.split('\n')[1:]]
	for category in open('item_shop.txt').read().split('\n\n')
}
player_hitpoints = 100
boss = Character(*map(int, re.findall(r'(\d+)', open('input.txt').read())))
loss_costs = []


def can_win_with_stats(damage: int, armor: int) -> bool:
	damage_to_boss = max(1, damage - boss.armor)
	damage_to_player = max(1, boss.damage - armor)
	boss_rounds = math.ceil(boss.hitpoints / damage_to_boss)
	player_rounds = math.ceil(player_hitpoints / damage_to_player)
	return boss_rounds <= player_rounds


def fight_with_items(items: List[Item]) -> None:
	cost, damage, armor = map(sum, zip(*items))
	if not can_win_with_stats(damage, armor):
		loss_costs.append(cost)


def find_most_expensive_loss() -> int:
	for weapon in item_shop['Weapons']:
		for armor in item_shop['Armor'] + [Item(0, 0, 0)]:
			for ring1, ring2 in itertools.combinations(item_shop['Rings'] + [Item(0, 0, 0)] * 2, 2):
				fight_with_items([weapon, armor, ring1, ring2])

	return max(loss_costs)


print(find_most_expensive_loss())
