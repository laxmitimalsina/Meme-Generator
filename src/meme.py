import os
import random
import argparse
import typing
from Ingestor import Ingestor
from MemeGenerator import ImageCaptioner as MemeEngine
from QuoteEngine.Quote import QuoteModel


def generate_meme(path=None, body=None, author=None):
    """ Generate a meme given an path and a quote """
    img = None
    quote = None

    if path is None:
        images = "./_data/photos/dog/"
        imgs = []
        for root, dirs, files in os.walk(images):
            imgs = [os.path.join(root, name) for name in files]

        img = random.choice(imgs)
    else:
        img = path[0]

    if body is None:
        quote_files = [
            "./_data/DogQuotes/DogQuotesTXT.txt",
            "./_data/DogQuotes/DogQuotesDOCX.docx",
            "./_data/DogQuotes/DogQuotesPDF.pdf",
            "./_data/DogQuotes/DogQuotesCSV.csv",
        ]
        quotes = []
        for f in quote_files:
            quotes.extend(Ingestor.parse(f))

        quote = random.choice(quotes)
    else:
        if author is None:
            raise Exception("Author Required if Body is Used")
        quote = QuoteModel(body, author)

    meme = MemeEngine("./tmp")
    path = meme.make_meme(img, quote.body, quote.author)
    return path


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Welcome to meme generator")
    parser.add_argument("--path", type=str)
    parser.add_argument("--body", type=str)
    parser.add_argument("--author", type=str)
    args = parser.parse_args()
    path = args.path
    body = args.body
    author = args.author
    print(generate_meme(path, body, author))
