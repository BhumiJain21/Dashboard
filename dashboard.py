import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Hypothetical data simulating database query result
data = {
    "Name": ["Alice", "Bob", "Alice", "Charlie", "Bob", "Alice"],
    "Question": ["Q1", "Q1", "Q2", "Q2", "Q3", "Q3"],
    "Rating": [5, 4, 3, 2, 5, 4]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Data visualization
plt.figure(figsize=(10, 6))
sns.countplot(data=df, x="Question", hue="Rating")
plt.title("Customer Satisfaction Survey Results")
plt.xlabel("Question")
plt.ylabel("Count")
plt.legend(title="Rating")
plt.tight_layout()
plt.show()
# Histogram: Rating distribution
plt.figure(figsize=(8, 6))
sns.histplot(df['Rating'], bins=5, kde=False, color="skyblue", edgecolor="black")
plt.title("Histogram of Ratings")
plt.xlabel("Rating")
plt.ylabel("Frequency")
plt.xticks(range(1, 6))
plt.grid(axis="y", linestyle="--", alpha=0.7)
plt.show()
import matplotlib.pyplot as plt

# Pie chart: Overall rating distribution
rating_counts = df['Rating'].value_counts()
plt.figure(figsize=(8, 8))
plt.pie(rating_counts, labels=rating_counts.index, autopct='%1.1f%%', startangle=140, colors=sns.color_palette("pastel"))
plt.title("Overall Rating Distribution")
plt.show()
# Bar chart: Average rating per question
avg_rating_per_question = df.groupby('Question')['Rating'].mean()
plt.figure(figsize=(8, 6))
avg_rating_per_question.plot(kind='bar', color="orange", edgecolor="black")
plt.title("Average Rating per Question")
plt.xlabel("Question")
plt.ylabel("Average Rating")
plt.xticks(rotation=0)
plt.grid(axis="y", linestyle="--", alpha=0.7)
plt.tight_layout()
plt.show()
# Line Chart: Average rating per question
avg_rating_per_question = df.groupby('Question')['Rating'].mean()
plt.figure(figsize=(10, 6))
avg_rating_per_question.plot(kind="line", marker="o", color="blue", linewidth=2)
plt.title("Line Chart: Average Rating per Question")
plt.xlabel("Question")
plt.ylabel("Average Rating")
plt.xticks(range(len(avg_rating_per_question)), avg_rating_per_question.index)
plt.grid(axis="y", linestyle="--", alpha=0.7)
plt.tight_layout()
plt.show()
# Ribbon Chart (Stacked Bar Chart)
pivot_df = df.pivot_table(index="Question", columns="Rating", aggfunc="size", fill_value=0)
pivot_df.plot(kind="bar", stacked=True, figsize=(10, 6), colormap="coolwarm", edgecolor="black")
plt.title("Ribbon Chart: Ratings by Question")
plt.xlabel("Question")
plt.ylabel("Count of Ratings")
plt.legend(title="Rating")
plt.tight_layout()
plt.show()
# Area Chart: Cumulative ratings by question
cumulative_df = pivot_df.cumsum(axis=0)
cumulative_df.plot(kind="area", figsize=(10, 6), alpha=0.7, colormap="viridis")
plt.title("Area Chart: Cumulative Ratings by Question")
plt.xlabel("Question")
plt.ylabel("Cumulative Count of Ratings")
plt.legend(title="Rating")
plt.tight_layout()
plt.show()
