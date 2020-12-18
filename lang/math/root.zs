# © Zuse Authors 2020
# Nth Root Function

# Get the nth root of a value.
fn Number (
    # Value to get the nth root of.
    Number value,
    # 'n'
    Number n = 2
) { value ^ Reciprocal(n) } -> [
    Test([16, 3], 2),
    Test([64], 8)
]