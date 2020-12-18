# © Zuse Authors 2020
# Natural Logarithm Function

# Returns the natural logarithm (base e) of a number.
fn Number (
    # The number whose base-e natural logarithm should be returned.
    Number value
) { Log(value, E()) } -> [
    Test([5], 1.60943791)
]