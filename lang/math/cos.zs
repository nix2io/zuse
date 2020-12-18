# © Zuse Authors 2020
# Cosine Function

# Returns the Cosine of a number.
fn Number (
    # The number whose cosine should be returned in radians.
    Number value
) { ctx.stdfunc.cos(value) } -> [
    Test([.5], .8775825618903728)
]