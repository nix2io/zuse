# © Zuse Authors 2020
# Subtract Function

# Subtracts two numbers.
fn Number (
    # Left hand number expression.
    Number left,
    # Right hand number expression.
    Number right
) { left + Opposite(right) } -> [
    Test([3, 1], 2)
]