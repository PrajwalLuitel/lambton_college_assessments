# Hello, wer're trying to learn a bit of scripting with R language which is mostly used for statistical measures
data()

dim(iris)

names(iris)
str(iris)
head(iris)

head(iris,2)

tail(iris)
tail(iris,2)

# multiple ways of accessing first 3 rows
iris[1:3,]

# to say iris.sepalLength[0:11] in R, we do:
iris$Sepal.Length[1:10]

iris[1:10, "Sepal.Length"]

# Exploring individual variables
summary(iris)

install.packages("Hmisc")
library(Hmisc)
describe(iris)

range(iris$Sepal.Length)
quantile(iris$Sepal.Length)
quantile(iris$Sepal.Length, c(0.3,0.35,0.65))

fruits <- c("apple", "banana","orange")
fruits

message <- c("Happy", "Birthday", 2, "You")
message

# Histogram
hist(iris$Sepal.Length)

# pie chart
pie(table(iris$Species))

# Bar chart
barplot(table(iris$Species))


# Create a scatter plot with different shapes for each species
plot(iris$Sepal.Length, iris$Petal.Length, col = iris$Species)

# Add axis labels
xlab("Sepal Length")
ylab("Petal Length")

# Add a title
title("Scatter plot of Sepal Length vs. Petal Length with different shapes for each species")

# Add a legend
legend("topright", legend = levels(iris$Species), col = c("black", "red", "green"), pch = c(1, 19, 18))

boxplot(iris$Sepal.Length)
boxplot(iris$Petal.Length)
boxplot(iris$Sepal.Length, ylim = c(4, 8), col = iris$Species)

install.packages("ggplot2")
library(ggplot2)
ggplot(iris, aes(Sepal.Length, Petal.Length, col=Species))+geom_point()

# creating a grid of scatter plot
pairs(iris[,3:1])