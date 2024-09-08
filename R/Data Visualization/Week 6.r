# Install necessary packages
install.packages("ggplot2")
install.packages("gridExtra")

# Load the library
library(ggplot2)
library(gridExtra)

# Using the built-in mtcars dataset
data <- mtcars

# Line graph using mpg (miles per gallon) over index
line_plot <- ggplot(data, aes(x = seq_along(mpg), y = mpg)) +
  geom_line() +
  labs(title = "Line Graph", x = "Index", y = "Miles per Gallon (mpg)")

# Area graph using mpg (miles per gallon) over index
area_plot <- ggplot(data, aes(x = seq_along(mpg), y = mpg)) +
  geom_area(fill = "lightblue", alpha = 0.5) +
  labs(title = "Area Graph", x = "Index", y = "Miles per Gallon (mpg)")

# Multiple time series line graph using mpg and hp (horsepower)
multiple_line_plot <- ggplot(data, aes(x = seq_along(mpg))) +
  geom_line(aes(y = mpg, color = "mpg")) +
  geom_line(aes(y = hp, color = "hp")) +
  labs(title = "Multiple Time Series Line Graph", x = "Index", y = "Value") +
  scale_color_manual(name = "Legend", values = c("mpg" = "blue", "hp" = "red"))

# LOESS smoothing using mpg over index
loess_plot <- ggplot(data, aes(x = seq_along(mpg), y = mpg)) +
  geom_point() +
  geom_smooth(method = "loess") +
  labs(title = "LOESS Smoothing", x = "Index", y = "Miles per Gallon (mpg)")

grid.arrange(line_plot, area_plot, multiple_line_plot, loess_plot, ncol = 2)