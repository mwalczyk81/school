# Install and load necessary libraries
install.packages("lubridate") # Install lubridate if not already installed
library(ggplot2)
library(gridExtra)
library(lubridate) # For working with dates

# Load the economics dataset
data("economics")

# Create a new column for the year
economics$year <- year(economics$date)

# Create the histogram
histogram_plot <- ggplot(economics, aes(x=unemploy)) +
  geom_histogram(binwidth=500, fill="blue", color="black") +
  labs(title="Histogram of Unemployment",
       x="Number of Unemployed",
       y="Frequency") +
  theme_minimal()

# Create the density plot
density_plot <- ggplot(economics, aes(x=unemploy)) +
  geom_density(fill="blue", alpha=0.5) +
  labs(title="Density Plot of Unemployment",
       x="Number of Unemployed",
       y="Density") +
  theme_minimal()

# Create the boxplot
boxplot_plot <- ggplot(economics, aes(x=as.factor(year), y=unemploy)) +
  geom_boxplot(fill="blue", color="black") +
  labs(title="Boxplot of Unemployment by Year",
       x="Year",
       y="Number of Unemployed") +
  theme_minimal()

# Create the violin plot
violin_plot <- ggplot(economics, aes(x=as.factor(year), y=unemploy)) +
  geom_violin(fill="blue", color="black") +
  labs(title="Violin Plot of Unemployment by Year",
       x="Year",
       y="Number of Unemployed") +
  theme_minimal()

write.csv(economics, "economics_with_year.csv", row.names = FALSE)

# Verify the file has been written
file.exists("economics_with_year.csv")
# Arrange all plots in a grid
grid.arrange(histogram_plot, density_plot, boxplot_plot, violin_plot, ncol=2)
