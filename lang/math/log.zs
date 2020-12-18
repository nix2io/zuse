# © Zuse Authors 2020
# Logarithm Function

# Returns the logarithm (base n) of a number.
fn Number (
    # The number whose base-n logarithm should be returned.
    Number value,
    # Base number of the logarithm.
    Number base = 10
) { ctx.stdfunc.log(value, base) } -> [
    Test([100, 10], 2),
    Test([81, 3], 4)
]