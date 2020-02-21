import ps4b as ps


sentence = "Hello*, is this! me?"

message = ps.Message(sentence)

#print(message.get_message_text())
#print(message.get_valid_words())
#print(message.build_shift_dict(shift = 2))

message2 = ps.PlaintextMessage(sentence,3)
#print(message2.get_valid_words())



#print(message2.get_message_text_encrypted())

cipher = ps.CiphertextMessage(message2.get_message_text_encrypted())
#print("is it working?")
#print(cipher.decrypt_message())


ciph_msg = ps.CiphertextMessage("ifmmp")

plain_msg = ps.PlaintextMessage("Hello",1)

print("we're applying the shift code")

plain_cipher = plain_msg.apply_shift(1)
print(plain_msg.get_message_text())
print(plain_msg.get_message_text_encrypted())


print("we're deciphering the message")

ciph_decode = ciph_msg.decrypt_message()
print(ciph_msg.get_message_text())
print(ciph_decode)

