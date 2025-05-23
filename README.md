# Riemann-Zeta-Function-Visualizer
Riemann Zeta Function Visualizer
Collecting workspace information# Riemann Zeta Function Visualizer

This application provides an interactive visualization tool for exploring the Riemann Zeta function in the complex plane. It allows users to calculate specific values and generate 3D surface plots of both the magnitude and phase of the function.

## Features

- **Single Point Calculation**: Calculate the exact value, magnitude, and phase of ζ(s) for any specific point s = σ + it
- **3D Surface Visualization**: Generate interactive 3D plots showing:
  - Magnitude (|ζ(s)|) surface
  - Phase (Arg(ζ(s))) surface
- **Adjustable Parameters**: Customize the visualization range and resolution:
  - σ and t boundaries for the complex plane
  - Number of points for resolution control
- **User-friendly Interface**: Simple GUI built with Tkinter for easy interaction

## Installation

1. Clone this repository:
   ```
   git clone https://github.com/neyzenu/riemann-zeta-function-visualizer.git
   cd riemann-zeta-function-visualizer
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Requirements

The application requires the following Python packages:
- numpy >= 1.20.0
- matplotlib >= 3.5.0
- scipy >= 1.7.0
- plotly >= 5.5.0

## Usage

Run the application:
```
python vex.py
```

### Calculate a Single Value

1. Enter σ and t values in the top section
2. Click "Hesapla" (Calculate)
3. View the results: complex value, magnitude, and phase

### Generate 3D Surface Plots

1. Set the range parameters (σ min/max, t min/max)
2. Adjust the number of points for desired resolution
3. Click "3B Grafik Oluştur" (Generate 3D Graph)
4. Explore the generated 3D visualizations of magnitude and phase

## About the Riemann Zeta Function

The Riemann Zeta function ζ(s) is a function of complex variable s that has significant importance in number theory, particularly in the distribution of prime numbers. The Riemann Hypothesis, one of the most famous unsolved problems in mathematics, concerns the zeros of this function.

This visualizer helps in exploring the behavior of this function across different regions of the complex plane, providing insights into its magnitude and phase characteristics.

