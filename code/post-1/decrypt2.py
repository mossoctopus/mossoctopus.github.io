def decrypt(text, key):
	result = ""
	for i in range(len(text)):						# for each character in the cipher text...
		char = text[i]
		alphabet_position = ord(char) - 96 				# lower case a is equal to 97. Converting the lowercase letter to alphabet position
		decrypted_char = (alphabet_position - key)
		if decrypted_char < 1:						# in case decryption results in a negative value due to a complete rotation during encryption
			decrypted_char = decrypted_char + 26			# for example, 'a' as cipher text when key=d=4. The decryption should result in w=23.
		decrypted_char += 96						# converting back to ASCII char value
		result+= chr(decrypted_char)					# creating plain text string for each decrypted char
	return result


txt = input("Cipher text: ")
k = int(input("Key (as an integer from 1 to 26): "))
print (decrypt(txt,k))
