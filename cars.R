View (dat_cars)
  # 2 
cov (x = dat_cars$Weight, y = dat_cars$Power) # 2778.947

  # 3 
hist (dat_cars$Price, 
      main = "Histogram of Car Prices",
      xlab = "Car Prices")

  # 4
round (cor (x = dat_cars$Weight, y = dat_cars$Price), 
       digits = 2) # -0.31

  # 5
plot (x = dat_cars$Weight, y = dat_cars$Power, 
      col = "seagreen3", 
      xlab = "Weight in Kilograms",
      ylab = "Horsepower (HP)")

  # 6
table (dat_cars$Quality) / length (dat_cars$Quality)

  # 7 
summary (dat_cars$Power [dat_cars$Weight > 2000])

  # 8
class (dat_cars$Type) 

boxplot (dat_cars$Price ~ dat_cars$Type, 
         xlab = "Car Type", 
         ylab = "Car Price")

  # 9
Weight_std <- scale (dat_cars$Weight)

dat_cars$Weight_std <- Weight_std

  # 10
var (dat_cars$Price [dat_cars$Size == "Medium"])
