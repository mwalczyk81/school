# Load necessary packages if not already installed
if (!requireNamespace("ggplot2", quietly = TRUE)) install.packages("ggplot2")
if (!requireNamespace("dplyr", quietly = TRUE)) install.packages("dplyr")
if (!requireNamespace("tidyr", quietly = TRUE)) install.packages("tidyr")
if (!requireNamespace("gridExtra", quietly = TRUE)) install.packages("gridExtra")
if (!requireNamespace("scales", quietly = TRUE)) install.packages("scales")

# Load necessary libraries
library(ggplot2)
library(dplyr)
library(tidyr)
library(gridExtra)
library(scales)

# Load the midwest dataset
data("midwest", package = "ggplot2")

# Summarize data: calculate total population for each state
midwest_summary <- midwest %>%
  group_by(state) %>%
  summarize(total_population = sum(poptotal, na.rm = TRUE))

# Create a horizontal bar chart for total population by state with formatted numbers
horizontal_bar_chart <- ggplot(midwest_summary, aes(x = reorder(state, total_population), y = total_population)) +
  geom_bar(stat = "identity") +
  coord_flip() +
  ggtitle("Total Population by State") +
  xlab("State") +
  ylab("Total Population") +
  scale_y_continuous(labels = comma)

# Display the horizontal bar chart
print(horizontal_bar_chart)


# Summarize data: calculate average percentage of white and Asian populations for each state
midwest_summary_stack <- midwest %>%
  group_by(state) %>%
  summarize(avg_percwhite = mean(percwhite, na.rm = TRUE),
            avg_percasian = mean(percasian, na.rm = TRUE)) %>%
  pivot_longer(cols = c(avg_percwhite, avg_percasian), names_to = "variable", values_to = "value")

# Create a stacked bar chart for percentage of white and Asian populations by state
stacked_bar_chart <- ggplot(midwest_summary_stack, aes(x = state, y = value, fill = variable)) +
  geom_bar(stat = "identity", position = "stack") +
  ggtitle("Average Percentage of White and Asian Populations by State") +
  xlab("State") +
  ylab("Average Percentage") +
  scale_fill_manual(values = c("avg_percwhite" = "blue", "avg_percasian" = "red"))

# Display the stacked bar chart
print(stacked_bar_chart)

# Summarize data: calculate average population density for each state
midwest_summary_heatmap <- midwest %>%
  group_by(state) %>%
  summarize(avg_popdensity = mean(popdensity, na.rm = TRUE))

# Prepare data for heatmap
heatmap_data <- midwest_summary_heatmap %>%
  pivot_longer(cols = avg_popdensity, names_to = "variable", values_to = "value")

# Create a heatmap for population density by state
heatmap_plot <- ggplot(heatmap_data, aes(x = state, y = variable, fill = value)) +
  geom_tile() +
  ggtitle("Heatmap of Population Density by State") +
  xlab("State") +
  ylab("Variable") +
  scale_fill_gradient(low = "white", high = "blue")

# Display the heatmap
print(heatmap_plot)

# Save the midwest dataset to a CSV file
write.csv(midwest, "midwest.csv", row.names = FALSE)


# Arrange the plots in a grid and display them
grid.arrange(horizontal_bar_chart, stacked_bar_chart, heatmap_plot, ncol = 1)

