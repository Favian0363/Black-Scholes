import math

def cdf(probability_value): # cumulative distribution function for standard normal distribution
    return 0.5 * (1 + math.erf(probability_value / math.sqrt(2)))

curr_price = round(float(input('Enter the current price of asset: ')), 2)                           # current price of asset
strike_price = round(float(input('Enter the exercise price of asset: ')), 2)                        # price at which the option can be exercised
risk_free_rate = round(float(input('Enter the risk free interest rate of asset: ')), 2)             # must be in decimal form (eg: 15% must be 0.15)
time_to_exp = round(float(input('Enter the time to expiration of option (in days): ')), 2) / 365    # must be in years (days/365, months/12)
volatility = round(float(input('Enter the volatility of asset: ')), 2)                              # sigma...
euler = math.e                                                                                      # euler's constant

d_one = (math.log(curr_price/strike_price) + (risk_free_rate + (volatility ** 2)/2) * time_to_exp) / (volatility * math.sqrt(time_to_exp))
d_two = d_one - volatility * math.sqrt(time_to_exp)

call_formula = curr_price * cdf(d_one) - strike_price * math.exp(-risk_free_rate * time_to_exp) * cdf(d_two)

print(f'Value of d_one: {d_one}')
print(f'Value of d_two: {d_two}')
print(f'Theoretical value of call option: {call_formula}')