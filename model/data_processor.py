import numpy as np
import math
from operator import itemgetter

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
            
            for key, value in sorted_vocab:
                prob_vocab[key] = (math.sqrt(10000*float(value)/j)+1) * (float(1.0)/(10000*float(value)/j))
                no_vocab[key] = float(value)
            
            print(f"\nUnique:\t{len(vocab)}\nTotal Words:\t{j}")

            return prob_vocab, no_vocab
    
    def make_training_data(self, file, prob_vocab, no_vocab, n=3):
        text = []
        with open(file, 'r') as f:
            for line in f:
                text = line.split()

        data_raw = []
        l = 0
        for i in range(n+1, len(text)-n):
            if no_vocab[text[i]] < 15:
                continue
            l+=1
            temp_context = [text[j] for j in range(i-n, i+n+1) if(j!=i and no_vocab[text[j]]>=15)]
            temp_context.insert(0, text[i])
            data_raw.append(temp_context)
        
        print(f"Length after removing: {len(data_raw)}")


        int_to_words = {}
        word_to_int = {}
        x = 0

        for i, val in enumerate(data_raw):
            if val[0] in word_to_int:
                continue
            word_to_int[val[0]] = x
            int_to_words[x] = val[0]
            x+=1
        
        print(f"Unique after removing: {x}")

        return word_to_int, int_to_words, data_raw
