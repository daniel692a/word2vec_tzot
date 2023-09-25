import numpy as np
import sklearn
import math
import sys
from operator import itemgetter
import copy

class DataProcessor:
    def remove_new_line(self, file, out):
        with open(file, 'r') as f, open(out, 'w+') as g:
            for line in f:
                temp =  line.replace('\n', ' ')
                g.write(temp)
        print("Created merged dataset...\n")
        
    def compute_vocab(self, file):
            j = 0
            vocab = {}
            text = []
            with open(file, 'r') as f:
                for line in f:
                    text = line.split()

            for word in text:
                j+=1
                if word in vocab:
                    vocab[word]+=1
                    continue
                vocab[word] = 1

            sorted_vocab = sorted(vocab.items(), key = itemgetter(1))

            prob_vocab = {}
            no_vocab = {}
            
            for key, value in sorted_vocab():
                prob_vocab[key] = (math.sqrt(10000*float(value)/j)+1) * (float(1.0)/(10000*float(value)/j))
                no_vocab[key] = float(value)
            
            print(f"\nUnique:\t{len(vocab)}\nTotal Words:\t{j}")

            return prob_vocab, no_vocab
    
    def make_training_data(self, file, prob_vocab, no_vocab, n=3):
        
