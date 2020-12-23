# © Zuse Authors 2020
# Cosine Function

# Returns the Cosine of a number.
fn (
    # The number whose cosine should be returned in radians.
    Number value
): Number {
    return ctx.stdfunc.cos(
        value=value
    );
} -> [
    Test([.5], .8775825618903728)
]