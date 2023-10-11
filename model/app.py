from data_processor import DataProcessor

if __name__ == '__main__':
    processor = DataProcessor()
    prob_vocab, no_vocab = processor.compute_vocab('./corpus.txt')
    print(prob_vocab, no_vocab, sep='\n')