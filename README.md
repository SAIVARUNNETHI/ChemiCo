# Team Name : ChemiCo 
# Project Title : 🧪 Chemical Reaction Predictor with 3D Molecular Visualization

A web application that predicts chemical reaction outcomes using SMILES notation and visualizes the resulting molecules in both 2D and 3D. Built for chemists, researchers, and students to enhance understanding of molecular transformations using AI and cheminformatics.


---

## 📚 Table of Contents

- [📖 Project Description](#-project-description)
- [⚙ Features](#-features)
- [🧬 Sample Use Case](#-sample-use-case)
- [🏗 Architecture Description](#-architecture-description)
- [🧪 Tech Stack / Built With](#-tech-stack--built-with)
- [📦 Requirements / Installation](#-requirements--installation)
- [🤝 Credits](#-credits)


## 📖 Project Description

This web application is designed to assist chemists, researchers, and students in predicting the outcomes of chemical reactions by using **SMILES** (Simplified Molecular Input Line Entry System) notation. It uses advanced cheminformatics libraries and AI-driven atom mapping to:

- Predict products of chemical reactions
- Visualize the structure of reactants and products in both **2D and 3D**
- Highlight **atom-level transformations** using attention-guided mapping

The application is built entirely in **Python** using the **Streamlit** framework, providing an intuitive and interactive interface. Users simply input a reaction in SMILES format, and the app maps the atoms using **rxnmapper** (a transformer-based AI model), processes the data, and visualizes the molecules using **py3Dmol**.

---

## ⚙ Features

- Accepts single or multiple SMILES-based reactions
- Predicts the most likely product compounds
- Shows atom-level changes using `rxnmapper`
- Visualizes molecular structures in **3D** using `py3Dmol`
- Multi-page interface:
  - Reaction Predictor
  - Molecule Analyzer
  - About Section

---

## 🧬 Sample Use Case

Input:  
C1=CC=CC=C1Br + [Na+][OH-] >> C1=CC=CC=C1OH + NaBr

Output:
Predicted reaction with mapped atoms.
3D model of C1=CC=CC=C1OH (Phenol).


---

## 🏗 Architecture Description

### 1. User Interface (Frontend - Streamlit)
- Users enter chemical reactions in SMILES format
- Streamlit provides a responsive UI with multiple pages:
  - **Predictor Page**: Input reaction(s), view prediction and molecule visualization
  - **Analyzer Page**: View 2D and 3D structures of any SMILES molecule
  - **About Page**: Info on project, team, and tech stack

### 2. Backend & Logic

#### a. Reaction Prediction (rxnmapper)
- Uses transformer-based deep learning model to predict atom-level mappings  
- **Input Example:**  
  `CC(=O)OC.O>>CC(=O)O.CO`  
- **Output:**  
  `[CH3:1]C(=O)[O:6][CH3:5].[OH2:4] >> [CH3:1]C(=O)[OH:4].[CH3:5][OH:6]`

#### b. Molecular Parsing (RDKit)
- Parses SMILES strings into molecular objects
- Generates:
  - 2D molecular images
  - 3D mol blocks for visualization

#### c. 3D Visualization (py3Dmol)
- Renders interactive 3D molecule viewers using WebGL
- Streamlit embeds viewer via HTML components

### 3. Result Rendering
- Outputs atom-mapped reactions
- Extracts and visualizes the first product in 3D
- Uses Streamlit + py3Dmol integration for rendering

---

## 🧪 Tech Stack / Built With

- 🧠 **Python**
- 🧬 **RDKit** – SMILES parsing and molecule visualization
- ⚛️ **rxnmapper** – AI-powered atom mapping
- 🔬 **py3Dmol** – 3D molecular visualization
- 🌐 **Streamlit** – Web application interface

---

## 📦 Requirements / Installation

**Key Libraries Used:**

- `streamlit` – Web interface  
- `rdkit` – Molecule parsing and structure generation  
- `rxnmapper` – Atom mapping using transformer-based model  
- `py3Dmol` – 3D molecular visualization  
- `Pillow` – Image handling for molecular drawings  

> 💡 You can create a `requirements.txt` file with the above dependencies.  
> ✅ No GPU required. Works on any machine with **Python 3.7+**

---

## 🤝 Credits

Developed by **Team ChemiCo** 💡  
Made with ❤️ for researchers, students, and chemistry enthusiasts.

