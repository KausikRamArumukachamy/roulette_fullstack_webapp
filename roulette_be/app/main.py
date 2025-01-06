# import os
# import pandas as pd
# from fastapi import FastAPI, HTTPException
# from fastapi.middleware.cors import CORSMiddleware
# from pydantic import BaseModel
# # from app.routes import router

# # Initialize the FastAPI app
# app = FastAPI()

# # Include the router
# # app.include_router(router)

# # Add CORS middleware
# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=["http://localhost:3000"],  # Allow requests from your React app
#     allow_credentials=True,
#     allow_methods=["*"],  # Allow all methods (GET, POST, etc.)
#     allow_headers=["*"],  # Allow all headers
# )

# # Define Pydantic model for stats
# class Stats(BaseModel):
#     red_statistic: float
#     black_statistic: float
#     odd_statistic: float
#     even_statistic: float
#     high_statistic: float
#     low_statistic: float
#     total_count: int

# class NumberInput(BaseModel):
#     number:int

# # Initialize the dataframe
# columns = ['number', 'colour', 'odd_even', 'high_low', 'red_statistic', 
#            'black_statistic', 'odd_statistic', 'even_statistic', 'high_statistic', 
#            'low_statistic']

# df = pd.DataFrame(columns=columns)

# # Initialize global statistics
# red_statistic = 48.65
# black_statistic = 48.65
# odd_statistic = 48.65
# even_statistic = 48.65
# high_statistic = 48.65
# low_statistic = 48.65

# # Total number of stats
# total_count = 500

# red_count = round(red_statistic * total_count / 100)
# black_count = round(black_statistic * total_count / 100)
# green_count = total_count - red_count - black_count  # Green count is the remaining
# odd_count = round(odd_statistic * total_count / 100)
# even_count = round(even_statistic * total_count / 100)
# high_count = round(high_statistic * total_count / 100)
# low_count = round(low_statistic * total_count / 100)

# # Define the red and black numbers based on European Roulette rules
# red_numbers = {1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36}
# black_numbers = {2, 4, 6, 8, 10, 11, 13, 15, 17, 20, 22, 24, 26, 28, 29, 31, 33, 35}

# # Variables to store previous values
# previous_colour = 'Black'
# previous_odd_even = 'Even'
# previous_high_low = 'High'

# # Directory and file path for CSV
# data_directory = "data"
# if not os.path.exists(data_directory):
#     os.makedirs(data_directory)

# data_file_path = os.path.join(data_directory, "roulette_data.csv")

# # Function to calculate counts based on statistics
# def calculate_counts(stats_list):
#     global red_count, black_count, green_count, odd_count, even_count, high_count, low_count
    
#     # Extract stats from the list
#     red_statistic, black_statistic, odd_statistic, even_statistic, high_statistic, low_statistic, total_count = stats_list

#     red_count = round(red_statistic * total_count / 100)
#     black_count = round(black_statistic * total_count / 100)
#     green_count = total_count - red_count - black_count  # Green count is the remaining
#     odd_count = round(odd_statistic * total_count / 100)
#     even_count = round(even_statistic * total_count / 100)
#     high_count = round(high_statistic * total_count / 100)
#     low_count = round(low_statistic * total_count / 100)

#     count_list = [red_count, black_count, green_count, odd_count, even_count, high_count, low_count]
#     return count_list

# # Function to classify the number
# def classify_number(number):
#     if number == 0:
#         colour = 'Green'
#         odd_even = 'Neither'
#         high_low = 'Neither'
#     else:
#         colour = 'Red' if number in red_numbers else 'Black'
#         odd_even = 'Odd' if number % 2 != 0 else 'Even'
#         high_low = 'Low' if number <= 18 else 'High'

#     return colour, odd_even, high_low

# # Function to update the dataframe and save to CSV
# def update_df(number):
#     global df, red_count, black_count, green_count, odd_count, even_count, high_count, low_count
#     global red_statistic, black_statistic, odd_statistic, even_statistic, high_statistic, low_statistic
#     global previous_colour, previous_odd_even, previous_high_low

#     # Classify the input number
#     colour, odd_even, high_low = classify_number(number)

#     # Update counts
#     if colour == 'Red':
#         red_count += 1
#         if previous_colour == 'Black':
#             black_count -= 1
#     elif colour == 'Black':
#         black_count += 1
#         if previous_colour == 'Red':
#             red_count -= 1
#     elif colour == 'Green':
#         green_count += 1

#     if odd_even == 'Odd':
#         odd_count += 1
#         even_count -= 1
#     elif odd_even == 'Even':
#         even_count += 1
#         odd_count -= 1

#     if high_low == 'Low':
#         low_count += 1
#         high_count -= 1
#     elif high_low == 'High':
#         high_count += 1
#         low_count -= 1

#     # Update statistics
#     red_statistic = (red_count / total_count) * 100
#     black_statistic = (black_count / total_count) * 100
#     green_statistic = (green_count / total_count) * 100
#     odd_statistic = (odd_count / total_count) * 100
#     even_statistic = (even_count / total_count) * 100
#     high_statistic = (high_count / total_count) * 100
#     low_statistic = (low_count / total_count) * 100

#     # Update previous values
#     previous_colour = colour
#     previous_odd_even = odd_even
#     previous_high_low = high_low

#     # Add new row to dataframe
#     new_row = pd.DataFrame({
#         'number': [number],
#         'colour': [colour],
#         'odd_even': [odd_even],
#         'high_low': [high_low],
#         'red_statistic': [red_statistic],
#         'black_statistic': [black_statistic],
#         'odd_statistic': [odd_statistic],
#         'even_statistic': [even_statistic],
#         'high_statistic': [high_statistic],
#         'low_statistic': [low_statistic],
#     })
#     df = pd.concat([df, new_row], ignore_index=True)

#     # Save the updated dataframe to CSV
#     df.to_csv(data_file_path, index=False)

# # API endpoint to update stats
# @app.post("/update-stats")
# def update_stats(stats: Stats):
#     try:
#         # Log the received data
#         print(f"Received stats: {stats}")

#         # Update global statistics
#         global red_statistic, black_statistic, odd_statistic
#         global even_statistic, high_statistic, low_statistic, total_count

#         # Overwrite the global statistics with the received values
#         red_statistic = stats.red_statistic
#         black_statistic = stats.black_statistic
#         odd_statistic = stats.odd_statistic
#         even_statistic = stats.even_statistic
#         high_statistic = stats.high_statistic
#         low_statistic = stats.low_statistic
#         total_count = stats.total_count

#         # Create a list with the stats
#         stats_list = [
#             red_statistic, black_statistic, odd_statistic, even_statistic, high_statistic, low_statistic, total_count
#         ]

#         # Call the function to calculate counts
#         count_list = calculate_counts(stats_list)

#         # Print the updated statistics and counts
#         print(f"Updated stats: {red_statistic}, {black_statistic}, {odd_statistic}, {even_statistic}")
#         print(f"Updated counts: {count_list}")

#         return {"message": "Statistics updated successfully"}
#     except Exception as e:
#         print(f"Error: {e}")
#         raise HTTPException(status_code=500, detail="Internal Server Error")

# @app.post("/add-last-draw")
# def add_last_draw(input: NumberInput):
#     try:
#         # Call the update_df function to update the statistics
#         update_df(input.number)
#         return {"message": "Last draw added successfully", "last_draw": input.number}
#     except Exception as e:
#         raise HTTPException(status_code=500, detail=str(e))

import os
import pandas as pd
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from app.routes import router

# Initialize the FastAPI app
app = FastAPI()

# Include the router
app.include_router(router)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # Allow requests from your React app
    allow_credentials=True,
    allow_methods=["*"],  # Allow all methods (GET, POST, etc.)
    allow_headers=["*"],  # Allow all headers
)

# Define Pydantic model for stats
class Stats(BaseModel):
    red_statistic: float
    black_statistic: float
    odd_statistic: float
    even_statistic: float
    high_statistic: float
    low_statistic: float
    total_count: int

class NumberInput(BaseModel):
    number: int

# Initialize global statistics
red_statistic = 48.65
black_statistic = 48.65
odd_statistic = 48.65
even_statistic = 48.65
high_statistic = 48.65
low_statistic = 48.65

# Total number of stats
total_count = 500

red_count = round(red_statistic * total_count / 100)
black_count = round(black_statistic * total_count / 100)
green_count = total_count - red_count - black_count  # Green count is the remaining
odd_count = round(odd_statistic * total_count / 100)
even_count = round(even_statistic * total_count / 100)
high_count = round(high_statistic * total_count / 100)
low_count = round(low_statistic * total_count / 100)

# Define the red and black numbers based on European Roulette rules
red_numbers = {1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36}
black_numbers = {2, 4, 6, 8, 10, 11, 13, 15, 17, 20, 22, 24, 26, 28, 29, 31, 33, 35}

# Variables to store previous values
previous_colour = 'Black'
previous_odd_even = 'Even'
previous_high_low = 'High'

# Directory and file path for CSV
data_directory = "data"
if not os.path.exists(data_directory):
    os.makedirs(data_directory)

data_file_path = os.path.join(data_directory, "roulette_data.csv")

# Initialize the dataframe (empty at the start)
columns = ['number', 'colour', 'odd_even', 'high_low', 'red_statistic', 
           'black_statistic', 'odd_statistic', 'even_statistic', 'high_statistic', 
           'low_statistic']
df = pd.DataFrame(columns=columns)
df.to_csv(data_file_path, index=False)

# Function to create a new file or reset the existing one at the start of a session
def reset_file():
    global df  # Ensure the global dataframe variable is updated
    # Reset the DataFrame
    df = pd.DataFrame(columns=columns)
    # Write to the CSV file, overwriting any existing file
    df.to_csv(data_file_path, index=False)

# Call reset_file at the beginning of each session to ensure fresh file
reset_file()

# Function to calculate counts based on statistics
def calculate_counts(stats_list):
    global red_count, black_count, green_count, odd_count, even_count, high_count, low_count
    
    # Extract stats from the list
    red_statistic, black_statistic, odd_statistic, even_statistic, high_statistic, low_statistic, total_count = stats_list

    red_count = round(red_statistic * total_count / 100)
    black_count = round(black_statistic * total_count / 100)
    green_count = total_count - red_count - black_count  # Green count is the remaining
    odd_count = round(odd_statistic * total_count / 100)
    even_count = round(even_statistic * total_count / 100)
    high_count = round(high_statistic * total_count / 100)
    low_count = round(low_statistic * total_count / 100)

    count_list = [red_count, black_count, green_count, odd_count, even_count, high_count, low_count]
    return count_list

# Function to classify the number
def classify_number(number):
    if number == 0:
        colour = 'Green'
        odd_even = 'Neither'
        high_low = 'Neither'
    else:
        colour = 'Red' if number in red_numbers else 'Black'
        odd_even = 'Odd' if number % 2 != 0 else 'Even'
        high_low = 'Low' if number <= 18 else 'High'

    return colour, odd_even, high_low

# Function to update the dataframe and save to CSV
def update_df(number):
    global df, red_count, black_count, green_count, odd_count, even_count, high_count, low_count
    global red_statistic, black_statistic, odd_statistic, even_statistic, high_statistic, low_statistic
    global previous_colour, previous_odd_even, previous_high_low

    # Classify the input number
    colour, odd_even, high_low = classify_number(number)

    if not os.path.exists(data_file_path):
        raise HTTPException(status_code=404, detail="Data file not found")
    
    df = pd.read_csv(data_file_path)

    # Update counts
    if colour == 'Red':
        red_count += 1
        if previous_colour == 'Black':
            black_count -= 1
    elif colour == 'Black':
        black_count += 1
        if previous_colour == 'Red':
            red_count -= 1
    elif colour == 'Green':
        green_count += 1

    if odd_even == 'Odd':
        odd_count += 1
        even_count -= 1
    elif odd_even == 'Even':
        even_count += 1
        odd_count -= 1

    if high_low == 'Low':
        low_count += 1
        high_count -= 1
    elif high_low == 'High':
        high_count += 1
        low_count -= 1

    # Update statistics
    red_statistic = (red_count / total_count) * 100
    black_statistic = (black_count / total_count) * 100
    green_statistic = (green_count / total_count) * 100
    odd_statistic = (odd_count / total_count) * 100
    even_statistic = (even_count / total_count) * 100
    high_statistic = (high_count / total_count) * 100
    low_statistic = (low_count / total_count) * 100

    # Update previous values
    previous_colour = colour
    previous_odd_even = odd_even
    previous_high_low = high_low

    # Add new row to dataframe
    new_row = pd.DataFrame({
        'number': [number],
        'colour': [colour],
        'odd_even': [odd_even],
        'high_low': [high_low],
        'red_statistic': [red_statistic],
        'black_statistic': [black_statistic],
        'odd_statistic': [odd_statistic],
        'even_statistic': [even_statistic],
        'high_statistic': [high_statistic],
        'low_statistic': [low_statistic],
    })
    df = pd.concat([df, new_row], ignore_index=True)

    # Save the updated dataframe to CSV
    df.to_csv(data_file_path, index=False)

# API endpoint to update stats
@app.post("/update-stats")
def update_stats(stats: Stats):
    try:
        # Log the received data
        print(f"Received stats: {stats}")

        # Update global statistics
        global red_statistic, black_statistic, odd_statistic
        global even_statistic, high_statistic, low_statistic, total_count

        # Overwrite the global statistics with the received values
        red_statistic = stats.red_statistic
        black_statistic = stats.black_statistic
        odd_statistic = stats.odd_statistic
        even_statistic = stats.even_statistic
        high_statistic = stats.high_statistic
        low_statistic = stats.low_statistic
        total_count = stats.total_count

        # Create a list with the stats
        stats_list = [
            red_statistic, black_statistic, odd_statistic, even_statistic, high_statistic, low_statistic, total_count
        ]

        # Call the function to calculate counts
        count_list = calculate_counts(stats_list)

        print(f"Updated counts: {count_list}")

        return {"message": "Statistics updated successfully"}
    except Exception as e:
        print(f"Error: {e}")
        raise HTTPException(status_code=500, detail="Internal Server Error")

@app.post("/add-last-draw")
def add_last_draw(input: NumberInput):
    try:
        # Call the update_df function to update the statistics
        update_df(input.number)
        return {"message": "Last draw added successfully", "last_draw": input.number}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))