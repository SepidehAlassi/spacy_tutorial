import spacy
import os
from cairosvg import svg2png

from spacy.lang.xx import MultiLanguage

nlp_en = spacy.load("en_core_web_sm")

def dependency_visualization(text):
        tokenized_text = nlp_en(text)
        svg = spacy.displacy.render(tokenized_text, style = "dep")
        # svg2png(svg, write_to="sen_dep.png", background_color='white')
        with open(os.path.join(os.getcwd(), "sen_dep.svg"), "w",  encoding="utf-8") as file:
            file.write(svg)


def tokenization(sentence):
    words = nlp_en(sentence)
    for word in words:
        print(word.text)



def multi_linguagl():
    nlp = MultiLanguage()
    # With lazy-loading
    nlp_mixed = spacy.blank("xx")
    nlp_mixed

if __name__ == '__main__':
    test_sentence = "Open your eyes, see that everything is connected to everything else!"
    # tokenization(test_sentence)
    # dependency_visualization(test_sentence)


    # sentiment_analysis()
    # multi_linguagl()


