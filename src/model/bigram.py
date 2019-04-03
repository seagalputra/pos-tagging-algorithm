from collections import Counter

def get_bigram(dataset):
    """Fungsi untuk membuat bigram dari list.
    
    Input list berisi string yang nantinya digenerate bigram dan mengembalikan
    objek berupa dictionary python.
    
    Args:
        dataset: list satu dimensi.
        
    Return:
        dictionary yang memuat bigram dan banyaknya bigram pada list tersebut.
    """
    
    bigrams = []
    for i in range(len(dataset)-1):
        bigrams.append((dataset[i], dataset[i+1]))
    count_bigrams = Counter(bigrams)
    
    return bigrams, dict(count_bigrams)