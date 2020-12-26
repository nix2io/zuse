# © Zuse Authors 2020
# Add Function

# Add two numbers.
fn (
    # Left number expression.
    Number left,
    # Right number expression.
    Number right
): Number {
    return ctx.stdfunc.add(
        left=left,
        right=right
    );
} -> [
    Test([1, 2], 3)
]