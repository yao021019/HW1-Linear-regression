# Simple Linear Regression (CRISP-DM)

This project is a Python application that demonstrates simple linear regression, following the CRISP-DM (Cross-Industry Standard Process for Data Mining) methodology. The application is built using Streamlit, allowing users to interactively explore the concepts of linear regression.

## Features

-   **Data Generation:** Generate synthetic data based on the linear equation `y = ax + b + noise`.
-   **Interactive Parameters:** Users can modify the following parameters to see their effect on the model:
    -   `a`: The slope of the line.
    -   `b`: The y-intercept of the line.
    -   `noise`: The amount of random noise added to the data.
    -   `num_points`: The number of data points to generate.
-   **Visualization:** The application provides a visual representation of:
    -   The generated data points (scatter plot).
    -   The original line (`y = ax + b`).
    -   The fitted linear regression line.
-   **Model Evaluation:** The performance of the model is evaluated using metrics like Mean Squared Error (MSE) or R-squared.

## CRISP-DM Methodology

This project follows the CRISP-DM methodology, which consists of the following phases:

### 1. Business Understanding
- **Objective:** Create a web application that demonstrates simple linear regression.
- **Goal:** The user should be able to understand the process of linear regression, visualize the data and the regression line, and see the impact of changing parameters.
- **Success Criteria:** A deployed web application where users can interact with the linear regression model.

### 2. Data Understanding
- **Data Source:** We will generate synthetic data for this problem.
- **Data Generation:** The data will be generated based on the linear equation `y = ax + b + noise`.
- **Parameters:**
    - `a`: Slope of the line (user-configurable).
    - `b`: Intercept of the line (user-configurable).
    - `noise`: Random noise added to the data points (user-configurable).
    - `num_points`: Number of data points to generate (user-configurable).

### 3. Data Preparation
- **Process:**
    1.  Generate `x` values (e.g., a sequence of numbers).
    2.  Generate `y` values using the formula `y = ax + b + noise`.
    3.  The data will be prepared in a format suitable for training a linear regression model (e.g., pandas DataFrame).

### 4. Modeling
- **Model:** Simple Linear Regression.
- **Implementation:**
    1.  Use a Python library like `scikit-learn` to implement the linear regression model.
    2.  The model will be trained on the generated data (`x` and `y` values).
    3.  The model will learn the optimal `a` and `b` from the data.

### 5. Evaluation
- **Metrics:**
    -  Mean Squared Error (MSE) or R-squared value to evaluate the model's performance.
- **Visualization:**
    -  Plot the generated data points (scatter plot).
    -  Plot the original line (`y = ax + b`).
    -  Plot the fitted regression line.
    -  Display the learned coefficients (`a` and `b`) and the evaluation metrics.

### 6. Deployment
- **Framework:** Choose either Streamlit or Flask for the web application. Streamlit is generally easier for data-focused apps.
- **User Interface (UI):**
    -  Create sliders or input boxes for the user to modify `a`, `b`, `noise`, and `num_points`.
    -  Display the plots and evaluation results.
    -  Include explanations for each step of the CRISP-DM process.
- **Deployment Platform:** The final application will be deployed to a cloud platform (e.g., Streamlit Cloud, Heroku, etc.) to be accessible via a public URL.

## How to Run

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/yao021019/HW1-Linear-regression.git
    cd HW1-Linear-regression
    ```
2.  **Install the dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
3.  **Run the application:**
    ```bash
    streamlit run app.py
    ```
