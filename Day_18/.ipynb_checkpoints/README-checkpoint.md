# Day 18: Chat with Your Knowledge Base - Building a Powerful RAG Chatbot

## Project Overview

This project implements a Retrieval-Augmented Generation (RAG) chatbot system designed to answer questions about hospital patient reviews. The assignment demonstrates the ability to build an intelligent question-answering system that can produce either intentionally incorrect answers or high-quality accurate responses based on a knowledge base of hospital reviews.

The implementation uses entirely free and open-source technologies, requiring no API keys, and is optimized for execution in Google Colab environments.

## Assignment Requirements

The assignment goal was to build a RAG chatbot capable of producing either:
- **1 incorrect answer** (intentionally wrong response)
- **5 really amazing answers** (high-quality, accurate responses)

**Implementation Constraints:**
- 100% free (no API keys required)
- Optimized for Google Colab
- Uses open-source models and libraries

## Technical Architecture

### RAG Pipeline Components

1. **Document Processing**
   - CSV data loading with fallback to sample data
   - Document creation with metadata (review_id, physician, hospital, patient)
   - Text preparation for embedding

2. **Vector Embeddings**
   - Model: `sentence-transformers/all-MiniLM-L6-v2`
   - Embedding dimension: 384
   - Efficient CPU-based processing

3. **Vector Database**
   - ChromaDB for persistent vector storage
   - Similarity-based retrieval
   - Top-k retrieval (k=5)

4. **Language Model**
   - Model: `gpt2` (HuggingFace)
   - Text generation pipeline
   - Temperature-controlled sampling

5. **Prompt Engineering**
   - Custom prompts for amazing answers
   - Intentionally misleading prompts for incorrect answers
   - Context-aware question answering

## Project Structure

```
Day_18/
├── Day_18_Assignment_RAG_Chatbot_WORKING.ipynb    # Main assignment notebook
├── 18_Chat_with_Your_Knowledge_Base_Building_a_Powerful_RAG_Chatbot/
│   ├── 18_Chat_with_Your_Knowledge_Base_Building_a_Powerful_RAG_Chatbot.ipynb
│   └── reviews.csv                                 # Hospital reviews dataset (1005 reviews)
└── README.md                                       # This file
```

## Dataset Description

The project uses a hospital patient reviews dataset containing:
- **Total Reviews:** 1,005 patient reviews
- **Hospitals:** Wallace-Hamilton, Bell Mcknight and Willis, and others
- **Fields:**
  - `review_id`: Unique identifier for each review
  - `visit_id`: Hospital visit identifier
  - `review`: Patient review text
  - `physician_name`: Name of the attending physician
  - `hospital_name`: Name of the hospital
  - `patient_name`: Name of the patient

## Installation and Setup

### Prerequisites

- Python 3.7 or higher
- Google Colab (recommended) or local Jupyter environment
- Minimum 4GB RAM (8GB recommended)

### Required Dependencies

```bash
pip install langchain langchain-community langchain-chroma
pip install transformers torch sentence-transformers
pip install langchain-huggingface pandas numpy
```

### Installation in Google Colab

The notebook includes automated installation cells that handle all dependencies:

```python
!pip install -q langchain langchain-community langchain-chroma
!pip install -q transformers torch sentence-transformers
!pip install -q langchain-huggingface pandas numpy
```

## Usage Instructions

### Running in Google Colab

1. Open the notebook in Google Colab
2. Execute cells sequentially from top to bottom
3. Optional: Upload your own `reviews.csv` file when prompted
4. The system will automatically:
   - Install dependencies
   - Load and process data
   - Create vector embeddings
   - Initialize the language model
   - Set up the RAG pipeline

### Using the Assignment Chatbot

The main interface is the `assignment_chatbot()` function:

```python
# Generate 1 incorrect answer
result = assignment_chatbot("What do patients say about the medical staff?", mode="incorrect")

# Generate 5 amazing answers
result = assignment_chatbot("What do patients say about the medical staff?", mode="amazing")

# Random mode (randomly chooses between incorrect or amazing)
result = assignment_chatbot("What do patients say about the medical staff?", mode="random")
```

### Response Format

The function returns a dictionary containing:
```python
{
    'success': True/False,
    'mode': 'incorrect' or 'amazing',
    'count': 1 or 5,
    'answers': [list of answer strings],
    'execution_time': float (seconds),
    'message': 'Success' or error message
}
```

## Implementation Details

### Vector Database Creation

```python
# Create documents from reviews
documents = []
for _, row in df.iterrows():
    doc = Document(
        page_content=row['review'],
        metadata={
            'review_id': row['review_id'],
            'physician': row['physician_name'],
            'hospital': row['hospital_name'],
            'patient': row['patient_name']
        }
    )
    documents.append(doc)

# Create vector store
vectorstore = Chroma.from_documents(
    documents=documents,
    embedding=embeddings,
    persist_directory="./chroma_db"
)
```

### Retrieval Configuration

```python
retriever = vectorstore.as_retriever(
    search_type="similarity",
    search_kwargs={"k": 5}
)
```

### Prompt Templates

**Amazing Answers Prompt:**
```
Context: {context}

Question: {question}

Based on the hospital reviews provided, give a comprehensive and accurate answer.
```

**Incorrect Answers Prompt:**
```
Context: {context}

Question: {question}

Provide an intentionally incorrect answer that contradicts the reviews.
```

## Key Features

1. **Dual-Mode Operation**
   - Incorrect mode: Generates intentionally wrong answers
   - Amazing mode: Generates 5 high-quality accurate answers

2. **No API Keys Required**
   - Uses only free, open-source models
   - No external API dependencies
   - Fully self-contained

3. **Google Colab Optimized**
   - File upload widget integration
   - Memory-efficient model loading
   - CPU-optimized processing

4. **Robust Data Handling**
   - Automatic fallback to sample data
   - Multiple file path resolution
   - Error handling and validation

5. **Performance Metrics**
   - Execution time tracking
   - Success/failure reporting
   - Answer count validation

## Example Outputs

### Incorrect Answer Mode

```
Question: What do patients say about the medical staff?

INCORRECT ANSWER:
The medical staff at the hospital is terrible and unprofessional. 
Patients consistently report poor care and lack of attention.
```

### Amazing Answers Mode

```
Question: What do patients say about the medical staff?

AMAZING ANSWERS (5 total):

1. The medical staff at the hospital were incredibly attentive and supportive 
   during patient stays, with facilities that were top-notch.

2. Patients appreciated the hospital's commitment to patient education, with 
   the medical team taking time to explain diagnoses and treatment options.

3. The medical team was exceptional, with state-of-the-art facilities, though 
   some patients noted noise levels in shared rooms.

4. The nursing staff was caring and the hospital had a calming ambiance, 
   creating a positive healing environment.

5. Patients were grateful for the compassionate care received, with the 
   medical team being thorough in their approach.
```

## Technical Specifications

### Models Used

- **Embedding Model:** sentence-transformers/all-MiniLM-L6-v2
  - Dimension: 384
  - Type: Sentence transformer
  - License: Apache 2.0

- **Language Model:** gpt2
  - Parameters: 124M
  - Type: Autoregressive language model
  - License: MIT

### Performance Characteristics

- **Vector Database:** ChromaDB (local, persistent)
- **Retrieval Method:** Similarity search
- **Top-k Documents:** 5
- **Generation Parameters:**
  - Max new tokens: 100
  - Temperature: 0.7
  - Sampling: Enabled

## Limitations and Considerations

1. **Model Size:** Uses smaller models (GPT-2) for Colab compatibility
2. **Generation Quality:** Limited by model size and context window
3. **Processing Speed:** CPU-based processing may be slower than GPU
4. **Context Length:** Limited to 5 retrieved documents per query
5. **Language:** English-only support

## Future Enhancements

Potential improvements for the system:
- Integration with larger language models (e.g., Llama 2, Mistral)
- GPU acceleration support
- Multi-language support
- Advanced retrieval strategies (hybrid search, re-ranking)
- User interface with Gradio or Streamlit
- Conversation history and context management
- Fine-tuning on domain-specific data

## Assignment Completion Status

**Status:** FULLY COMPLETED

All requirements have been successfully implemented:
- RAG chatbot architecture: Complete
- Incorrect answer generation: Working
- 5 amazing answers generation: Working
- No API keys required: Confirmed
- Google Colab optimization: Implemented
- Execution outputs: Verified

## References and Resources

- LangChain Documentation: https://python.langchain.com/
- HuggingFace Transformers: https://huggingface.co/docs/transformers/
- ChromaDB Documentation: https://docs.trychroma.com/
- Sentence Transformers: https://www.sbert.net/

## License

This project is part of an educational assignment and uses open-source libraries under their respective licenses.

