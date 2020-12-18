# © Zuse Authors 2020
# Add Function

# Add two numbers.
fn Number (
    # Left number expression.
    Number left,
    # Right number expression.
    Number right
) { ctx.stdfuns.math.add(left, right) } -> [
    Test([1, 2], 3)
]