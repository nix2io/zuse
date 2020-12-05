# Standard Types

## Primary Datatypes

### Any

- **Abstract**

The any type is the parent type for all types in the language.

You are not able to instantiate this type but you can use it as a type for arguments.

----

### Text

Strings in Zuse are represented as Text but are treated the same.

#### Arguments

| Name    | Type     | Description           |
|---------|----------|-----------------------|
| `value` | `string` | The value of the text |

#### Example

```json5
[
  "Text",
  {
    "value": "Hello World"
  }
]
```

----

### Number

Integers and floats are represented as Numbers in Zuse and can be converted for specifc language interaction.

> **_NOTE_**  I want this class to be the C group in math

<img height="100px" src="https://upload.wikimedia.org/wikipedia/commons/thumb/a/a0/NumberSetinC.svg/1200px-NumberSetinC.svg.png">

I will have more types of numbers

#### Arguments

| Name    | Type                         | Description             |
|---------|------------------------------|-------------------------|
| `value` | `int`, `float`, `double` etc | The value of the number |

#### Example

```json5
[
  "Number",
  {
    "value": 64
  }
]
```

----

### Boolean

Strait forward.

#### Arguments

| Name    | Type              | Description              |
|---------|-------------------|--------------------------|
| `value` | `boolean`, `bool` | The value of the boolean |

#### Example

```json5
[
  "Boolean",
  {
    "value": true
  }
]
```

### Null

`null`, `None`, & `undefined` should all be represented as `Null` in Zuse.

#### Arguments

*Null takes no arguments*

#### Example

```json5
[
  "Null",
  {}
]
```

## Secondary Data Types

### Array

To represent an `array` or `list` use an `Array`.
This is one of the types that requires an element type, which depends on other types.

#### Arguments

| Name    | Type              | Description              | Default      |
|---------|-------------------|--------------------------|--------------|
| `value` | `array` or `list` | The value of the array   | `[]`         |

#### Example

```json5
[
  "Array",
  {
    "value": [
      [
        "Text",
        {
          "value": "foo"
        }
      ],
      [
        "Text",
        {
          "value": "bar"
        }
      ]
    ]
  }
]
```

### Dictionary

### Set
