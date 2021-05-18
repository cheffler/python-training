# Error Handling

Catch errors in try catch (try, except)

Can use `else` for other actions (if no error)

Can use `finally` to do something regardless

`except` can be target for specific error types
`except` errors can be put into a variable using `as`
multiple error types can be caught by the same `except` clause

```py
try:
  40/0

except (TypeError, ZeroDivisionError) as err
  print(f"this is the error: {err}")

else:
  print('no error')

finally:
  print('the last word')
```
