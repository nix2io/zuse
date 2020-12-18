# © Zuse Authors 2020
# Cotangent Function

# Returns the Cotangent of a number.
fn Number (
    # The number whose cotangent should be returned in radians.
    Number value
) { 
    Reciprocal(
        Tan(value)
    )
} -> [
    Test([1], 57.28996163)
]