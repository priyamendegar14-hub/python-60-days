#number analyzer
number=int(input("enter a number:"))
total=0
even_count=0
odd_count=0

print("number:")
for i in range(1,number+1):
    print(i)

#sum
total= total + i
#even nd odd         
if i % 2 == 0:
    even_count = even_count + 1
else:
    odd_count = odd_count + 1

print("sum:",total)
print("even numbers:",even_count)
print("odd numbers:",odd_count)
print("largest number:",number)



