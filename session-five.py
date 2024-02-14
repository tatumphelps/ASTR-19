
def table(start, end, num_enteries):
	step = (end - start) / (num_entries - 1)
	x_values = [start + i * step for i in range(num_entries)]
	sin_values = [math.sin(x) for x in x_values]


def print_table(x_values, sin_values):
	print("x\t\t sini(x)")
	print("--------------------------")
	for x, sini_x in zip(x_vaues, sin_values):
		print(f"{x:.6f}\t {sin_x:.6f}")


def main():
	start = 0
	end = 2 
	num_entriies = 1000

	x_values, sin_values = generate_table(start, end, num_enteries)
	print_table(x_values, sin_values)


	if __name__ == "__main__":
		main()