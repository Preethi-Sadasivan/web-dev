def converttobinary(n):
  if n > 1:
    converttobinary(n//2 )
  print(n%2 , end=" " )



dec=int(input("Enter a number to find it's Binary Value"))
converttobinary(dec)
print()


