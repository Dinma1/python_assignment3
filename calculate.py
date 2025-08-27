def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        discount_amount = price * (discount_percent / 100)
        final_price = price - discount_amount
        return final_price
    else:
        return price

# Example usage and test cases
if __name__ == "__main__":
    # Test cases
    print("Testing calculate_discount function:")
    print()
    
    # Test with 25% discount (should apply discount)
    original_price = 100.00
    discount = 25
    result = calculate_discount(original_price, discount)
    print(f"Original price: ${original_price}")
    print(f"Discount: {discount}%")
    print(f"Final price: ${result}")
    print()
    
    # Test with 15% discount (should return original price)
    original_price = 80.00
    discount = 15
    result = calculate_discount(original_price, discount)
    print(f"Original price: ${original_price}")
    print(f"Discount: {discount}%")
    print(f"Final price: ${result}")
    print()
    
    # Test with exactly 20% discount (should apply discount)
    original_price = 50.00
    discount = 20
    result = calculate_discount(original_price, discount)
    print(f"Original price: ${original_price}")
    print(f"Discount: {discount}%")
    print(f"Final price: ${result}")
    print()
    
    # Test with 0% discount (should return original price)
    original_price = 120.00
    discount = 0
    result = calculate_discount(original_price, discount)
    print(f"Original price: ${original_price}")
    print(f"Discount: {discount}%")
    print(f"Final price: ${result}")


    def calculate_discount(price, discount_percent):
        if discount_percent >= 20:
            discount_amount = price * (discount_percent / 100)
            final_price = price - discount_amount
            return final_price
        else:
            return price

def main():
    """Main function to handle user input and display results."""
    try:
        # Get user input
        original_price = float(input("Enter the original price of the item: $"))
        discount_percentage = float(input("Enter the discount percentage: "))
        
        # Validate input
        if original_price < 0:
            print("Error: Price cannot be negative!")
            return
        
        if discount_percentage < 0:
            print("Error: Discount percentage cannot be negative!")
            return
        
        # Calculate the final price
        final_price = calculate_discount(original_price, discount_percentage)
        
        # Display results
        if final_price < original_price:
            discount_amount = original_price - final_price
            print(f"\nDiscount applied!")
            print(f"Original price: ${original_price:.2f}")
            print(f"Discount ({discount_percentage}%): ${discount_amount:.2f}")
            print(f"Final price: ${final_price:.2f}")
        else:
            print(f"\nNo discount applied (discount must be 20% or more)")
            print(f"Price remains: ${original_price:.2f}")
    
    except ValueError:
        print("Error: Please enter valid numbers for price and discount percentage!")

# Run the program
if __name__ == "__main__":
    print("=== Discount Calculator ===")
    print("Note: Discount only applies if 20% or more\n")
    
    # Allow multiple calculations
    while True:
        main()
        
        continue_choice = input("\nWould you like to calculate another discount? (y/n): ")
        if continue_choice.lower() not in ['y', 'yes']:
            print("Thank you for using the Discount Calculator!")
            break