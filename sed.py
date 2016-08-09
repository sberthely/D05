

# import os

def sed(word_to_replace, replacing_word, source_file, destination_file):
	try: 

		# cwd = os.getcwd()
		# print(cwd)

		in_file = open(source_file, 'r')
		out_file = open(destination_file, 'w')

		for line in in_file:
			line = line.replace(word_to_replace, replacing_word)
			out_file.write(line)

		in_file.close()
		out_file.close()

	except:
		print('Something went wrong opening the files.')

def main():
    sed('Selenne', 'Mike', 'ORIGINAL.txt', 'DESTINATION.txt')


if __name__ == '__main__':
    main()