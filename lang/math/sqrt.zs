# © Zuse Authors 2020
# Cube Root Function

# Get the square root of a value.
fn (
    # Value to get the square root of.
    Number value
): Number {
    Root(
        value=value,
        n=2
    )
} -> [
    Test([64], 8),
    Test([16], 4)
]