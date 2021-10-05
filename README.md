# Chapter 16: Text Representation and Word Embeddings

## Vectorizing textual data
## http://www.datascience-in-tourism.com/

***Roman Egger***
* Salzburg University of Applied Sciences, Innovation and Management in Tourism

![text.png](https://github.com/DataScience-in-Tourism/Chapter-16-Text-Representation-and-Word-Embeddings/blob/main/text.png)

### Abstract

Today, a vast amount of unstructured text data is consistently at our disposal. Owing to the rapid increase in user-generated content on the one hand and powerful, ready-to-use machine learning algorithms on the other hand, automated text analysis can now be carried out in a way that would have been unimaginable a few years ago. However, in order to be able to analyze textual data further, it first becomes necessary to extract features and transform the text into numerical values which is required by many algorithms. As such, this chapter will present the basics of vectorizing text, beginning with the most simple approaches of text representation and increasing in complexity and performance as each subsequent algorithm is presented. The aim of this chapter is, thus, to convey the intuition behind each approach in a straightforward manner and to focus on the elements that are relevant for practical application.

-----------------------

In this Jupyter Notebook, we will use a number of techniques to create word vectors. We start with One Hot Encoding and Bag of Words, will apply TF-IDF and move on to more complex and powerful techniques like Word2Vec, Fasttext, GloVe, ELMO and BERT

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

# Install dependencies with my versions
pip install -r requirements_pinned.txt

# install the dependencies according the requirements_pinned.txt if you want to us the same library versions

# Use your preferred IDE in order to run the notebooks
```
[See my LinkedIn Profile](https://www.linkedin.com/in/prof-dr-roman-egger-b645601/)
