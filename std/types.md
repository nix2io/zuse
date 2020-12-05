# Standard Types

## Primary Datatypes

### Any

- **Abstract**

The any type is the parent type for all types in the language.

You are not able to instantiate this type but you can use it as a type for arguments.

----

### Text

- Parent: [Any](#any)

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

- Parent: [Any](#any)

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

- Parent: [Any](#any)

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

----

### Null

- Parent: [Any](#any)

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

- Parent: [Any](#any)

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

----

### Object

- Parent: [Any](#any)

Zuse uses objects to represent key:value pairs.

All keys are represented as `Text`.

#### Arguments

| Name    | Type               | Description              | Default      |
|---------|--------------------|--------------------------|--------------|
| `value` | `object` or `dict` | The value of the object  | `{}`         |

#### Example

```json5
[
  "Object",
  {
    "value": {
      "foo": [
        "Text",
        {
          "value": "bar"
        }
      ]
    }
  }
]
```

This would be the same as:

```json5
{
  "foo": "bar"
}
```

----

### Set

- Parent: [Array](#array)

A set is an array that can not contain duplicate elements.
The `Set` inherits the same attributes as Array.

The difference is that certain functions like [`Push`](./functions#push) or [`Add`](./functions#add) work differently because they will check for duplicate elements.

----

### Character

- Parent: [Text](#text)

A character is a single unicode character.

It inherits all the same properties as Text but can only be a single character therefore a lot of Text functions will not work with `Character`.

#### Arguments

| Name    | Type              | Description                |
|---------|-------------------|----------------------------|
| `value` | `string`, `char`  | The value of the character |

#### Example

```json5
[
  "Character",
  {
    "value": "A"
  }
]
```

----

### Function

Every non standard function is of type `Function`.

Every function is anonymous and needs to be declared in order to be called when in runtime.

#### Arguments

| Name         | Type                                       | Description                     | Default |
|--------------|--------------------------------------------|---------------------------------|---------|
| `arguments`  | [`Array`](#array)<[`Argument`](#argument)> | An array of arugments           | `[]`    |
| `returnType` | [`Any`](#any)                              | The return type of the function |         |
| `logic`      | Function                                   | The code to execute when called |         |

> **_NOTE_**  Not sure if I want to use the word `logic` to represent the code to execute.

> **_NOTE_**  Not sure how I want to make the Type for the logic

#### Example

```json5
// create a function to square a given number
[
  "Function",
  {
    "arguments": [
      "Array",
      {
        "value": [
          [
            "Argument",
            {
              "name": [
                "Text",
                {
                  "value": "numb"
                }
              ],
              "type": [
                "Type",
                {
                  "typeName": "Number"
                }
              ]
            }
          ]
        ]
      }
    ],
    "returnType": [
      "Type",
      {
        "typeName": "Number"
      }
    ],
    "logic": [
      "Return",
      {
        "value": [
          "Multiply",
          {
            "value_left": [
              "Var",
              {
                "name": [
                  "Text",
                  {
                    "value": "numb"
                  }
                ]
              }
            ],
            "value_right": [
              "Var",
              {
                "name": [
                  "Text",
                  {
                    "value": "numb"
                  }
                ]
              }
            ]
          }
        ]
      }
    ]
  }
]
```

In Typescript, the equivilent would be.

```typescript
(numb: number): number => number * number;
```

or Python *(however, python does not support types)*
```py
lambda numb: numb * numb;
```

----
