def calculate_discount(price, discount_percent):
    #calculate the discounted price if discount_percent >= 20
    if discount_percent >= 20:
        discount_amount = price * (discount_percent / 100) 
        final_price = price - discount_amount
        print(f"The final price after a {discount_percent}% discount is: {final_price:.2f}")  
        return final_price
    else:
        return price
        print(f"No discount applied. The price remains: {original_price:.2f}")
 
    

original_price = float(input("Enter the original price of the item: ")) 
discount_percent = float(input("Enter the discount percentage: "))  

final_price = calculate_discount(original_price, discount_percent)
