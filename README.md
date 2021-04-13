# Motivational Meme Generator 
## Introduction ![meme_generator_demo](https://user-images.githubusercontent.com/65842436/114586160-a7d06280-9c84-11eb-85a8-d9bfed9b214b.gif)


## Meme Generator overview
Goal of Meme Generator is to build a "meme generator" application, to generate memes dynamically that includes image with an quote. It handel the quotes from different file formats.

Meme Generator has following functionalities:
 -Interacts with variety of filetypes
 -Loads quotes from variety of filetypes(CSVs, PDF, Word Documents)
 -Loads, manipulates and saves images
 -Has two user input interface- web service and command-line tool


 ## How to run the program 
 The program can run in two ways.Before we run program we need to create virtual enviroment.
  -Navigate the root directory and create a virtual enviroment.($ python3 -m venv name)
  -Source activate the virtual enviroment ($ source env/bin/activate)
  -Install all the dependencies from the requirements.txt ($ pip install -r requirements.txt)
  
  ## Run from command line 
  meme.py has codes to run the application from command line.It take three optional arguments:
   --path:Path to the image file
   --body:Quote body to add to the image
   --author:Quote author to add to the image

 ## Run flask app
  -From root directory src run flask with command $python app.py
  -"Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)" will be displayed on the terminal,use any browser to run the address.
  -Use Random botton get meme automaticatlly or Use Creator button to make meme on your own.Fill the form with image url,quote and author.

## Project Modules 
 - Project has 2 modules 
  -QuoteEngine -Loads quotes from variety of filetypes(CSVs, PDF, Word Documents)
  -MemeGenerator-Has files to handel image captioning.

  Each class and function has docstring with details on arguments and return.  


  









