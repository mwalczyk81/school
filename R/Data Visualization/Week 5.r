# Load necessary libraries
# Install necessary packages if not already installed
install.packages(c("ggplot2", "GGally", "reshape2", "ggcorrplot", "gridExtra"))

# Load the libraries
library(ggplot2)
library(GGally)
library(reshape2)
library(ggcorrplot)
library(gridExtra)

# Scatterplot: mpg vs. wt from mtcars
scatter <- ggplot(mtcars, aes(x=wt, y=mpg)) +
  geom_point() +
  theme_minimal() +
  ggtitle("Scatterplot of MPG vs. Weight")

# Correlogram: correlation matrix of mtcars
cor_matrix <- cor(mtcars)
correlogram <- ggcorrplot::ggcorrplot(cor_matrix, lab = TRUE) +
  ggtitle("Correlogram of mtcars")

# Slope graph: comparing hp (horsepower) across different cars
slope_data <- mtcars[, c("hp", "carb", "gear")]
slope_data$car <- rownames(mtcars)
slope_data_melt <- melt(slope_data, id.vars="car")

slope_graph <- ggplot(slope_data_melt, aes(x=variable, y=value, group=car, color=car)) +
  geom_line() +
  geom_point(size=3) +
  theme_minimal() +
  ggtitle("Slope Graph of HP, Carburetors, and Gears")

# Arrange plots
grid.arrange(scatter, correlogram, slope_graph, nrow=2, ncol=2)


# Scatterplot: mpg vs. wt from mtcars
scatter <- ggplot(mtcars, aes(x=wt, y=mpg)) +
  geom_point() +
  theme_minimal() +
  ggtitle("Scatterplot of MPG vs. Weight")

# Correlogram: correlation matrix of mtcars
cor_matrix <- cor(mtcars)
correlogram <- ggcorrplot::ggcorrplot(cor_matrix, lab = TRUE) +
  ggtitle("Correlogram of mtcars")

# Slope graph: comparing hp (horsepower) across different cars
slope_data <- mtcars[, c("hp", "carb", "gear")]
slope_data$car <- rownames(mtcars)
slope_data_melt <- melt(slope_data, id.vars="car")

slope_graph <- ggplot(slope_data_melt, aes(x=variable, y=value, group=car, color=car)) +
  geom_line() +
  geom_point(size=3) +
  theme_minimal() +
  ggtitle("Slope Graph of HP, Carburetors, and Gears")

# Arrange plots
grid.arrange(scatter, correlogram, slope_graph, nrow=2, ncol=2)
