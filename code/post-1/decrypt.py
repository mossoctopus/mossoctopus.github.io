def decrypt(text, key):
	result = ""
	decrypt_key = 26 - key;
	for i in range(len(text)):						# for each character in the cipher text...
		char = text[i]
		alphabet_position = ord(char) - 96 				# lower case a is equal to 97. Converting the lowercase letter to alphabet position
		decrypted_char = (alphabet_position + decrypt_key) % 26		# % is the modulo operation in Python
		decrypted_char += 96						# converting back to ASCII char value
		result+= chr(decrypted_char)					# creating plain text string for each decrypted char
	return result


txt = input("Cipher text: ")
k = int(input("Key (as an integer from 1 to 26): "))
print (decrypt(txt,k))
