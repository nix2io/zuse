# © Zuse Authors 2020
# Absolute Function

# Returns the absolute value of a number.
fn (
    # Number to get the absolute.
    Number value
): Number {
    if IsNegative(
        value=value
    ) {
        return Opposite(
            value=value
        );
    } else {
        return value;
    }
} -> [
    Test([-1], 1),
    Test([1], 1)
]