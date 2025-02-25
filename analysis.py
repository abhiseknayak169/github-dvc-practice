import pandas as pd
#Added greet function
def greet(name):
    return f"Hello, {name}!"

#Added farewell function
def farewell(name):
    return f"Goodbye, {name}!"

#Added sum function
def sum_values():
    df = pd.read_csv('data/sample_data.csv')
    return df['value'].sum()

if __name__ == "__main__":
    user_name = input("Enter your name: ")
    print(greet(user_name))
    print(farewell(user_name))
    print(f"Sum of values: {sum_values()}")