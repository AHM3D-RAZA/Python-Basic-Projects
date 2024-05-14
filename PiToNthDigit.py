import math

def pi_to_nth_digit(n):
    pi_str = str(math.pi)
    new_pi = "3"
    if n <= 15:
        new_pi += "."
        for i in range(n):
            new_pi += pi_str[i+2]
    else:
        new_pi = str(math.pi)

    print(new_pi)
print(math.pi)

pi_to_nth_digit(15)