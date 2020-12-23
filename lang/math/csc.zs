# © Zuse Authors 2020
# Cosecant Function

# Returns the Cosecant of a number.
fn (
    # The number whose cosecant should be returned in radians.
    Number value
): Number {
    return Reciprocal(
        value=Sin(
            value=value
        )
    );
} -> [
    Test([1], 57.29868849)
]