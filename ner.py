from nltk.tag import StanfordNERTagger
import argparse
from nltk import word_tokenize
from re import sub
from itertools import groupby

# st_ner = StanfordNERTagger('english.muc.7class.distsim.crf.ser.gz')
st_ner = StanfordNERTagger('english.all.3class.distsim.crf.ser.gz')


def sentence_tagger(sentence_list):
    named_entities = st_ner.tag_sents(sentence_list)
    return named_entities


def get_nodes(tagged_words):
    ent = []
    for tag, chunk in groupby(tagged_words, lambda x:x[1]):
        if tag != "O":
            tuple1 = (sub(r'\s+([?.!,"])', r'\1', " ".join(w for w, t in chunk)), tag)
            ent.append(tuple1)
    return ent


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-s", "--sentence", default='Bill Gates is married to Melinda Gates.')
    args = parser.parse_args()
    sentence_lis = [args.sentence]
    sentence_list = [word_tokenize(sent) for sent in sentence_lis]
    print sentence_list
    named_tags = sentence_tagger(sentence_list)
    print named_tags
    for ne in named_tags:
        named_entities = get_nodes(ne)
        print named_entities