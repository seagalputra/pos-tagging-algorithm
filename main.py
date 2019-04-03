from src.model import *
from src.utils import *

def main():
    filename = 'data/corpus.tsv'
    sentences, tags = load_data(filename)

    # mengambil 1020 data awal
    data_train, data_test, tags_train, tags_test = sentences[:1000], sentences[1000:1020], tags[:1000], tags[1000:1020]

    data_train = list(flatten(data_train))
    tags_train = list(flatten(tags_train))

    hidden_table = get_emission_table(data_train, tags_train)
    
    # menggunakan baseline model untuk memprediksi suatu tag pada kalimat
    predict = []
    for sentence in data_test:
        predict_tags = predict_common_tag(sentence, hidden_table)
        predict.append(predict_tags)

    flatten_tags_test = list(flatten(tags_test))
    flatten_predict = list(flatten(predict))

    accuracy = get_accuracy_baseline(flatten_predict, flatten_tags_test)
    print("Akurasi model baseline:",accuracy)

if __name__ == "__main__":
    main()