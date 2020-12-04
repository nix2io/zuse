# Zuse Lang Specification
The Zuse Language is a functional language representing symbols to compute the world's information.

## My vision

This is not meant to be used to write long complex programs, it should be used for small individual functions that are able to be combined to create greater functionality.

I am basing this project off of the wolfram language, however my goal is to make this opensource and allow people to create their own functions to add to the codebase.

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

## The Name

Named after [Konrad Zuse](https://en.wikipedia.org/wiki/Konrad_Zuse)
