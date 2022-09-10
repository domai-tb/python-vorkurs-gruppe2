# TASK 7

# Schreibe ein Programm, dass alles geraden und ungeraden Zahlen von 0 bis 100 ausgibt:
print(*(f'{i} ist {"gerade" if i%2 == 0 else "ungerade"}.' for i in range(101)), sep='\n')
