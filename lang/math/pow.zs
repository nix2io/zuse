# © Zuse Authors 2020
# Power Function

# Rases a number to a power.
fn Number (
    # Value to get raised.
    Number value,
    # Exponent to raise to.
    Number exp
) { ctx.stdfunc.pow(value, exp) } -> [
    Test([3, 2], 9)
]