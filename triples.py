from StanfordOpenIEPython.main import stanford_ie
import argparse
import os

FILE_PATH = 'StanfordOpenIEPython/sentences.txt'

def triples_extractor(sentence):
    try:
        os.remove(FILE_PATH)
    except:
        pass
    with open(FILE_PATH, 'a') as text:
        text.write(sentence)
    triples_raw = stanford_ie('sentences.txt', verbose=True)
    triples = [[trip.lstrip() for trip in triple] for triple in triples_raw]
    return triples


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-s", "--sentence", default='Bill Gates is married to Melinda Gates.')
    args = parser.parse_args()
    sentence = args.sentence
    print triples_extractor(sentence)