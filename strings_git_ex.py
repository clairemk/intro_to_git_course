def string_helloworld():
	return "Hello World!"


def string_myname(name):
	return f"My name is {name}."


def print_all_strings(name_list):
	print(string_helloworld())

	for name_i in name_list:
		print(string_myname(name_i))


if __name__ == "__main__":

	print_all_strings(name_list=["Biff", "Chip", "Kipper", "Cla"])