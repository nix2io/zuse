# © Zuse Authors 2020
# Modulus Function

# Modulus math.
fn (
    # Left hand number expression.
    Number left,
    # Right hand number expression.
    Number right
): Number {
    return ctx.stdfunc.mod(
        left=left,
        right=right
    );
} -> [
    Test([5, 2], 1),
    Test([4, 2], 0)
]