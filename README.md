# Bridge Simulation Software

> This project aims to use regression-modelling to find the best bridge set up given specific paramters about wood type, and material amount

## 📌 Overview
This software aims to assist 

This software aims to generate the optimal bridge specs, based on the assumption of distributed load, and specific joint type.

## 🚀 Features


## ⚙️ Installation


### 1. Clone Repository
```bash
# Clone the repository
git clone https://github.com/nrodreon/bridgeSimulationSoftware.git
```

### 2. Set up a virtual environment

Select the command matching your operating system to create and activate your environment:

#### 🪟 Windows
```bash
# Create the virtual environment
python -m venv .venv

# Activate the virtual environment
.\.venv\Scripts\activate
```

#### 🍎 🐧 Mac / Linux
```bash
# Create the virtual environment
python3 -m venv venv
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

## 💻 Usage

Edit the main.py file by adding

```python
specificWood = Wood(woodName, elasticity, tensileStrength, compressiveStrength)

specificPlank = Plank(woodType, width, depth) #in meters
```

Always run the application from the project root directory using the module flag:

```bash
python -m src.main
```


## 📄 License

Distributed under the MIT License. See `LICENSE` for more information.
