# © Zuse Authors 2020
# Modulus Function

# Modulus math.
fn Number (
    # Left hand number expression.
    Number left,
    # Right hand number expression.
    Number right
) { ctx.stdfunc.mod(left, right) } -> [
    Test([5, 2], 1),
    Test([4, 2], 0)
]