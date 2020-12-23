# © Zuse Authors 2020
# Power Function

# Rases a number to a power.
fn (
    # Value to get raised.
    Number value,
    # Exponent to raise to.
    Number exp
): Number {
    return ctx.stdfunc.pow(
        value=value,
        exp=exp
    );
} -> [
    Test([3, 2], 9)
]