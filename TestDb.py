"""Most Important Pandas Keywords for Data Analysts:
🔹 DataFrame & Series Basics
pd.DataFrame() – create a DataFrame

.head() / .tail() – view first/last rows

.info() – structure and non-null counts

.describe() – summary statistics

.shape / .columns / .dtypes – structure details

🔹 Column Selection & Filtering
df["column"] – select a single column (as Series)

df[["col1", "col2"]] – select multiple columns

df[df["column"] > value] – filter rows by condition

.isin(), .str.contains() – filter using list or text

.loc[] / .iloc[] – label or index-based selection

🔹 Aggregation & Grouping
.groupby() – group data by one or more columns

.agg() – apply multiple aggregation functions

.sum(), .mean(), .count(), .max(), .min() – aggregate stats

.value_counts() – count frequency of unique values

🔹 Sorting & Ranking
.sort_values() – sort rows

.sort_index() – sort by index

.rank() – assign rank to values

🔹 Merging & Joining
pd.merge() – SQL-style join on DataFrames

.join() – join based on index

pd.concat() – stack DataFrames vertically or horizontally

🔹 Missing Data Handling
.isnull() / .notnull() – detect missing values

.fillna() – fill missing values

.dropna() – remove missing values

🔹 Column Operations
.apply() – apply custom functions

.map() / .replace() – value transformation

.astype() – change data type

🔹 Exporting & Importing
pd.read_csv() / pd.read_excel() – read files

.to_csv() / .to_excel() – save DataFrames

📌 Bonus: Useful Shortcuts for EDA (Exploratory Data Analysis)
python
Copy
Edit
df.describe(include='all')  # Summary of all columns
df.nunique()                # Number of unique values per column
df.corr()                   # Correlation matri"""