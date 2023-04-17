from project import reading_all_stats, sum_of_stats, cost_efficiency


def test_reading_all_stats():
    assert reading_all_stats("Alistar") == "ALISTAR: Hp: 800, Mana: 175, Armor: 50, Mr: 50, Dps: 28, Atk spd: 0.55, Damage: 50, Range: 1, Cost: 3"

    assert reading_all_stats("all") == ['ALISTAR: Hp: 800, Mana: 175, Armor: 50, Mr: 50, Dps: 28, Atk spd: 0.55, Damage: 50, Range: 1, Cost: 3', 'ANNIE: Hp: 750, Mana: 90, Armor: 40, Mr: 40, Dps: 24, Atk spd: 0.6, Damage: 40, Range: 2, Cost: 2', 'APHELIOS: Hp: 800, Mana: 140, Armor: 30, Mr: 30, Dps: 72, Atk spd: 0.9, Damage: 80, Range: 4, Cost: 5', 'ASHE: Hp: 500, Mana: 50, Armor: 15, Mr: 15, Dps: 42, Atk spd: 0.7, Damage: 60, Range: 4, Cost: 1', 'AURELION SOL: Hp: 850, Mana: 90, Armor: 30, Mr: 30, Dps: 28, Atk spd: 0.7, Damage: 40, Range: 4, Cost: 4']

    assert reading_all_stats("wrongname") == "Wrong name"


def test_sum_of_stats():
    assert sum_of_stats("Alistar") == "ALISTAR = 776.55 on 3 cost"

    assert sum_of_stats("All") == ['ALISTAR = 776.55 on 3 cost', 'ANNIE = 782.6 on 2 cost', 'APHELIOS = 804.9 on 5 cost', 'ASHE = 544.7 on 1 cost', 'AURELION SOL = 864.7 on 4 cost']

    assert sum_of_stats("wrongname") == "Wrong name"


def test_cost_efficiency():
    assert cost_efficiency("Alistar") == "ALISTAR: 258.84999999999997"

    assert cost_efficiency("all") == ['ALISTAR: 258.84999999999997', 'ANNIE: 391.3', 'APHELIOS: 160.98', 'ASHE: 544.7', 'AURELION SOL: 216.175']

    assert cost_efficiency("wrongname") == "Wrong name"