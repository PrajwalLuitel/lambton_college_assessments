data()

library(ggplot2)


dim(mpg)

View(mpg)
names(mpg)
str(mpg)

?mpg

?mean

?filter

install.packages("dplyr")
library(dplyr)

filter(mpg, cty > 20)

# add a new column showing the city mileage in km/ltr
mpg_metric <- mutate(mpg, city_km <- cty * 0.425144)
View(mpg_metric)

# perform the above task using the pipe operator
mpg_metric_2 <- mpg %>%
    mutate(kmpl <- cty * 0.425144)
dim(mpg_metric_2)

# for every type of car, find the mean engine displacement
mpg %>%
    group_by(class) %>%
    summarise(mean(displ))

?ggplot

# creating a histogram to examine the city mileage column
ggplot(mpg, aes(x = cty)) +
    geom_histogram(bins = 10) +
    labs(x="City Mileage")

# return all the rows that contain toyota car
filter(mpg, tolower(manufacturer) == "toyota")


# another way to do it
mpg %>%
    filter(grepl('toyota',ignore.case = TRUE, manufacturer))


# display all the toyota cars from mtcars
View(mtcars)

# row_filter <- grepl("toyota", ignore.case = TRUE, rownames(mtcars))
# my_data <- mtcars[row_filter, ]
# head(my_data)

mtcars[grepl("toyota", ignore.case = TRUE, rownames(mtcars))]

sqrt(54)

x <- seq(1,10,by=0.5)
print(x)

print()

rnorm(10)
