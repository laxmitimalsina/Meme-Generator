import random
from os import listdir
from os.path import isfile, join
import requests
from flask import Flask, render_template, request
from Ingestor import Ingestor
from MemeGenerator import ImageCaptioner as MemeEngine
import os

app = Flask(__name__)

meme = MemeEngine("./static")


def setup():
    """ Load all resources """
    output_quotes = []
    quote_files = [
        "./_data/DogQuotes/DogQuotesTXT.txt",
        "./_data/DogQuotes/DogQuotesDOCX.docx",
        "./_data/DogQuotes/DogQuotesPDF.pdf",
        "./_data/DogQuotes/DogQuotesCSV.csv",
    ]
    for file in quote_files:
        quotes = Ingestor.parse(file)
        output_quotes.extend(quotes)
    images_path = "./_data/photos/dog/"
    imgs = [
        join(images_path, img)
        for img in listdir(images_path)
        if isfile(join(images_path, img))
    ]
    return output_quotes, imgs


quotes, imgs = setup()
print(quotes, imgs)


@app.route("/")
def meme_rand():
    """ Generate a random meme """
    img = random.choice(imgs)
    quote = random.choice(quotes)
    print("generating random meme from meme_rand", img, quote)
    path = meme.make_meme(img, quote.body, quote.author)
    return render_template("meme.html", path=path)


@app.route("/create", methods=["GET"])
def meme_form():
    """ User input for meme information """
    return render_template("meme_form.html")


@app.route("/create", methods=["POST"])
def meme_post():
    """ Create a user defined meme """
    image_url = request.form["image_url"]
    body = request.form["body"]
    author = request.form["author"]
    r = requests.get(image_url, allow_redirects=True)
    tmp = f"./static/input.png"
    open(tmp, "wb").write(r.content)
    path = meme.make_meme(tmp, body, author)
    os.remove("./static/input.png")

    return render_template("meme.html", path=path)


if __name__ == "__main__":
    app.run(debug=True)
