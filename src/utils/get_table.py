def get_emission_table(words, tags):
    """Membuat tabel emisi dari input kata dan tags.
    
    Fungsi untuk mengembalikan sebuah tabel dari kata dan kemunculan tags terhadap kata tersebut.
    
    Args:
        words: list kata.
        tags: list tags.
    
    Return:
        dictionary yang merepresntasikan tabel emisi.
    """
    
    # Membuat representasi tabel emission probability dari HMM
    hidden_state = {}
    for word in words:
        # Jika word belum pernah ditemui maka akan digenerate
        # tagset berserta probabilitasnya
        if word not in hidden_state.keys():
            word_tags = []
            for idx, wrd in enumerate(words):
                if wrd == word :
                    word_tags.append(tags[idx])
            # Membuat dictionary berisi semua tagset dari sebuah word
            # pada korpus. Berserta jumlah kemunculan setiap tagsetnya
            tag_count = {}
            for tag in word_tags:
                if tag not in tag_count.keys():
                    tag_count[tag] = 1
                else:
                    tag_count[tag] += 1
            total = 0
            # Mengubah jumlah kemunculan menjadi probabilitas
            tag_prob = {}
            for count in tag_count.values():
                total += count
            for tagset in tag_count.keys():
                tag_prob[tagset] = tag_count[tagset]/total
            hidden_state[word] = tag_prob
        else:
            # Jika word sudah pernah ditemui maka akan dilewati
            continue
    return(hidden_state)