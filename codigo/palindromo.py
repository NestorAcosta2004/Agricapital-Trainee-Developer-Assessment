def palindromo(ejemplo):
    ejemplo = ejemplo.replace(" ","").lower()
    if ejemplo == ejemplo[::-1]:
        return True
    else:
        return False

print(palindromo("luz azul"))
print(palindromo("radar"))
print(palindromo("hola"))