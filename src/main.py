from model import get_bigram
from utils import load_data
from utils import flatten

def main():
    filename = 'data/corpus.tsv'
    sentences, tags = load_data(filename)

    # mengambil 1020 data awal
    data_train, data_test, tags_train, tags_test = sentences[:1000], sentences[1000:1020], tags[:1000], tags[1000:1020]

    tags_train = list(flatten(tags_train))
    bigrams, count_bigrams = get_bigram(tags_train)
    print(count_bigrams)

if __name__ == "__main__":
    main()