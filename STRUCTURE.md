# Project Structure

```
Automated-ML-using-Google-Colab/
├── README.md                          # Main documentation
├── LICENSE                           # MIT License
├── requirements.txt                  # Python dependencies (reference)
├── .gitignore                       # Git ignore rules
├── test_notebooks.py                # Validation script
├── Automated_Classification_ML.ipynb # Classification notebook
├── Automated_Regression_ML.ipynb     # Regression notebook
└── examples/
    └── README.md                    # Examples documentation
```

## Quick Links

- **Classification Notebook**: [Open in Colab](https://colab.research.google.com/github/hasanmisaii/Automated-ML-using-Google-Colab/blob/main/Automated_Classification_ML.ipynb)
- **Regression Notebook**: [Open in Colab](https://colab.research.google.com/github/hasanmisaii/Automated-ML-using-Google-Colab/blob/main/Automated_Regression_ML.ipynb)

## Notebook Features

### Classification Notebook
- 20 code cells, 12 documentation sections
- 10+ algorithms including Random Forest, XGBoost, SVM
- Automated preprocessing and hyperparameter tuning
- Confusion matrices, ROC curves, feature importance
- SMOTE for imbalanced datasets
- Model persistence and prediction functions

### Regression Notebook  
- 20 code cells, 12 documentation sections
- 12+ algorithms including Linear, Random Forest, XGBoost
- Automatic target transformation for skewed data
- Residual analysis and learning curves
- Bootstrap confidence intervals
- Comprehensive evaluation metrics

## Usage Workflow

1. **Open notebook** in Google Colab
2. **Choose data source**: Demo datasets or upload CSV
3. **Run all cells** for complete automated analysis
4. **Review results**: Performance tables, visualizations, insights
5. **Download models**: Trained models saved as .pkl files
6. **Make predictions**: Use provided functions on new data

## Technical Specifications

- **Environment**: Google Colab optimized
- **Dependencies**: Auto-installed via pip
- **Data formats**: CSV files with header row
- **Output formats**: Jupyter notebook with embedded results
- **Model formats**: Pickle/Joblib serialization
- **Visualization**: Matplotlib, Seaborn, Plotly

## Validation Status

✅ All notebooks validated for:
- Proper JSON structure
- Required code and markdown cells
- Essential ML workflow components
- Google Colab compatibility
- Professional documentation standards