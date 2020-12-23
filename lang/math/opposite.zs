# © Zuse Authors 2020
# Opposite Function

# Return the opposite number.
fn (
    # Number to get the opposite.
    Number value
): Number {
    return value * -1;
} -> [
    Test([2], -2)
]