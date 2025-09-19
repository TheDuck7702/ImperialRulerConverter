from fractions import Fraction

def decimal_to_ruler_fraction(value):
    denominators = [8, 16]
    closest = None
    closest_diff = float("inf")

    for d in denominators:
        # Round the decimal to nearest fraction with denominator d
        numerator = round(value * d)
        frac = Fraction(numerator, d)
        diff = abs(value - float(frac))

        if diff < closest_diff:
            closest = frac
            closest_diff = diff

    return f"{closest.numerator}/{closest.denominator}\""

# Example use
while True:
    try:
        user_input = input("Enter a decimal (or 'q' to quit): ")
        if user_input.lower() == "q":
            break
        decimal_value = float(user_input)
        print("Closest fraction on your ruler:", decimal_to_ruler_fraction(decimal_value))
    except ValueError:
        print("Please enter a valid decimal number.")