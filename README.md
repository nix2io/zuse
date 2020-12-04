# XLang
The X Language is a functional language representing symbols to compute the world's information.

## Datetypes

Information on datatypes is located [here](datatypes.md)

## Examples

```py
# Zip type
Set(
  # Set the name to Zip
  "Zip",
  # Set the value of Zip to a Type
  Type(
    # Let the type extend off of Text
    Extends(
      Type(Text)
    ),
    # Set length to equal 5
    Length(5),
    # Value is numeric
    IsNumeric()
  )
)
      


# this would create a GetWeather function
Set(
  # Set the name to GetWeather
  "GetWeather",
  # Set the value to a function
  Function(
    # array of arguments
    [
      Argument(
        # name of argument
        "zipCode",
        # type of argument to Zip
        Type(Zip)
      )
    ],
    # return type to WeatherReport (not listed but it would just be an Object type)
    Type(WeatherReport),
    # The code to execute
    # In this case it is a return statement
    Return(
      # Parse JSON string
      ParseJSON(
        # Do a Get request to a URL
        HTTPGet(
          # use a string template to format
          TemplateLiteral(
            Text("http://wttr.in/%s?format=j1"),
            Var("zipCode")
          )
        )
      )
    )
  )
)

# call that function

GetWeather(
  Zip("06824")
)

```
