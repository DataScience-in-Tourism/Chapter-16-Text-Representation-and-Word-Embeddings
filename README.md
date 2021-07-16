# Chapter 16: Text Representation and Word Embeddings
## http://www.datascience-in-tourism.com/

***Author***
Roman Egger - Salzburg University of Applied Sciences, Innovation and Management in Tourism

![text.png](https://github.com/DataScience-in-Tourism/Chapter-16-Text-Representation-and-Word-Embeddings/blob/main/text.png)

### Abstract

Today, a vast amount of unstructured text data is consistently at our disposal. Owing to the rapid increase in user-generated content on the one hand and powerful, ready-to-use machine learning algorithms on the other hand, automated text analysis can now be carried out in a way that would have been unimaginable a few years ago. However, in order to be able to analyze textual data further, it first becomes necessary to extract features and transform the text into numerical values which is required by many algorithms. As such, this chapter will present the basics of vectorizing text, beginning with the most simple approaches of text representation and increasing in complexity and performance as each subsequent algorithm is presented. The aim of this chapter is, thus, to convey the intuition behind each approach in a straightforward manner and to focus on the elements that are relevant for practical application.

-----------------------

In this Jupyter Notebooks, we will show how to vectorize your text-data using: 
* Latent Dirichlet Allocation (LDA)
* None- Negative Matrix Factorizaton (NMF) 
* Correlation Expanation CorEX
* Top2Vec
* BERTopic

The dataset we will use to extract topics from was crawled by the author and contains 2890 descriptions of airbnb-Experiences from the following European cities: Amsterdam, Athens, Berlin, Brussels, Copenhagen, Helsinki, London, Madrid, Oslo, Paris, Prague, Rome, Stockholm, Viwenna and Warsaw.

### Environment Setup

This notebooks were created using `Python 3.6`.  To set-up your local environment run in terminal the commands below:

```bash
# Clone the repository.

# (Windows Optional) Create a new Python environment and activate it.
python -m venv .env
.env\Scripts\activate

# (Ubuntu Optional) Create a new Python environment and activate it.
python3 -m venv .env
source .env/bin/activate

# Install the dependencies.
pip install -r requirements.txt

# install the dependencies according the requirements_pinned.txt if you want to us the same library versions

# Use your preferred IDE in order to run the notebooks
```
[See my LinkedIn Profile](https://www.linkedin.com/in/prof-dr-roman-egger-b645601/)
