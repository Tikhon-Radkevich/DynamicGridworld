# Predicting Sales Quantity in our Dynamic Gridworld

Welcome to [this competition](https://www.kaggle.com/competitions/predicting-sales-quantity-in-our-dynamic-gridworld), where your predictive skills meet the dynamic sales landscape of our simulated Gridworld. In this 2-dimensional world of 150x150 squares, each housing multiple cities and stores, your goal is to forecast product sales.

Leverage provided data, including city attributes, advertisement levels, and pricing, to develop models that uncover patterns and insights. This is your opportunity to explore creative feature engineering in a spatially correlated landscape.

Prepare to navigate Gridworld's intricacies, and familiarize yourself with datasets and features. Best of luck in this exciting challenge!

![](img.jpg)

## Dataset Description
Step into the captivating world of our competition and predict the sales in our Gridworld. The following data is at your disposal. The features are few, but the options for creative feature-engineering are sheer endless.

### Explore the Data Files
- **train.csv:** Build your model on this dataset.
- **test.csv:** This dataset contains the stores for the final submission.
- **sample_submission.csv:** An exemplar submission file, aligning you with the submission format.
- **supplemental_cities.csv:** Additional information about each city.

### Features
- **quantity:** Your target-variable.
- **id:** A unique identifier for each record.
- **city_id:** City's identification code in the format "x/y/city_nr."
- **price:** Unit price in the specified store.
- **store_id:** Not a unique identifier.
- **ad_level:** Advertisement expenses as an ordinal feature.
- **population:** A city's population.
- **education_level:** A score describing the level of education in a city.
- **median_income:** A city's median income.

## Evaluation
Submissions will be evaluated based on their Root Mean Squared Error (RMSE) between the predicted sales quantities and the actual sales quantities for the test set.

## Modeling Approach Overview

In this competition, I adopted a two-step modeling approach to tackle the challenge of predicting sales quantity. The first step involves creating a model to predict the mean quantity value for each store in each city, providing a foundation for understanding the general sales trends within different urban areas. The second step refines this prediction by developing a model that forecasts the quantity for a specific store relative to the mean quantity in its respective city. This approach leverages the power of two complementary models to capture both city-wide and store-specific sales patterns.

### Explore Further
For a detailed exploration of this approach and its results, please refer to my Kaggle notebook: [My Kaggle Notebook](https://www.kaggle.com/code/tikhonradk/dynamic-grid-world)

Feel free to join the discussion and share your insights: [Discussion](https://www.kaggle.com/competitions/predicting-sales-quantity-in-our-dynamic-gridworld/discussion/442896)



