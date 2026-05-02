
#importing pandas to handle data
import pandas as pd
#importing train test split function to split the data to train a model and to test it as well
from sklearn.model_selection import train_test_split
#importing the random forest regressor instead of decision tree regressor to decrease the mean absolute error in calculations
from sklearn.ensemble import RandomForestRegressor
#importing to calculate mean absolute error
from sklearn.metrics import mean_absolute_error

#reading the sprint csv file into a data frame
sprint_data = pd.read_csv('sprint_data.csv')

#this is what we want to predict
y = sprint_data['sprint_time_100m']

#these are the values that will be used as clues to predict the final sprint time (y)
predictors = ['age', 'height_cm', 'weight_kg', 'sleep_hours',
                 'hydration_litres', 'weekly_sprint_sessions',
                 'recovery_days', 'max_squat_kg', 'max_deadlift_kg',
                 'reaction_time_sec', 'personal_best_100m']

#storing the predictors of the sprint data to the value (x)
X = sprint_data[predictors]

#testing and training using the split function
train_X, val_X, train_y, val_y = train_test_split(X, y, random_state=1)
#finding patterns using the regressor
sprint_model = RandomForestRegressor(random_state=1)
#fitting/training the model to show that x leads to y and asking the model to find patterns
sprint_model.fit(train_X, train_y)

#predicting
predictions = sprint_model.predict(val_X)
#finding the mean absolute error
mae = mean_absolute_error(val_y, predictions)
print(f"Mean Absolute Error: {mae:.2f} seconds")


#predicting your sprint times
print("\n--- Predict Your Sprint Time ---")

#replace your stats in the "my_stats" below
my_stats = pd.DataFrame([{
    'age': 16,
    'height_cm': 173,
    'weight_kg': 63,
    'sleep_hours': 8,
    'hydration_litres': 2.5,
    'weekly_sprint_sessions': 3,
    'recovery_days': 1,
    'max_squat_kg': 80,
    'max_deadlift_kg': 80,
    'reaction_time_sec': 0.12,
    'personal_best_100m': 11.45
}])

my_prediction = sprint_model.predict(my_stats)
print(f"Predicted 100m time: {my_prediction[0]:.2f} seconds")
