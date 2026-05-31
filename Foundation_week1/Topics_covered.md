# Foundation Week 1: Algorithm Insights

**Author:** Abhinav Kanduri  
**GitHub:** @Abhinav-kanduri  
**LinkedIn:** https://www.linkedin.com/in/abhinav-kanduri-a943b9353/  
**Purpose:** Knowledge transfer only.

## Course Navigation

- [Course home](../README.md)
- [Foundation Week 1 dashboard](README.md)
- [Machine Learning algorithms](Machine_Learning_Algorithms.md)
- [Natural Language Processing techniques](Natural_Language_Processing_Techniques.md)
- [Deep Learning algorithms](Deep_Learning_Algorithms.md)
- [Transformer architecture](Transformer_Architecture_End_to_End.md)
- [Transformer model families](Transformer_Model_Families.md)

This file summarizes the topics covered in **Algorithm Insights: A Problem-First Guide**.

The main idea is:

> Do not start by asking, "Which algorithm should I use?"
>
> Start by asking, "What problem am I solving?"

Once the problem type is clear, choosing the right algorithm becomes much easier.

## Contents

- Core idea
- Machine learning algorithms
- Natural language processing techniques
- Deep learning architectures
- Why transformers are important
- Problem-to-algorithm guide
- Banking case study
- Simple interview rule

## Core Idea

Every algorithm is designed for a specific kind of problem.

A good workflow is:

1. Name the problem.
2. Match it to the correct algorithm family.
3. Choose the best algorithm based on the data and business need.

Common problem families:

- Regression: predict a number.
- Classification: predict a category.
- Clustering: group similar items without labels.
- Anomaly detection: find unusual patterns.
- Natural language processing: understand human language.
- Deep learning: learn complex patterns from images, speech, text, and sequences.
- Generative AI: create new text, images, code, or other content.

## Machine Learning Algorithms

Machine learning is used for prediction, classification, grouping, feature reduction, pattern discovery, and anomaly detection.

### Prediction and Boosting

- **Linear Regression**
  - Solves: Predicting a continuous number.
  - Used for: House prices, sales forecasting, revenue prediction.

- **Logistic Regression**
  - Solves: Predicting yes/no outcomes.
  - Used for: Fraud detection, churn prediction, loan approval.

- **Decision Tree**
  - Solves: Rule-based decision-making.
  - Used for: Segmentation, claim approval, risk decisions.

- **Random Forest**
  - Solves: Improving accuracy and reducing overfitting.
  - Used for: Credit scoring, fraud detection, medical prediction.

- **Gradient Boosting**
  - Solves: Correcting mistakes from earlier models.
  - Used for: Pricing, ranking, risk prediction.

- **XGBoost**
  - Solves: High-accuracy modeling on structured data.
  - Used for: Finance risk, fraud detection, machine learning competitions.

- **LightGBM**
  - Solves: Fast modeling on large structured datasets.
  - Used for: Large datasets and recommendation systems.

- **CatBoost**
  - Solves: Modeling data with many categorical features.
  - Used for: Merchant prediction and retail offers.

### Classification, Clustering, and Detection

- **Support Vector Machine**
  - Solves: Classification with clear boundaries.
  - Used for: Text classification and image classification.

- **K-Nearest Neighbors**
  - Solves: Similarity-based prediction.
  - Used for: Recommendations and user similarity.

- **Naive Bayes**
  - Solves: Fast text classification.
  - Used for: Spam detection and sentiment analysis.

- **K-Means Clustering**
  - Solves: Grouping data without labels.
  - Used for: Customer segmentation and merchant segmentation.

- **Hierarchical Clustering**
  - Solves: Discovering groups with hierarchy.
  - Used for: Market segmentation and document grouping.

- **Principal Component Analysis**
  - Solves: Reducing too many features.
  - Used for: Visualization and feature reduction.

- **Isolation Forest**
  - Solves: Detecting unusual data points.
  - Used for: Fraud detection and unusual transactions.

- **Association Rule Mining**
  - Solves: Discovering relationships between products.
  - Used for: Market basket analysis.

## Natural Language Processing

Natural Language Processing, or NLP, helps machines understand and work with human language.

It is used for documents, emails, reviews, chats, transcripts, search queries, and customer feedback.

### Text Cleaning and Representation

- **Tokenization**
  - Breaks text into smaller pieces.
  - Used in LLMs, search engines, and chatbots.

- **Stopword Removal**
  - Removes common low-value words.
  - Used in basic text cleaning.

- **Stemming**
  - Reduces words to rough root forms.
  - Used in search engines.

- **Lemmatization**
  - Converts words to proper base forms.
  - Used in document search and text analytics.

- **Bag of Words**
  - Converts text into word counts.
  - Used in basic text classification.

- **TF-IDF**
  - Finds important words in a document.
  - Used in search ranking and document matching.

- **Word2Vec**
  - Represents word meaning as vectors.
  - Used for semantic similarity and recommendations.

- **GloVe**
  - Creates meaning-based word vectors.
  - Used for text similarity and text understanding.

- **FastText**
  - Handles rare words and misspellings.
  - Used in multilingual text processing.

### Understanding and Generation

- **Named Entity Recognition**
  - Extracts names, dates, locations, amounts, and other entities.
  - Used in information extraction.

- **Part-of-Speech Tagging**
  - Identifies grammar roles such as noun, verb, and adjective.
  - Used in language analysis.

- **Sentiment Analysis**
  - Detects emotion or opinion.
  - Used for reviews and customer feedback.

- **Topic Modeling**
  - Finds hidden topics in documents.
  - Used for news grouping and ticket clustering.

- **Text Classification**
  - Assigns a category to text.
  - Used for ticket routing and spam detection.

- **Text Summarization**
  - Converts long text into a shorter summary.
  - Used for legal, medical, and research documents.

- **Semantic Search**
  - Searches by meaning instead of exact keywords.
  - Used in RAG and enterprise search.

- **Question Answering**
  - Finds or generates answers from text.
  - Used in chatbots and document assistants.

## Deep Learning Architectures

Deep learning is useful for complex patterns in images, speech, language, time series, and generative AI.

- **Artificial Neural Network**
  - Learns complex non-linear patterns.
  - Used for classification, prediction, and scoring.

- **Convolutional Neural Network**
  - Understands images.
  - Used for image classification and object detection.

- **Recurrent Neural Network**
  - Works with sequence data.
  - Used for time series, text, and speech.

- **Long Short-Term Memory**
  - Remembers long sequence patterns.
  - Used for forecasting, speech, and language.

- **Gated Recurrent Unit**
  - Handles sequences with faster training.
  - Used for chatbots and time series.

- **Autoencoder**
  - Compresses data and detects anomalies.
  - Used for fraud detection, noise removal, and feature learning.

- **Generative Adversarial Network**
  - Generates synthetic data.
  - Used for image generation and data augmentation.

- **Transformer**
  - Understands and generates long-context content.
  - Used for LLMs, translation, and summarization.

- **BERT-style Model**
  - Performs deep text understanding.
  - Used for search, classification, and question answering.

- **GPT-style Model**
  - Generates text one token at a time.
  - Used for chatbots, content generation, and code generation.

- **Vision Transformer**
  - Uses attention for image understanding.
  - Used for image classification and document understanding.

- **Diffusion Model**
  - Generates high-quality images.
  - Used for image generation and design tools.

## Why Transformers Matter

Transformers changed modern AI because they can look at the full sequence at once instead of reading one word at a time.

Important ideas:

- **Self-attention:** Each word can decide how much every other word matters for context.
- **Parallel reading:** Long passages can be processed more efficiently.
- **Long context:** Meaning can be carried across larger documents.

Transformers power:

- Large language models
- Translation systems
- Summarization tools
- Semantic search
- Chatbots
- BERT-style models
- GPT-style models

## Problem-to-Algorithm Guide

Use this guide when choosing an algorithm.

- **Predict a number**
  - Use Linear Regression, Random Forest, or Gradient Boosting.

- **Predict yes/no**
  - Use Logistic Regression, Decision Tree, Random Forest, or XGBoost.

- **Classify many categories**
  - Use Logistic Regression, SVM, Random Forest, or Neural Network.

- **Group similar customers**
  - Use K-Means or Hierarchical Clustering.

- **Detect fraud or anomalies**
  - Use Isolation Forest, Autoencoder, Random Forest, or Gradient Boosting.

- **Recommend products**
  - Use KNN, Matrix Factorization, Deep Learning, or Embeddings.

- **Understand text**
  - Use TF-IDF, Word Embeddings, or Transformer.

- **Classify text**
  - Use Naive Bayes, SVM, or BERT.

- **Summarize documents**
  - Use Transformer or Large Language Models.

- **Build a chatbot**
  - Use Transformer, GPT-style Model, or RAG.

- **Understand images**
  - Use CNN or Vision Transformer.

- **Generate images**
  - Use GAN or Diffusion Model.

- **Forecast future values**
  - Use Linear Regression, Random Forest, LSTM, or Transformer.

## Case Study: One Bank, Five Problems

A single bank may need different algorithms for different business questions.

- **Question:** Will this customer default on a loan?
  - Problem type: Classification.
  - Algorithms: Logistic Regression, Random Forest, XGBoost.

- **Question:** How much loan can they safely get?
  - Problem type: Number prediction.
  - Algorithms: Linear Regression, Gradient Boosting.

- **Question:** Which customers behave similarly?
  - Problem type: Grouping.
  - Algorithms: K-Means, Hierarchical Clustering.

- **Question:** Is this transaction suspicious?
  - Problem type: Anomaly detection.
  - Algorithms: Isolation Forest, Autoencoder, Random Forest.

- **Question:** What is the customer saying?
  - Problem type: Text understanding.
  - Algorithms: Named Entity Recognition, Sentiment Analysis, Transformer.

## Simple Rule to Remember

- Regression means number prediction.
- Classification means category prediction.
- Clustering means grouping without labels.
- Anomaly detection means finding unusual patterns.
- NLP means text understanding.
- Deep learning means complex data learning and generation.
- Transformers mean context understanding and content generation.

## Interview-Friendly Answer

When explaining your algorithm choice, say:

> I chose this algorithm because the business problem is a regression, classification, clustering, anomaly detection, text understanding, or generation problem.

The strongest answer starts with the business problem and then connects it to the correct algorithm family.
