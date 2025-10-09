import json
import pickle
import pandas as pd
import os

# Globals for model and preprocessing parameters
model = None
xform_params = None

def init():
    global model, xform_params

    # Load model
    model_path = os.path.join(os.getenv("AZUREML_MODEL_DIR", "."), "model.pkl")
    with open(model_path, "rb") as f:
        model = pickle.load(f)

    # Init transformation parameters. Controleer of "lotfrontage_mean", "masvnrtype_mode" en "final columns" hetzelfde is als je in train notebook!
    xform_params = {
        "lotfrontage_mean": 69.58426966292134, 
        "masvnrtype_mode": "BrkFace", 
        "categorical_cols": ["Neighborhood", "HouseStyle", "MasVnrType"], 
        "exterqual_mapping": {"Po": 1, "Fa": 2, "TA": 3, "Gd": 4, "Ex": 5}, 
        "exterqual_na": "TA", 
        "final_columns": ['LotFrontage', 'GrLivArea', 'GarageArea', 'ExterQual', 
                          'YearBuilt', 'YrSold', 'OverallQual', 'HouseAge', 
                          'Neighborhood_Blmngtn', 'Neighborhood_Blueste', 
                          'Neighborhood_BrDale', 'Neighborhood_BrkSide', 
                          'Neighborhood_ClearCr', 'Neighborhood_CollgCr', 
                          'Neighborhood_Crawfor', 'Neighborhood_Edwards', 
                          'Neighborhood_Gilbert', 'Neighborhood_Greens', 
                          'Neighborhood_GrnHill', 'Neighborhood_IDOTRR', 
                          'Neighborhood_Landmrk', 'Neighborhood_MeadowV', 
                          'Neighborhood_Mitchel', 'Neighborhood_NAmes', 
                          'Neighborhood_NPkVill', 'Neighborhood_NWAmes', 
                          'Neighborhood_NoRidge', 'Neighborhood_NridgHt', 
                          'Neighborhood_OldTown', 'Neighborhood_SWISU', 
                          'Neighborhood_Sawyer', 'Neighborhood_SawyerW', 
                          'Neighborhood_Somerst', 'Neighborhood_StoneBr', 
                          'Neighborhood_Timber', 'Neighborhood_Veenker', 
                          'HouseStyle_1.5Fin', 'HouseStyle_1.5Unf', 
                          'HouseStyle_1Story', 'HouseStyle_2.5Fin', 
                          'HouseStyle_2.5Unf', 'HouseStyle_2Story', 
                          'HouseStyle_SFoyer', 'HouseStyle_SLvl', 
                          'MasVnrType_BrkCmn', 'MasVnrType_BrkFace', 
                          'MasVnrType_CBlock', 'MasVnrType_Stone']
    }


def preprocess(df):
    """Apply the same preprocessing as during training."""
    lotfrontage_mean = xform_params["lotfrontage_mean"]
    masvnrtype_mode = xform_params["masvnrtype_mode"]
    categorical_cols = xform_params["categorical_cols"]
    exterqual_mapping = xform_params["exterqual_mapping"]
    exterqual_na = xform_params["exterqual_na"]
    final_columns = xform_params["final_columns"]

    # Feature engineering
    df['HouseAge'] = df['YrSold'] - df['YearBuilt']
    df['OverallQual'] = df['OverallQual'].clip(lower=1, upper=10)
    df['LotFrontage'] = df['LotFrontage'].fillna(lotfrontage_mean)
    df['MasVnrType'] = df['MasVnrType'].fillna(masvnrtype_mode)
    df = pd.get_dummies(df, columns=categorical_cols)
    df['ExterQual'] = df['ExterQual'].map(exterqual_mapping)
    df['ExterQual'] = df['ExterQual'].fillna(exterqual_mapping[exterqual_na])

    # Align columns
    df = df.reindex(columns=final_columns, fill_value=0)

    return df


def run(raw_data):
    try:
        # Parse incoming request
        if isinstance(raw_data, str):
            data = json.loads(raw_data)
        else:
            data = raw_data

        # Convert to DataFrame
        df = pd.DataFrame(data)

        # Apply preprocessing
        X_new = preprocess(df)

        # Predict
        predictions = model.predict(X_new)

        # Return as JSON
        return json.dumps({"predictions": predictions.tolist()})
    except Exception as e:
        return json.dumps({"error": str(e)})