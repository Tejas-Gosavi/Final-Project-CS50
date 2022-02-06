# News classifier web app
Hello, My name is **Tejas Gosavi**.

This is my **CS50: Introduction to Computer Science** final project.

This is a NLP(Natural language processing) - based web app which classifies news.

We give news title/description as input and as a output it classifies news in certain category.

Dataset used for this project is bbc news headlines dataset which i downloaded from **kaggle**.

Algorithm used to predict category is **Multinomial Naive Bayes**, which is
very much famous/used for text classification. It is based on **Bayes Theorem**.

## Prerequisites
You must have these Tool installed.
 - Python
 - Node.js
 - Jupyter notebook
 - Visual studio code

## Project Structure
1. /backend - This dir. contains code related to server.

2. /frontend - This dir. contains code related to UI.

## Running the project
You need to install all dependencies related to project.
 - Backend - Refer to this [link](./backend/README.md).
 - Frontend - Refer to this [link](./frontend/README.md).

After installing all dependencies follow these steps. 
1. Open CMD goto /backend dir. of this project and run following command.
      
    ```
    flask run
    ```
    By default, flask will run on port 5000.

2. Open CMD goto /frontend dir. of this project and run following command.
	```
	npm run serve
	```
	By default, Vue.js will run on port 8080.

3. Navigate to URL http://127.0.0.1:8080

4. and... Voila our web app is started.
