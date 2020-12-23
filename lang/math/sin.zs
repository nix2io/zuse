# © Zuse Authors 2020
# Sine Function

# Returns the Sine of a number.
fn (
    # The number whose sine should be returned in radians.
    Number value
): Number {
    return ctx.stdfunc.sin(value);
} -> [
    Test([.5], 0.479425538604203)
]