'''from sklearn.naive_bayes import GaussianNB
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, RobustScaler
from imblearn.over_sampling import RandomOverSampler
import pandas as pd
import pickle

# 1. Load data from Excel file
df = pd.read_excel('pendigitalan_with_analysis_redo.xlsx')

# 2. Drop irrelevant columns
df = df.drop(['Nama', 'No_Tel', 'Nm_Syarikat', 'Sjl_Halal', 'Cap_dgngn'], axis=1)

# 3. Handle multi-category values
def convert_to_numeric(value):
    if isinstance(value, str):
        return value.split(',')[0].strip()
    return value

# Apply conversion to the necessary columns
columns_to_fix = ['SuggestedVerticals']
for col in columns_to_fix:
    df[col] = df[col].apply(convert_to_numeric)

# 4. Encode categorical columns to numeric
label_columns = [
    'Ind_Perniagaan', 'Lokasi_Sasaran_Audiens', 'Cara_Beli', 'Slrn_Phbngn',
    'K_Pghntrn', 'Plt_Talian', 'Trmnl_Byrn', 'Cr_Byrn', 'Slrn_Fzkl',
    'Mjrt_Kaum', 'Akt_Pmsrn', 'Kpst_Tgkt_Digital'
]
le = LabelEncoder()
for col in label_columns:
    df[col] = le.fit_transform(df[col].astype(str))

# Encode the target column (SuggestedVerticals)
y_le = LabelEncoder()
df['SuggestedVerticals'] = y_le.fit_transform(df['SuggestedVerticals'].astype(str))

# 5. Separate features (X) and target (y)
X = df.drop(['SuggestedVerticals', 'No_KP'], axis=1)  # Drop 'No_KP' and target column from features
y = df['SuggestedVerticals']

# 6. Fill missing values with column means
numeric_columns = X.select_dtypes(include=[float, int]).columns
X[numeric_columns] = X[numeric_columns].fillna(X[numeric_columns].mean())

# 7. Use RobustScaler to handle outliers
scaler = RobustScaler()
X = pd.DataFrame(scaler.fit_transform(X), columns=X.columns)

# 8. Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 9. Handle class imbalance using RandomOverSampler
ros = RandomOverSampler(random_state=42)
X_res, y_res = ros.fit_resample(X_train, y_train)

# 10. Train a Naive Bayes model
model = GaussianNB()
model.fit(X_res, y_res)

# 11. Save the model, scaler, and label encoder
with open('naive_bayes_model.pkl', 'wb') as f:
    pickle.dump(model, f)
with open('scaler.pkl', 'wb') as f:
    pickle.dump(scaler, f)
with open('label_encoder.pkl', 'wb') as f:
    pickle.dump(y_le, f)

# 12. Function to make a prediction using the trained model
def make_prediction():
    print("Enter the following details for prediction:")
    user_input = []
    for col in X.columns:  # Use the same columns as used in training
        value = float(input(f"{col}: "))
        user_input.append(value)

    # Convert to DataFrame and scale the input
    input_df = pd.DataFrame([user_input], columns=X.columns)
    scaled_input = scaler.transform(input_df)

    # Predict using the model
    prediction = model.predict(scaled_input)

    # Convert the prediction back to the original label
    predicted_label = y_le.inverse_transform(prediction)

    print(f"Predicted category: {predicted_label[0]}")

# 13. Call the function to make a prediction
make_prediction()

'''
from sklearn.naive_bayes import GaussianNB
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, RobustScaler
from imblearn.over_sampling import RandomOverSampler
import pandas as pd
import pickle

# 1. Load data from Excel file
df = pd.read_excel('pendigitalan_with_analysis_redo.xlsx')

# 2. Drop irrelevant columns
df = df.drop(['Nama', 'No_Tel', 'Nm_Syarikat', 'Sjl_Halal', 'Cap_dgngn'], axis=1)

# 3. Remove duplicate values based on 'No_KP'
df = df.drop_duplicates(subset='No_KP')

# 4. Handle multi-category values
def convert_to_numeric(value):
    if isinstance(value, str):
        return value.split(',')[0].strip()
    return value

# Apply conversion to the necessary columns
columns_to_fix = ['SuggestedVerticals']
for col in columns_to_fix:
    df[col] = df[col].apply(convert_to_numeric)

# 5. Encode categorical columns to numeric
label_columns = [
    'Ind_Perniagaan', 'Lokasi_Sasaran_Audiens', 'Cara_Beli', 'Slrn_Phbngn',
    'K_Pghntrn', 'Plt_Talian', 'Trmnl_Byrn', 'Cr_Byrn', 'Slrn_Fzkl',
    'Mjrt_Kaum', 'Akt_Pmsrn', 'Kpst_Tgkt_Digital'
]
le = LabelEncoder()
for col in label_columns:
    df[col] = le.fit_transform(df[col].astype(str))

# Encode the target column (SuggestedVerticals)
y_le = LabelEncoder()
df['SuggestedVerticals'] = y_le.fit_transform(df['SuggestedVerticals'].astype(str))

# 6. Separate features (X) and target (y)
X = df.drop(['SuggestedVerticals', 'No_KP'], axis=1)  # Drop 'No_KP' and target column from features
y = df['SuggestedVerticals']

# 7. Fill missing values with column means
numeric_columns = X.select_dtypes(include=[float, int]).columns
X[numeric_columns] = X[numeric_columns].fillna(X[numeric_columns].mean())

# 8. Use RobustScaler to handle outliers
scaler = RobustScaler()
X = pd.DataFrame(scaler.fit_transform(X), columns=X.columns)

# 9. Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 10. Handle class imbalance using RandomOverSampler
ros = RandomOverSampler(random_state=42)
X_res, y_res = ros.fit_resample(X_train, y_train)

# 11. Train a Naive Bayes model
model = GaussianNB()
model.fit(X_res, y_res)

# 12. Save the model, scaler, and label encoder
with open('naive_bayes_model.pkl', 'wb') as f:
    pickle.dump(model, f)
with open('scaler.pkl', 'wb') as f:
    pickle.dump(scaler, f)
with open('label_encoder.pkl', 'wb') as f:
    pickle.dump(y_le, f)

# 13. Function to make a prediction using the trained model
def make_prediction():
    print("Enter the following details for prediction:")
    user_input = []
    for col in X.columns:  # Use the same columns as used in training
        value = float(input(f"{col}: "))
        user_input.append(value)

    # Convert to DataFrame and scale the input
    input_df = pd.DataFrame([user_input], columns=X.columns)
    scaled_input = scaler.transform(input_df)

    # Predict using the model
    prediction = model.predict(scaled_input)

    # Convert the prediction back to the original label
    predicted_label = y_le.inverse_transform(prediction)

    print(f"Predicted category: {predicted_label[0]}")

# 14. Call the function to make a prediction
make_prediction()
