# © Zuse Authors 2020
# Reciprocal Function

# Return the reciprocal of a number.
fn (
    # Value to get the reciprocal of.
    Number value
): Number {
    return value ^ -1;
} -> [
    Test([2], 0.5),
    Test([4], 0.25)
]