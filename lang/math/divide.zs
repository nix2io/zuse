# © Zuse Authors 2020
# Divide Function

# Divide two numbers.
fn (
    # Left number expression.
    Number left,
    # Right number expression.
    Number right
): Number {
    return ctx.stdfunc.divide(
        left=left,
        right=right
    );
} -> [
    Test([6, 3], 2)
]