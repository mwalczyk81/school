if (!requireNamespace("ggplot2", quietly = TRUE)) install.packages("ggplot2")
if (!requireNamespace("dplyr", quietly = TRUE)) install.packages("dplyr")
if (!requireNamespace("treemapify", quietly = TRUE)) install.packages("treemapify")
if (!requireNamespace("gridExtra", quietly = TRUE)) install.packages("gridExtra")
if (!requireNamespace("lubridate", quietly = TRUE)) install.packages("lubridate")

# Load the necessary libraries
library(ggplot2)
library(dplyr)
library(gridExtra)
library(treemapify)
library(lubridate)
# Load the economics dataset
# Load the mtcars dataset
data("mtcars")

# Create a new column for the number of cylinders as a factor
mtcars$cyl <- as.factor(mtcars$cyl)

# Aggregate data for the pie chart
pie_data <- mtcars %>%
  group_by(cyl) %>%
  summarise(count = n(), .groups = 'drop')

# Calculate percentages
pie_data <- pie_data %>%
  mutate(percentage = count / sum(count) * 100)

# Create labels with percentages
labels <- paste0(pie_data$cyl, " cyl: ", round(pie_data$percentage, 1), "%")

# Create pie chart
pie(pie_data$count, labels = labels, main = "Distribution of Cars by Cylinders")

# Prepare data for grouped bar plot
bar_data <- mtcars %>%
  group_by(cyl) %>%
  summarise(mpg = mean(mpg), hp = mean(hp), .groups = 'drop')

# Convert to matrix format
bar_matrix <- bar_data %>%
  pivot_longer(cols = c("mpg", "hp"), names_to = "variable", values_to = "value") %>%
  pivot_wider(names_from = variable, values_from = value) %>%
  column_to_rownames(var = "cyl") %>%
  as.matrix()

# Create grouped bar plot
barplot(t(bar_matrix), beside = TRUE, col = c("blue", "red"), legend = TRUE,
        args.legend = list(x = "topright", inset = c(-0.2, 0)),
        main = "Average MPG and HP by Cylinders",
        xlab = "Cylinders", ylab = "Value")

# Prepare data for treemap
treemap_data <- mtcars %>%
  group_by(cyl) %>%
  summarise(total_mpg = sum(mpg), .groups = 'drop') %>%
  mutate(cyl = as.character(cyl))

# Create the treemap
treemap(treemap_data,
        index = "cyl",
        vSize = "total_mpg",
        title = "Treemap of Total MPG by Cylinders",
        palette = "Blues")

# Convert base R plots to grobs
pie_grob <- recordPlot()
grouped_bar_grob <- recordPlot()

# Capture the current treemap plot
treemap_grob <- recordPlot()

# Create a blank ggplot as a placeholder if needed
blank_plot <- ggplot() + theme_void()

# Arrange all plots in a grid
grid.arrange(grobTree(pie_grob), grobTree(grouped_bar_grob), grobTree(treemap_grob), ncol = 2)

