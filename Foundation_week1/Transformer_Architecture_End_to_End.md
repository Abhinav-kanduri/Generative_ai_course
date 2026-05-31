# Transformer Architecture End to End

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
- [Deep Learning algorithms](Deep_Learning_Algorithms.md)
- [Transformer model families](Transformer_Model_Families.md)

This README explains **Transformer architecture** from the ground up:

- Why Transformers came into picture
- What problem they solved
- How the architecture works internally
- How encoder, decoder, and attention fit together
- Why Transformers became the foundation of Large Language Models
- Important research papers to know

## 1. Why Transformers Came Into Picture

Before Transformers, most Natural Language Processing systems used recurrent or sequence-based models.

Earlier architectures included:

- **Recurrent Neural Network**
  - Problem: Processes text word by word, so training is slow.

- **Long Short-Term Memory Network**
  - Problem: Has better memory than a basic RNN, but still processes sequentially.

- **Gated Recurrent Unit**
  - Problem: Faster than LSTM, but still struggles with very long context.

- **Sequence-to-sequence encoder-decoder models**
  - Problem: Useful for translation, but compresses the whole input into limited hidden states.

- **Attention-based recurrent models**
  - Problem: Improved alignment, but still depended on recurrent sequential processing.

The major problem was:

> Language is not always understood word by word. Sometimes one word depends on another word far away in the sentence.

Example:

> The customer cancelled the credit card because it was stolen.

Here, the model must understand that **it** refers to **credit card**, not **customer**.

Older RNN and LSTM models process tokens one after another. That makes them slower to train and weaker at capturing long-distance relationships.

Attention mechanisms were introduced before Transformers to help models align important words during translation. Bahdanau attention showed that learning to align and translate improved neural machine translation compared with basic encoder-decoder approaches.

The Transformer paper, **Attention Is All You Need**, introduced an architecture based only on attention mechanisms, removing recurrence and convolution entirely. This allowed models to process tokens more in parallel and capture relationships between words more directly.

## 2. Simple One-Line Definition

A **Transformer** is a deep learning architecture that understands relationships between tokens using **self-attention**, instead of reading a sentence only one word at a time.

## 3. What Problem Transformers Solved

Transformers solved several major problems from earlier architectures:

- **Sequential processing was slow**
  - Transformer solution: Process tokens in parallel during training.

- **Long sentences were difficult**
  - Transformer solution: Self-attention connects every token with every other token.

- **Earlier models forgot far-away context**
  - Transformer solution: Attention scores decide which tokens matter most.

- **Translation and summarization needed better alignment**
  - Transformer solution: Encoder-decoder attention improves source-target alignment.

- **Scaling models was difficult**
  - Transformer solution: Transformer architecture scales well into Large Language Models.

## 4. Transformer Architecture End to End

The original Transformer has two major parts:

1. **Encoder**
2. **Decoder**

The encoder understands the input sentence.

The decoder generates the output sentence.

Full flow:

```text
Input Sentence
  v
Tokenization
  v
Token Embeddings
  v
Positional Encoding
  v
Encoder Block 1
  v
Encoder Block 2
  v
Encoder Block N
  v
Decoder Block 1
  v
Decoder Block 2
  v
Decoder Block N
  v
Linear Layer
  v
Softmax
  v
Predicted Output Token
```

## 5. Example Sentence

Example sentence:

> The customer reported that the card was stolen.

The Transformer first breaks it into tokens:

```text
["The", "customer", "reported", "that", "the", "card", "was", "stolen"]
```

Then each token is converted into a numerical vector called an **embedding**.

Embeddings capture meaning, but embeddings alone do not know word order. So the Transformer adds **positional encoding**.

Without position:

```text
customer reported card stolen
```

With position:

```text
1-The
2-customer
3-reported
4-that
5-the
6-card
7-was
8-stolen
```

This helps the model understand both:

1. Meaning of each word
2. Position of each word in the sentence

## 6. Core Component: Self-Attention

Self-attention answers one important question:

> For each token, which other tokens in the sentence are important?

Example:

> The customer reported that the card was stolen.

When the model looks at the word **stolen**, it should pay more attention to:

```text
card
reported
customer
```

It should pay less attention to:

```text
the
that
was
```

Self-attention gives different importance scores to different words.

The core attention formula from the Transformer is:

```text
Attention(Q, K, V) = softmax((Q * K^T) / sqrt(d_k)) * V
```

Meaning of each term:

- **Query**
  - What the current token is looking for.

- **Key**
  - What each token offers.

- **Value**
  - The actual information carried by each token.

- **Softmax**
  - Converts scores into attention weights.

Simple meaning:

> Query asks a question, Key checks relevance, and Value provides the information.

## 7. Query, Key, and Value Example

Sentence:

> The card was stolen.

For the word **stolen**:

- **Query**
  - "What thing was stolen?"

- **Key**
  - Each word says, "I may be relevant."

- **Value**
  - The actual meaning of each word.

- **Strong attention**
  - card

- **Weak attention**
  - the
  - was

So the model learns that **stolen** is strongly connected to **card**.

## 8. Multi-Head Attention

One attention head may focus on grammar.

Another attention head may focus on meaning.

Another attention head may focus on entity relationships.

Example sentence:

> The customer reported that the card was stolen.

Possible attention heads:

- **Head 1**
  - Focus: Subject, such as customer.

- **Head 2**
  - Focus: Object, such as card.

- **Head 3**
  - Focus: Event, such as stolen.

- **Head 4**
  - Focus: Relationship between card and stolen.

This is why it is called **multi-head attention**.

Instead of learning only one relationship pattern, the Transformer learns many relationship patterns at the same time.

## 9. Encoder Block

The encoder is responsible for understanding the input.

Each encoder block follows this flow:

```text
Input
  v
Multi-Head Self-Attention
  v
Add and Normalize
  v
Feed-Forward Neural Network
  v
Add and Normalize
  v
Encoder Output
```

Encoder responsibilities:

- **Self-attention**
  - Understand relationships between words.

- **Add and normalize**
  - Stabilize training.

- **Feed-forward network**
  - Learn deeper transformations.

- **Stacked encoder layers**
  - Build deeper understanding.

In models like **BERT**, the encoder is used to deeply understand text by looking at both left and right context. The BERT paper introduced deep bidirectional Transformer pretraining for language understanding tasks.

## 10. Decoder Block

The decoder generates output one token at a time.

Each decoder block follows this flow:

```text
Previous Output Tokens
  v
Masked Multi-Head Self-Attention
  v
Add and Normalize
  v
Encoder-Decoder Attention
  v
Add and Normalize
  v
Feed-Forward Neural Network
  v
Add and Normalize
  v
Decoder Output
```

## 11. Why Masked Attention Is Needed

During generation, the model should not see future words.

Example:

> The card was ___

The model should predict **stolen** without already seeing the word **stolen**.

So masked self-attention hides future tokens.

This is the foundation of decoder-only models like GPT-style language models. GPT-2 used a large Transformer language model trained on WebText and showed strong zero-shot behavior across language modeling tasks.

## 12. Encoder-Only, Decoder-Only, and Encoder-Decoder Transformers

Modern Transformer models come in three major types.

### Encoder-Only Transformers

Examples:

- BERT-style models

Best for:

- Text classification
- Sentiment analysis
- Entity extraction
- Semantic search

How they work:

- Read the full input.
- Understand context from both left and right sides.
- Produce representations useful for understanding tasks.

### Decoder-Only Transformers

Examples:

- GPT-style models

Best for:

- Chatbots
- Text generation
- Code generation
- Next-token prediction

How they work:

- Generate text one token at a time.
- Use masked attention so future tokens are hidden.

### Encoder-Decoder Transformers

Examples:

- Text-to-Text Transfer Transformer, or T5

Best for:

- Translation
- Summarization
- Question answering

How they work:

- Encoder understands the input.
- Decoder generates the output.

The T5 paper unified many NLP tasks into a text-to-text format, covering summarization, question answering, classification, and more.

## 13. End-to-End Transformer Flow With Example

Task:

> Translate "I love machine learning" into another language.

Step-by-step flow:

```text
Input:
"I love machine learning"

Step 1: Tokenization
["I", "love", "machine", "learning"]

Step 2: Embeddings
Each token becomes a vector.

Step 3: Positional Encoding
The model learns token order.

Step 4: Encoder Self-Attention
Each word attends to other words.
"machine" attends to "learning".
"love" attends to "I".

Step 5: Encoder Output
The input sentence meaning is represented.

Step 6: Decoder Starts
The decoder begins with a start token.

Step 7: Masked Self-Attention
The decoder predicts one word at a time.

Step 8: Encoder-Decoder Attention
The decoder looks back at encoder output.

Step 9: Softmax
The model chooses the most probable next word.

Step 10: Final Output
The translated sentence is generated.
```

## 14. Why Transformers Became the Foundation of Large Language Models

Transformers became the foundation of modern AI because they are:

- **Parallelizable**
  - Faster to train compared with recurrent models.

- **Scalable**
  - Can be trained with large datasets and large parameter counts.

- **Context-aware**
  - Every token can attend to every other token.

- **Flexible**
  - Works for text, images, audio, video, code, and multimodal data.

- **Transferable**
  - Can be pretrained once and then fine-tuned or prompted for many tasks.

This is why Transformer architecture became the foundation for:

- BERT-style models
- GPT-style models
- T5
- Transformer-XL
- Longformer
- Vision Transformer
- Modern Large Language Models

## 15. Important Research Papers on Transformers

### Foundational Papers

- **Neural Machine Translation by Jointly Learning to Align and Translate**
  - Why it matters: Introduced attention-based alignment for translation before Transformers.
  - Link: https://arxiv.org/abs/1409.0473

- **Attention Is All You Need**
  - Why it matters: Introduced the Transformer architecture and removed recurrence and convolution.
  - Link: https://arxiv.org/abs/1706.03762

- **BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding**
  - Why it matters: Popularized encoder-only Transformers for language understanding.
  - Link: https://arxiv.org/abs/1810.04805

- **Language Models are Unsupervised Multitask Learners**
  - Why it matters: Showed strong decoder-only Transformer language modeling and zero-shot behavior.
  - Link: https://cdn.openai.com/better-language-models/language_models_are_unsupervised_multitask_learners.pdf

- **Exploring the Limits of Transfer Learning with a Unified Text-to-Text Transformer**
  - Why it matters: Unified many NLP tasks into a text-to-text format.
  - Link: https://arxiv.org/abs/1910.10683

### Advanced Transformer Papers

- **Transformer-XL: Attentive Language Models Beyond a Fixed-Length Context**
  - Main contribution: Added segment-level recurrence and improved long-context language modeling.
  - Link: https://arxiv.org/abs/1901.02860

- **Longformer: The Long-Document Transformer**
  - Main contribution: Introduced attention that scales linearly for long documents.
  - Link: https://arxiv.org/abs/2004.05150

- **An Image is Worth 16x16 Words: Transformers for Image Recognition at Scale**
  - Main contribution: Applied pure Transformer architecture to image patches for computer vision.
  - Link: https://arxiv.org/abs/2010.11929

Transformer-XL addressed fixed-length context limitations using segment-level recurrence and new positional encoding.

Longformer addressed the quadratic cost of self-attention for long documents using local and global attention patterns.

Vision Transformer showed that a pure Transformer could work well for image classification by treating image patches like tokens.

## 16. Best Interview Explanation

You can explain Transformers like this:

> Transformers came into picture because earlier RNN and LSTM models processed text sequentially, which made training slow and made it difficult to capture long-range dependencies. The Transformer solved this by using self-attention, where every token can directly attend to every other token in the sentence. This allows the model to understand context better and train more efficiently in parallel.
>
> The architecture starts with tokenization, then token embeddings and positional encodings are added. The encoder uses multi-head self-attention and feed-forward layers to understand the input. The decoder uses masked self-attention, encoder-decoder attention, and feed-forward layers to generate output one token at a time. This architecture became the foundation for modern Large Language Models, including encoder-only models like BERT, decoder-only models like GPT-style systems, and encoder-decoder models like T5.

## 17. Simple Memory Trick

Remember Transformer using this flow:

```text
Tokens
  v
Embeddings
  v
Position
  v
Attention
  v
Multi-Head Attention
  v
Feed-Forward Network
  v
Encoder or Decoder
  v
Softmax
  v
Output
```

Remember why Transformers came:

```text
Recurrent models were slow and struggled with long context.
Transformers used attention to understand all token relationships directly.
```

The most important paper to start with is **Attention Is All You Need**, because it is the original Transformer paper and the base for most modern Large Language Model architectures.

## Quick Revision Notes

- Transformer is based on attention, not recurrence.
- Self-attention compares every token with every other token.
- Multi-head attention learns different types of relationships at the same time.
- Positional encoding gives the model word order.
- Encoder understands input.
- Decoder generates output.
- Masked attention prevents the decoder from seeing future tokens.
- Encoder-only models are best for understanding.
- Decoder-only models are best for generation.
- Encoder-decoder models are best for transformation tasks like translation and summarization.
