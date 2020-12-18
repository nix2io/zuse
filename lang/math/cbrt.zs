# © Zuse Authors 2020
# Cube Root Function

# Get the cube root of a value.
fn Number (
    # Value to get the cube root of.
    Number value
) { Root(value, 3) } -> [
    Test([16], 2),
    Test([81], 3)
]