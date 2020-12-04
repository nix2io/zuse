# Datetypes

Creating a type is done by the [`Type` function](./functions#type.md).

## Primary data

### Number

```js
// Definition
Type(Number)

// Number has different options
Type(
  Number,
  Min(1), // min value
  Max(9), // max value
  Whole() // has to be a whole number
)

// Instantiation
Number(1)
```

### Boolean

```js
// Definition
Type(Boolean)

// Instantiation
Boolean(true)
```

### Character

```js
// Definition
Type(Character)
// Options
Type(
  Character,
  Uppercase() // has to be uppercase
)

// Instantiation
Character('H')
```

### Null & Undefined [WIP]
I'm not sure how I want to handle null or undefined, if they are going to be the same or not.

```js
Null()
```

## Datetype Modifiers (Generics)

### Array

```js
// Definition
Type(
  Array,
  Type(Character)
)
// Options
Type(
  Array,
  Type(Number),
  Max(5)
)

Array(
  Character('H'),
  Character('E'),
  Character('L'),
  Character('L'),
  Character('O')
)
```

