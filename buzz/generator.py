from __future__ import print_function
import random

buzz = ('continuous testing', 'continuous integration', 'continuous deployment', 'continuous improvement', 'devops')
adjectives = ('complete', 'modern', 'self-service',	'integrated',	'end-to-end')
adverbs = ('Mang may tinh mang cao', 'He quan trị CSDL', 'Khai thac du lieu va ung dung', 'Lap trinh java', 'AV4')
names = ('20424048','Vu Linh','20HCB1', 'HCMUS')

def sample(l, n = 1):
		result = random.sample(l, n)
		if n == 1:
				return result[0]
		return result

def generate_buzz():
		buzz_terms = sample(buzz, 2)
		print(buzz_terms)
		phrase = ' '.join([sample(adjectives), buzz_terms[0], sample(adverbs), sample(names), buzz_terms[1]])
		return phrase.title()

if __name__ == "__main__":
		print(generate_buzz())