import csv
from pprint import pprint

def main():
	with open('rotten_test.csv', 'rb') as csvfile:
		freq_reader = csv.reader(csvfile, delimiter=';', quotechar='|')
		review_list = []
		review = ()
		for row in freq_reader:
			review = row[0], row[1]
			review_list.append(review)

		list_of_words = []
		unique_dict = {}
		for row in review_list:
			temp_list_of_words = row[0].split()
			for temp_word in temp_list_of_words:
				list_of_words.append(temp_word)
			
		for word in list_of_words:
			unique_dict[word] = 0.0

		for k, v in unique_dict.iteritems():
			word_count = 0
			sum_rate = 0
			for sentence in review_list:
				temp_list_of_words = sentence[0].split()
				for word in temp_list_of_words:
					if k == word:
						word_count = word_count + 1
						#print sentence[1]
						sum_rate = sum_rate + float(sentence[1]) 
			
			unique_dict[k]= sum_rate / word_count

		pprint(unique_dict)

#		fyrsta_lina = review_list[0]
#		print fyrsta_lina[0].split()
#		#print fyrsta_lina[1]

if __name__ == "__main__":
	main()