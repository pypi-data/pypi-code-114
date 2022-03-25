from .vocab import vocab_string 
vocab = vocab_string.split("\n")
vocab_inv = { i:w for i , w in enumerate(vocab)}
vocab = { w : i for i , w in enumerate(vocab)}

doublehash_vocab = [ w[2:] for w in vocab if w.startswith("##") ]
doublehash_vocab = { w : i for i , w in enumerate(doublehash_vocab)} 

symbols = {'~', ':', "'", '+', '[', '\\', '@', '^', '{', '%', '(', '-', '"', '*', '|', ',', '&', '<', '`', '}', '.', '_', '=', ']', '!', '>', ';', '?', '#', '$', ')', '/' , "\n"}


def get_word_token( word ):
	if word in vocab:
		return [vocab[ word ]]

	best_word = None
	best_len = 1000000

	for w in doublehash_vocab:
		if word.endswith( w ) and word[:  -len(w)  ] in vocab:
			if len(w) < best_len:
				best_len = len(w)
				best_word = word[:  -len(w)  ]  , w 

	if not best_word is None:
		return [ vocab[best_word[0]] , vocab["##" + best_word[1]]  ]

	return [vocab["[UNK]"]]


def tokenize( sentence , max_len=30 ):
	sentence = sentence.lower()
	for s in symbols:
		sentence = sentence.replace(s , " "+s+" ")
	sentence = sentence.split(" ")
	sentence = [ w for w in sentence if len(w) > 0 ]

	ret = [ vocab["[CLS]"] ]
	for w in sentence:
		ret +=  get_word_token(w) 
	ret += [ vocab["[SEP]"]]
	mask = [ 1 for _ in  ret ]

	ret = ret[:max_len]
	mask = mask[:max_len]

	if len(ret) < max_len:
		n_extra = max_len -  len(ret)
		ret += [ 0 for _ in range(n_extra )]
		mask += [ 0 for _ in range(n_extra )]

	
	return {'input_ids' : ret , 'attention_mask' : mask} 



if __name__ == "__main__":
	print( tokenize( "This is a good thing's. its snowing" , 30))

