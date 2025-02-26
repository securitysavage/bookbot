from stats import wordcount

def get_book_text(path):
	with open(path) as f:
		file_contents = f.read()
		return file_contents

def main():
	contents = get_book_text("books/frankenstein.txt")
	num_words = wordcount(contents)
	print (f"{num_words} words found in the document")

main()
