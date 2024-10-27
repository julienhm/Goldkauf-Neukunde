
import streamlit as st

def calculate_gold_investment(gold_spot_price_per_kg, portfolio_value):
    # Gold bar options in grams and their respective values based on the spot price
    gold_bar_options = [500, 250, 100]  # Prioritize larger bars first

    # Calculate the target investment in gold (1/3 of the portfolio)
    target_gold_investment = portfolio_value / 3

    # Convert the gold spot price to price per gram
    gold_spot_price_per_gram = gold_spot_price_per_kg / 1000

    # Calculate the value of each gold bar option
    gold_bar_values = {bar: bar * gold_spot_price_per_gram for bar in gold_bar_options}

    # Try all possible combinations of 500g, 250g, and 100g bars
    best_combination = None
    closest_value = float('inf')  # Initialize with a large value

    # No limit on the number of bars, calculate iteratively
    for num_500g in range(100):  # Increase range as needed
        for num_250g in range(100):  # Increase range as needed
            for num_100g in range(100):  # Increase range as needed
                total_gold = num_500g * 500 + num_250g * 250 + num_100g * 100
                total_investment = total_gold * gold_spot_price_per_gram

                # Calculate the difference between current total investment and target
                difference = abs(total_investment - target_gold_investment)

                # Prioritize combinations with fewer total bars if difference is small
                if difference < closest_value or (difference == closest_value and (num_500g + num_250g + num_100g) < (best_combination[0] + best_combination[1] + best_combination[2])):
                    closest_value = difference
                    best_combination = (num_500g, num_250g, num_100g, total_gold, total_investment)

    # Extract the best combination
    num_500g, num_250g, num_100g, total_gold, total_investment = best_combination

    # Calculate the percentage of the portfolio invested in gold
    gold_investment_percentage = (total_investment / portfolio_value) * 100

    return total_gold, total_investment, num_500g, num_250g, num_100g, gold_investment_percentage


# Example usage
gold_spot_price_per_kg = 75000  # price for 1 kg of gold in CHF
portfolio_value = 674356  # Einzahlungsbetrag in CHF

total_gold, total_investment, num_500g, num_250g, num_100g, gold_investment_percentage = calculate_gold_investment(
    gold_spot_price_per_kg, portfolio_value)

print(f"Total gold to buy: {total_gold} grams")
print(f"Total investment in gold: {total_investment:.2f}")
print(f"Number of 500g bars: {num_500g}")
print(f"Number of 250g bars: {num_250g}")
print(f"Number of 100g bars: {num_100g}")
print(f"Percentage of portfolio invested in gold: {gold_investment_percentage:.2f}%")

# Streamlit app setup
st.title("Gold Investment Calculator")

# Input fields for the user to enter their data
portfolio_value = st.number_input("Enter your portfolio value (CHF):", min_value=0.0, step=1000.0, value=674356.0)
gold_spot_price_per_kg = st.number_input("Enter the current gold spot price per kg (CHF):", min_value=0.0, step=1000.0, value=75000.0)

# Button to trigger the calculation
if st.button("Calculate Gold Investment"):
    total_gold, total_investment, num_500g, num_250g, num_100g, gold_investment_percentage = calculate_gold_investment(
        gold_spot_price_per_kg, portfolio_value
    )

    # Display the results
    st.write(f"Total gold to buy: {total_gold} grams")
    st.write(f"Total investment in gold: CHF {total_investment:.2f}")
    st.write(f"Number of 500g bars: {num_500g}")
    st.write(f"Number of 250g bars: {num_250g}")
    st.write(f"Number of 100g bars: {num_100g}")
    st.write(f"Percentage of portfolio invested in gold: {gold_investment_percentage:.2f}%")