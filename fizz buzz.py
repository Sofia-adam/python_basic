for fizzbuzz in range(51):
    if fizzbuzz % 3 == 0 and fizzbuzz % 5 == 0:
        # If divisible by both 3 and 5, print "fizzbuzz" and continue to the next iteration
        print("fizzbuzz")
        continue
    elif fizzbuzz % 3 == 0:
        # If divisible only by 3, print "fizz" and continue to the next iteration
        print("fizz")
        continue
    elif fizzbuzz % 5 == 0:
        # If divisible only by 5, print "buzz" and continue to the next iteration
        print("buzz")
        continue
    # If the number is neither divisible by 3 nor 5, print the number itself
    print(fizzbuzz)