# © Zuse Authors 2020
# Cube Root Function

# Get the square root of a value.
fn Number (
    # Value to get the square root of.
    Number value
) { Root(value, 2) } -> [
    Test([64], 8),
    Test([16], 4)
]