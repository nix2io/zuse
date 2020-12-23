# © Zuse Authors 2020
# Secant Function

# Returns the Secant of a number.
fn (
    # The number whose secant should be returned in radians.
    Number value
): Number {
    return Reciprocal(
        value=Cos(
            value=value
        )
    );
} -> [
    Test([1], 1.00015232)
]