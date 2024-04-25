import pandas as pd

def load_happiness_data():
    happiness_data = pd.read_csv('world-happiness-report-2021.csv')
    happiness_data.rename(columns={'Country': 'Country', 'Ladder Score': 'Healthy_life_expectancy'}, inplace=True)
    return happiness_data
