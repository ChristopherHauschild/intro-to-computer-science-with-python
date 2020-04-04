def fizzbuzz(x):
    if not (x % 3) and x % 5:
        return("Fizz")
    else:
        if not (x % 5) and x % 3:
            return("Buzz")
        else:
            if not (x % 3) and not (x % 5):
                return("FizzBuzz")
            else:
                return(x)
