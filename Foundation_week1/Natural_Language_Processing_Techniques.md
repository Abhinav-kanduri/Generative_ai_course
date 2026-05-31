# Natural Language Processing Techniques and Algorithms

**Author:** Abhinav Kanduri  
**GitHub:** @Abhinav-kanduri  
**LinkedIn:** https://www.linkedin.com/in/abhinav-kanduri-a943b9353/  
**Purpose:** Knowledge transfer only.

## Course Navigation

- [Course home](../README.md)
- [Foundation Week 1 dashboard](README.md)
- [Foundation Week 1 overview](Topics_covered.md)
- [Machine Learning algorithms](Machine_Learning_Algorithms.md)
- [Deep Learning algorithms](Deep_Learning_Algorithms.md)
- [Transformer architecture](Transformer_Architecture_End_to_End.md)
- [Transformer model families](Transformer_Model_Families.md)

This README summarizes common **Natural Language Processing (NLP)** techniques and the business problems they solve.

NLP is used when applications need to understand, search, classify, extract, summarize, translate, or generate human language.

## How to Use This Guide

Start with the problem:

1. Do you need to clean text?
2. Do you need to convert text into features?
3. Do you need to classify text?
4. Do you need to extract names, dates, amounts, or IDs?
5. Do you need semantic search or question answering?
6. Do you need summarization, translation, or text generation?

Once the problem is clear, choose the matching NLP technique.

## 1. Text Preprocessing Techniques

Text preprocessing prepares raw text for analysis or machine learning.

- **Tokenization**
  - What it does: Breaks text into words, subwords, or sentences.
  - Solves: Preparing text for machine learning models.

- **Lowercasing**
  - What it does: Converts all text into lowercase.
  - Solves: Reducing duplicate word variations like "Bank" and "bank".

- **Stopword Removal**
  - What it does: Removes common words like "is", "the", and "and".
  - Solves: Improving keyword-focused text analysis.

- **Stemming**
  - What it does: Reduces words to rough root forms, such as "running" to "run".
  - Solves: Search engines and keyword matching.

- **Lemmatization**
  - What it does: Converts words to proper dictionary forms.
  - Solves: Better text normalization than stemming.

- **Punctuation Removal**
  - What it does: Removes symbols and special characters.
  - Solves: Cleaning noisy text data.

- **Spelling Correction**
  - What it does: Fixes spelling mistakes.
  - Solves: Chatbots, search engines, and customer feedback analysis.

- **Text Normalization**
  - What it does: Standardizes slang, short forms, emojis, and abbreviations.
  - Solves: Social media analysis and chat data cleaning.

- **Sentence Segmentation**
  - What it does: Splits paragraphs into sentences.
  - Solves: Document summarization and question answering.

## 2. Feature Extraction Techniques

Feature extraction converts text into numerical or structured representations that models can use.

- **Bag of Words**
  - What it does: Represents text using word frequency.
  - Solves: Basic text classification.

- **Term Frequency-Inverse Document Frequency**
  - What it does: Gives importance scores to words.
  - Solves: Search ranking and document similarity.

- **N-Grams**
  - What it does: Captures word combinations like "credit card".
  - Solves: Phrase detection and sentiment analysis.

- **Word Embeddings**
  - What it does: Converts words into numerical vectors.
  - Solves: Semantic similarity and recommendations.

- **Sentence Embeddings**
  - What it does: Converts full sentences into vectors.
  - Solves: Semantic search and document matching.

- **Document Embeddings**
  - What it does: Converts full documents into vectors.
  - Solves: Document clustering and document retrieval.

## 3. Text Classification Algorithms

Text classification assigns text into categories such as billing, complaint, refund, positive, negative, spam, or not spam.

- **Naive Bayes**
  - Solves: Spam detection, sentiment classification, and email filtering.

- **Logistic Regression**
  - Solves: Customer complaint classification and ticket routing.

- **Support Vector Machine**
  - Solves: Document classification and legal text classification.

- **Decision Tree**
  - Solves: Rule-based text categorization.

- **Random Forest**
  - Solves: Multi-category text classification.

- **Gradient Boosting**
  - Solves: High-accuracy text classification.

- **Extreme Gradient Boosting**
  - Solves: Large-scale classification problems.

- **Neural Networks**
  - Solves: Complex text classification.

- **BERT**
  - Solves: Intent detection, sentiment classification, and document classification.

- **Transformer-based Classifiers**
  - Solves: Modern enterprise-level text classification.

Example problems:

- Classify customer emails into billing, technical, refund, or complaint.
- Identify whether feedback is positive, negative, or neutral.
- Detect whether a message is spam or not.
- Route support tickets to the right department.

## 4. Sentiment Analysis Techniques

Sentiment analysis identifies emotion, opinion, tone, or satisfaction in text.

- **Lexicon-Based Sentiment Analysis**
  - Solves: Simple positive or negative word scoring.

- **Naive Bayes**
  - Solves: Basic sentiment classification.

- **Logistic Regression**
  - Solves: Sentiment prediction from reviews.

- **Support Vector Machine**
  - Solves: High-dimensional text sentiment classification.

- **Long Short-Term Memory Network**
  - Solves: Sentiment in sequential text.

- **BERT**
  - Solves: Context-aware sentiment understanding.

- **Large Language Models**
  - Solves: Deep sentiment, emotion, tone, and intent understanding.

Example problems:

- Understand if customer reviews are positive or negative.
- Detect angry customers in call transcripts.
- Monitor brand reputation from social media.
- Identify satisfaction trends from survey responses.

## 5. Named Entity Recognition Techniques

Named Entity Recognition, or NER, identifies important entities in text.

- **Rule-Based Entity Recognition**
  - Solves: Detecting known patterns like dates, phone numbers, and identifiers.

- **Regular Expressions**
  - Solves: Extracting structured patterns from text.

- **Conditional Random Field**
  - Solves: Sequence labeling and entity extraction.

- **Hidden Markov Model**
  - Solves: Older sequence tagging tasks.

- **Long Short-Term Memory Network**
  - Solves: Entity extraction from sequence data.

- **BiLSTM with CRF**
  - Solves: Strong entity recognition with sequence modeling.

- **BERT**
  - Solves: Modern entity extraction.

- **Large Language Models**
  - Solves: Flexible entity extraction from complex documents.

Example problems:

- Extract names, dates, amounts, and locations from documents.
- Identify policy numbers or claim numbers.
- Extract company names from contracts.
- Detect sensitive personal information from text.

## 6. Intent Detection Techniques

Intent detection identifies what a user wants to do.

- **Keyword Matching**
  - Solves: Basic intent detection.

- **Rule-Based Matching**
  - Solves: FAQ bots and menu-based assistants.

- **Logistic Regression**
  - Solves: Simple chatbot intent classification.

- **Support Vector Machine**
  - Solves: Intent classification.

- **Neural Networks**
  - Solves: Multi-intent classification.

- **BERT**
  - Solves: Context-aware intent detection.

- **Large Language Models**
  - Solves: Open-ended intent understanding.

Example problems:

- "I want to reset my password" means password reset intent.
- "My card was charged twice" means billing dispute intent.
- "Where is my order?" means order tracking intent.
- Agent assistants use intent classification to understand customer issues.

## 7. Topic Modeling Techniques

Topic modeling discovers hidden themes from large text datasets.

- **Latent Dirichlet Allocation**
  - Solves: Discovering topics from documents.

- **Non-Negative Matrix Factorization**
  - Solves: Topic extraction from text.

- **Latent Semantic Analysis**
  - Solves: Finding hidden semantic patterns.

- **K-Means with Embeddings**
  - Solves: Grouping similar text documents.

- **Hierarchical Clustering**
  - Solves: Organizing documents into topic trees.

- **BERT Topic Modeling**
  - Solves: Modern topic modeling with embeddings.

Example problems:

- Find common reasons customers complain.
- Group thousands of reviews into themes.
- Understand call center issue categories.
- Analyze survey responses without labels.

## 8. Text Similarity and Semantic Search

Text similarity and semantic search find related meaning between texts.

- **Cosine Similarity**
  - Solves: Measuring similarity between text vectors.

- **Jaccard Similarity**
  - Solves: Comparing word overlap.

- **TF-IDF Similarity**
  - Solves: Keyword-based document matching.

- **Word Embedding Similarity**
  - Solves: Meaning-based word comparison.

- **Sentence Transformer Embeddings**
  - Solves: Semantic sentence matching.

- **Dense Vector Search**
  - Solves: Semantic search.

- **Sparse Vector Search**
  - Solves: Keyword-based search.

- **Hybrid Search**
  - Solves: Combining keyword and semantic search.

Example problems:

- Find similar support tickets.
- Match a user query to the correct document chunk.
- Recommend similar articles.
- Find duplicate customer complaints.

## 9. Question Answering Techniques

Question answering systems answer user questions from text or retrieved knowledge.

- **Rule-Based Question Answering**
  - Solves: Simple FAQ matching.

- **Information Retrieval-Based Question Answering**
  - Solves: Finding the best document and extracting an answer.

- **Machine Reading Comprehension**
  - Solves: Reading a passage and answering questions.

- **BERT**
  - Solves: Extractive question answering.

- **Retrieval Augmented Generation**
  - Solves: Answering using retrieved documents.

- **Large Language Models**
  - Solves: Natural answer generation.

Example problems:

- Answer questions from policy documents.
- Build a chatbot over company documents.
- Answer from product manuals.
- Help agents find troubleshooting steps.

## 10. Text Summarization Techniques

Text summarization reduces long text into shorter meaningful text.

- **Extractive Summarization**
  - Solves: Picking important sentences from the original text.

- **Abstractive Summarization**
  - Solves: Generating a new summary in natural language.

- **TextRank**
  - Solves: Graph-based extractive summarization.

- **Transformer Models**
  - Solves: High-quality summarization.

- **Large Language Models**
  - Solves: Meeting notes, call summaries, and document summaries.

Example problems:

- Summarize customer call transcripts.
- Summarize legal or policy documents.
- Summarize long email threads.
- Generate executive summaries.

## 11. Text Generation Techniques

Text generation creates human-like text.

- **Template-Based Generation**
  - Solves: Fixed-format response generation.

- **Markov Chains**
  - Solves: Basic text generation.

- **Recurrent Neural Networks**
  - Solves: Sequence-based generation.

- **Long Short-Term Memory Networks**
  - Solves: Better sequence generation.

- **Transformer Decoder Models**
  - Solves: Modern text generation.

- **Large Language Models**
  - Solves: Chatbots, content generation, and code generation.

Example problems:

- Generate chatbot responses.
- Generate email drafts.
- Generate product descriptions.
- Generate answers from retrieved context.

## 12. Machine Translation Techniques

Machine translation converts text from one language to another.

- **Rule-Based Machine Translation**
  - Solves: Dictionary and grammar-based translation.

- **Statistical Machine Translation**
  - Solves: Probability-based translation.

- **Sequence-to-Sequence Models**
  - Solves: Neural translation.

- **Attention-Based Models**
  - Solves: Better context translation.

- **Transformer Models**
  - Solves: Modern translation systems.

- **Large Language Models**
  - Solves: Multilingual translation and localization.

Example problems:

- Translate English to Spanish.
- Translate customer messages in real time.
- Localize website content.
- Translate documents.

## 13. Speech and Text Processing Techniques

Speech and text processing is used when working with voice data and transcripts.

- **Speech-to-Text**
  - Solves: Converting audio into text.

- **Text-to-Speech**
  - Solves: Converting text into voice.

- **Speaker Diarization**
  - Solves: Identifying who spoke and when.

- **Keyword Spotting**
  - Solves: Detecting important words in audio.

- **Sentiment Analysis on Transcript**
  - Solves: Understanding customer emotion.

- **Call Transcript Summarization**
  - Solves: Summarizing customer-agent conversations.

Example problems:

- Convert customer calls into text.
- Analyze agent-customer conversations.
- Detect fraud-related words in calls.
- Summarize call center conversations.

## 14. Information Extraction Techniques

Information extraction converts unstructured text into structured data.

- **Regular Expressions**
  - Solves: Extracting emails, phone numbers, and codes.

- **Named Entity Recognition**
  - Solves: Extracting names, dates, and organizations.

- **Relation Extraction**
  - Solves: Identifying relationships between entities.

- **Dependency Parsing**
  - Solves: Understanding grammar relationships.

- **Table Extraction**
  - Solves: Extracting tabular data from documents.

- **Large Language Models**
  - Solves: Extracting structured JSON from documents.

Example problems:

- Extract invoice number, amount, and date.
- Extract skills from resumes.
- Extract terms from contracts.
- Extract claim details from insurance documents.

## 15. Text Clustering Techniques

Text clustering groups similar text without labels.

- **K-Means Clustering**
  - Solves: Grouping similar documents.

- **Hierarchical Clustering**
  - Solves: Creating topic hierarchies.

- **DBSCAN**
  - Solves: Finding dense groups and outliers.

- **Gaussian Mixture Model**
  - Solves: Probabilistic grouping.

- **Embedding-Based Clustering**
  - Solves: Grouping text by semantic meaning.

Example problems:

- Group similar complaints.
- Find themes in feedback.
- Organize knowledge base articles.
- Detect unusual support tickets.

## 16. Text Ranking and Reranking Techniques

Ranking and reranking choose the best documents, chunks, or answers.

- **Best Matching 25**
  - Solves: Keyword-based ranking.

- **Dense Retrieval**
  - Solves: Semantic ranking.

- **Cross-Encoder Reranking**
  - Solves: More accurate reranking of retrieved results.

- **Reciprocal Rank Fusion**
  - Solves: Combining multiple ranking results.

- **Learning to Rank**
  - Solves: Learning ranking from user behavior.

Example problems:

- Retrieve the best document chunks for a chatbot.
- Improve search result quality.
- Rank answers by relevance.
- Improve Retrieval Augmented Generation accuracy.

## Most Important NLP Techniques for Real Projects

- **Customer support chatbot**
  - Best techniques: Intent detection, semantic search, Retrieval Augmented Generation, summarization.

- **Resume screening**
  - Best techniques: Named entity recognition, classification, similarity matching.

- **Fraud detection from text**
  - Best techniques: Keyword detection, entity extraction, classification.

- **Sentiment analysis**
  - Best techniques: Text classification and transformer models.

- **Document search**
  - Best techniques: Dense search, sparse search, hybrid search, reranking.

- **Call center analytics**
  - Best techniques: Speech-to-text, sentiment analysis, topic modeling, summarization.

- **Email classification**
  - Best techniques: Naive Bayes, logistic regression, transformer classifier.

- **Contract analysis**
  - Best techniques: Named entity recognition, relation extraction, summarization.

- **Policy question answering**
  - Best techniques: Retrieval Augmented Generation and question answering.

- **Social media monitoring**
  - Best techniques: Sentiment analysis, slang normalization, topic modeling.

## Simple Interview-Friendly Summary

NLP mainly solves these problems:

- **Understand text meaning**
  - Use embeddings and transformers.

- **Classify text**
  - Use text classification.

- **Extract important details**
  - Use named entity recognition.

- **Find similar documents**
  - Use semantic search.

- **Answer questions**
  - Use question answering and Retrieval Augmented Generation.

- **Summarize long text**
  - Use text summarization.

- **Generate responses**
  - Use text generation.

- **Translate languages**
  - Use machine translation.

- **Detect emotion**
  - Use sentiment analysis.

- **Group similar texts**
  - Use topic modeling and clustering.

- **Rank best results**
  - Use search ranking and reranking.

The most commonly used NLP techniques in modern AI projects are:

- Tokenization
- Embeddings
- Text classification
- Named entity recognition
- Semantic search
- Reranking
- Summarization
- Question answering
- Retrieval Augmented Generation
- Large Language Models

## Interview Tip

When explaining an NLP solution, start with the business problem first.

Example:

> Since the problem is to answer questions from company documents, I would use Retrieval Augmented Generation. First, I would retrieve the most relevant document chunks using semantic search, then use a Large Language Model to generate an answer grounded in those documents.
