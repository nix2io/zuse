# © Zuse Authors 2020
# Multiply Function

# Multiply two numbers.
fn Number (
    # Left hand number expression.
    Number left,
    # Right hand number expression,
    Number right
) { ctx.stdfunc.multiply(left, right) } -> [
    Test([2, 3], 6)
]