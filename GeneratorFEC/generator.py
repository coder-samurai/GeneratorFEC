import random
import string


class Generator:
	
	def __init__(self, lettersLower=True, 
	lettersUpper=True, numbers=True, symbols=True, SaveFile=False, Number_Of_Letters=1):
		
		self.lettersLowercase = string.ascii_lowercase
		
		self.lettersUppercase = string.ascii_uppercase
		
		self.numbers = string.digits
		
		self.symbols = string.punctuation
		
		self.NOL = Number_Of_Letters
		
		self.LL = lettersLower
		
		self.LU = lettersUpper
		
		self.NM = numbers
		
		self.SM = symbols
		
		self.SF = SaveFile
	
	def start(self):
		
		for i in range(1):
			
			generator = ''
			
			for c in range(self.NOL):
				
				letterLower = random.choice(self.lettersLowercase)
				
				letterUpper = random.choice(self.lettersUppercase)
				
				Number = random.choice(self.numbers)
				
				Symbol = random.choice(self.symbols)
				
				ALL = [letterLower, letterUpper, Number, Symbol]
				
				if self.LL == False:
					ALL.remove(letterLower)
				else:
					None
				
				if self.LU == False:
					ALL.remove(letterUpper)
				else:
					None
				
				if self.NM == False:
					ALL.remove(Number)
				else:
					None
				
				if self.SM == False:
					ALL.remove(Symbol)
				else:
					None
				
				result = random.choice(ALL)
				
				generator += result
				
			if self.SF == False:
				
				return generator
				
			else:
				
				file = open('generator.txt', 'a+')
				
				file.write(f'{generator}\n')
				
				file.close()
				
				return 'Saved in file"generator.txt"\n'
