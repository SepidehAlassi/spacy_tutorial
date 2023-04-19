import spacy
import os
from cairosvg import svg2png
from spacytextblob.spacytextblob import SpacyTextBlob
import pandas as pd
from svglib.svglib import svg2rlg
from reportlab.graphics import renderPM

nlp_en = spacy.load("en_core_web_sm")
nlp_en.add_pipe('spacytextblob')


def visualize_dependency(text, filename):
    """
    This is the solution to the exercise 1 of the session 11.
    The function gets a text to feed in the spaCy pipeline with English model for NLP processes.
    It retrieves the dependency graph of the text and stores it as SVG and PNG files.
    :param text: an English text
    :param filename: name of output files
    :return: writes the results in .svg and .png files
    """
    doc = nlp_en(text)
    svg = spacy.displacy.render(doc, style="dep")

    # svg2png(svg, write_to=filename+".png", background_color='white')
    with open(os.path.join(os.getcwd(), filename+".svg"), "w",  encoding="utf-8") as svg_file:
        svg_file.write(svg)
    drawing = svg2rlg(filename+".svg")
    renderPM.drawToFile(drawing, filename+".png", fmt="PNG")


def get_lemma(doc, filename):
    """
    This function performs text lemmatization
    :param doc: an spacy document object
    :param filename: name of the resulting .txt file
    :return: writes the lemmatized form of text in a .txt file
    """
    lemma_text = " ".join([token.lemma_ for token in doc])
    with open(filename+'_lemma.txt', "w") as lemma_file:
        lemma_file.write(lemma_text)


def classify_text(text, filename):
    """
    This function contains the solution to the exercise 2
     of the session 11
    :param text: a given text to be classified
    :param filename: the name of output files
    :return: write results in .txt and .html files
    """
    # Process whole documents
    doc = nlp_en(text)

    print("Noun phrases:", [chunk.text for chunk in doc.noun_chunks])
    print("sentences:", [sentence for sentence in doc.sents])

    # get lemmatized form and save it
    get_lemma(doc, filename)

    # Find named entities, phrases and concepts
    for entity in doc.ents:
        print(entity.text, entity.label_)

    html = spacy.displacy.render(doc, style="ent")
    with open(filename + ".html", "w", encoding="utf-8") as output_file:
        output_file.write(html)


def sentiment_analysis_text(text, model):
    """
    Retrieves results of the sentiment analysis on the given text using the specified model
    :param text: a text
    :param model: a pre-trained spaCy model for a language like English, German, etc.
    :return: the polarity and subjectivity scores
    """
    doc = model(text)
    return doc._.polarity, doc._.subjectivity


def analyze_sentiments_hotel_reviews(review_file):
    """
    Performs sentiment analyzes on the hotel reviews given in a CSV file.
    Creates a new DataFrame with additional sentiment analysis results.
    :param review_file: A CSV file containing hotel reviews
    :return: writes the results to an .xlsx file
    """
    review_dic = {'Review': [], 'Rating': [], 'Polarity': [], 'Subjectivity':[]}
    reviews_updated_df = pd.DataFrame(review_dic)
    reviews_df = pd.read_csv(review_file)
    for index, row in reviews_df.head(1000).iterrows():
        review = row['Review']
        rating = row['Rating']
        polarity, subjectivity = sentiment_analysis_text(review, nlp_en)
        reviews_updated_df.loc[index] = [review, rating, polarity, subjectivity]
    print('average subjectivity:', reviews_updated_df.Subjectivity.mean())
    negatives = reviews_updated_df.loc[reviews_updated_df["Polarity"] < -0.3]
    negatives_rows, negatives_cols = negatives.shape
    print('Number of Negatives:', negatives_rows)
    writer = pd.ExcelWriter('hotel_reviews.xlsx')
    reviews_updated_df.to_excel(writer)
    writer.save()


def main():
    visualize_dependency(text="When you dive into the sea, you are diving into the origin of us all.",
                         filename='dependency')

    thurn_interview = 'When Sebastian Thrun started working on self-driving cars at ' \
                      'Google in 2007, few people outside of the company took him ' \
                      'seriously. "I can tell you many senior CEOs of major American ' \
                      'car companies would shake my hand and turn away because I was ' \
                      'not worth talking to," said Sebastian Thrun, in an interview with' \
                      ' Times earlier this week.'

    classify_text(text=thurn_interview, filename="thurn_interview")
    analyze_sentiments_hotel_reviews(review_file=os.path.join('data', 'tripadvisor_hotel_reviews.csv'))


if __name__ == '__main__':
    main()

