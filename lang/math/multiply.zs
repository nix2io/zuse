# © Zuse Authors 2020
# Multiply Function

# Multiply two numbers.
fn (
    # Left hand number expression.
    Number left,
    # Right hand number expression,
    Number right
): Number {
    return ctx.stdfunc.multiply(
        left=left,
        right=right
    );
} -> [
    Test([2, 3], 6)
]