import csv
import sys


def main():
	print("1 = all stats of chousen chempion ")
	print("2 = sum of stats of chousen chempion ")
	print("3 = cost eficency of chousen chempion ")

	choice = input("number betwen 1 - 3:  ").strip()

	if choice == "1":
		name = input("name or all: ").strip()
		print(reading_all_stats(name))

	elif choice == "2":
		name = input("name or all: ").strip()
		print(sum_of_stats(name))

	elif choice == "3":
		name = input("name or all: ").strip()
		print(cost_efficiency(name))

	else:
		print("wrong input")
		sys.exit()


def reading_all_stats(a):

	with open("TFT.csv","r") as csv_tft:
		tft = csv.DictReader(csv_tft)

		b = str(a).upper()

		values = []

		for row in tft:
			if b == row["NAME"]:
				return(f"{row['NAME']}: Hp: {row['HEALTH']}, Mana: {row['MANA']}, Armor: {row['ARMOR']}, Mr: {row['MR']}, Dps: {row['DPS']}, Atk spd: {row['ATK_SPD']}, Damage: {row['DAMAGE']}, Range: {row['RANGE']}, Cost: {row['COST']}")


			elif b == "ALL":
					g = (f"{row['NAME']}: Hp: {row['HEALTH']}, Mana: {row['MANA']}, Armor: {row['ARMOR']}, Mr: {row['MR']}, Dps: {row['DPS']}, Atk spd: {row['ATK_SPD']}, Damage: {row['DAMAGE']}, Range: {row['RANGE']}, Cost: {row['COST']}")
					values.append(g)

			else:
				return("Wrong name")

		return values

def sum_of_stats(a):
	with open("TFT.csv","r") as csv_tft:
		tft = csv.DictReader(csv_tft)

		b = str(a).upper()

		value2 = []

		for row in tft:
			if b == row["NAME"]:
				sum_of_stats = int(row["HEALTH"]) - int(row["MANA"]) + int(row["ARMOR"]) + int(row["MR"]) + float(row["ATK_SPD"]) + int(row["DAMAGE"]) + int(row["RANGE"])
				return(f'{row["NAME"]} = {sum_of_stats} on {row["COST"]} cost')


			if b == "ALL":
				sum_of_stats = int(row["HEALTH"]) - int(row["MANA"]) + int(row["ARMOR"]) + int(row["MR"]) + float(row["ATK_SPD"]) + int(row["DAMAGE"]) + int(row["RANGE"])
				g = (f'{row["NAME"]} = {sum_of_stats} on {row["COST"]} cost')
				value2.append(g)

			else:
				return("Wrong name")

		return(value2)

def cost_efficiency(a):
	with open("TFT.csv","r") as csv_tft:
		tft = csv.DictReader(csv_tft)

		b = str(a).upper()

		value3 = []

		for row in tft:
			if b == row["NAME"]:
				sum_of_stats = int(row["HEALTH"]) - int(row["MANA"]) + int(row["ARMOR"]) + int(row["MR"]) + float(row["ATK_SPD"]) + int(row["DAMAGE"]) + int(row["RANGE"])
				e = sum_of_stats/int(row["COST"])
				return(f"{row['NAME']}: {e}")


			if b == "ALL":
				sum_of_stats = int(row["HEALTH"]) - int(row["MANA"]) + int(row["ARMOR"]) + int(row["MR"]) + float(row["ATK_SPD"]) + int(row["DAMAGE"]) + int(row["RANGE"])
				e = sum_of_stats/int(row["COST"])
				g = (f"{row['NAME']}: {e}")
				value3.append(g)


			else:
				return("Wrong name")

		return(value3)


if __name__ == "__main__":
	main()