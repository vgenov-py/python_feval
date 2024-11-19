students = "Sara, Luisa, Pedro, Marcelo, María, MAría, Noria"

students_lower = students.lower()

x = students_lower.count("maría")

students_upper = students.upper()

y = students_upper.count(" ")


nums = "1, 2, 7, 6, 9, 8, 7"

user_num_1 = "x"
user_num_2 = "3"

n_user_num_1 = nums.count(user_num_1)
n_user_num_2 = nums.count(user_num_2)

"Cuando n_user_num sea igual a 1"
"if n_user_num == 1"
"if n_user_num_2 == 1"

if n_user_num_1 == 1 and n_user_num_2 == 1: # -> False
    print("El usuario ha ganado!")
elif user_num_1 == "x":
    print("El usuario ha ganado!")
else:
    print("El usuario ha perdido...")