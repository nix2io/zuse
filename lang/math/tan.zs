# © Zuse Authors 2020
# Tangent Function

# Returns the Tangent of a number.
fn (
    # The number whose tangent should be returned in radians.
    Number value
): Number {
    return ctx.stdfunc.tan(
        value=value
    );
} -> [
    Test([.5], 0.5463024898437905)
]