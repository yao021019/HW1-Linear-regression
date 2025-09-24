import streamlit as st
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

st.set_page_config(layout="wide")
st.title("Interactive Linear Regression with Outlier Detection")

# --- Sidebar for User Inputs ---
st.sidebar.header("Parameters")
st.sidebar.write("Adjust the parameters to generate new data and see the model's response.")

n = st.sidebar.slider("Number of data points (n)", 100, 1000, 300)
a = st.sidebar.slider("Coefficient (a)", -10.0, 10.0, 2.5)
var = st.sidebar.slider("Noise Variance (var)", 0.0, 1000.0, 50.0)

# --- Data Generation ---
st.header("Data Generation")
st.write("""
We generate `n` data points based on the linear equation `y = ax + b + noise`.
- **n**: Number of data points.
- **a**: The coefficient for x.
- **b**: A fixed intercept (set to 5 for this demo).
- **noise**: Normally distributed noise `N(0, var)`.
""")

# Generate data
np.random.seed(42)
b = 5
x = np.random.rand(n, 1) * 10
noise = np.random.randn(n, 1) * np.sqrt(var)
y = a * x + b + noise

df = pd.DataFrame({"x": x.flatten(), "y": y.flatten()})

# --- Linear Regression and Visualization ---
st.header("Linear Regression Visualization")

# Model fitting
model = LinearRegression()
model.fit(x, y)
y_pred = model.predict(x)
df['y_pred'] = y_pred

# --- Outlier Identification ---
st.header("Outlier Identification")
st.write("The top 5 outliers (points furthest from the regression line) are identified and labeled on the plot.")

df['distance'] = np.abs(df['y'] - df['y_pred'])
outliers = df.nlargest(5, 'distance')

# --- Plot ---
fig, ax = plt.subplots(figsize=(12, 7))

# Plot data points
ax.scatter(df['x'], df['y'], alpha=0.6, label="Generated Data")

# Plot regression line
ax.plot(df['x'], df['y_pred'], color='red', linewidth=2, label="Linear Regression Line")

# Highlight and label outliers
ax.scatter(outliers['x'], outliers['y'], color='orange', s=100, edgecolors='k', zorder=5, label="Top 5 Outliers")
for i, row in outliers.iterrows():
    ax.text(row['x'] + 0.1, row['y'], f"({row['x']:.1f}, {row['y']:.1f})", fontsize=9)

ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_title("Linear Regression and Outlier Detection")
ax.legend()
ax.grid(True)

st.pyplot(fig)

# --- Regression Results ---
st.header("Regression Results")
st.write(f"The generated data has a true relationship of: `y = {a:.2f}x + {b} + noise`")
st.write(f"The linear regression model learned the relationship: `y = {model.coef_[0][0]:.2f}x + {model.intercept_[0]:.2f}`")

st.write("Top 5 Outliers:")
st.dataframe(outliers[['x', 'y', 'distance']].style.format("{:.2f}"))