# © Zuse Authors 2020
# Secant Function

# Returns the Secant of a number.
fn Number (
    # The number whose secant should be returned in radians.
    Number value
) {
    Reciprocal(
        Cos(value)
    )
} -> [
    Test([1], 1.00015232)
]