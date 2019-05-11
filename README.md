# Wine Quality Prediction

Our source dataset contains red and white wine samples of Portugese "Vinho Verde" wine. Each sample contains 12 attributes derived from physicochemical tests. Using Python's scikit-learn machine learning library, we ran multiple classification, regression and clustering algorithms to predict quality of the wine. 

You can read more about the datasets [here](http://archive.ics.uci.edu/ml/datasets/Wine+Quality)

## Repository Structure
* **data** - this folder contains dataset files. The _clean_data are the final files after applying feature selection and outlier detection techniques. 
* **model** - this folder contains optimized machine learning models
* **static**
    1. **css** - contains stylesheet information
    2. **images** - contains images from jupyter notebook
    3. **js** - contains javascript files to display plotly visualization
* **templates** - this folder contains html pages for landing page and results page
* **.ipynb files** are Jupyter notebooks used to implement machine learning
* **script.py** file contains flask app

## Running the app locally

Download all files from this repository except archives to you local machine. Review requirements.txt file and make sure you have all the necessary python packages installed on your computer. 
From gitbash, run below command: 
```
FLASK_APP=script/app.py flask run
```
From your web browser, navigate to (http://localhost:5000/) to launch the app. 

## Heroku app

[Heroku link](https://thawing-wildwood-93546.herokuapp.com/)

## Citations

* **P. Cortez, A. Cerdeira, F. Almeida, T. Matos and J. Reis**. 
*Modeling wine preferences by data mining from physicochemical properties. In Decision Support Systems, Elsevier, 47(4):547-553, 2009.* - [ReadMore](http://www3.dsi.uminho.pt/pcortez/wine/)