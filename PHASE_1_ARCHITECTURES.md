# Deep Learning Architectures for Federated Learning

## 1. MobileNetV2
- **Overview**: MobileNetV2 is an efficient deep learning architecture designed for mobile and edge devices.
- **Specifications**:
  - Depthwise separable convolutions
  - Inverted residual structure
  - Linear bottlenecks
- **Federated Learning Suitability Score**: 8/10
- **Considerations for Medical Imaging**:
  - Suitable for real-time inference on mobile devices in medical applications.
  - Performs well with limited computational resources, making it ideal for federated scenarios where devices vary in capability.

## 2. ResNet-18
- **Overview**: ResNet-18 is a deep residual learning framework that helps in training very deep networks.
- **Specifications**:
  - 18 layers deep
  - Residual blocks with skip connections
  - Batch normalization layers
- **Federated Learning Suitability Score**: 7/10
- **Considerations for Medical Imaging**:
  - Effective feature learning helps in identifying complex patterns in medical images.
  - The model's performance may vary without adequate data distribution across devices, especially with non-IID data.

## 3. EfficientNet-B0
- **Overview**: EfficientNet-B0 is a highly scalable and efficient architecture from the EfficientNet family.
- **Specifications**:
  - Compound scaling via width, depth, and resolution
  - Squeeze-and-excitation blocks
- **Federated Learning Suitability Score**: 9/10
- **Considerations for Medical Imaging**:
  - Excellent performance with limited data.
  - Effectively manages non-IID data situations using GroupNorm normalization, which stabilizes learning across varying data distributions.

## Non-IID Data Handling with GroupNorm
- **Importance**: Non-IID data is common in medical imaging federated learning scenarios due to varying data sources and patient demographics.
- **GroupNorm Normalization Strategy**:
  - Helps keep the training stable across devices with different data distributions.
  - Group normalization operates on groups of channels which can be more beneficial compared to batch normalization in small batch sizes prevalent in federated settings.

---