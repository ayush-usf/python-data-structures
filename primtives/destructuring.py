print(" ============ Basic Destructuring =================")

currencies = 1, 75  # type(currencies)) =  <class 'tuple'>
currencies2 = [1, 50]
currencies3 = {1, 40} or set([1, 40])   # Unsorted coz keys hashed

usd, inr1 = currencies
cad, inr2 = currencies2
dhm, inr3 = currencies3

print('\ncurrencies (tuple): 1, 75 =', currencies)
print(f'usd, inr = {usd}, {inr1}')
print('currencies (list): [1, 50] =', currencies2)
print(f'cad, inr = {cad}, {inr2}')
print('currencies (set): {1, 40} =', currencies3)
print(f'dhm, inr = {dhm}, {inr3}\n')

print("====================== Ignoring Values ========================")
person = ("Bob", 42, "Mechanic")
name, _, profession = person

print(name, profession)

print("=========== Destructuring in a list of tuples =================")
friends = [("Ayush", 23), ("Adarsh", 25), ("Ameya", 21)]

for friend in friends:
    print('friend: ', friend)

for name, age in friends:
    print('name, age: ', name, age)


print("============== Replacing array elements =========================")
a = [1,2,3,4,5,6]
print('a: ', a)

start, len = 0, len(a) - 1

print('start: ', start)
print('len: ', len)

if a[start] % 2 == 0: 
    start += 1
else:
    a[start], a[len] = a[len], a[start]
    len -= 1

print('a: ', a)

print("=== Replacing multiple array elements (Separating even/odd elems) ======")
A = [1,2,3,4,5,6]
print('A: ', A)

# def even_odd(A):
#     next_even, next_odd = 0, len(A) - 1
#     while next_even < next_odd:
#         if A[next_even] % 2 == 0: 
#             next_even += 1
#         else:
#             A[next_even], A[next_odd] = A[next_odd], A[next_even] 
#             next_odd -= 1
#     return A

# A = even_odd([1,2,3,4,5,6])
# print('A: ', A)


    