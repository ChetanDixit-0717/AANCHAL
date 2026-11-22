# AANCHAL 🌱
### AI-Assisted Nutrition & Child Health Awareness Layer

**An AI-powered child nutrition and health awareness platform designed for parents, caregivers, and Anganwadi workers.**

<p align="center">
  <b>Making child nutrition awareness accessible, understandable, and technology-driven.</b>
</p>

---

## 📌 About AANCHAL

AANCHAL is an AI-assisted child nutrition and health awareness platform that aims to simplify nutritional information and improve access to reliable health-related knowledge within communities.

The platform combines Optical Character Recognition (OCR), Large Language Models (LLMs), Retrieval-Augmented Generation (RAG), and Machine Learning to provide accessible, child-focused nutrition awareness.

Designed with the needs of parents, caregivers, and Anganwadi workers in mind, AANCHAL aims to bridge the gap between complex nutritional information and practical everyday understanding.

## 🎯 Objectives

- Simplify nutritional information available on packaged food labels.
- Provide child-focused nutrition awareness using AI.
- Enable knowledge-based responses to nutrition-related queries.
- Promote awareness regarding sugar content in food products.
- Improve access to childhood vaccination information.
- Explore ML-based child health risk prediction.

## ✨ Key Features

### 1. Nutrition Label Scanner (OCR + LLM)

- Extracts nutritional information from food label images using Tesseract OCR.
- Applies image preprocessing techniques to improve text recognition.
- Extracts nutritional values such as calories, fats, sugar, protein, sodium, and carbohydrates.
- Implements OCR confidence scoring to identify potentially inaccurate extractions.
- Flags low-confidence results for manual review.
- Uses Groq-powered LLM integration to generate child-focused nutritional awareness.
- Supports dynamic inputs such as child age and serving size.

### 2. Nutrition Awareness Chatbot

- AI-powered conversational interface for nutrition-related queries.
- Provides simple and understandable responses.
- Uses LangChain for LLM integration and prompt management.
- Supports context-aware nutrition conversations.

### 3. Knowledge-Based Responses (RAG)

- Retrieves relevant information from a structured nutrition knowledge base.
- Uses document loading and text-splitting pipelines.
- Generates embeddings for semantic retrieval.
- Uses vector storage and retrieval for relevant knowledge discovery.
- Implements evidence checking to improve response reliability.
- Combines retrieved knowledge with an LLM to generate contextual answers.

### 4. Sugar Label Checker

- Helps users understand sugar content in packaged food products.
- Provides simplified, child-focused sugar-related awareness.

### 5. Vaccination Awareness Module

- Provides childhood vaccination-related educational information.
- Aims to improve awareness of vaccination schedules.

### 6. Child Health Risk Prediction

- Explores Machine Learning-based child health risk assessment.
- Aims to identify potential health and nutritional risk indicators using relevant input parameters.

---

## 🛠️ Technology Stack

| Category | Technologies |
|---|---|
| Programming Language | Python |
| OCR | Tesseract OCR, Pytesseract |
| Image Processing | OpenCV, NumPy |
| LLM Provider | Groq API |
| LLM Framework | LangChain |
| Prompt Engineering | LangChain Prompt Templates |
| RAG | Document Processing, Text Chunking, Embeddings, Semantic Retrieval |
| Vector Database | ChromaDB |
| Data Processing | Python, NumPy |
| Testing | Pytest |
| Version Control | Git & GitHub |

*The frontend technology stack and additional ML technologies will be documented as their implementation progresses.*

## 🏗️ Project Architecture

```text
                         AANCHAL
                            |
                    Frontend Application
                            |
                     Backend Integration
                            |
              +-------------+-------------+
              |             |             |
         Nutrition      Nutrition      Health
          Scanner       Chatbot       Awareness
              |             |             |
             OCR           RAG        Future Modules
              |             |             |
        Text Extraction  Knowledge    Vaccination
              |          Retrieval    Awareness
        Nutrition Data      |             |
              |         Embeddings    Sugar Checker
              |             |             |
              +-------------+        ML Prediction
                            |
                       Groq LLM API
                            |
                    AI-Generated Responses
```

## 📂 Project Structure

```text
AANCHAL/
│
├── chatbot/
│   ├── __init__.py
│   ├── chatbot.py
│   └── prompt_templates.py
│
├── data/
│   ├── knowledge_base/
│   │   ├── anganwadi_guidelines/
│   │   ├── child_nutrition/
│   │   ├── complementary_feeding/
│   │   ├── food_label_awareness/
│   │   ├── food_safety/
│   │   ├── nutrients/
│   │   └── source_registry.md
│   │
│   ├── sample_images/
│   │
│   └── vector_store/
│
├── docs/
│
├── llm/
│   ├── __init__.py
│   ├── model_loader.py
│   ├── nutrition_analyzer.py
│   ├── output_parser.py
│   └── prompt_templates.py
│
├── notebooks/
│   ├── image_processing_exploration.ipynb
│   └── image_processing_experiments.ipynb
│
├── ocr/
│   ├── __init__.py
│   ├── image_loader.py
│   ├── image_preprocessing.py
│   ├── nutrition_extractor.py
│   ├── pipeline.py
│   └── text_recognizer.py
│
├── outputs/
│
├── rag/
│   ├── __init__.py
│   ├── document_loader.py
│   ├── embedding_model.py
│   ├── evidence_checker.py
│   ├── qa_pipeline.py
│   ├── retriever.py
│   ├── text_splitter.py
│   └── vector_store.py
│
├── tests/
│
├── .env
├── .gitattributes
├── .gitignore
└── requirements.txt
```

## ⚙️ Installation & Setup

### 1. Clone the Repository

```bash
git clone https://github.com/ChetanDixit-0717/AANCHAL.git
cd AANCHAL
```

### 2. Create a Virtual Environment

```bash
python -m venv .venv
```

Activate the environment:

**Windows (PowerShell):**

```powershell
.venv\Scripts\Activate.ps1
```

### 3. Install Dependencies

```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
```

### 4. Install Tesseract OCR

Install Tesseract OCR separately on your system.

Ensure that its executable is accessible through the system PATH or configure its location using the `TESSERACT_CMD` environment variable.

### 5. Configure Environment Variables

Create a `.env` file in the project root:

```env
GROQ_API_KEY=your_groq_api_key
```

Keep API credentials private. Never commit `.env` to GitHub.

### 6. Run Tests

Run the project tests using:

```bash
pytest tests/
```

*Individual modules can be tested independently during development.*

---

## 🚧 Development Progress

AANCHAL is being developed in 11 milestones.

| # | Milestone | Status |
|---|---|---|
| 1 | Project Setup & Environment | ✅ Completed |
| 2 | OCR – Nutrition Label Extraction | ✅ Completed |
| 3 | LLM Integration & Prompt Engineering | ✅ Completed |
| 4 | Nutrition Awareness Chatbot | ✅ Completed |
| 5 | Knowledge-Based Responses (RAG) | ✅ Completed |
| 6 | Sugar Label Checking | 🔄 Next |
| 7 | Vaccination Awareness Module | ⏳ Pending |
| 8 | Child Health Risk Prediction | ⏳ Pending |
| 9 | Module Integration | ⏳ Pending |
| 10 | Testing, Validation & Bug Fixes | ⏳ Pending |
| 11 | Documentation & Final Presentation | ⏳ Pending |

**Current progress: 5 of 11 milestones completed.**

---

## 🔮 Future Scope

- Complete frontend and backend integration.
- Improve OCR accuracy across different food label formats.
- Expand the verified nutrition knowledge base.
- Introduce multilingual chatbot support.
- Develop sugar label checking capabilities.
- Integrate childhood vaccination awareness.
- Implement ML-based child health risk prediction.
- Improve accessibility for rural and underserved communities.

## ⚠️ Important Disclaimer

AANCHAL is an educational and awareness-oriented project. It is not intended to replace professional medical advice, diagnosis, or treatment.

Nutritional information printed on food labels may use adult-based reference values. Such values should not automatically be interpreted as children's daily nutritional requirements.

AI-generated responses and extracted information should be reviewed appropriately, particularly when dealing with child health-related concerns.

## 👥 Project Team

**Institution:** VIT Bhopal University

**Project Domain:** Artificial Intelligence & Machine Learning

**Team Members:**

- Chetan Dixit

---

## 🔗 Repository

GitHub: [ChetanDixit-0717/AANCHAL](https://github.com/ChetanDixit-0717/AANCHAL)

---

<p align="center">
  <b>AANCHAL 🌱</b><br/>
  <i>Making child nutrition awareness more accessible, one step at a time.</i>
</p>
