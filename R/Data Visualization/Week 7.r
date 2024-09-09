# Install necessary packages if not already installed
if (!require(ggplot2)) install.packages("ggplot2")
if (!require(dplyr)) install.packages("dplyr")
if (!require(maps)) install.packages("maps")
if (!require(cartogram)) install.packages("cartogram")
if (!require(gridExtra)) install.packages("gridExtra")
if (!require(sf)) install.packages("sf")
if (!require(viridis)) install.packages("viridis")

# Load necessary libraries
library(ggplot2)
library(dplyr)
library(maps)
library(cartogram)
library(gridExtra)
library(sf)
library(viridis)

# 1. Symbol Map

# Load the quakes dataset
data(quakes)

# Create symbol map
symbol_map <- ggplot(data = quakes) +
  borders("world", colour = "gray85", fill = "gray80") +
  geom_point(aes(x = long, y = lat, size = mag), color = "blue", alpha = 0.6) +
  scale_size_area(max_size = 10) +
  theme_minimal() +
  labs(title = "Earthquakes off the Coast of Fiji",
       x = "Longitude",
       y = "Latitude")

# 2. Choropleth Map

# Load the USArrests dataset
data(USArrests)

# Convert row names to a column
USArrests$state <- rownames(USArrests)

# Get map data for the USA
states_map <- map_data("state")

# Merge map data with USArrests data
USArrests <- USArrests %>%
  rename(region = state) %>%
  mutate(region = tolower(region))

states_map <- left_join(states_map, USArrests, by = "region")

# Create choropleth map
choropleth_map <- ggplot(data = states_map) +
  geom_polygon(aes(x = long, y = lat, group = group, fill = Murder), color = "white") +
  scale_fill_viridis_c(option = "C") +
  theme_minimal() +
  labs(title = "Murder Arrests in the USA (1973)",
       fill = "Murder Rate",
       x = "Longitude",
       y = "Latitude")

# 3. Cartogram

# Get world map data
world_map <- st_as_sf(map("world", plot = FALSE, fill = TRUE))

# Create sample population data
set.seed(123)
pop_data <- data.frame(ID = unique(world_map$ID),
                       pop = runif(length(unique(world_map$ID)), min = 1e6, max = 1e8))

# Merge map data with population data
world_map <- world_map %>%
  left_join(pop_data, by = "ID")

# Transform to a projected coordinate system
world_map <- st_transform(world_map, crs = "+proj=robin")

# Create a cartogram
world_map_cartogram <- cartogram_cont(world_map, "pop")

# Convert back to data frame for ggplot2
world_map_cartogram_df <- st_as_sf(world_map_cartogram)

# Create cartogram plot
cartogram_map <- ggplot(data = world_map_cartogram_df) +
  geom_sf(aes(fill = pop)) +
  scale_fill_viridis_c(option = "C") +
  theme_minimal() +
  labs(title = "Population Cartogram",
       fill = "Population",
       x = "Longitude",
       y = "Latitude")

# Display all maps together
grid.arrange(symbol_map, choropleth_map, cartogram_map, ncol = 1)
