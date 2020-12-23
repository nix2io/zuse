# © Zuse Authors 2020
# Subtract Function

# Subtracts two numbers.
fn (
    # Left hand number expression.
    Number left,
    # Right hand number expression.
    Number right
): Number {
    return left + Opposite(
        value=right
    );
} -> [
    Test([3, 1], 2)
]