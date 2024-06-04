jumpRange = int(input("¿De qué número deseas saber la tabla de multiplicar?: "))
endRange = int(input(f"\nOk, querés saber la tabla del {jumpRange}, hasta qué número deseas ver la tabla?: "))
for x, i in enumerate(range(0, endRange +1, jumpRange)):
  print(f"\n{jumpRange} * {x} = {i}\n")