import numpy as np
import pandas as pd


def string_helloworld():
	return "Hello World!"


def string_myname(name):
	return f"My name is {name}."


def print_all_strings(name_list):
	print(string_helloworld())

	for name_i in name_list:
		print(string_myname(name_i))


if _name_ == "_main_":

	print_all_strings(name_list=["Biff", "Chip", "Kipper"])