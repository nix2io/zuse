# © Zuse Authors 2020
# Absolute Function

# Returns the absolute value of a number.
fn Number (
    # Number to get the absolute.
    Number value
) { Opposite(value) if value < 0 else value } -> [
    Test([-1], 1),
    Test([1], 1)
]