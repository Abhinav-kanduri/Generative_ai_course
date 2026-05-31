# Machine Learning Algorithms by Category

**Author:** Abhinav Kanduri  
**GitHub:** @Abhinav-kanduri  
**LinkedIn:** https://www.linkedin.com/in/abhinav-kanduri-a943b9353/  
**Purpose:** Knowledge transfer only.

## Course Navigation

- [Course home](../README.md)
- [Foundation Week 1 dashboard](README.md)
- [Foundation Week 1 overview](Topics_covered.md)
- [Natural Language Processing techniques](Natural_Language_Processing_Techniques.md)
- [Deep Learning algorithms](Deep_Learning_Algorithms.md)
- [Transformer architecture](Transformer_Architecture_End_to_End.md)
- [Transformer model families](Transformer_Model_Families.md)

This README organizes common machine learning algorithms by problem type. Use it as a quick reference when deciding which algorithm family fits a project, assignment, or interview question.

## How to Choose an Algorithm

Start with the problem:

1. Are you predicting a number?
2. Are you predicting a class or category?
3. Are you grouping similar data points?
4. Are you reducing features?
5. Are you detecting unusual behavior?
6. Are you working with text, images, time series, or rewards?

Once the problem is clear, choose from the matching algorithm category.

## 1. Supervised Learning

Supervised learning algorithms learn from labeled data. The dataset already contains input features and the correct output.

### Regression Algorithms

Use regression when the output is a continuous value, such as price, salary, revenue, or temperature.

- **Linear Regression**
  - Used for predicting continuous values like price, salary, and sales.

- **Polynomial Regression**
  - Used for non-linear continuous prediction.

- **Ridge Regression**
  - Used for regression with regularization to reduce overfitting.

- **Lasso Regression**
  - Used for feature selection and regularized regression.

- **Elastic Net Regression**
  - Used when combining Ridge and Lasso regularization.

- **Decision Tree Regression**
  - Used for rule-based prediction of continuous values.

- **Random Forest Regression**
  - Used for more accurate regression using multiple trees.

- **Gradient Boosting Regression**
  - Used for strong predictive regression models.

- **XGBoost Regression**
  - Used for high-performance boosting regression.

- **LightGBM Regression**
  - Used for fast boosting on large datasets.

- **CatBoost Regression**
  - Used when the dataset has many categorical features.

- **Support Vector Regression**
  - Used for regression with support vector machines.

- **K-Nearest Neighbors Regression**
  - Used for prediction based on nearby data points.

- **Neural Network Regression**
  - Used for deep learning-based continuous prediction.

### Classification Algorithms

Use classification when the output is a class or category, such as yes/no, spam/not spam, approved/rejected, or fraud/not fraud.

- **Logistic Regression**
  - Used for binary classification.

- **Decision Tree Classifier**
  - Used for rule-based classification.

- **Random Forest Classifier**
  - Used for classification using multiple decision trees.

- **Support Vector Machine**
  - Used for classification with margin separation.

- **K-Nearest Neighbors Classifier**
  - Used for classification based on nearby examples.

- **Naive Bayes**
  - Used for text classification and spam detection.

- **Gradient Boosting Classifier**
  - Used for high-accuracy classification.

- **XGBoost Classifier**
  - Used for advanced boosting classification.

- **LightGBM Classifier**
  - Used for fast and scalable classification.

- **CatBoost Classifier**
  - Used for classification with categorical data.

- **AdaBoost Classifier**
  - Used for boosting weak models into stronger models.

- **Linear Discriminant Analysis**
  - Used for classification and dimensionality reduction.

- **Quadratic Discriminant Analysis**
  - Used for classification with non-linear boundaries.

- **Neural Network Classifier**
  - Used for complex classification problems.

- **Multilayer Perceptron**
  - Used for feed-forward neural network classification.

## 2. Unsupervised Learning

Unsupervised learning algorithms find patterns in unlabeled data.

### Clustering Algorithms

Use clustering when you want to group similar data points without predefined labels.

- **K-Means Clustering**
  - Used for customer segmentation and grouping similar data.

- **Hierarchical Clustering**
  - Used for tree-based grouping.

- **DBSCAN**
  - Used for density-based clustering and outlier detection.

- **Mean Shift Clustering**
  - Used for finding natural clusters.

- **Gaussian Mixture Model**
  - Used for probabilistic clustering.

- **Agglomerative Clustering**
  - Used for bottom-up hierarchical clustering.

- **Spectral Clustering**
  - Used for graph-based clustering.

- **BIRCH**
  - Used for large-scale clustering.

- **Affinity Propagation**
  - Used for finding representative examples.

### Dimensionality Reduction Algorithms

Use dimensionality reduction when the dataset has too many features and you want to simplify it while keeping useful information.

- **Principal Component Analysis**
  - Used for reducing features while keeping important information.

- **Linear Discriminant Analysis**
  - Used for reducing dimensions for classification.

- **t-SNE**
  - Used for visualizing high-dimensional data.

- **UMAP**
  - Used for fast visualization and dimensionality reduction.

- **Autoencoders**
  - Used for neural network-based compression.

- **Factor Analysis**
  - Used for finding hidden factors.

- **Independent Component Analysis**
  - Used for separating independent signals.

### Association Rule Learning

Use association rule learning when you want to find relationships between items.

- **Apriori Algorithm**
  - Used for market basket analysis.

- **FP-Growth**
  - Used for faster frequent itemset mining.

- **Eclat Algorithm**
  - Used for association rule mining.

## 3. Semi-Supervised Learning

Semi-supervised learning is useful when only a small part of the dataset is labeled and most of the data is unlabeled.

- **Self-Training**
  - Used when a model labels unlabeled data and retrains itself.

- **Label Propagation**
  - Used for spreading labels through similar data points.

- **Label Spreading**
  - Used like label propagation, but with regularization.

- **Semi-Supervised Support Vector Machine**
  - Used for classification with limited labels.

- **Pseudo Labeling**
  - Used for assigning predicted labels to unlabeled data.

## 4. Reinforcement Learning

Reinforcement learning is used when an agent learns by taking actions and receiving rewards.

- **Q-Learning**
  - Used for learning the best action strategy.

- **Deep Q-Network**
  - Used for reinforcement learning with neural networks.

- **SARSA**
  - Used for action-value learning.

- **Policy Gradient**
  - Used for learning policies directly.

- **Actor-Critic**
  - Used for combining value learning and policy learning.

- **Proximal Policy Optimization**
  - Used for stable reinforcement learning training.

- **Advantage Actor-Critic**
  - Used for policy optimization.

- **Deep Deterministic Policy Gradient**
  - Used for continuous action problems.

- **Monte Carlo Methods**
  - Used for learning from complete episodes.

- **Temporal Difference Learning**
  - Used for learning from partial experience.

## 5. Ensemble Learning

Ensemble learning combines multiple models to improve accuracy, stability, and generalization.

- **Bagging**
  - Used for reducing variance.

- **Random Forest**
  - Used for bagging with decision trees.

- **AdaBoost**
  - Used for boosting weak learners.

- **Gradient Boosting**
  - Used for sequential error correction.

- **XGBoost**
  - Used for optimized gradient boosting.

- **LightGBM**
  - Used for fast boosting on large data.

- **CatBoost**
  - Used for boosting with categorical feature handling.

- **Voting Classifier**
  - Used for combining multiple models by voting.

- **Stacking**
  - Used for combining models using another model.

- **Blending**
  - Used like stacking, but with validation data.

## 6. Deep Learning

Deep learning algorithms use neural networks to model complex patterns.

- **Artificial Neural Network**
  - Used for general prediction and classification.

- **Convolutional Neural Network**
  - Used for image processing and computer vision.

- **Recurrent Neural Network**
  - Used for sequential data.

- **Long Short-Term Memory Network**
  - Used for time series and language data.

- **Gated Recurrent Unit**
  - Used for faster sequence modeling.

- **Transformer**
  - Used for Large Language Models and modern Natural Language Processing.

- **Autoencoder**
  - Used for feature compression and anomaly detection.

- **Variational Autoencoder**
  - Used for generative modeling.

- **Generative Adversarial Network**
  - Used for image generation.

- **Graph Neural Network**
  - Used for graph-based data such as social networks.

- **Siamese Network**
  - Used for similarity matching.

- **Diffusion Model**
  - Used for image and media generation.

## 7. Natural Language Processing Algorithms

NLP algorithms are used for text, language, and document understanding.

- **Naive Bayes**
  - Used for spam detection and sentiment analysis.

- **Logistic Regression**
  - Used for text classification.

- **Support Vector Machine**
  - Used for document classification.

- **Conditional Random Field**
  - Used for Named Entity Recognition.

- **Hidden Markov Model**
  - Used for sequence tagging.

- **Word2Vec**
  - Used for word embeddings.

- **GloVe**
  - Used for word embeddings.

- **FastText**
  - Used for text embeddings.

- **BERT**
  - Used for language understanding.

- **Transformer Models**
  - Used for modern Large Language Models.

- **Sequence-to-Sequence Models**
  - Used for translation and summarization.

## 8. Anomaly Detection

Anomaly detection algorithms are used to find unusual patterns, outliers, suspicious behavior, or rare events.

- **Isolation Forest**
  - Used for fraud detection and outlier detection.

- **One-Class Support Vector Machine**
  - Used for novelty detection.

- **Local Outlier Factor**
  - Used for detecting local anomalies.

- **Autoencoders**
  - Used for deep learning-based anomaly detection.

- **Elliptic Envelope**
  - Used for statistical anomaly detection.

- **DBSCAN**
  - Used for outlier detection in clusters.

## 9. Time Series Algorithms

Time series algorithms are used for forecasting data over time.

- **ARIMA**
  - Used for time series forecasting.

- **SARIMA**
  - Used for seasonal forecasting.

- **Exponential Smoothing**
  - Used for forecasting trends.

- **Prophet**
  - Used for business forecasting.

- **Long Short-Term Memory Network**
  - Used for deep learning forecasting.

- **Temporal Convolutional Network**
  - Used for sequence forecasting.

- **Transformer-based Forecasting**
  - Used for advanced time series prediction.

- **Random Forest Forecasting**
  - Used for machine learning-based forecasting.

- **XGBoost Forecasting**
  - Used for strong tabular time series forecasting.

## Most Commonly Used Algorithms in Real Projects

For interviews and real-world projects, focus especially on these algorithms:

- **Linear Regression**
  - Foundation algorithm for regression.

- **Logistic Regression**
  - Foundation algorithm for classification.

- **Decision Tree**
  - Easy to explain and interpret.

- **Random Forest**
  - Strong baseline model for many tasks.

- **XGBoost**
  - High-performance model for tabular data.

- **LightGBM**
  - Fast model for large-scale data.

- **CatBoost**
  - Strong choice when categorical features are important.

- **K-Means**
  - Basic and popular clustering algorithm.

- **Principal Component Analysis**
  - Common feature reduction method.

- **Naive Bayes**
  - Useful for text classification.

- **Support Vector Machine**
  - Useful for classification problems.

- **K-Nearest Neighbors**
  - Simple similarity-based learning algorithm.

- **Neural Networks**
  - Foundation for deep learning.

- **Transformer**
  - Foundation of modern Large Language Models.

- **Isolation Forest**
  - Common anomaly detection algorithm.

## Quick Interview Tip

When asked which algorithm to use, answer by naming the problem type first.

Example:

> Since the business problem is classification, I would start with Logistic Regression as a baseline, then compare it with Random Forest, XGBoost, LightGBM, or CatBoost depending on accuracy, speed, and interpretability needs.

The best answer connects the business problem, the data type, and the algorithm family.
