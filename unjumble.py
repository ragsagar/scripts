import sys

dictfile = "/usr/share/dict/cracklib-small"

def get_words(text):
	""" Return a list of dict words """
	return text.split()
	

def get_possible_words(words,jword):
	""" Return a list of possible solutions """
	possible_words = []
	jword_length = len(jword)
	for word in words:
		jumbled_word = jword
		if len(word) == jword_length:
			letters = list(word)
			for letter in letters:
				if jumbled_word.find(letter) != -1:
					jumbled_word = jumbled_word.replace(letter,'',1)
			if not jumbled_word:
				possible_words.append(word)
	return possible_words		
			
				
if __name__ == '__main__':
	words = get_words(file(dictfile).read())
	if len(sys.argv) != 2:
		print "python %s <jumbled word>" % sys.argv[0]
		sys.exit()
	jumbled_word = sys.argv[1]
	words = get_possible_words(words,jumbled_word)
	print "possible words :"
	print '\n'.join(words)

