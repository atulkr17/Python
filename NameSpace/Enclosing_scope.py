def outer():
  a=3
  def inner():
    print(a)
  inner()
  print('outer function')

a=1
outer()
print('main program')