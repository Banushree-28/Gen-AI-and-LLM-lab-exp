# 🤖 GenAI and LLM Laboratory

This repository contains the implementations of the **Generative AI and Large Language Models (GenAI & LLM) Laboratory** experiments.

The experiments cover text generation, prompt engineering, conversational AI, summarization, sentiment analysis, RAG, code generation, image generation, multimodal AI, model fine-tuning, multimedia content generation, and deployment of Generative AI applications.

## 📚 Experiments

| No. | Experiment                                                                          | Main Concept / Technology             |
| --- | ----------------------------------------------------------------------------------- | ------------------------------------- |
| 1   | Text Generation Using Pre-Trained Foundation Models                                 | GPT-2, Hugging Face Transformers      |
| 2   | Prompt Engineering Techniques for Content Generation, Reasoning and Task Automation | Zero-shot, Few-shot, Chain-of-Thought |
| 3   | Conversational AI Chatbot Using Transformer-Based Language Models                   | DialoGPT                              |
| 4   | Text Summarization and Question-Answering System Using LLMs                         | BART, DistilBERT                      |
| 5   | Sentiment Analysis and Document Classification                                      | DistilBERT, BART-MNLI                 |
| 6   | Retrieval-Augmented Generation (RAG) System                                         | Sentence Transformers, FAISS, FLAN-T5 |
| 7   | AI-Powered Code Generation and Debugging Assistant                                  | CodeGen                               |
| 8   | Image Generation Application Using Diffusion Models                                 | Stable Diffusion                      |
| 9   | Multimodal AI Application Integrating Text and Image Inputs                         | BLIP                                  |
| 10  | Fine-Tuning a Pre-Trained Language Model                                            | DistilBERT, IMDB Dataset              |
| 11  | AI-Based Content Generation for Text, Image and Multimedia                          | FLAN-T5, Stable Diffusion, gTTS       |
| 12  | Deployment and Evaluation of a Generative AI Application                            | Gradio, Transformers, ROUGE           |

---

## 🛠️ Technologies Used

* **Python 3.9+**
* Hugging Face Transformers
* PyTorch
* Diffusers
* Sentence Transformers
* FAISS
* LangChain
* Datasets
* Scikit-learn
* Pillow
* gTTS
* Gradio
* Evaluate
* ROUGE
* Jupyter Notebook / Google Colab / VS Code

---

## 🔬 Experiment Details

### 1. Text Generation Using Pre-Trained Foundation Models

A text generation application is developed using the **GPT-2** foundation model and Hugging Face Transformers.

**Concepts Covered:**

* Foundation Models
* GPT-2
* Text generation
* Greedy decoding
* Sampling
* Temperature
* Top-k sampling
* Top-p / Nucleus sampling

---

### 2. Prompt Engineering Techniques

Different prompting strategies are implemented and compared using a Large Language Model.

**Techniques Covered:**

* Zero-shot prompting
* One-shot prompting
* Few-shot prompting
* Chain-of-Thought prompting
* Content generation
* Reasoning
* Task automation

The experiment demonstrates how prompt structure can influence the quality of an LLM's output.

---

### 3. Conversational AI Chatbot

A multi-turn conversational chatbot is developed using **Microsoft DialoGPT**.

**Concepts Covered:**

* Transformer-based language models
* Dialogue generation
* Conversation history
* Multi-turn conversations
* Sampling and beam-search concepts

The chatbot maintains previous conversation context while generating responses.

---

### 4. Text Summarization and Question Answering

A system combining **text summarization** and **question answering** is implemented using pre-trained transformer models.

**Models Used:**

* `facebook/bart-large-cnn`
* `distilbert-base-cased-distilled-squad`

**Tasks:**

* Abstractive text summarization
* Extractive question answering
* Confidence score generation

---

### 5. Sentiment Analysis and Document Classification

Pre-trained foundation models are used for sentiment analysis and zero-shot document classification.

**Models Used:**

* `distilbert-base-uncased-finetuned-sst-2-english`
* `facebook/bart-large-mnli`

**Tasks:**

* Positive/negative sentiment classification
* Multi-class document classification
* Zero-shot classification
* Confidence score analysis

---

### 6. Retrieval-Augmented Generation (RAG)

A basic **RAG system** is implemented by combining document retrieval with LLM-based generation.

**Technologies Used:**

* Sentence Transformers
* FAISS
* Hugging Face Transformers
* FLAN-T5

**Workflow:**

```text
Documents
    ↓
Text Chunks
    ↓
Embeddings
    ↓
FAISS Vector Database
    ↓
Similarity Search
    ↓
Relevant Context
    ↓
LLM
    ↓
Grounded Answer
```

RAG allows the model to generate answers based on retrieved external knowledge and helps reduce hallucination.

---

### 7. AI-Powered Code Generation and Debugging Assistant

A code-generation model is used to generate Python code from natural-language instructions and assist with debugging.

**Model Used:**

* `Salesforce/codegen-350M-mono`

**Tasks:**

* Natural-language-to-code generation
* Code completion
* Bug identification
* Code correction
* Code explanation

---

### 8. Image Generation Using Diffusion Models

A text-to-image generation application is implemented using **Stable Diffusion**.

**Model Used:**

* `runwayml/stable-diffusion-v1-5`

**Concepts Covered:**

* Diffusion models
* Forward noising process
* Reverse denoising process
* Text conditioning
* Guidance scale
* Image generation

A GPU-enabled environment such as Google Colab is recommended for this experiment.

---

### 9. Multimodal AI Application

A multimodal AI application is developed using **BLIP** to process both image and text inputs.

**Tasks:**

* Image captioning
* Visual Question Answering (VQA)

**Models Used:**

* `Salesforce/blip-image-captioning-base`
* `Salesforce/blip-vqa-base`

**Workflow:**

```text
Input Image
     ↓
Vision Encoder
     ↓
Visual Features
     ↓
       ┌───────────────┐
       ↓               ↓
Image Captioning    Question Answering
       ↓               ↓
    Text Output     Answer
```

---

### 10. Fine-Tuning a Pre-Trained Language Model

A pre-trained **DistilBERT** model is fine-tuned for sentiment classification using the IMDB dataset.

**Technologies Used:**

* DistilBERT
* Hugging Face Datasets
* Transformers Trainer
* PyTorch
* Scikit-learn

**Process:**

```text
Pre-trained DistilBERT
        ↓
Domain-specific Dataset
        ↓
Tokenization
        ↓
Fine-Tuning
        ↓
Evaluation
        ↓
Fine-Tuned Model
```

The experiment demonstrates transfer learning and task-specific model adaptation.

---

### 11. AI-Based Multimedia Content Generation

An integrated Generative AI pipeline is developed to generate **text, image, and audio** from a single topic.

**Models / Libraries Used:**

* FLAN-T5 for text generation
* Stable Diffusion for image generation
* gTTS for text-to-speech

**Workflow:**

```text
User Topic
    ↓
Text Generation
    ↓
Generated Text
    ├──────────────→ Image Generation
    │                       ↓
    │                  Generated Image
    │
    └──────────────→ Text-to-Speech
                            ↓
                     Generated Audio
```

The final output is a multimedia content package containing text, image, and audio.

---

### 12. Deployment and Evaluation of a Generative AI Application

A Generative AI application is deployed as an interactive web application using **Gradio** and evaluated using ROUGE metrics.

**Technologies Used:**

* Gradio
* Hugging Face Transformers
* Evaluate
* ROUGE
* Hugging Face Spaces / cloud APIs

**Application Workflow:**

```text
User Input
    ↓
Gradio Interface
    ↓
AI Model
    ↓
Generated Output
    ↓
ROUGE Evaluation
```

The experiment demonstrates the complete lifecycle of a Generative AI application from model inference to deployment and evaluation.

---

## ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/<your-username>/<your-repository-name>.git
cd <your-repository-name>
```

Install the required Python packages:

```bash
pip install transformers torch
pip install sentence-transformers faiss-cpu
pip install diffusers accelerate
pip install datasets scikit-learn
pip install pillow
pip install gtts
pip install gradio evaluate rouge_score
pip install langchain
```

Some experiments may require additional dependencies depending on the execution environment.

---

## 💻 Recommended Environment

The experiments can be executed using:

* **Google Colab**
* **Jupyter Notebook**
* **VS Code**

For computationally intensive experiments such as **Stable Diffusion and model fine-tuning**, a GPU-enabled environment such as Google Colab is recommended.

---

## 📁 Repository Structure

A recommended repository structure is:

```text
GenAI-LLM-Lab/
│
├── README.md
│
├── Experiment-01-Text-Generation/
│   └── experiment_01.ipynb
│
├── Experiment-02-Prompt-Engineering/
│   └── experiment_02.ipynb
│
├── Experiment-03-Chatbot/
│   └── experiment_03.ipynb
│
├── Experiment-04-Summarization-QA/
│   └── experiment_04.ipynb
│
├── Experiment-05-Sentiment-Classification/
│   └── experiment_05.ipynb
│
├── Experiment-06-RAG/
│   └── experiment_06.ipynb
│
├── Experiment-07-Code-Assistant/
│   └── experiment_07.ipynb
│
├── Experiment-08-Image-Generation/
│   └── experiment_08.ipynb
│
├── Experiment-09-Multimodal-AI/
│   └── experiment_09.ipynb
│
├── Experiment-10-Fine-Tuning/
│   └── experiment_10.ipynb
│
├── Experiment-11-Multimedia-Generation/
│   └── experiment_11.ipynb
│
└── Experiment-12-Deployment-Evaluation/
    └── experiment_12.ipynb
```

---

## 🎯 Learning Outcomes

After completing these experiments, the following concepts are explored:

* Understanding Generative AI and Foundation Models
* Working with Large Language Models
* Text generation using pre-trained models
* Prompt engineering techniques
* Building conversational AI systems
* Text summarization and question answering
* Sentiment and document classification
* Retrieval-Augmented Generation
* Vector databases and embeddings
* AI-assisted code generation and debugging
* Diffusion-based image generation
* Multimodal AI
* Fine-tuning transformer models
* Text-to-speech generation
* Generative AI application deployment
* Model evaluation using NLP metrics

---

## 📌 Notes

* Model downloads may require an internet connection during the first execution.
* Some Hugging Face models may require significant RAM or GPU memory.
* Stable Diffusion and fine-tuning experiments are better suited for GPU environments.
* API-based implementations may require valid API credentials.
* Generated outputs can vary between executions depending on the model and generation parameters.

---

## 👩‍💻 Author

**Banu Shree**

Generative AI & LLM Laboratory
Computer Science / Data Science

---

⭐ If you find this repository useful, consider giving it a star!
