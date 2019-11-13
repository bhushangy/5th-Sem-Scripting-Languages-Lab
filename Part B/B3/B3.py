class Rev:
	
	def __init__(self,sen,lis,rsen,vcnt):
		self.sen = sen
		self.lis = []
		self.rsen = rsen
		self.vcnt = 0

	def reverse(self):  #if u r not passing any arg and u r refering to the class variables, then u have to use self for every refernce to class variable made..
		for i in self.sen:
			if i.lower() in ['a','e','i','o','u']:
				self.vcnt+=1
		#print(self.vcnt)
		self.lis = self.sen.split()
		self.lis.reverse()
		for i in self.lis:
			self.rsen+=i
			self.rsen+=' '

		#print(self.rsen)




p1 = Rev('thomas shelby birmingham',[],'',0)
p1.reverse()
p2 = Rev('aeiou aeio aei',[],'',0)
p2.reverse()
p3 = Rev('yea bitch',[],'',0)
p3.reverse()

print(sorted([(p.rsen,p.vcnt) for p in (p1,p2,p3)],key = lambda x: x[1],reverse=True))
		