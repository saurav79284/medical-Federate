"""
RNN Model Implementation for Medical Federate

This module contains Recurrent Neural Network implementations including
LSTM and GRU models for sequential medical data analysis.
"""

import torch
import torch.nn as nn


class MedicalLSTM(nn.Module):
    """
    Long Short-Term Memory Network for Sequential Medical Data
    
    Designed for analyzing time-series medical data such as patient
    vitals, ECG signals, or treatment timelines.
    """
    
    def __init__(self, input_size, hidden_size, num_layers, num_classes, dropout=0.5):
        """
        Initialize LSTM model.
        
        Args:
            input_size (int): Size of input features
            hidden_size (int): Size of hidden state
            num_layers (int): Number of LSTM layers
            num_classes (int): Number of output classes
            dropout (float): Dropout probability
        """
        super(MedicalLSTM, self).__init__()
        
        self.hidden_size = hidden_size
        self.num_layers = num_layers
        
        self.lstm = nn.LSTM(
            input_size=input_size,
            hidden_size=hidden_size,
            num_layers=num_layers,
            batch_first=True,
            dropout=dropout if num_layers > 1 else 0
        )
        
        self.fc1 = nn.Linear(hidden_size, 128)
        self.fc2 = nn.Linear(128, num_classes)
        self.dropout = nn.Dropout(dropout)
    
    def forward(self, x):
        """
        Forward pass of LSTM network.
        
        Args:
            x (torch.Tensor): Input tensor of shape (batch_size, seq_length, input_size)
            
        Returns:
            torch.Tensor: Output logits of shape (batch_size, num_classes)
        """
        # LSTM forward pass
        lstm_out, (h_n, c_n) = self.lstm(x)
        
        # Use last output
        last_output = lstm_out[:, -1, :]
        
        # Fully connected layers
        x = torch.relu(self.fc1(last_output))
        x = self.dropout(x)
        x = self.fc2(x)
        
        return x


class MedicalGRU(nn.Module):
    """
    Gated Recurrent Unit Network for Sequential Medical Data
    
    Similar to LSTM but with fewer parameters, suitable for
    federated learning scenarios.
    """
    
    def __init__(self, input_size, hidden_size, num_layers, num_classes, dropout=0.5):
        """
        Initialize GRU model.
        
        Args:
            input_size (int): Size of input features
            hidden_size (int): Size of hidden state
            num_layers (int): Number of GRU layers
            num_classes (int): Number of output classes
            dropout (float): Dropout probability
        """
        super(MedicalGRU, self).__init__()
        
        self.hidden_size = hidden_size
        self.num_layers = num_layers
        
        self.gru = nn.GRU(
            input_size=input_size,
            hidden_size=hidden_size,
            num_layers=num_layers,
            batch_first=True,
            dropout=dropout if num_layers > 1 else 0
        )
        
        self.fc1 = nn.Linear(hidden_size, 128)
        self.fc2 = nn.Linear(128, num_classes)
        self.dropout = nn.Dropout(dropout)
    
    def forward(self, x):
        """
        Forward pass of GRU network.
        
        Args:
            x (torch.Tensor): Input tensor of shape (batch_size, seq_length, input_size)
            
        Returns:
            torch.Tensor: Output logits of shape (batch_size, num_classes)
        """
        # GRU forward pass
        gru_out, h_n = self.gru(x)
        
        # Use last output
        last_output = gru_out[:, -1, :]
        
        # Fully connected layers
        x = torch.relu(self.fc1(last_output))
        x = self.dropout(x)
        x = self.fc2(x)
        
        return x


def create_lstm_model(input_size, hidden_size, num_layers, num_classes):
    """Factory function to create LSTM model."""
    return MedicalLSTM(input_size, hidden_size, num_layers, num_classes)

def create_gru_model(input_size, hidden_size, num_layers, num_classes):
    """Factory function to create GRU model."""
    return MedicalGRU(input_size, hidden_size, num_layers, num_classes)