import csv
from pprint import pprint

def main():
	with open('training_set_short.csv', 'rb') as csvfile:
		training_set_reader = csv.reader(csvfile, delimiter=';', quotechar='|')
		review_list = []
		review = ()
		for row in training_set_reader:
			review = row[0], row[1]					#0 row[0]: reviews #row[0]: rate
			review_list.append(review)

		list_of_words = []
		unique_dict = {}
		curious = []
		for row in review_list:
			temp_list_of_words = row[0].split()		#splits up the sentences into list of words
			for temp_word in temp_list_of_words:
				list_of_words.append(temp_word)
			
		for word in list_of_words:
			unique_dict[word] = 0.0					#no duplicates in dict

		for k, v in unique_dict.iteritems():
			word_count = 0
			sum_rate = 0
			for sentence in review_list:			#counts the word in training set and finds out the cumulative rate for all words
				temp_list_of_words = sentence[0].split()
				for word in temp_list_of_words:
					if k == word:
						word_count = word_count + 1
						sum_rate = sum_rate + float(sentence[1]) 
			
			unique_dict[k]= sum_rate / word_count	#average rate
			curious.append((k, sum_rate))
		for i in curious:
			print i

	total_per_grade = { 0:0, 1:0, 2:0, 3:0, 4:0 }
	with open('test_set_short.csv', 'rb') as csvfile:
		test_set_reader = csv.reader(csvfile, delimiter=';', quotechar='|')
		review_list_TS = []
		review_TS = ()
		# Row consists of a sentence followed by a grade
		for row in test_set_reader:
			total_per_grade[int(row[1])] = total_per_grade[int(row[1])] + 1
			# Count total points for sentence
			total = 0
			# Number of words that are in the dict
			freq = 0

			# Look at every word in the review sentence
			for word in row[0]:

				# Search if the word is in the dictionary
				for k, v in unique_dict.iteritems():
					# If the word is in the dictionary
					if word == k:
						# Add up the total points
						total = total + v
						# And increase the frequency of words in that matched in this sentence
						freq = freq + 1
						

			# Store 2-tuple of a 3-tuple of (Sentence, (Grade, Total points, Frequency))
			review_TS = row[0], (int(row[1]), total, freq)
			# Store all of it in a list of 2-tuples of 3-tuples
			review_list_TS.append(review_TS)
		
		# Key,Value pair where the grade is the key
		# and the frequency of that grade is the value
		grouping = { 0:0, 1:0, 2:0, 3:0, 4:0 }

		# Loop through the list of 2-tuples
		for entry in review_list_TS:
			# Only check the cases where the frequency was not 0
			if entry[1][2] != 0:
				# Compute the rounded value of dividing total/freq.
				value = int(round(entry[1][1]/entry[1][2]))
				# Add to the total for that particular grade group
				grouping[value] = grouping[value] + 1

		print "Grade\tTotal\tEstimate"
		for k,v in grouping.iteritems():
			for kk, vv in total_per_grade.iteritems():
				if k == kk:
					print str(k) + "\t\t" + str(vv) + "\t\t" + str(v)




if __name__ == "__main__":
	main()