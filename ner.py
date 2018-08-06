from nltk.tag import StanfordNERTagger
import argparse
from nltk import word_tokenize

# st_ner = StanfordNERTagger('english.muc.7class.distsim.crf.ser.gz')
st_ner = StanfordNERTagger('english.all.3class.distsim.crf.ser.gz')


def sentence_tagger(sentence_list):
    named_entities = st_ner.tag_sents(sentence_list)
    return named_entities


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-s", "--sentence", default='Bill Gates is married to Melinda Gates.')
    args = parser.parse_args()
    sentence_lis = [args.sentence]
    sentence_list = [word_tokenize(sent) for sent in sentence_lis]
    print sentence_list
    named_tags = sentence_tagger(sentence_list)
    print named_tags