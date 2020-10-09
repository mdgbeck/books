library(tidyverse)
library(tidymodels)
library(scales)
library(mdgr)

theme_set(theme_minimal())

data(ames)

# looks at price
ggplot(ames, aes(x = Sale_Price)) +
  geom_histogram(bins = 50) +
  scale_x_continuous(labels = dollar)

# data skewed - log transform
ggplot(ames, aes(x = Sale_Price)) +
  geom_histogram(bins = 50) +
  scale_x_log10()

ames <- ames %>% 
  mutate(Sale_Price = log10(Sale_Price))

set.seed(123)

ames_split <- initial_split(ames, prob = .8, strata = Sale_Price)
ames_train <- training(ames_split)
ames_test <- testing(ames_split)


base_model <- lm(Sale_Price ~ Neighborhood + log10(Gr_Liv_Area) + Year_Built + Bldg_Type, data = ames_train)
tidy(base_model)

simple_ames <- 
  recipe(Sale_Price ~ Neighborhood + Gr_Liv_Area + Year_Built + Bldg_Type,
         data = ames_train) %>% 
  step_log(Gr_Liv_Area, base = 10) %>% 
  step_dummy(all_nominal())

simple_ames <- prep(simple_ames, training = ames_train, retain = TRUE)

# recipe is what to do to data
# bake execute recipe on particular data set to view data that model will take in
# must use prepped recipe
test_ex <- bake(simple_ames, new_data = ames_test)

ggplot(ames_train, aes(y = Neighborhood)) +
  geom_bar() +
  labs(y = NULL)

# combine lower 1% of neighborhoods into one "other" category
simple_ames <- 
  recipe(Sale_Price ~ Neighborhood + Gr_Liv_Area + Year_Built + Bldg_Type,
         data = ames_train) %>% 
  step_log(Gr_Liv_Area, base = 10) %>% 
  step_other(Neighborhood, threshold = 0.01) %>% 
  step_dummy(all_nominal())


# add interaction term
simple_ames <- 
  recipe(Sale_Price ~ Neighborhood + Gr_Liv_Area + Year_Built + Bldg_Type,
         data = ames_train) %>% 
  step_log(Gr_Liv_Area, base = 10) %>% 
  step_other(Neighborhood, threshold = 0.01) %>% 
  step_dummy(all_nominal()) %>%
  # step below don't need to recall log on Gr_Liv_Area as prev step does for all
  # make sure step_dummy before if interations use needed dummies
  step_interact( ~ Gr_Liv_Area:starts_with('Bldg_Type'))

