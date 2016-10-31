import os
import sys
import matplotlib.pyplot as plt
import numpy as np





# Definition of the class 
class FastaParser(object):
	def __init__(self, path): # Initialize instance of the fastaperser
		self.path = path
		if not os.path.exists(path):
			raise IOError ("The %s does not exist" % path)

		# Make a dictionary of sequences
		
		seqdict = {} 
		for line in open(path, "r").readlines():
			if '>' in line: # Record the name of the sequence and leave it with an empty sequence
				seqname = line.rstrip("\n")[1:]
				seqdict[seqname] = ""
			else:
				seqdict[seqname] = str(seqdict[seqname]) + line.rstrip("\n") # Concatenate the sequence data until you reach a new name

		self.seq = seq
		self.seqdict = seqdict
		self.count = len(self.seqdict.keys())

	

	# The length of the dictionary list of keys is equal to the number of sequences
	def __len__(self):
		return len(self.seqdict.keys())

	

	# To iterate over the new object
	def __getitem__(self, n):
		if type(n) is int: # If user uses number indexes
			key = self.seqdict.keys()[n]
			return self.seqdict[key]
			
			# If the index is out of range the dictionary automatically throws an IndexError exception
		else: # If they use the name of the sequence instead
			return self.seqdict[n]

	

 def extract_length(self, maxlength):#Filter the sequences and return shorter
        
        self.maxlength = max_length
        seq_list = []
        for line in self.seq:
            if len(line) <= max_length:
                seq_list.append(line)
        return seq_list



    def length_dist(self, path): # A graph of the length distribution of the sequences and saves it in pdf format 
        
        directory = os.path.split(path)
        sh.mkdir("-p", directory)

        length_list = []

        for line in self.seq:
            length_list.append(len(line))
       
        a = np.array(length_list)
        a.sort()
        f = plt.figure()
        a_mean = np.mean(a)
        a_std = np.std(a)
        p = stats.norm.pdf(a, a_mean, a_std)
        plt.xlabel('Sequence length')
        plt.ylabel('Number of sequences')
        plt.plot(a, p)
        plt.show()
        f.savefig(path)


       