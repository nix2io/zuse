# © Zuse Authors 2020
# Logarithm Function

# Returns the logarithm (base n) of a number.
fn (
    # The number whose base-n logarithm should be returned.
    Number value,
    # Base number of the logarithm.
    Number base = 10
): Number {} -> [
    Test([100, 10], 2),
    Test([81, 3], 4)
]