# Day 10: Creative AI - Generating Art with Neural Style Transfer and Gender Style Transfer

## Project Overview

This project explores the creative applications of artificial intelligence through two main components: Neural Style Transfer and Gender Style Transfer using Generative Adversarial Networks (GANs). The project demonstrates how pre-trained deep learning models can be leveraged to manipulate and transform facial features, specifically focusing on gender transformation through latent space manipulation.

## Objective

To demonstrate the practical application of GANs for creative AI tasks, specifically:
- Understanding and implementing gender style transfer using pre-trained GAN models
- Manipulating latent space vectors to achieve controlled facial feature transformations
- Generating smooth transitions between male and female facial characteristics
- Exploring the creative potential of AI in digital art and image generation

## Dataset Information

### CelebA Dataset (via Pre-trained Models)
- **Source**: Large-scale face attributes dataset used for training the GAN models
- **Images**: Over 200,000 celebrity face images
- **Resolution**: 128×128 pixels (generator output)
- **Features**: Diverse facial attributes including gender, age, and various facial characteristics

### Gender Vector
- **Format**: NumPy array (.npy file)
- **Dimensions**: (1, 100) - matching generator input dimensions
- **Purpose**: Learned direction in latent space representing gender transformation
- **Range**: Continuous values from -0.4687 to 0.5326 (Mean: -0.0101, Std: 0.2173)

## Project Structure

```
Day_10/
├── Creative_AI_Generating_Art_with_Neural_Style_Transfer.ipynb
├── gender-classification-with-mobilenet.ipynb
├── Assignment/
│   └── Assignment_Gender_Style_Transfer.ipynb
├── Face-Generator-with-GAN-main/
│   ├── Face_Generators.ipynb
│   ├── face-generator-with-gan.ipynb
│   ├── generator_100.h5
│   ├── generator_200.h5
│   ├── generator_300.h5
│   ├── generator_400.h5
│   ├── generator_500.h5
│   ├── generator_600.h5
│   ├── generator_700.h5
│   └── README.md
├── Gender-Style-Transfer-main/
│   ├── gender_vec.npy
│   ├── female_images_data.csv
│   ├── male_images_data.csv
│   ├── grid_face_transformation.gif
│   └── README.md
└── README.md
```

## Analysis Workflow

### Main Project Components
1. **Neural Style Transfer Introduction**: Overview of creative AI applications
2. **GAN Model Understanding**: Exploration of pre-trained face generation models
3. **Gender Classification**: MobileNet-based gender classification implementation

### Assignment Implementation
1. **Model Loading**: Load pre-trained generator model (generator_700.h5)
2. **Vector Loading**: Import gender transformation vector (gender_vec.npy)
3. **Base Image Generation**: Create random face images using the generator
4. **Gender Transformation**: Apply gender vector with varying strengths
5. **Visualization**: Display transformation results across the male-female spectrum
6. **Analysis**: Comprehensive evaluation of transformation effects

## Key Findings

### Gender Style Transfer Results
- **Successful Transformation**: Achieved smooth transitions from male to female characteristics
- **Generator Performance**: generator_700.h5 (highest epoch) provided optimal results
- **Transformation Range**: -2.5 (very male) to +2.5 (very female) scaling factors
- **Visual Quality**: High-quality 128×128 pixel face generation with realistic features

### Transformation Characteristics
1. **Facial Structure**: Male variations show more angular jawlines; female variations display softer, rounded features
2. **Hair and Styling**: Gender vector affects hair length and styling patterns
3. **Skin Texture**: Female variations tend toward smoother skin appearance
4. **Eye and Eyebrow Features**: Female variations often show more defined eyebrows and varied eye shapes

## Technical Implementation

### Model Architecture
- **Generator**: Pre-trained GAN model with 100-dimensional latent space input
- **Output**: 128×128×3 RGB images
- **Training**: Trained on CelebA dataset for realistic face generation
- **Epochs**: Multiple checkpoints available (100-700 epochs)

### Gender Vector Implementation
```python
def generate_gender_variations(base_noise, gender_vector, num_variations=10, strength_range=(-3, 3)):
    """
    Generate gender variations by adding scaled gender vector to base noise.
    
    Args:
        base_noise: Base noise vector
        gender_vector: Gender transformation vector
        num_variations: Number of variations to generate
        strength_range: Range of scaling factors (negative=male, positive=female)
    
    Returns:
        variations: Generated image variations
        strengths: Scaling factors used
    """
    strengths = np.linspace(strength_range[0], strength_range[1], num_variations)
    variations = []
    
    for strength in strengths:
        modified_noise = base_noise + strength * gender_vector
        generated_image = generator.predict(modified_noise.reshape(1, -1), verbose=0)
        variations.append(generated_image[0])
    
    return np.array(variations), strengths
```

### Performance Metrics
- **Model Loading**: Successful loading of generator_700.h5 (best performing model)
- **Vector Compatibility**: Perfect dimensional match between gender vector and generator input
- **Generation Speed**: Efficient batch processing for multiple variations
- **Memory Optimization**: Implemented for Google Colab compatibility

## Deliverables

### Notebooks
1. **Main Notebook**: Introduction to neural style transfer and creative AI concepts
2. **Gender Classification**: MobileNet implementation for gender recognition
3. **Assignment Solution**: Complete gender style transfer implementation with analysis

### Pre-trained Models
- **Generator Models**: 7 checkpoint models (100-700 epochs) for face generation
- **Gender Vector**: Learned transformation vector for gender manipulation
- **Supporting Data**: CSV files with male and female image metadata

### Key Features
- Automatic model selection (highest epoch number)
- Comprehensive error handling and validation
- Professional visualization with descriptive labels
- Memory-optimized implementation for resource constraints
- Detailed technical analysis and documentation

## Installation and Usage

### Prerequisites
```bash
pip install tensorflow numpy matplotlib pandas opencv-python pillow
```

### Required Dependencies
- **TensorFlow**: 2.20.0 or compatible version
- **NumPy**: For array operations and vector manipulation
- **Matplotlib**: For visualization and plotting
- **Pandas**: For data handling and CSV processing
- **OpenCV**: For image processing operations

### Running the Project
1. **Main Analysis**: Open and run the main notebook for neural style transfer concepts
2. **Gender Classification**: Execute the MobileNet gender classification notebook
3. **Assignment**: Run the assignment notebook for complete gender style transfer implementation

### Model Requirements
- **Generator Models**: Download and place in `Face-Generator-with-GAN-main/` directory
- **Gender Vector**: Ensure `gender_vec.npy` is available in `Gender-Style-Transfer-main/` directory
- **GPU Support**: Recommended for faster inference (CPU compatible)

## Results and Impact

### Technical Achievements
| Component | Specification | Performance |
|-----------|--------------|-------------|
| Generator Input | 100-dimensional latent space | Optimal compatibility |
| Output Resolution | 128×128×3 RGB | High-quality generation |
| Gender Vector | (1, 100) dimensions | Perfect dimensional match |
| Transformation Range | -2.5 to +2.5 scaling | Smooth transitions |
| Model Checkpoints | 7 available (100-700 epochs) | generator_700.h5 selected |

### Creative Applications
1. **Digital Art**: Automated generation of diverse facial representations
2. **Character Design**: Controlled manipulation of character attributes
3. **Research Tool**: Understanding gender representation in AI-generated content
4. **Educational**: Demonstrating latent space manipulation concepts

## Future Enhancements

1. **Extended Attributes**: Implement additional facial attribute vectors (age, expression, hair color)
2. **Higher Resolution**: Upgrade to higher resolution generators for improved quality
3. **Interactive Interface**: Develop real-time manipulation interface
4. **Custom Training**: Train specialized models on specific datasets
5. **Multi-attribute Control**: Simultaneous manipulation of multiple facial attributes
6. **Video Generation**: Extend to temporal sequences and video generation

## Technical Notes

- **Model Compatibility**: Requires TensorFlow 2.x for proper model loading
- **Memory Management**: Optimized for Google Colab environment constraints
- **Reproducibility**: Fixed random seeds ensure consistent results
- **Scalability**: Framework easily adaptable to other GAN-based transformations
- **Error Handling**: Comprehensive validation for missing files and incompatible models

## External Resources

- **Face Generator Repository**: https://github.com/AshishJangra27/Face-Generator-with-GAN
- **Gender Style Transfer Repository**: https://github.com/AshishJangra27/Gender-Style-Transfer
- **Kaggle Notebooks**: Referenced implementations and datasets
- **CelebA Dataset**: Source dataset for model training

This project successfully demonstrates the creative potential of AI through practical implementation of gender style transfer, achieving professional-grade results while providing comprehensive documentation and analysis for educational and research purposes.
