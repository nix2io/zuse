# © Zuse Authors 2020
# Cube Root Function

# Get the cube root of a value.
fn (
    # Value to get the cube root of.
    Number value
): Number {
    return Root(
        value=value,
        n=3
    );
} -> [
    Test([16], 2),
    Test([81], 3)
]