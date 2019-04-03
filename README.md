# POS (Part-Of-Speech) Tagging Algorithm

This software is for tagging a word using several algorithm. This program use two algorithm (Baseline and HMM-Viterbi).
A POS (Part-Of-Speech) tagging is a software that reads text in some language and assigns parts of speech to each word (and other token), such as noun, verb, adjective, etc.

This POS tagging software use Indonesian corpus for training data. But, it can use other language corpus too. Just add training data with words and tags on it.

# Issues

If you are dealing with issue, please refer to [issues](https://github.com/seagalputra/pos-tagging-algorithm/issues) tab to discuss with us.

# Requirements

- Python 3.7
- nltk

# How to Execute

```bash
python pos_tagger.py [sentence] [method]
```
```
Args:
  [sentences] : string of sentences to predict the tags
  [method] : method for predicting the tags
    -B, --baseline : predict using baseline method
    -V, --viterbi : predict using viterbi method
```
