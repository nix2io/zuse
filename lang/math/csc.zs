# © Zuse Authors 2020
# Cosecant Function

# Returns the Cosecant of a number.
fn Number (
    # The number whose cosecant should be returned in radians.
    Number value
) {
    Reciprocal(
        Sin(value)
    )
} -> [
    Test([1], 57.29868849)
]