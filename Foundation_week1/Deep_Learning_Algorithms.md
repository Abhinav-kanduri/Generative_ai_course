# Deep Learning Algorithms and Their Use Cases

**Author:** Abhinav Kanduri  
**GitHub:** @Abhinav-kanduri  
**LinkedIn:** https://www.linkedin.com/in/abhinav-kanduri-a943b9353/  
**Purpose:** Knowledge transfer only.

## Course Navigation

- [Course home](../README.md)
- [Foundation Week 1 dashboard](README.md)
- [Foundation Week 1 overview](Topics_covered.md)
- [Machine Learning algorithms](Machine_Learning_Algorithms.md)
- [Natural Language Processing techniques](Natural_Language_Processing_Techniques.md)
- [Transformer architecture](Transformer_Architecture_End_to_End.md)
- [Transformer model families](Transformer_Model_Families.md)

This README summarizes common **Deep Learning algorithms and architectures** and the types of problems they solve.

Deep learning is useful when data contains complex patterns, such as images, speech, text, sequences, graphs, recommendations, and multimodal inputs.

## How to Use This Guide

Start with the problem:

1. Are you working with structured prediction?
2. Are you analyzing images or video?
3. Do you need object detection or image segmentation?
4. Are you working with sequences, text, or time series?
5. Do you need generation, recommendations, speech processing, or graph learning?
6. Do you need a system that learns from rewards?

Once the problem is clear, choose the matching deep learning architecture.

## 1. Artificial Neural Networks

Artificial Neural Networks learn patterns from structured data using layers of neurons.

- **Artificial Neural Network**
  - What it does: Learns non-linear patterns from structured data.
  - Solves: Classification, regression, prediction, and scoring.

- **Multilayer Perceptron**
  - What it does: Uses a basic feed-forward neural network.
  - Solves: Customer churn prediction, fraud detection, loan approval, and price prediction.

Example use cases:

- Predict whether a customer will leave.
- Predict house price or sales amount.
- Predict credit risk score.

## 2. Convolutional Neural Networks

Convolutional Neural Networks, or CNNs, are mainly used for image, video, and visual pattern recognition.

- **Convolutional Neural Network**
  - What it does: Extracts visual patterns such as edges, shapes, and objects.
  - Solves: Image classification, object detection, and medical imaging.

- **LeNet**
  - What it does: Uses an early image recognition network.
  - Solves: Digit recognition.

- **AlexNet**
  - What it does: Uses a deep image classification model.
  - Solves: Large-scale image classification.

- **VGGNet**
  - What it does: Uses deep stacked convolution layers.
  - Solves: Image classification.

- **ResNet**
  - What it does: Uses skip connections to train deeper networks.
  - Solves: Image classification and medical image analysis.

- **DenseNet**
  - What it does: Connects each layer to every other layer.
  - Solves: Image recognition and feature reuse.

- **MobileNet**
  - What it does: Uses a lightweight image model.
  - Solves: Mobile and edge device vision.

- **EfficientNet**
  - What it does: Uses an optimized image model.
  - Solves: High-accuracy image classification.

- **Inception Network**
  - What it does: Captures features at multiple scales.
  - Solves: Object and image recognition.

Example use cases:

- Identify whether an image contains a cat or dog.
- Detect defective products in manufacturing.
- Analyze medical scans.
- Recognize handwritten digits.

## 3. Object Detection Algorithms

Object detection is used when you need to locate and classify objects inside an image.

- **Region-Based Convolutional Neural Network**
  - What it does: Detects objects using region proposals.
  - Solves: Object detection.

- **Fast Region-Based Convolutional Neural Network**
  - What it does: Speeds up region-based object detection.
  - Solves: Object localization.

- **Faster Region-Based Convolutional Neural Network**
  - What it does: Improves detection speed using region proposal networks.
  - Solves: Real-time object detection.

- **You Only Look Once**
  - What it does: Detects objects in one forward pass.
  - Solves: Real-time detection.

- **Single Shot Detector**
  - What it does: Performs fast object detection.
  - Solves: Surveillance and traffic monitoring.

- **RetinaNet**
  - What it does: Handles class imbalance in object detection.
  - Solves: Detecting small or rare objects.

- **Detectron-style Models**
  - What it does: Provides advanced object detection frameworks.
  - Solves: Production computer vision systems.

Example use cases:

- Detect cars and people in video.
- Detect damaged packages.
- Detect traffic signs.
- Detect items on retail shelves.

## 4. Image Segmentation Algorithms

Image segmentation is used when each pixel in an image needs to be classified.

- **Fully Convolutional Network**
  - What it does: Performs pixel-level classification.
  - Solves: Semantic segmentation.

- **U-Net**
  - What it does: Provides strong image segmentation, especially for medical images.
  - Solves: Tumor, organ, and cell segmentation.

- **Mask Region-Based Convolutional Neural Network**
  - What it does: Detects objects and creates object masks.
  - Solves: Instance segmentation.

- **DeepLab**
  - What it does: Uses advanced convolution methods for segmentation.
  - Solves: Road, object, and scene segmentation.

- **Segment Anything Model**
  - What it does: Performs general-purpose segmentation.
  - Solves: Interactive and zero-shot segmentation.

Example use cases:

- Separate tumor area from a medical image.
- Detect road lanes in self-driving cars.
- Separate foreground and background.
- Identify individual objects in an image.

## 5. Recurrent Neural Networks

Recurrent Neural Networks are mainly used for sequence data.

- **Recurrent Neural Network**
  - What it does: Learns from sequential data.
  - Solves: Time series, text, and speech problems.

- **Long Short-Term Memory Network**
  - What it does: Remembers long-term dependencies.
  - Solves: Language modeling and forecasting.

- **Gated Recurrent Unit**
  - What it does: Provides a faster sequence model than LSTM.
  - Solves: Text and time series prediction.

- **Bidirectional Recurrent Neural Network**
  - What it does: Reads sequences forward and backward.
  - Solves: Better context understanding.

- **Bidirectional Long Short-Term Memory Network**
  - What it does: Captures past and future context.
  - Solves: Named entity recognition and sentiment analysis.

Example use cases:

- Predict the next word in a sentence.
- Forecast stock or sales trends.
- Analyze customer call transcripts.
- Detect named entities in text.

## 6. Sequence-to-Sequence Models

Sequence-to-sequence models are used when both input and output are sequences.

- **Encoder-Decoder Model**
  - What it does: Converts one sequence into another.
  - Solves: Translation and summarization.

- **Sequence-to-Sequence with Attention**
  - What it does: Focuses on important input words.
  - Solves: Better translation and summarization.

- **Pointer Generator Network**
  - What it does: Copies important words from source text.
  - Solves: Document summarization.

- **Transformer Encoder-Decoder**
  - What it does: Uses modern sequence transformation.
  - Solves: Translation, summarization, and question answering.

Example use cases:

- Translate English to French.
- Summarize a document.
- Convert speech transcripts into clean notes.
- Generate an answer from a passage.

## 7. Transformer-Based Algorithms

Transformers are used in modern Large Language Models, NLP, vision, speech, and multimodal AI.

- **Transformer**
  - What it does: Uses attention to understand relationships between tokens.
  - Solves: Language understanding and generation.

- **Encoder-Only Transformer**
  - What it does: Deeply understands input text.
  - Solves: Classification, entity recognition, and semantic search.

- **Decoder-Only Transformer**
  - What it does: Generates text token by token.
  - Solves: Chatbots, content generation, and code generation.

- **Encoder-Decoder Transformer**
  - What it does: Converts one text sequence to another.
  - Solves: Translation and summarization.

- **BERT**
  - What it does: Provides contextual language understanding.
  - Solves: Sentiment analysis and entity extraction.

- **GPT**
  - What it does: Performs text generation and reasoning.
  - Solves: Chatbots and assistants.

- **Text-to-Text Transfer Transformer**
  - What it does: Converts every task into a text-to-text format.
  - Solves: Translation, summarization, and classification.

- **Vision Transformer**
  - What it does: Applies transformer architecture to images.
  - Solves: Image classification.

- **Swin Transformer**
  - What it does: Uses hierarchical vision transformers.
  - Solves: Object detection and segmentation.

- **Retrieval-Augmented Transformer Models**
  - What it does: Combines retrieval with generation.
  - Solves: Document question answering.

Example use cases:

- Build a chatbot.
- Answer questions from documents.
- Classify customer complaints.
- Generate code.
- Summarize legal documents.

## 8. Autoencoder Algorithms

Autoencoders learn compressed representations of data.

- **Autoencoder**
  - What it does: Compresses and reconstructs data.
  - Solves: Dimensionality reduction and anomaly detection.

- **Denoising Autoencoder**
  - What it does: Removes noise from data.
  - Solves: Image cleaning and signal cleaning.

- **Sparse Autoencoder**
  - What it does: Learns important hidden features.
  - Solves: Feature learning.

- **Variational Autoencoder**
  - What it does: Generates new data from a learned distribution.
  - Solves: Image generation and synthetic data.

- **Convolutional Autoencoder**
  - What it does: Applies autoencoders to images.
  - Solves: Image compression and reconstruction.

Example use cases:

- Detect unusual transactions.
- Compress images.
- Remove noise from images.
- Generate synthetic images.

## 9. Generative Adversarial Networks

Generative Adversarial Networks, or GANs, are used to generate realistic synthetic data.

- **Generative Adversarial Network**
  - What it does: Uses a generator and discriminator to create realistic data.
  - Solves: Image generation.

- **Deep Convolutional Generative Adversarial Network**
  - What it does: Generates images using convolutional layers.
  - Solves: Image synthesis.

- **Conditional Generative Adversarial Network**
  - What it does: Generates data based on a condition.
  - Solves: Controlled image generation.

- **Cycle Generative Adversarial Network**
  - What it does: Converts one image style to another.
  - Solves: Image-to-image translation.

- **Style Generative Adversarial Network**
  - What it does: Generates high-quality realistic images.
  - Solves: Face generation and design generation.

Example use cases:

- Generate synthetic faces.
- Convert day images to night images.
- Create artificial training data.
- Improve low-resolution images.

## 10. Diffusion Models

Diffusion models are used in modern image, video, audio, and generative AI systems.

- **Diffusion Model**
  - What it does: Learns to remove noise step by step to generate data.
  - Solves: Image generation.

- **Denoising Diffusion Probabilistic Model**
  - What it does: Generates data through a denoising process.
  - Solves: High-quality image synthesis.

- **Latent Diffusion Model**
  - What it does: Performs diffusion in compressed latent space.
  - Solves: Faster image generation.

- **Stable Diffusion-style Models**
  - What it does: Generates images from text.
  - Solves: Creative image generation.

- **Video Diffusion Models**
  - What it does: Generates or edits videos.
  - Solves: Video generation.

Example use cases:

- Generate images from text.
- Edit images using prompts.
- Generate product mockups.
- Generate synthetic training images.

## 11. Graph Neural Networks

Graph Neural Networks are used when data is represented as nodes and relationships.

- **Graph Neural Network**
  - What it does: Learns from graph-structured data.
  - Solves: Relationship prediction.

- **Graph Convolutional Network**
  - What it does: Applies convolution on graph data.
  - Solves: Node classification.

- **Graph Attention Network**
  - What it does: Uses attention over graph neighbors.
  - Solves: Link prediction.

- **GraphSAGE**
  - What it does: Provides scalable graph learning.
  - Solves: Large graph recommendations.

- **Message Passing Neural Network**
  - What it does: Passes information between connected nodes.
  - Solves: Molecular modeling and fraud rings.

Example use cases:

- Detect fraud networks.
- Recommend friends or products.
- Analyze molecule structure.
- Detect suspicious account relationships.

## 12. Deep Reinforcement Learning

Deep reinforcement learning is used when an agent learns by taking actions and receiving rewards.

- **Deep Q-Network**
  - What it does: Combines Q-learning with neural networks.
  - Solves: Game playing and decision systems.

- **Double Deep Q-Network**
  - What it does: Reduces overestimation in Q-learning.
  - Solves: Stable decision learning.

- **Dueling Deep Q-Network**
  - What it does: Separates value and advantage learning.
  - Solves: Better action selection.

- **Policy Gradient Network**
  - What it does: Learns action policy directly.
  - Solves: Robotics and control systems.

- **Actor-Critic Network**
  - What it does: Combines policy and value learning.
  - Solves: Complex decision-making.

- **Proximal Policy Optimization**
  - What it does: Provides stable deep reinforcement learning.
  - Solves: Robotics, games, and optimization.

- **Deep Deterministic Policy Gradient**
  - What it does: Handles continuous actions.
  - Solves: Autonomous systems.

Example use cases:

- Train a game-playing agent.
- Optimize pricing decisions.
- Optimize ad or offer recommendations.
- Train robot movement.

## 13. Recommendation Deep Learning Algorithms

Recommendation deep learning algorithms are used for personalization and ranking.

- **Neural Collaborative Filtering**
  - What it does: Learns user-item interaction patterns.
  - Solves: Product recommendation.

- **Deep Factorization Machine**
  - What it does: Combines deep learning and feature interactions.
  - Solves: Click prediction.

- **Wide and Deep Network**
  - What it does: Combines memorization and generalization.
  - Solves: Search and recommendation.

- **Deep Interest Network**
  - What it does: Models user behavior interest.
  - Solves: E-commerce recommendation.

- **Two-Tower Model**
  - What it does: Learns user and item embeddings separately.
  - Solves: Large-scale retrieval.

- **Sequential Recommendation Model**
  - What it does: Uses user behavior sequence.
  - Solves: Next-item recommendation.

Example use cases:

- Recommend products to users.
- Recommend movies or videos.
- Rank search results.
- Predict click-through rate.

## 14. Speech Deep Learning Algorithms

Speech deep learning algorithms are used for audio, voice, and speech processing.

- **Convolutional Neural Network for Speech**
  - What it does: Extracts audio features.
  - Solves: Speech classification.

- **Recurrent Neural Network for Speech**
  - What it does: Processes audio sequences.
  - Solves: Speech recognition.

- **Connectionist Temporal Classification**
  - What it does: Aligns audio and text without exact timestamps.
  - Solves: Speech-to-text.

- **WaveNet**
  - What it does: Generates realistic speech audio.
  - Solves: Text-to-speech.

- **Transformer Speech Models**
  - What it does: Understands and generates speech sequences.
  - Solves: Speech recognition.

- **Whisper-style Models**
  - What it does: Converts speech into text.
  - Solves: Multilingual transcription.

Example use cases:

- Convert calls into text.
- Generate voice from text.
- Detect speaker emotion.
- Identify speakers.

## 15. Multimodal Deep Learning Algorithms

Multimodal deep learning is used when a system works with more than one data type, such as text, image, audio, or video.

- **Contrastive Language-Image Pretraining**
  - What it does: Connects images and text.
  - Solves: Image-text matching.

- **Vision-Language Models**
  - What it does: Understands both images and text.
  - Solves: Visual question answering.

- **Multimodal Transformer**
  - What it does: Processes text, image, audio, or video together.
  - Solves: Multimodal reasoning.

- **Image Captioning Models**
  - What it does: Generates text descriptions from images.
  - Solves: Image captioning.

- **Visual Question Answering Models**
  - What it does: Answers questions about images.
  - Solves: Image reasoning.

Example use cases:

- Ask questions about an image.
- Generate captions for images.
- Search images using text.
- Analyze documents with text and images.

## Most Common Deep Learning Algorithms in Real Projects

- **Image classification**
  - Use CNN, ResNet, or EfficientNet.

- **Object detection**
  - Use You Only Look Once or Faster R-CNN.

- **Image segmentation**
  - Use U-Net or Mask R-CNN.

- **Text classification**
  - Use Transformer or BERT.

- **Chatbot**
  - Use decoder-only Transformer or Large Language Model.

- **Document question answering**
  - Use Transformer or Retrieval Augmented Generation.

- **Text summarization**
  - Use encoder-decoder Transformer.

- **Time series forecasting**
  - Use LSTM, GRU, or Transformer.

- **Fraud detection**
  - Use ANN, Autoencoder, or Graph Neural Network.

- **Recommendation system**
  - Use Two-Tower Model or Neural Collaborative Filtering.

- **Speech-to-text**
  - Use Transformer Speech Models or Connectionist Temporal Classification.

- **Image generation**
  - Use Diffusion Model or Generative Adversarial Network.

- **Anomaly detection**
  - Use Autoencoder or Variational Autoencoder.

- **Graph relationship analysis**
  - Use Graph Neural Network.

## Interview-Friendly Summary

Deep learning mainly solves these types of problems:

- **Structured prediction**
  - Use Artificial Neural Networks.

- **Image understanding**
  - Use Convolutional Neural Networks.

- **Object detection**
  - Use You Only Look Once or Faster R-CNN.

- **Pixel-level image analysis**
  - Use U-Net or Mask R-CNN.

- **Sequential data understanding**
  - Use RNN or LSTM.

- **Text understanding**
  - Use transformer encoder models.

- **Text generation**
  - Use transformer decoder models.

- **Translation and summarization**
  - Use encoder-decoder transformer models.

- **Anomaly detection**
  - Use autoencoders.

- **Synthetic data generation**
  - Use GANs or diffusion models.

- **Graph-based relationship learning**
  - Use Graph Neural Networks.

- **Decision optimization**
  - Use Deep Reinforcement Learning.

- **Personalization**
  - Use deep recommendation models.

- **Speech processing**
  - Use speech transformers and recurrent networks.

- **Multimodal understanding**
  - Use vision-language models.

The most important deep learning algorithms to focus on are:

- Artificial Neural Networks
- Convolutional Neural Networks
- Recurrent Neural Networks
- Long Short-Term Memory Networks
- Transformers
- Autoencoders
- Generative Adversarial Networks
- Diffusion Models
- Graph Neural Networks
- Deep Reinforcement Learning models

## Interview Tip

When explaining a deep learning solution, begin with the data type and the business problem.

Example:

> Since the task is image classification, I would start with a Convolutional Neural Network. For higher accuracy, I would compare ResNet, EfficientNet, or Vision Transformer depending on the dataset size, speed requirement, and deployment environment.
