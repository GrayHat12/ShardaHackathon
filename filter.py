import pandas as pd
from nltk.tokenize import sent_tokenize


def filt(data=""):
    sentences = sent_tokenize(data)

    new_sentences = pd.Series(sentences).str.replace("[^a-zA-Z\d]", " ")

    new_sentences = [i.lower() for i in new_sentences]

    l = [i.split() for i in new_sentences]

    common_words = ["a", "about", "above", "after", "again", "against", "all", "am", "an", "and", "any", "are", "as",
                    "at", "be", "because", "been", "before", "being", "below", "between", "both", "but", "by", "could",
                    "did", "do", "does", "doing", "down", "during", "each", "few", "for", "further", "had", "has",
                    "have", "having", "he", "he'd", "he'll", "he's", "her", "here", "here's", "hers", "herself", "him",
                    "himself", "his", "how", "how's", "i", "i'd", "i'll", "i'm", "i've", "if", "in", "into", "is", "it",
                    "it's", "its", "itself", "let's", "me", "more", "most", "my", "myself", "nor", "of", "once", "only",
                    "or", "other", "ought", "our", "ours", "ourselves", "out", "over", "own", "same", "she", "she'd",
                    "she'll", "she's", "should", "so", "some", "such", "than", "that", "that's", "the", "their",
                    "theirs", "them", "themselves", "then", "there", "there's", "these", "they", "they'd", "they'll",
                    "they're", "they've", "this", "those", "through", "too", "under", "until", "up", "very", "was",
                    "we", "we'd", "we'll", "we're", "we've", "were", "what", "what's", "when", "when's", "where",
                    "where's", "which", "while", "who", "who's", "whom", "why", "why's", "with", "would", "you",
                    "you'd", "you'll", "you're", "you've", "your", "yours", "yourself", "yourselves"]

    new_sentences = [[j for j in i if j not in common_words] for i in l]

    return new_sentences

#print(filt('Hello Book me a ticket to goa . And tell me'))