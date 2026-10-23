# 💰 Smart Expense Tracker

**Log, analyze and visualize your spending with Python**

![Python](https://img.shields.io/badge/Python-3.9%2B-3776AB?logo=python&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-150458?logo=pandas&logoColor=white)
![NumPy](https://img.shields.io/badge/NumPy-Computation-013243?logo=numpy&logoColor=white)
![Matplotlib](https://img.shields.io/badge/Matplotlib-Charts-11557c)
![Seaborn](https://img.shields.io/badge/Seaborn-Visualization-4c72b0)
![Jupyter](https://img.shields.io/badge/Jupyter-Notebook-F37626?logo=jupyter&logoColor=white)

---

## 📖 About the Project

The **Smart Expense Tracker** is a Python application that helps users log their expenses, organise them into categories, and understand their spending patterns through summaries and charts.

It brings together the core concepts of the course in one project:

| Concept | Where it is used |
|---|---|
| 🔁 Control structures and arrays | Input validation with loops, conditions and a list of valid categories |
| 🧱 OOP | The `ExpenseTracker` class with four methods |
| 🔢 NumPy | Totals and averages calculated on arrays |
| 🐼 Pandas | Loading, cleaning, grouping and filtering the dataset |
| 📊 Matplotlib and Seaborn | Bar chart, line graph, pie chart and histogram |

---

## ✨ Features

- ✅ **Expense input and validation**: checks the date format, a positive amount and a valid category
- 🗂️ **`ExpenseTracker` class** with these methods:
  - `add_expense()` logs a new expense and saves it to the CSV
  - `get_summary()` returns the total, average and category-wise totals
  - `filter_expenses()` filters by category, date range or amount
  - `generate_report()` prints a summary with key metrics
- 🧹 **Data cleaning**: handles missing or invalid entries and tidies category names
- 📈 **Analysis**: monthly average spending, spending percentage by category, top category and top month
- 🎨 **Four visualizations** with titles, labels and legends

---

## 🧾 Sample Output

Running `generate_report()` on the 60-row sample dataset prints:

```text
===== EXPENSE REPORT =====
Total expenses : 53031.00
Average expense: 883.85
Top category   : Entertainment
Top month      : 2026-04
Transactions   : 60
```

**Spending by category**

| Category | Total | Share |
|---|---:|---:|
| Entertainment | 24,976 | 47.10% |
| Food | 13,384 | 25.24% |
| Transport | 7,477 | 14.10% |
| Utilities | 7,194 | 13.57% |

**Monthly average spending:** 8838.50

---

## 🗃️ Dataset

`expenses.csv` is a sample dataset of 60 expenses from January to June 2026.

| Column | Description | Example |
|---|---|---|
| `Date` | Date of the expense (YYYY-MM-DD) | 2026-01-01 |
| `Amount` | Amount spent | 940 |
| `Category` | Food, Transport, Utilities or Entertainment | Food |
| `Description` | What the expense was for | Lunch at cafe |

---

## 🚀 Getting Started

### Prerequisites
- Python 3.9 or newer
- Jupyter Notebook (optional, for the notebook version)

### Installation
```bash
# 1. Clone this repository
git clone https://github.com/<your-username>/<your-repo-name>.git
cd <your-repo-name>

# 2. Install the libraries
pip install pandas numpy matplotlib seaborn
```

### Run the script
```bash
python expense_tracker.py
```

### Or run the notebook
```bash
jupyter notebook
```
Open `smart_expense_tracker_application.ipynb` and run the cells one at a time from top to bottom. Keep `expenses.csv` in the same folder.

---

## 💻 Usage Example

```python
tracker = ExpenseTracker("expenses.csv")

tracker.generate_report()                                   # summary report
tracker.filter_expenses({"category": "Food", "min_amount": 500})   # Food expenses of 500 or more
tracker.filter_expenses({"start": "2026-02-01", "end": "2026-02-28"})  # February expenses
tracker.add_expense("2026-10-22", 5000, "Entertainment", "Concert")    # log a new expense
```

---

## 📁 Project Structure

```text
smart-expense-tracker/
├── expense_tracker.py                      # main script
├── smart_expense_tracker_application.ipynb # step by step notebook
├── expenses.csv                            # sample dataset
├── screenshots/
│   ├── bar_chart.png
│   ├── line_graph.png
│   ├── pie_chart.png
│   └── histogram.png
└── README.md
```
## graphs screenshots
<img width="941" height="588" alt="Screenshot 2026-10-23 171418" src="https://github.com/user-attachments/assets/004046fa-d624-4713-96d9-b8f1c4166b74" />

<img width="1190" height="596" alt="Screenshot 2026-10-23 171452" src="https://github.com/user-attachments/assets/89da0359-6da7-4479-a613-0292e4484bd3" />

<img width="1172" height="722" alt="Screenshot 2026-10-23 171522" src="https://github.com/user-attachments/assets/38ce2af8-979e-40d6-a811-98b0e51720ea" />

<img width="1095" height="562" alt="Screenshot 2026-10-23 171544" src="https://github.com/user-attachments/assets/b91a61d9-02da-4103-a238-e69b71ebac84" />

---

## 🛡️ Edge Cases Handled

- Invalid dates, such as `abc` or the wrong format, are rejected and asked again
- Zero, negative or non-numeric amounts are rejected
- Categories outside the allowed list are rejected
- Missing or invalid rows in the CSV are removed during cleaning
- An empty dataset prints `No data available.` instead of crashing

---


---

Built with Python, Pandas, NumPy, Matplotlib and Seaborn.

*Quality is our Motto. Shaping skills for scaling higher.*
