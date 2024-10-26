# %% [markdown]
# ### Import data

# %%
import math
import pyreadr
import matplotlib.pyplot as plt

data = pyreadr.read_r("./dat_cars.Rdata")
# To confirm reading - should print "['Ford', ... , 'Alfa Romeo']"" (20 values)
print(data["dat_cars"]["Brand"].values)


# %% [markdown]
# ### Proper Graphics Representation for Price

# %%

prices_k_euros = [price/1_000 for price in data["dat_cars"]["Price"].values]
brands = data["dat_cars"]["Brand"].values

plt.title("Car Prices per Brand")
plt.xlabel("Brand")
plt.ylabel("Price (in thousands of Euros)")
plt.xticks(rotation=90)
plt.bar(brands, prices_k_euros)
plt.show()

# %% [markdown]
# ### Covariance between Weight and Price
#
# Using *Covariance* definition from
# https://www.statisticshowto.com/probability-and-statistics/statistics-definitions/covariance/

# %%
prices = data["dat_cars"]["Price"].values
weights = data["dat_cars"]["Weight"].values
mean_price = sum(prices)/len(prices)
mean_weight = sum(weights)/len(weights)
# Assuming the number of values is the same for prices and weights
cov_num = 0
for i in range(len(prices)):
    cov_num += (weights[i] - mean_weight)*(prices[i] - mean_price)
cov = cov_num / (len(prices) - 1)
print(f"Covariance between Weight and Price is {cov}")


# %% [markdown]
# ### Correlation between Weight and Price
#
# Assuming the desired *Correlation Coeficient* is the *Pearson's Correlation
# defined in
# https://www.statisticshowto.com/probability-and-statistics/correlation-coefficient-formula/#definition
#

# %%
prices = data["dat_cars"]["Price"].values
weights = data["dat_cars"]["Weight"].values
sum_weights = sum(weights)
sum_prices = sum(prices)
sum_products = 0    # the sum of the weight x price products
sum_sq_weights = 0  # the sum of the squared weights
sum_sq_prices = 0   # the sum of the squared prices
for i in range(len(prices)):
    sum_products += weights[i] * prices[i]
    sum_sq_weights += weights[i] * weights[i]
    sum_sq_prices += prices[i] * prices[i]
corr_num = len(prices)*sum_products - sum_weights*sum_prices
corr_sq_den_weight = len(weights)*sum_sq_weights-math.pow(sum_weights, 2)
corr_sq_den_prices = len(prices)*sum_sq_prices-math.pow(sum_prices, 2)
corr_den = corr_sq_den_weight * corr_sq_den_prices
corr = corr_num / corr_den
print(f"Pearson's Correlation between Weight and Price is {corr}")

# %% [markdown]
# As the Correlation between Weight and Price is quite close to zero, the
# conclusion is that Weight and Price are not related.

# %% [markdown]
# ### Scatterplot of Weight and Power

# %% [markdown]
#

# %%
weights = data["dat_cars"]["Weight"].values
powers = data["dat_cars"]["Power"].values

plt.scatter(weights, powers)
plt.show()
