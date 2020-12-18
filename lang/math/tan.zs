# © Zuse Authors 2020
# Tangent Function

# Returns the Tangent of a number.
fn Number (
    # The number whose tangent should be returned in radians.
    Number value
) { ctx.stdfunc.tan(value) } -> [
    Test([.5], 0.5463024898437905)
]