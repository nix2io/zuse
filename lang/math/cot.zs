# © Zuse Authors 2020
# Cotangent Function

# Returns the Cotangent of a number.
fn (
    # The number whose cotangent should be returned in radians.
    Number value
): Number { 
    return Reciprocal(
        value=Tan(
            value=value
        )
    );
} -> [
    Test([1], 57.28996163)
]