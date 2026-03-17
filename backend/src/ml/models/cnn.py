"""
CNN Model Implementation for Medical Federate

This module contains the Convolutional Neural Network model implementation
used for medical image analysis in federated learning scenarios.
"""

import torch
import torch.nn as nn
import torch.nn.functional as F


class MedicalCNN(nn.Module):
    """
    Convolutional Neural Network for Medical Image Analysis
    
    Architecture optimized for federated learning with reasonable
    parameter count for distributed training.
    """
    
    def __init__(self, num_classes=2, input_channels=1):
        """
        Initialize the CNN model.
        
        Args:
            num_classes (int): Number of output classes
            input_channels (int): Number of input channels (1 for grayscale, 3 for RGB)
        """
        super(MedicalCNN, self).__init__()
        
        # Convolutional layers
        self.conv1 = nn.Conv2d(input_channels, 32, kernel_size=3, padding=1)
        self.conv2 = nn.Conv2d(32, 64, kernel_size=3, padding=1)
        self.conv3 = nn.Conv2d(64, 128, kernel_size=3, padding=1)
        
        # Batch normalization
        self.bn1 = nn.BatchNorm2d(32)
        self.bn2 = nn.BatchNorm2d(64)
        self.bn3 = nn.BatchNorm2d(128)
        
        # Pooling
        self.pool = nn.MaxPool2d(2, 2)
        
        # Fully connected layers
        self.fc1 = nn.Linear(128 * 32 * 32, 256)
        self.fc2 = nn.Linear(256, 128)
        self.fc3 = nn.Linear(128, num_classes)
        
        # Dropout for regularization
        self.dropout = nn.Dropout(0.5)
    
    def forward(self, x):
        """
        Forward pass of the network.
        
        Args:
            x (torch.Tensor): Input tensor of shape (batch_size, channels, height, width)
            
        Returns:
            torch.Tensor: Output logits of shape (batch_size, num_classes)
        """
        # Block 1
        x = self.pool(F.relu(self.bn1(self.conv1(x))))
        
        # Block 2
        x = self.pool(F.relu(self.bn2(self.conv2(x))))
        
        # Block 3
        x = self.pool(F.relu(self.bn3(self.conv3(x))))
        
        # Flatten
        x = x.view(x.size(0), -1)
        
        # Fully connected layers
        x = F.relu(self.fc1(x))
        x = self.dropout(x)
        x = F.relu(self.fc2(x))
        x = self.dropout(x)
        x = self.fc3(x)
        
        return x


def create_cnn_model(num_classes=2, input_channels=1):
    """
    Factory function to create a CNN model.
    
    Args:
        num_classes (int): Number of output classes
        input_channels (int): Number of input channels
        
    Returns:
        MedicalCNN: Initialized CNN model
    """
    return MedicalCNN(num_classes=num_classes, input_channels=input_channels)