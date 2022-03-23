from prettytable import PrettyTable
from print import *

print("String Indexer", SM,GREEN)
print("\n")
print(" ( Shows positive and negative index values of the string ) ")
print("\n")

user_input = input(" Enter the string to be indexed: ")




def display_table():
	list_var = []

	positive_index = []

	neg_index = []

	new_neg_index = []


	for i,j in enumerate(user_input):
		positive_index.append(i)
		neg_index.append(i)
		list_var.append(j)


	for i,n in enumerate(neg_index,start=1):
		new_neg_index.append(-abs(i))


	new_neg_index.reverse()




	myTable = PrettyTable(header=False)

	myTable.add_row(positive_index)
	myTable.add_row(list_var)
	myTable.add_row(new_neg_index)


	print(myTable)

def html_table():
	list_var = []

	positive_index = []

	neg_index = []

	new_neg_index = []


	for i,j in enumerate(user_input):
		positive_index.append(i)
		neg_index.append(i)
		list_var.append(j)


	for i,n in enumerate(neg_index,start=1):
		new_neg_index.append(-abs(i))


	new_neg_index.reverse()



	myTable = PrettyTable(header=False)

	myTable.add_row(positive_index)
	myTable.add_row(list_var)
	myTable.add_row(new_neg_index)


	with open(user_input+".html",'w') as file:
		file.write(myTable.get_html_string())
		file.close()

	print("Html file created.....")

option1 = "\t1. Display the index values here"

option2 = "\t2. Get html version of the table"

print("\n")
print("\tOPTIONS: ",RED)
print("\n")
print(option1,YELLOW)
print("\n")
print(option2,YELLOW)
print("\n")

u_option = int(input(" Enter your choice (1 or 2): "))

if u_option == 1 and len(user_input)>15:
	print("Since length of string greater than 15, option 2 is best, Choosing option2")
	html_table()
elif u_option == 1 and len(user_input)<15:
	display_table()
elif u_option == 2:
	html_table()
else:
	pass

