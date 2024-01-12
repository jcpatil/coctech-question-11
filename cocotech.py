import numpy as np

# Set the random seed for reproducibility
np.random.seed(42)

# Function to generate random sales data for a year
def generate_sales_data():
    days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
    
    # Generate random price for each month
    price_per_month = np.random.uniform(20, 30, size=12)
    
    # Initialize empty arrays to store data
    units_sold_per_day = np.random.randint(100, 1001, size=365)
    amount_per_day = units_sold_per_day * price_per_month[0]  # Assuming the price remains constant for each month
    
    # Generate data for each day of the year
    for month in range(1, 12):
        start_day = sum(days_in_month[:month])
        end_day = start_day + days_in_month[month]
        
        # Generate random units sold and amount for each day
        units_sold_per_day[start_day:end_day] = np.random.randint(100, 1001, size=days_in_month[month])
        amount_per_day[start_day:end_day] = units_sold_per_day[start_day:end_day] * price_per_month[month]
    
    return months, units_sold_per_day, amount_per_day

# Generate sales data
months, units_sold, amount = generate_sales_data()

# Reshape arrays for easier analysis
units_sold_per_month = units_sold.reshape(12, -1)
amount_per_month = amount.reshape(12, -1)

# Reshape arrays for quarterly analysis
units_sold_per_quarter = units_sold.reshape(4, -1)
amount_per_quarter = amount.reshape(4, -1)

# 1. For each month: Units sold and amount
for i, month in enumerate(months):
    print(f"{month}: Units Sold - {np.sum(units_sold_per_month[i])}, Amount - {np.sum(amount_per_month[i])}")

# 2. For each quarter: Units sold and amount
for i in range(4):
    print(f"Quarter {i+1}: Units Sold - {np.sum(units_sold_per_quarter[i])}, Amount - {np.sum(amount_per_quarter[i])}")

# 3. Quarter with the maximum sale in terms of amount
max_amount_quarter = np.argmax(np.sum(amount_per_quarter, axis=1)) + 1
print(f"The quarter with the maximum sale in terms of amount is Quarter {max_amount_quarter}")

# 4. Quarter with the maximum sales in terms of units
max_units_quarter = np.argmax(np.sum(units_sold_per_quarter, axis=1)) + 1
print(f"The quarter with the maximum sales in terms of units is Quarter {max_units_quarter}")
