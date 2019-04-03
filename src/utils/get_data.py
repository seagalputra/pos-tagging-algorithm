from itertools import chain

def load_data(filename):
    """Fungsi untuk melakukan load data pada file .tsv maupun .txt

    File yang digunakan yaitu file .tsv maupun file yang mampu dibuka
    menggunakan teks editor. Dalam file tersebut terdapat tag pembuka <kalimat>
    dan diakhiri tag penutup </kalimat> yang berfungsi sebagai penanda bahwa
    entitas tersebut termasuk ke dalam satu kalimat.

    Args:
        filename: string dari nama file yang akan diload datanya.

    Return:
        list dari kata-kata dan tags dengan index yang menunjukkan posisi kalimat tersebut.
    """

    # Load data dan buka sebagai file
    sentences = []
    tags = []
    with open(filename) as file:
        contents = file.readlines()

    # Hapus karakter \n yang tidak dibutuhkan
    contents = [content.strip() for content in contents]
    idx = 0
    while idx < len(contents):
        word = []
        tag = []
        # looping sampai menemukan pattern dengan awalan </kalimat
        while not contents[idx].startswith('</kalimat'):
            # kondisi jika menemukan sebuah data yang tidak memiliki awalan <kalimat
            if not contents[idx].startswith('<kalimat'):
                temp_word, temp_tag = contents[idx].split("\t")
                word.append(temp_word.lower())
                tag.append(temp_tag)
            idx += 1
        sentences.append(word)
        tags.append(tag)
        idx += 2

    return sentences, tags

def flatten(multi_list):
    """Mengembalikan list multi dimensi ke dalam list satu dimensi.

    Input list yang masuk di proses menggunakan method from_iterable dari
    package itertools dan mengembalikan object berupa generator yang iterable.

    Args:
        multi_list: list multi dimensi.

    Return:
        list satu dimensi yang nantinya digunakan untuk pemrosesan lebih lanjut.
    """

    return chain.from_iterable(multi_list)