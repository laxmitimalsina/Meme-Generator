# Motivational Meme Generator 
## Introduction ![meme_generator_demo](https://user-images.githubusercontent.com/65842436/114586160-a7d06280-9c84-11eb-85a8-d9bfed9b214b.gif)


## Meme Generator overview
The goal of Meme Generator is to build a "meme generator" application, to generate memes dynamically that includes an image with a quote. It handles the quotes from different file formats.

Meme Generator has the following functionalities:
* Interacts with a variety of filetypes
* Loads quotes from a variety of filetypes(CSVs, PDF, Word Documents)
* Loads, manipulates, and saves images
* Has two user input interface- web service and command-line tool

## How to run the program 
The program can run in two ways. Before we run the program we need to create a virtual environment.
* Navigate the root directory and create a virtual environment.--$ python3 -m venv name
* Source activate the virtual environment --$ source env/bin/activate
* Install all the dependencies from the requirements.txt --$ pip install -r requirements.txt
  
 ## Run from the command line 
 meme.py has codes to run the application from the command line. It takes three optional arguments:
  --path: Path to the image file
  --body: Quote body to add to the image
  --author: Quote author to add to the image

## Run flask app
 * From root directory src run flask with the command $python app.py
 * "Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)" will be displayed on the terminal, use any browser to run the address.
 * Use the Random button to get meme automatically or Use the Creator button to make a meme on your own. Fill the form with the image URL, quote, and author.

## Project Modules 
 * Project has 2 modules 
 * QuoteEngine -Loads quotes from variety of filetypes(CSVs, PDF, Word Documents)
 * MemeGenerator-Has files to handel image captioning.

 Each class and function has a docstring with details on arguments and return.    


  









