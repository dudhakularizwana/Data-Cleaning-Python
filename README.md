# 🧹 Data Cleaning Using Python

## 📌 Project Overview

This project demonstrates basic **Data Cleaning and Preprocessing using Python**. It uses a sample customer dataset containing Customer ID, Age, Income, and Score.

The project handles missing values, removes duplicate records, and uses interpolation to fill missing sequential values.

## 🎯 Objectives

* Remove duplicate records
* Handle missing values
* Use median imputation for Age
* Use mean imputation for Income
* Use linear interpolation for Score
* Remove any remaining null values
* Create a clean dataset for further analysis

## 🛠️ Technologies Used

* Python
* Pandas
* NumPy
* VS Code
* Git & GitHub

## 📊 Dataset

The sample dataset contains the following columns:

| Column      | Description                           |
| ----------- | ------------------------------------- |
| Customer_ID | Unique customer identification number |
| Age         | Customer age                          |
| Income      | Customer income                       |
| Score       | Customer score                        |

## 🔧 Data Cleaning Steps

### 1. Removing Duplicates

Duplicate records are removed using:

```python
df = df.drop_duplicates()
```

### 2. Handling Missing Age Values

Missing Age values are replaced using the median:

```python
df['Age'] = df['Age'].fillna(df['Age'].median())
```

### 3. Handling Missing Income Values

Missing Income values are replaced using the mean:

```python
df['Income'] = df['Income'].fillna(df['Income'].mean())
```

### 4. Interpolation for Score

Missing Score values are filled using linear interpolation:

```python
df['Score'] = df['Score'].interpolate(method='linear')
```

### 5. Removing Remaining Null Values

Any remaining missing values are removed:

```python
df_clean = df.dropna()
```

## 📈 Output

After data cleaning, the dataset contains:

* No duplicate records
* No missing Age values
* No missing Income values
* No missing Score values

### Cleaned Dataset

| Customer_ID | Age | Income | Score |
| ----------: | --: | -----: | ----: |
|         101 |  25 |  50000 |    70 |
|         102 |  32 |  60000 |    75 |
|         103 |  35 |  67400 |    80 |
|         104 |  40 |  80000 |    81 |
|         105 |  29 |  52000 |    82 |
|         106 |  32 |  95000 |    90 |

## ▶️ How to Run

### Step 1: Install Python

Make sure Python is installed on your computer.

### Step 2: Install Required Libraries

Open the VS Code terminal and run:

```bash
pip install pandas numpy
```

### Step 3: Run the Program

Run:

```bash
python data_cleaning_python.py
```

The cleaned dataset will be displayed in the terminal.

## 📁 Project Structure

```text
Data-Cleaning-Python/
│
├── data_cleaning_python.py
└── README.md
```

## 👩‍💻 Author

**DudekulaRizwana**

## ⭐ Conclusion

This project demonstrates the basic concepts of data cleaning using Python. Handling duplicates and missing values is an important step before performing data analysis or building Machine Learning models.

## ⭐ Thank You

Thank you for visiting this project!
