# Prompt Record

- create a promptRecord.md and record all the prompt I give you, alsocreate a log.md document record all the things you've done after this instruction
- now create a document named steps.md, and in side the document summarize steps we should do to implement the following tasks:HW1: write python to solve simple linear regression problem, following CRISP-DM steps,
             要有prompt and 過程, 不可只有CODE AND RESULT
             1. CRISP-DM
             2. allow user to modify a in ax+b, noise, number of points 
             3. streamlit or flask web, 框架 deployment
 
繳交: https://github.com/huanchen1107/20250920_AutoDeployLR
         https://aiotda.streamlit.app/
- and than please finish the steps until completely implements the tasks
- please follow the intructions and update the app.py, Features:
Data Generation:

Generate n data points (x, y) where n is a user-selectable value between 100 and 1000.
The relationship between x and y will be defined by y = ax + b + noise.
a: User-selectable coefficient between -10 and 10.
noise: Normally distributed noise N(0, var), where var (variance) is user-selectable between 0 and 1000.
Linear Regression Visualization:

Plot the generated data points.
Draw the calculated linear regression line in red.
Outlier Identification:

Identify and label the top 5 outliers (points furthest from the regression line).
User Interface:

Implement the application using Streamlit for an interactive web interface.
Allow users to adjust parameters (n, a, var) via sliders or input fields.
Display the generated plot and regression results. remember to update the promptRecord.md and log.md
- please move all documents in 物聯網數據分析與應用 into LinearRegression folder in the same folder
- please remember to update promptRecord.md and log.md whatever i say and you do
