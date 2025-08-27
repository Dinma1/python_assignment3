This repository contains educational materials and practical examples demonstrating a discount calculator.

# Features
 Interactive user interface
 Input validation (handles negative values and invalid input)
 Discount threshold logic (20% minimum)
 Multiple calculations in one session
 Formatted price display
 Error handling


# Running the Discount Calculator
1. **Clone or download the files**
2. **Run the program:**
   ```bash
   python discount_calculator.py
   ```

3. **Follow the prompts:**
   - Enter the original price of the item
   - Enter the discount percentage
   - View the calculated final price

# Example Usage

```
=== Discount Calculator ===
Note: Discount only applies if 20% or more

Enter the original price of the item: $100
Enter the discount percentage: 25

Discount applied!
Original price: $100.00
Discount (25%): $25.00
Final price: $75.00

Would you like to calculate another discount? (y/n): n
Thank you for using the Discount Calculator!
```

# Code Structure

# Functions

# `calculate_discount(price, discount_percent)`
- **Purpose**: Calculates final price after applying discount
- **Parameters**: 
  - `price` (float): Original price of the item
  - `discount_percent` (float): Discount percentage
- **Returns**: Final price (discounted or original if discount < 20%)
- **Logic**: Only applies discount if 20% or more

# `main()`
- Handles user input and output
- Validates input data
- Calls the discount calculation function
- Displays formatted results

