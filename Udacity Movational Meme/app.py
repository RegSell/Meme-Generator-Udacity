"""App function."""
import random
import os
import requests
from flask import Flask, render_template, abort, request
from MemeGenerator import MemeEngine
from QuoteEngine import Ingestor

app = Flask(__name__)

meme = MemeEngine('./static')


def setup():
    """Load all resources."""
    quotes = []

    quote_files = ['./_data/DogQuotes/DogQuotesTXT.txt',
                   './_data/DogQuotes/DogQuotesDOCX.docx',
                   './_data/DogQuotes/DogQuotesPDF.pdf',
                   './_data/DogQuotes/DogQuotesCSV.csv']

    for f in quote_files:
        try:
            quotes.extend(Ingestor.parse(f))
        except ValueError as error:
            print(f"ValueError: {error}")

    images_path = "./_data/photos/dog/"

    imgs = []
    for root, dirs, files in os.walk(images_path):
        imgs = [os.path.join(root, name) for name in files]

    return quotes, imgs


quotes, imgs = setup()


@app.route('/')
def meme_rand():
    """Generate a random meme."""
    img = None
    quote = None

    img = random.choice(imgs)
    quote = random.choice(quotes)

    path = meme.make_meme(img, quote.body, quote.author)
    return render_template('meme.html', path=path)


@app.route('/create', methods=['GET'])
def meme_form():
    """User input for meme information."""
    return render_template('meme_form.html')


@app.route('/create', methods=['POST'])
def meme_post():
    """Create a user defined meme."""
    image_url = request.form['image_url']
    body = request.form['body']
    author = request.form['author']

    try:
        r = requests.get(image_url, allow_redirects=True)
        tmp = f'./tmp({random.randint(0,100000000)}.jpg'
        with open(tmp, 'wb') as img:
            img.write(r.content)
        path = meme.make_meme(tmp, body, author)
        return render_template('meme.html', path=path)
    except Exception:
        print('Invalid URL, please enter valid image URL')
        return render_template('meme_error.html')


if __name__ == "__main__":
    app.run()
