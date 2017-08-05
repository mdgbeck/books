# go through the code in chapter 3 of Applied Predictive Modeling

library(tidyverse)
library(AppliedPredictiveModeling)
library(e1071)
library(caret)
library(gridExtra)
library(GGally)

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
  facet_wrap(~facet, scales="free") + 
  theme_minimal()

# comparing skewness of boxcox with lambda = -1
data_frame(
  value = c(seg_train$PerimCh1, log(seg_train_box$PerimCh1)),
  facet = c(rep("Natural", nrow(seg_train)), rep("Transformed", nrow(seg_train)))
) %>% 
  ggplot(aes(value)) +
  geom_histogram() +
  facet_wrap(~facet, scales="free") + 
  theme_minimal()

# compute prcomp is used to conduct PCA
pr <- prcomp(~ AvgIntenCh1 + EntropyIntenCh1, 
             data = seg_train_box,
             scale. = TRUE)

# visualize pca
seg_train_box %>% 
  mutate(Class = seg_train_full$Class) %>% 
  ggplot(aes(EntropyIntenCh1, AvgIntenCh1)) +
  geom_point(aes(color = Class), alpha=.5) + 
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




