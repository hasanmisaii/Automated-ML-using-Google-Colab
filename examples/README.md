# Examples Directory

This directory contains sample datasets and usage examples for the Automated ML notebooks.

## Sample Datasets

### Classification Examples
- `iris_sample.csv` - Classic iris flower classification dataset
- `customer_churn.csv` - Sample customer churn prediction data

### Regression Examples  
- `house_prices.csv` - Sample house price prediction data
- `sales_forecast.csv` - Sample sales forecasting data

## Usage

1. Download any sample dataset
2. Upload it to Google Colab using the file upload feature in the notebooks
3. Follow the automated ML pipeline

## Creating Your Own Dataset

Your CSV file should have:
- One target column (what you want to predict)
- Feature columns (input variables)
- Column headers in the first row
- No missing target values

### Example Structure

```csv
feature1,feature2,feature3,target
1.2,3.4,A,0
2.1,4.5,B,1
3.2,5.6,A,0
```

For best results:
- Use clear, descriptive column names
- Handle obvious data quality issues before upload
- Ensure sufficient data (100+ samples recommended)
- Balance your target classes for classification problems