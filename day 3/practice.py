#write a program to print numbers
for i in range (1,11):
    print(i)


#program to print even numbers 
for i in range (1,21):
    if i % 2 == 0:
        print(i)


#print then number from 1 to 20 but skip the number 10
for i in range (1,21):
    if i == 10:
        continue
    print(i)


#sum of number from 1 to 10 
total = 0
for i in range(1,11):
    total = total + i
    print(total)

#write a program to print the multiplacation table of 5 from 1 to 10 
for i in range (1,11):
    print(5*i)

#write a program to count how many even numbersare between 1 to 20 
count = 0
for i in range(1,21):
    if i % 2 == 0:
        count = count +1
        print(i)


#find the largest number
numbers=[10,25,7,40,18] 
largest=0
for i in numbers:
    if i>largest:
        largest = i
        print(largest)


        #write a program to print the multiplacation table of 7 from 1 to 10
        for i in range(1,11):
            print(7*i)



#reverse counting
for i in range(10,0,-1):
    print(i)
     