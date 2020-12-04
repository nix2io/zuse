# Internal

I want people to be able to define functions like this

```js
// xLang
Set(
  Text("sayHello"),
  Function(
    // input arguments
    Input(
      Text("name"),
      Type(Text),
    ),
    // return type
    Type(Text),
    // code
    Return(
      Concat(
        Text("Hello "),
        Var(
          Text("name")
        )
      )
    )
  )
)
```
This is the equivilent of 
```ts
// Typescript
const sayHello = (name: string): string => {
  return "Hello " + name;
}
```


