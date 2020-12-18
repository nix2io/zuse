# © Zuse Authors 2020
# Divide Function

# Divide two numbers.
fn Number (
    # Left number expression.
    Number left,
    # Right number expression.
    Number right
) { ctx.stdfunc.divide(left, right) } -> [
    Test([6, 3], 2)
]