# Day 14: Custom GPT Text Generation and Code-Focused Inference

## Project Overview

This project explores advanced natural language processing through two main components: building a custom GPT-style text generation engine and implementing a specialized Python code-focused inference system. The project demonstrates comprehensive understanding of transformer architectures, training pipelines, and practical deployment of language models for specific domain applications.

## Objective

To implement and demonstrate advanced NLP techniques:
- Build and train a custom GPT-2 style language model from scratch
- Implement domain-specific filtering for Python coding assistance
- Deploy pre-trained transformer models for specialized inference tasks
- Create robust text generation systems with proper evaluation and testing
- Understand the complete pipeline from model training to practical deployment

## Dataset Information

### TinyStories Dataset
- **Source**: `roneneldan/TinyStories` via Hugging Face Datasets
- **Purpose**: Training compact language models for story generation
- **Total Samples**: 2,119,719 short children's stories
- **Training Subset**: Streaming dataset with configurable batch processing
- **Content**: Simple narratives designed for small language model training
- **Format**: Text stories with consistent structure and vocabulary

### Model Architectures
- **Custom GPT-2**: Small-scale transformer for story generation
- **Pre-trained GPT-2**: Medium-sized model for Python coding assistance
- **Training Framework**: PyTorch with Transformers library integration

## Project Structure

```
Day_14/
├── 14_Build_Your_Own_GPT_Creating_a_Custom_Text_Generation_Engine.ipynb
├── Assignment/
│   └── Assignment_Python_Code_Focused_GPT2_Inference.ipynb
└── README.md
```

## Analysis Workflow

### Main Project Components

#### 1. Custom GPT Text Generation Engine
- **Model Architecture**: Small GPT-2 configuration with 4 layers, 4 attention heads
- **Training Pipeline**: Complete end-to-end training with checkpointing
- **Data Processing**: TinyStories dataset streaming and tokenization
- **Training Configuration**: AdamW optimizer, gradient clipping, learning rate scheduling
- **Checkpointing**: Periodic model and tokenizer saving for reproducibility
- **Inference**: Story generation from trained checkpoints

#### 2. Assignment: Python Code-Focused GPT-2 Inference
- **Pre-trained Model**: GPT-2 Medium (354,823,168 parameters)
- **Filtering System**: Comprehensive Python coding question detection
- **Response Generation**: Contextual Python programming assistance
- **Non-coding Handling**: Professional rejection of non-programming queries
- **Testing Framework**: Comprehensive validation with diverse test cases

## Key Findings

### Custom GPT Training Results

#### Model Specifications
- **Architecture**: GPT-2 style with custom configuration
  - **Vocabulary Size**: 50,257 tokens (GPT-2 tokenizer)
  - **Context Length**: 512 tokens
  - **Model Width**: 256 embedding dimensions
  - **Depth**: 4 transformer layers
  - **Attention Heads**: 4 heads per layer
- **Training Configuration**:
  - **Batch Size**: 52 (optimized for GPU memory)
  - **Total Epochs**: 12 (with resume capability)
  - **Optimizer**: AdamW with gradient clipping
  - **Device**: CUDA-enabled GPU training

#### Training Performance
- **Loss Progression**: Consistent decrease from initial epochs
  - **Epoch 1**: Average loss 1.2364
  - **Epoch 6**: Average loss 1.1440
  - **Epoch 12**: Final average loss 1.1167
- **Checkpointing**: Successful model saving after each epoch
- **Story Quality**: Progressive improvement in narrative coherence

### Python Code-Focused Inference Results

#### System Performance
- **Model**: GPT-2 Medium successfully loaded and configured
- **Filtering Accuracy**: 87.5% success rate (14/16 test cases)
- **Response Generation**: Contextual Python programming assistance
- **Processing Speed**: Efficient GPU-accelerated inference

#### Filtering System Analysis
- **Keywords Monitored**: 74 Python-related terms
- **Pattern Recognition**: 10 regex patterns for question detection
- **Decision Logic**: Robust filtering with detailed reasoning
- **Edge Cases**: 2 false positives due to overly broad keyword matching

## Technical Implementation

### Custom GPT Training Pipeline
```python
# Model Configuration
config = GPT2Config(
    vocab_size=len(tokenizer),
    n_positions=512,
    n_ctx=512,
    n_embd=256,
    n_layer=4,
    n_head=4,
    pad_token_id=tokenizer.pad_token_id
)

# Training Loop with Checkpointing
model = GPT2LMHeadModel(config)
optimizer = AdamW(model.parameters(), lr=5e-4)
```

### Python Coding Filter Implementation
```python
class PythonCodingFilter:
    def __init__(self):
        self.python_keywords = {
            'python', 'code', 'coding', 'programming', 'script', 'function',
            'class', 'method', 'variable', 'import', 'module', 'package'
        }
        # Additional keyword sets and pattern matching
```

### Response Generation System
```python
class PythonCodingAssistant:
    def generate_response(self, prompt: str) -> Dict[str, any]:
        # Filtering, enhancement, and generation pipeline
        is_coding, reason = self.filter.is_python_coding_question(prompt)
        if is_coding:
            # Generate contextual Python programming response
        else:
            # Return predefined non-coding message
```

## Deliverables

### Notebooks
1. **Custom GPT Engine**: Complete training pipeline for story generation
2. **Assignment Solution**: Python code-focused inference system with comprehensive testing

### Key Outputs
- **Trained Models**: Multiple checkpoint saves (epoch_1 through epoch_12)
- **Story Generation**: Progressive improvement in narrative quality
- **Coding Assistant**: Functional Python programming help system
- **Test Results**: Comprehensive validation with performance metrics

## Installation and Usage

### Prerequisites
```bash
# Core dependencies
pip install torch transformers datasets tqdm matplotlib

# For enhanced functionality
pip install jupyter ipykernel

# GPU support (recommended)
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118
```

### System Requirements
- **Python**: 3.8+ (tested with 3.11)
- **PyTorch**: 2.8.0+ with CUDA support
- **Memory**: 16GB+ RAM recommended for training
- **GPU**: NVIDIA GPU with 8GB+ VRAM (Tesla T4 or better)
- **Storage**: 10GB+ for datasets and model checkpoints

### Running the Project
1. **Custom GPT Training**: Execute the main notebook for complete training pipeline
2. **Assignment**: Run Assignment_Python_Code_Focused_GPT2_Inference.ipynb for coding assistant
3. **Model Loading**: Use saved checkpoints for inference and continued training

### Expected Runtime
- **Custom GPT Training**: 2-4 hours (12 epochs, GPU-accelerated)
- **Assignment Setup**: 10-15 minutes (model loading and initialization)
- **Inference**: Real-time response generation (1-5 seconds per query)

## Results and Impact

### Technical Achievements
| Component | Specification | Performance |
|-----------|--------------|-------------|
| Custom GPT | 4-layer transformer | Loss reduction to 1.1167 |
| Training Data | 2.1M TinyStories | Successful story generation |
| Pre-trained Model | GPT-2 Medium | 354M parameters loaded |
| Filtering System | 74 keywords + patterns | 87.5% accuracy |
| Test Coverage | 16 diverse scenarios | Comprehensive validation |
| Response Time | GPU-accelerated | 1-5 seconds per query |

### Practical Applications
1. **Educational Tools**: Custom language models for specific domains
2. **Code Assistance**: Specialized programming help systems
3. **Content Generation**: Automated story and text creation
4. **Research**: Understanding transformer training and deployment
5. **Production Systems**: Scalable NLP inference pipelines

## Assignment Completion Status

All assignment requirements successfully fulfilled:
- **Model Loading**: GPT-2 Medium successfully loaded with AutoModelForCausalLM and AutoTokenizer
- **Filtering Mechanism**: Comprehensive Python coding question detection system implemented
- **Response Generation**: Contextual Python programming assistance for coding questions
- **Non-coding Handling**: Professional predefined messages for non-programming queries
- **Testing**: Comprehensive test suite with 16 diverse scenarios validating filtering effectiveness

## Future Enhancements

1. **Advanced Architectures**: Implement GPT-3/4 style improvements
2. **Fine-tuning**: Domain-specific model adaptation
3. **Retrieval Augmentation**: RAG integration for enhanced responses
4. **Multi-modal**: Vision-language model integration
5. **Production Deployment**: API endpoints and scalable serving
6. **Evaluation Metrics**: Automated quality assessment systems

## Technical Notes

- **Memory Management**: Efficient GPU memory usage with gradient checkpointing
- **Reproducibility**: Fixed random seeds for consistent training results
- **Error Handling**: Robust exception management and fallback mechanisms
- **Scalability**: Streaming dataset processing for large-scale training
- **Monitoring**: Comprehensive logging and progress tracking
- **Checkpointing**: Automatic model saving for training interruption recovery

## External Resources

- **TinyStories Dataset**: https://huggingface.co/datasets/roneneldan/TinyStories
- **Transformers Library**: https://huggingface.co/docs/transformers/
- **GPT-2 Paper**: https://d4mucfpksywv.cloudfront.net/better-language-models/language_models_are_unsupervised_multitask_learners.pdf
- **PyTorch Documentation**: https://pytorch.org/docs/stable/index.html
- **CUDA Toolkit**: https://developer.nvidia.com/cuda-toolkit

This project successfully demonstrates advanced NLP techniques, from custom model training to specialized inference systems, providing a comprehensive framework for understanding and implementing transformer-based language models with practical applications in code assistance and text generation.
