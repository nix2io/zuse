# © Zuse Authors 2020
# To Radians Function

# Convert degrees to radians.
fn Number (
    # A number representing an angle in degrees that should be converted to radians.
    Number value
) { value * (Pi() / 180) } -> [
    Test([1], 0.0174533)
]