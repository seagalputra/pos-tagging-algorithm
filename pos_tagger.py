from src.method import *
from src.utils import *

from nltk import word_tokenize
import argparse

def main():
    filename = 'data/corpus.tsv'
    sentences, tags = load_data(filename)

    # mengambil 1020 data awal
    data_train, data_test, tags_train, tags_test = sentences[:1000], sentences[1000:1020], tags[:1000], tags[1000:1020]

    data_train = list(flatten(data_train))
    tags_train = list(flatten(tags_train))

    hidden_table = get_emission_table(data_train, tags_train)
    
    # menggunakan argparse untuk melakukan parsing command terminal
    parser = argparse.ArgumentParser()
    parser.add_argument("kalimat", help="Kalimat yang akan diberi tagging.")
    parser.add_argument("-B", "--baseline", help="Model baseline yang digunakan untuk memprediksi tag", action="store_true")
    parser.add_argument("-V", "--viterbi", help="Model viterbi yang digunakan untuk memprediksi tag", action="store_true")
    args = parser.parse_args()
    
    if args.baseline:
        sentence = word_tokenize(args.kalimat)
        predict_tags = predict_common_tag(sentence, hidden_table)
        print("Kalimat:", args.kalimat)
        print("Tags:", predict_tags)

    if args.viterbi:
        print("Kalimat:", args.kalimat)

if __name__ == "__main__":
    main()