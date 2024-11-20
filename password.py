'''
Validador de contraseñas
    Tener 8 o más caracteres
    Debe contener al menos una letra
    Debe contener al menos un número
    No puede contener espacios

'''
# len # -> nos da la cantidad de elementos de un iterable
# pwd = "contrassss 1"
# # Una contraseña es correcta CUANDO tiene 8 o MÁS caracters
# if len(pwd) >= 8:
#     print("La contraseña tiene 8 o más caracteres") # 
# else:
#     print("Longitud incorrecta")

# if not pwd.isalpha() and not pwd.isdigit():
#     print("La contraseña tiene al menos una letra")
#     print("La contraseña tiene al menos un número")

# if not pwd.count(" ") >= 1:
#     print("La contraseña no tiene espacios")
nums = [1, 2, 3, 3, 5]

nums[0] # -> 1
nums[-1] # -> 5
nums[0:3] # -> 1,2,3
nums.append(6)

if nums[0] > nums[3]: # -> 1 > 4
    print("Hola")


result = 0
for num in nums:
    result = result + num # result += num


repeated_numbers = [2,2,10,11,13,2,8,9,16,26,50,51,56,89,150,2,3,6,7,67,98, 1]

# repeated_numbers.sort(reverse=True)
# print(repeated_numbers)

result = 0
for num in repeated_numbers:
    result += num

# print(result/len(repeated_numbers))

# print(sum(repeated_numbers)/len(repeated_numbers))

max_num = max(repeated_numbers)
max_num_index = repeated_numbers.index(max_num)
repeated_numbers[max_num_index] = 1000
# print(repeated_numbers)


nums = [1,3,2,4]

def avg(sample):
    sample = sample.copy()
    return sum(sample)/len(sample)

nums_avg = avg(nums)
print(nums_avg)
print(nums)