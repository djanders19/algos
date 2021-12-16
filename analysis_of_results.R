library(ggplot2)
library(dplyr)

setwd("./Documents/school/algos/")
two_dim <- read.csv(file = "2dim.csv")
four_dim <- read.csv(file = "4dim.csv")
eight_dim <- read.csv(file = "8dim.csv")
sixteen_dim <- read.csv(file = "16dim.csv")
thirtytwo_dim <- read.csv(file = "32dim.csv")

# Plot the averages of rosenbrock in 2D:
ggplot(data = stack(two_dim[0:3]), mapping = aes(x = ind, y = values)) + 
  geom_boxplot() + 
  geom_point() +
  theme_minimal() +
  ggtitle("2D-Rosenbrock") +
  xlab("") +
  ylab("Minimum value found") +
  scale_x_discrete(labels=c("HC", "RRHC", "SA"))

# Plot the average of Rastrigin in 2D:
ggplot(data = stack(two_dim[4:6]), mapping = aes(x = ind, y = values)) + 
  geom_boxplot() + 
  geom_point() +
  theme_minimal() +
  ggtitle("2D-Rastrigin") +
  xlab("") +
  ylab("Minimum value found") +
  scale_x_discrete(labels=c("HC", "RRHC", "SA"))

# Plot the average of Ackley in 2D:
ggplot(data = stack(two_dim[7:9]), mapping = aes(x = ind, y = values)) + 
  geom_boxplot() + 
  geom_point() +
  theme_minimal() +
  ggtitle("2D-Ackley") +
  xlab("") +
  ylab("Minimum value found") +
  scale_x_discrete(labels=c("HC", "RRHC", "SA"))



# Plot the averages of rosenbrock in 2D:
ggplot(data = stack(thirtytwo_dim[0:3]), mapping = aes(x = ind, y = values)) + 
  geom_boxplot() + 
  geom_point() +
  theme_minimal() +
  ggtitle("32D-Rosenbrock") +
  xlab("") +
  ylab("Minimum value found") +
  scale_x_discrete(labels=c("HC", "RRHC", "SA"))

# Plot the average of Rastrigin in 2D:
ggplot(data = stack(thirtytwo_dim[4:6]), mapping = aes(x = ind, y = values)) + 
  geom_boxplot() + 
  geom_point() +
  theme_minimal() +
  ggtitle("32D-Rastrigin") +
  xlab("") +
  ylab("Minimum value found") +
  scale_x_discrete(labels=c("HC", "RRHC", "SA"))

# Plot the average of Ackley in 2D:
ggplot(data = stack(thirtytwo_dim[7:9]), mapping = aes(x = ind, y = values)) + 
  geom_boxplot() + 
  geom_point() +
  theme_minimal() +
  ggtitle("32D-Ackley") +
  xlab("") +
  ylab("Minimum value found") +
  scale_x_discrete(labels=c("HC", "RRHC", "SA"))
