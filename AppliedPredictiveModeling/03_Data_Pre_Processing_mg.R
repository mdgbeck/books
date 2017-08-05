# go through the code in chapter 3 of Applied Predictive Modeling

library(tidyverse)
library(AppliedPredictiveModeling)
library(e1071)
library(caret)
library(gridExtra)
library(GGally)
library(corrplot)
library(mlbench)

# call the data
data(segmentationOriginal)

# create data train
seg_train_full <- filter(segmentationOriginal, Case == "Train")

# remove first couple columns
seg_train <- seg_train_full[, -(1:3)]

# ratio for skewness rule of thumb
max(seg_train$VarIntenCh3) / min(seg_train$VarIntenCh3)

# compute skewness from e1071 package
skewness(seg_train$VarIntenCh3)

# caret's preProcess transform using boxcox
seg_box <- preProcess(seg_train, method = "BoxCox")

# apply transformation
seg_train_box <- predict(seg_box, seg_train)

# see the results for a predictor
seg_box$bc$VarIntenCh3

# comparing skewness of logged data
data_frame(
  value = c(seg_train$VarIntenCh3, log(seg_train$VarIntenCh3)),
  facet = c(rep(" Natural", nrow(seg_train)), rep("Log", nrow(seg_train)))
) %>% 
  ggplot(aes(value)) +
  geom_histogram() +
  facet_wrap(~facet, scales = "free") + 
  theme_minimal()

# comparing skewness of boxcox with lambda = -1
data_frame(
  value = c(seg_train$PerimCh1, log(seg_train_box$PerimCh1)),
  facet = c(rep("Natural", nrow(seg_train)), rep("Transformed", nrow(seg_train)))
) %>% 
  ggplot(aes(value)) +
  geom_histogram() +
  facet_wrap(~facet, scales = "free") + 
  theme_minimal()

# compute prcomp is used to conduct PCA
pr <- prcomp(~ AvgIntenCh1 + EntropyIntenCh1, 
             data = seg_train_box,
             scale. = TRUE)

# visualize pca
# looks like labels are backwards in book
seg_train_box %>% 
  mutate(Class = seg_train_full$Class) %>% 
  ggplot(aes(EntropyIntenCh1, AvgIntenCh1)) +
  geom_point(aes(color = Class), alpha = .5) + 
  theme_minimal()

as.data.frame(pr$x) %>% 
  mutate(class = seg_train_full$Class) %>% 
  ggplot(aes(PC1, PC2)) +
  geom_point(aes(color = class), alpha = .5) +
  scale_y_continuous(limits = c(-3, 3)) +
  theme_minimal()

# apply pca to entire set
# remove all columns with only one value
seg_remove <- apply(seg_train, 2, function(x) length(unique(x)) == 1)
seg_train <- seg_train[, !seg_remove]

seg_pca <- preProcess(seg_train, c("BoxCox", "center", "scale"))

seg_train_pca <- predict(seg_pca, seg_train)

seg_pr <- prcomp(seg_train_pca, center = TRUE, scale. = TRUE)

# using ggpairs from GGally pakcage
as.data.frame(seg_pr$x[, 1:3]) %>% 
  mutate(Class = seg_train_full$Class) %>% 
  ggpairs(aes(color = Class))

# compute correlation for corrplot
seg_corr <- cor(seg_train_pca)

corrplot(seg_corr, order = "hclust", tl.cex = .35)

# caret has function to calculate columns with > x correlation
high_corr <- findCorrelation(seg_corr, .75)


# create variables / dummy variable
data(cars)
type <- c("convertible", "coupe", "hatchback", "sedan", "wagon")
cars$Type <- factor(apply(cars[, 14:18], 1, function(x) type[which(x == 1)]))

cars_sub <- cars %>% 
  select(1, 2, 19) %>% 
  slice(sample(nrow(cars), 20))

levels(carSubset$Type)

simpleMod <- dummyVars(~Mileage + Type,
                       data = carSubset,
                       ## Remove the variable name from the
                       ## column name
                       levelsOnly = TRUE)
simpleMod

withInteraction <- dummyVars(~Mileage + Type + Mileage:Type,
                             data = carSubset,
                             levelsOnly = TRUE)
withInteraction
predict(withInteraction, head(carSubset))

# Exercises
data(Glass)
glass <- Glass

glass_long <- glass %>% 
  gather(key, value, -Type)

# look at density plots of each variable
ggplot(glass_long, aes(value)) +
  geom_density() +
  facet_wrap(~key, scales = "free")

glass %>% 
  select(-Type) %>% 
  ggpairs()
