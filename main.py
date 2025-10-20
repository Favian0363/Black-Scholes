import math

def n_func(probability_values):
    return -1

curr_price = float(input('Enter the current price of asset: '))                     # current price of asset
strike_price = float(input('Enter the exercise price of asset: '))                  # price at which the option can be exercised
risk_free_rate = float(input('Enter the risk free interest rate of asset: '))       # must be in decimal form (eg: 15% must be 0.15)
time_to_exp = float(input('Enter the time to expiration of option (in days): '))    # must be in years (days/365, months/12)
volatility = float(input('Enter the volatility of asset: '))                        # sigma...
euler = math.e                                                                      # euler's constant

d_one = (math.log(curr_price/strike_price) + ((risk_free_rate + (volatility**2)/2)*time_to_exp)) / volatility * math.sqrt(time_to_exp)
d_two = d_one - volatility * math.sqrt(time_to_exp)

call_formula = curr_price * n_func(d_one) - curr_price * euler**(-risk_free_rate*time_to_exp) * n_func(d_two)