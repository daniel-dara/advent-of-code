import re
from collections import namedtuple

player_hp = 50
player_mp = 500
player_spells = ('missile', 53), ('drain', 73), ('shield', 113), ('poison', 173), ('recharge', 229)
boss_hp, boss_damage = map(int, re.findall(r'\d+', open('input.txt').read()))
boss_spells = (('boss', 0),)
is_player_turn = True
mp_spent = 0
Effects = namedtuple('Effects', ('shield', 'poison', 'recharge'))
effects = Effects(0, 0, 0)

queue = [(is_player_turn, mp_spent, player_hp, player_mp, boss_hp, effects)]
lowest_mp_win = None

states = set()

while queue:
	state = queue.pop(0)

	if state in states:
		continue

	states.add(state)
	is_player_turn, mp_spent, player_hp, player_mp, boss_hp, effects = state

	if player_hp <= 0 or player_mp <= 0 or (lowest_mp_win is not None and mp_spent > lowest_mp_win):
		continue

	if boss_hp <= 0:
		lowest_mp_win = mp_spent
		continue

	for spell, mp_cost in (player_spells if is_player_turn else boss_spells):
		if not hasattr(effects, spell) or getattr(effects, spell) <= 1:
			queue.append((
				not is_player_turn,
				mp_spent + mp_cost,
				player_hp + (
					2 * (spell == 'drain') - 1 if is_player_turn else -max(1, boss_damage - 7 * (effects.shield > 0))
				),
				player_mp - mp_cost + 101 * (effects.recharge > 0),
				boss_hp - 4 * (spell == 'missile') - 2 * (spell == 'drain') - 3 * (effects.poison > 0),
				Effects(
					6 if spell == 'shield' else effects.shield - 1,
					6 if spell == 'poison' else effects.poison - 1,
					5 if spell == 'recharge' else effects.recharge - 1
				)
			))

print(lowest_mp_win)
