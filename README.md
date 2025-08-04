# Automated Machine Learning using Google Colab

A comprehensive collection of Jupyter notebooks for automated machine learning workflows optimized for Google Colab. These notebooks provide end-to-end ML pipelines for both classification and regression tasks with minimal manual intervention.

## 🚀 Features

- **Automated Data Preprocessing**: Handles missing values, feature scaling, and encoding automatically
- **Multiple Algorithm Comparison**: Tests 10+ algorithms simultaneously and ranks them by performance
- **Hyperparameter Tuning**: Automated grid search for optimal model parameters
- **Comprehensive Evaluation**: Multiple metrics, visualizations, and diagnostic plots
- **Google Colab Optimized**: Pre-configured for seamless execution in Google Colab
- **Model Persistence**: Save and load trained models for future use
- **Easy-to-Use**: Upload your dataset and run - minimal coding required

## 📚 Notebooks

### 1. Classification Tasks (`Automated_Classification_ML.ipynb`)

Complete automated pipeline for classification problems including:

- **Algorithms Tested**: Logistic Regression, Random Forest, SVM, KNN, Naive Bayes, Decision Tree, Gradient Boosting, AdaBoost, XGBoost, LightGBM
- **Evaluation Metrics**: Accuracy, Precision, Recall, F1-Score, AUC-ROC
- **Visualizations**: Confusion matrices, ROC curves, feature importance plots
- **Special Features**: 
  - Imbalanced dataset handling with SMOTE
  - Cross-validation with stratified sampling
  - Binary and multi-class classification support

**Example Use Cases**: Email spam detection, customer churn prediction, medical diagnosis, sentiment analysis

### 2. Regression Tasks (`Automated_Regression_ML.ipynb`)

Complete automated pipeline for regression problems including:

- **Algorithms Tested**: Linear Regression, Ridge, Lasso, Elastic Net, Random Forest, SVR, KNN, Decision Tree, Gradient Boosting, AdaBoost, XGBoost, LightGBM
- **Evaluation Metrics**: RMSE, MAE, R² Score, MAPE
- **Visualizations**: Residual plots, prediction vs actual plots, learning curves
- **Special Features**:
  - Automatic target transformation for skewed data
  - Residual analysis and normality testing
  - Confidence interval predictions with bootstrap sampling

**Example Use Cases**: House price prediction, sales forecasting, stock price prediction, demand estimation

## 🛠️ Quick Start

### Option 1: Use Demo Datasets (Recommended for first-time users)

1. Open the notebook in Google Colab:
   - [Classification Notebook](https://colab.research.google.com/github/hasanmisaii/Automated-ML-using-Google-Colab/blob/main/Automated_Classification_ML.ipynb)
   - [Regression Notebook](https://colab.research.google.com/github/hasanmisaii/Automated-ML-using-Google-Colab/blob/main/Automated_Regression_ML.ipynb)

2. Run all cells to see the demo with built-in datasets (Iris, Wine, Breast Cancer for classification; California Housing, Diabetes for regression)

3. Review the automated analysis and results

### Option 2: Use Your Own Dataset

1. Open the desired notebook in Google Colab
2. In the "Data Loading" section, uncomment the file upload code:
   ```python
   from google.colab import files
   uploaded = files.upload()
   filename = list(uploaded.keys())[0]
   df = pd.read_csv(filename)
   ```
3. Upload your CSV file when prompted
4. Specify your target column name
5. Run all cells to get automated ML analysis

## 📋 Requirements

All dependencies are automatically installed in the notebooks:
- scikit-learn
- pandas
- numpy
- matplotlib
- seaborn
- plotly
- xgboost
- lightgbm
- imbalanced-learn (for classification)
- scipy

## 🎯 What You Get

### Automatic Analysis
- ✅ Data exploration and visualization
- ✅ Missing value handling
- ✅ Feature preprocessing (scaling, encoding)
- ✅ Model training and comparison
- ✅ Hyperparameter tuning
- ✅ Performance evaluation
- ✅ Feature importance analysis
- ✅ Model saving and loading

### Comprehensive Reports
- 📊 Performance comparison tables
- 📈 Visualization dashboards
- 📋 Detailed metrics and statistics
- 🔍 Model diagnostics and insights
- 💾 Ready-to-use trained models

## 🎨 Sample Output

The notebooks generate professional-quality outputs including:

1. **Performance Comparison Tables**
   ```
   Model                    Accuracy  Precision  Recall   F1-Score
   Random Forest           0.9649    0.9651     0.9649   0.9649
   XGBoost                 0.9474    0.9485     0.9474   0.9477
   Gradient Boosting       0.9298    0.9308     0.9298   0.9301
   ```

2. **Automated Visualizations**
   - Model performance comparison charts
   - Confusion matrices and ROC curves (classification)
   - Residual plots and prediction accuracy (regression)
   - Feature importance rankings

3. **Trained Models**
   - Best performing model saved as `.pkl` file
   - Preprocessor pipeline for new data
   - Easy-to-use prediction functions

## 🔧 Customization

### Adding New Algorithms
```python
# Add to the models dictionary
models['Your Algorithm'] = YourAlgorithm(parameters)
```

### Custom Preprocessing
```python
# Modify the preprocessing pipeline
custom_transformer = Pipeline([
    ('your_step', YourTransformer()),
    ('scaler', StandardScaler())
])
```

### Different Metrics
```python
# Add custom evaluation metrics
custom_score = your_custom_metric(y_true, y_pred)
```

## 📱 Google Colab Tips

1. **GPU Acceleration**: For large datasets, enable GPU in Runtime → Change runtime type
2. **Persistent Storage**: Save important files to Google Drive
3. **File Management**: Use the file browser on the left to manage downloads
4. **Long Running Jobs**: Colab sessions timeout after 12 hours of inactivity
5. **RAM Management**: Monitor memory usage in the top-right corner

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request. Some ideas:

- Add new algorithms
- Improve visualizations
- Add more preprocessing options
- Create specialized notebooks for specific domains
- Add deep learning models

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

## 🆘 Support

If you encounter any issues:

1. Check that all cells are run in order
2. Ensure your dataset has a clear target column
3. Verify your CSV file format is correct
4. Try the demo datasets first to confirm everything works

## 🌟 Acknowledgments

- Built with scikit-learn, XGBoost, and LightGBM
- Optimized for Google Colab environment
- Inspired by automated ML best practices

---

**Start your automated ML journey today!** 🚀 Simply click on a notebook link above and begin exploring your data with professional-grade machine learning pipelines.