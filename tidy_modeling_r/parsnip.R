library(tidyverse)
library(tidymodels)
library(scales)

data(ames)

ames <- ames %>% 
  mutate(Sale_Price = log10(Sale_Price))
# use parsnip to fit models
# use translate to see what is happening under the hood
linear_reg() %>% set_engine('lm') %>% translate()

set.seed(123)

ames_split <- initial_split(ames, prob = .8, strata = Sale_Price)
ames_train <- training(ames_split)
ames_test <- testing(ames_split)

ames_rec <- 
  recipe(Sale_Price ~ Neighborhood + Gr_Liv_Area + Year_Built + Bldg_Type + 
           Latitude + Longitude, data = ames_train) %>% 
  step_log(Gr_Liv_Area, base = 10, id = 'my_id') %>% 
  step_other(Neighborhood, threshold = 0.01) %>% 
  step_dummy(all_nominal()) %>%
  # step below don't need to recall log on Gr_Liv_Area as prev step does for all
  # make sure step_dummy before if interations use needed dummies
  step_interact( ~ Gr_Liv_Area:starts_with('Bldg_Type')) %>% 
  # add natural spline using 20 df which could be tuned later
  step_ns(Latitude, Longitude, deg_free = 20) 

ames_rec_prepped <- prep(ames_rec)

# fit different models
lm_model <- linear_reg() %>% 
  set_engine('lm')

lm_form_fit <- lm_model %>% 
  fit(Sale_Price ~ Longitude + Latitude, data = ames_train)

lm_xy_fit <- lm_model %>% 
  fit_xy(
    x = select(ames_train, Longitude, Latitude),
    y = pull(ames_train, Sale_Price)
  )

lm_form_fit
# xy fit may not compute dummies some times? Not exactly clear difference
lm_xy_fit


# arguemnts are standaridized between packages in parsnip
rand_forest(trees = 1000, min_n = 5) %>% 
  set_engine('ranger') %>% 
  set_mode('regression') %>% 
  translate()

rand_forest(trees = 1000, min_n = 5) %>% 
  set_engine('ranger', verbose = TRUE) %>% 
  set_mode('regression')


# retrieving objects from parsnip models
lm_form_fit %>% pluck('fit')

tidy(lm_form_fit)

# making predictions
ames_test_small <- slice(ames_test, 1:5)

predict(lm_form_fit, new_data = ames_test_small)

ames_test_small %>% 
  select(Sale_Price) %>% 
  bind_cols(predict(lm_form_fit, ames_test_small)) %>% 
  bind_cols(predict(lm_form_fit, ames_test_small, type = 'pred_int'))


# use same steps with tree model
tree_model <- 
  decision_tree(min_n = 2) %>% 
  set_engine('rpart') %>% 
  set_mode('regression')

tree_fit <- 
  tree_model %>% 
  fit(Sale_Price ~ Longitude + Latitude, data = ames_train)

ames_test_small %>% 
  select(Sale_Price) %>% 
  bind_cols(predict(tree_fit, ames_test_small))
