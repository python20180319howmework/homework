def h(word):
	word=word[0].upper()+word[1:].lower()
	return word
print(list(map(h,["iIlH","LoUi","kOu"])))
