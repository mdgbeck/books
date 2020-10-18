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
  recipe(Sale_Price ~ Neighborhood + Gr_Liv_Area + Year_Built + Bldg_Type + Latitude,
         data = ames_train) %>% 
  step_log(Gr_Liv_Area, base = 10) %>% 
  step_other(Neighborhood, threshold = 0.01) %>% 
  step_dummy(all_nominal()) %>%
  # step below don't need to recall log on Gr_Liv_Area as prev step does for all
  # make sure step_dummy before if interations use needed dummies
  step_interact( ~ Gr_Liv_Area:starts_with('Bldg_Type')) %>% 
  # add natural spline using 20 df which could be tuned later
  step_ns(Latitude, deg_free = 20) %>% 
  # add pca for corr size variables
  # does not auto scale use step_normalize first if necessary
  step_pca(matches("(SF$)|(Gr_Liv)"))

# note that baking on new data keeps all values from prep on training data
# ie even scaling will use means from training on test data

# how to use in traditional modeling process
ames_rec <- 
  recipe(Sale_Price ~ Neighborhood + Gr_Liv_Area + Year_Built + Bldg_Type + Latitude,
         data = ames_train) %>% 
  step_log(Gr_Liv_Area, base = 10) %>% 
  step_other(Neighborhood, threshold = 0.01) %>% 
  step_dummy(all_nominal()) %>%
  # step below don't need to recall log on Gr_Liv_Area as prev step does for all
  # make sure step_dummy before if interations use needed dummies
  step_interact( ~ Gr_Liv_Area:starts_with('Bldg_Type')) %>% 
  # add natural spline using 20 df which could be tuned later
  step_ns(Latitude, deg_free = 20) 

ames_rec_prepped <- prep(ames_rec)
# next line doesn't work not sure if newer/ older package can handle null new_data
#ames_train_prepped <- bake(ames_rec_prepped, new_data=NULL)
ames_train_prepped <- bake(ames_rec_prepped, new_data = ames_train)
ames_test_prepped <- bake(ames_rec_prepped, new_data = ames_test)

# fit model
lm_fit <- lm(Sale_Price ~ ., data = ames_train_prepped)
glance(lm_fit)
tidy(lm_fit)
predict(lm_fit, ames_test_prepped %>% head())

# can use tidy on recipe as well
tidy(ames_rec_prepped)

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
tidy(ames_rec_prepped, id = 'my_id')

ames_rec %>% update_role(address, new_role = 'street_address')

lm_model <- linear_reg() %>% set_engine('lm')

lm_wflow <- 
  workflow() %>% 
  add_model(lm_model) %>% 
  add_recipe(ames_rec)

lm_fit <- fit(lm_wflow, ames_train)
tidy(lm_fit)

ames_test_res <- predict(lm_fit, new_data = ames_test %>% select(-Sale_Price))
ames_test_res <- bind_cols(ames_test_res, ames_test %>% select(Sale_Price))
ames_test_res

ggplot(ames_test_res, aes(x = Sale_Price, y = .pred)) +
  geom_abline(lty = 2) +
  geom_point(alpha = .5) +
  coord_obs_pred()

rmse(ames_test_res, truth = Sale_Price, estimate = .pred)

# use metric sets to set which values to compute
ames_metrics <- metric_set(rmse, rsq, mae)
ames_metrics(ames_test_res, truth = Sale_Price, estimate = .pred)


# test metrics for classification
data("two_class_example")
conf_mat(two_class_example, truth = truth, estimate = predicted)
accuracy(two_class_example, truth = truth, estimate = predicted)
mcc(two_class_example, truth, predicted)
f_meas(two_class_example, truth, predicted)

two_class_curve <- roc_curve(two_class_example, truth, Class1)
two_class_curve
autoplot(two_class_curve)
roc_auc(two_class_example, truth, Class1)

# resampling for exvaluating performance
rf_model <- 
  rand_forest(trees = 1000) %>% 
  set_engine('ranger') %>% 
  set_mode('regression')

rf_wflow <- 
  workflow() %>% 
  add_formula(
    Sale_Price ~ Neighborhood + Gr_Liv_Area + Year_Built + Bldg_Type +
      Latitude + Longitude) %>% 
  add_model(rf_model)

rf_fit <- rf_wflow %>% fit(data = ames_train)  

estimate_perf <- function(model, dat) {
  cl <- match.call()
  obj_name <- as.character(cl$model)
  data_name <- as.character(cl$dat)
  data_name <- gsub('ames_', '', data_name)
  
  reg_metrics <- metric_set(rmse, rsq)
  
  model %>% 
    predict(dat) %>% 
    bind_cols(dat %>% select(Sale_Price)) %>% 
    reg_metrics(Sale_Price, .pred) %>% 
    select(-.estimator) %>% 
    mutate(object = obj_name, data = data_name)
}

estimate_perf(rf_fit, ames_train)
estimate_perf(lm_fit, ames_train)
estimate_perf(rf_fit, ames_test)


set.seed(55)
ames_folds <- vfold_cv(ames_train, v = 10, repeats = 5)
ames_folds

bootstraps(ames_train, times = 5)
