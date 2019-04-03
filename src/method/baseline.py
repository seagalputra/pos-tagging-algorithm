import operator

def predict_common_tag(data, emmision_table):
    """Fungsi untuk memprediksi suatu tag dengan pendekatan baseline.
    
    Pendekatan baseline memungkinkan prediksi suatu tag dengan menghitung kemunculan suatu tag
    dalam corpus.
    
    Args:
        data: list berisi kata yang akan diprediksi.
        emmision_table: dictionary berisi tabel emisi
    
    Return:
        prediksi tags dari list data input
    """
    
    # dengan menggunakan hidden table untuk membangun baseline model berdasarkan corpus
    predict_tags = []
    for word in data:
        if word not in emmision_table.keys():
            predict_tags.append('NN')
        else:
            most_common_tag = max(emmision_table[word].items(), key=operator.itemgetter(1))[0]
            predict_tags.append(most_common_tag)
    
    return predict_tags

def get_accuracy_baseline(predict_list, test_list):
    """Fungsi untuk menghitung akurasi dari model baseline
    
    Hasil prediksi dari model baseline dibandingkan dengan data test yang berisi 
    tags sesungguhnya.
    
    Args:
        predict_list: list dari prediksi menggunakan baseline
        test_list: list berisi tags yang digunakan untuk validasi model
    
    Return:
        Mengembalikan nilai akurasi dari model yang dibangun
    
    """
    
    count = 0
    for i in range(len(predict_list)):
        if (predict_list[i] == test_list[i]):
            count += 1
    
    accuracy = count / len(test_list)
    return accuracy