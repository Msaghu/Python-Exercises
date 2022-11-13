#The famous fizz buzz

#1. Print the numbers 0 to 100
#2. For numbers that are evenly divisble by 3, print 'Fizz' instead of printing the number
#3.  For numbers that are evenlyle by 5, print 'Buzz' instead of printing the number
#4. For numbers evenly divisible 3 and 5,prnt 'FizzBuzz' instead or printing the number

 
#x = range(100)
#if x//3 == 0:
 #   print('Fizz')
#elif x//5 == 0:
 #   print('Buzz')
#elif x//3==0 AND x//5==0:
 #   print('FizzBuzz')


counter = 0

while counter <= 100:
    if counter % 15 == 0 :
        print('FizzBuzz')
    elif counter % 3 == 0:
        print('Fizz')
    elif counter % 5 == 0:
        print('Buzz')
    else:
        print(counter)

    counter += 1
 

#counter = 0
#hile counter <= 100:
 
 #counter += 1
  #  print(counter)

