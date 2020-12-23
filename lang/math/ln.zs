# © Zuse Authors 2020
# Natural Logarithm Function

# Returns the natural logarithm (base e) of a number.
fn (
    # The number whose base-e natural logarithm should be returned.
    Number value
): Number {
    return Log(
        value=value,
        base=E()
    );
} -> [
    Test([5], 1.60943791)
]