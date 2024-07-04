if (!requireNamespace("ggplot2", quietly = TRUE)) install.packages("ggplot2")
if (!requireNamespace("dplyr", quietly = TRUE)) install.packages("dplyr")
if (!requireNamespace("treemapify", quietly = TRUE)) install.packages("treemapify")
if (!requireNamespace("gridExtra", quietly = TRUE)) install.packages("gridExtra")
if (!requireNamespace("lubridate", quietly = TRUE)) install.packages("lubridate")

# Load necessary libraries
library(ggplot2)
library(dplyr)
library(treemapify)

# Load the mtcars dataset
data(mtcars)

# Pie Chart
cylinders_count <- mtcars %>% count(cyl)
pie_chart <- ggplot(cylinders_count, aes(x="", y=n, fill=factor(cyl))) +
  geom_bar(width=1, stat="identity") +
  coord_polar("y") +
  theme_void() +
  labs(fill="Cylinders", title="Pie Chart of Cylinders")

# Grouped Bar Plot
grouped_barplot <- ggplot(mtcars, aes(x=factor(cyl), y=mpg, fill=factor(gear))) +
  geom_bar(position="dodge", stat="identity") +
  labs(x="Cylinders", y="Miles Per Gallon", fill="Gears", title="Grouped Bar Plot of MPG by Cylinders and Gears")

# Stacked Bar Plot
stacked_barplot <- ggplot(mtcars, aes(x=factor(gear), fill=factor(cyl))) +
  geom_bar(position="stack") +
  labs(x="Gears", y="Count", fill="Cylinders", title="Stacked Bar Plot of Cylinders by Gears")

# Treemap
treemap_data <- mtcars %>%
  count(cyl, gear) %>%
  rename(count=n)
treemap_plot <- ggplot(treemap_data, aes(area=count, fill=factor(cyl), label=paste("Cyl:", cyl, "\nGear:", gear, "\nCount:", count))) +
  geom_treemap() +
  geom_treemap_text(colour="white", place="centre", grow=TRUE) +
  labs(title="Treemap of Cars by Cylinders and Gears", fill="Cylinders")

write.csv(mtcars, file = "mtcars.csv")

# Arrange plots in a grid
library(gridExtra)
grid.arrange(pie_chart, grouped_barplot, stacked_barplot, treemap_plot, ncol=2)