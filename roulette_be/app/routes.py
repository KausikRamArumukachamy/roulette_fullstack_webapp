# from fastapi import APIRouter, HTTPException
# import pandas as pd
# import os

# # Initialise the router
# router = APIRouter()

# # Path to the saved CSV file
# data_file_path = os.path.join("data", "roulette_data.csv")

# @router.get("/get-last-row")
# def get_last_row():
#     try:
#         if not os.path.exists(data_file_path):
#             raise HTTPException(status_code=404, detail="Data file not found")

#         df = pd.read_csv(data_file_path)

#         if df.empty:
#             return {"last_row": None}

#         # Get the last row of the dataframe
#         last_row = df.iloc[[-1]].to_dict(orient="records")[0]
#         return {"last_row": last_row}
#     except Exception as e:
#         raise HTTPException(status_code=500, detail=str(e))

# @router.delete("/remove-last-draw")
# def remove_last_draw():
#     try:
#         if not os.path.exists(data_file_path):
#             return {"message": "Data file not found. Nothing to remove."}

#         df = pd.read_csv(data_file_path)

#         if df.empty:
#             return {"message": "Dataframe is empty. Nothing to remove."}

#         # Remove the last row
#         df = df.iloc[:-1]

#         # Save the updated dataframe back to the file
#         df.to_csv(data_file_path, index=False)

#         return {"message": "Last draw removed successfully!"}
#     except Exception as e:
#         raise HTTPException(status_code=500, detail=str(e))

# @router.get("/get-redblack-stats")
# def get_redblack_stats():
#     try:
#         if not os.path.exists(data_file_path):
#             raise HTTPException(status_code=404, detail="Data file not found")

#         df = pd.read_csv(data_file_path)

#         if df.empty:
#             return {"redblack_stats": {}}

#         # Get the last row of the dataframe
#         last_row = df.iloc[[-1]].to_dict(orient="records")[0]

#         # Extract Red and Black statistics from the last row
#         last_red_statistic = last_row.get('red_statistic', None)
#         last_black_statistic = last_row.get('black_statistic', None)

#         # Return the last row statistics
#         return {
#             "last_red_statistic": last_red_statistic,
#             "last_black_statistic": last_black_statistic
#         }
#     except Exception as e:
#         raise HTTPException(status_code=500, detail=str(e))

# # New endpoint for Odd-Even statistics
# @router.get("/get-oddeven-stats")
# def get_oddeven_stats():
#     try:
#         if not os.path.exists(data_file_path):
#             raise HTTPException(status_code=404, detail="Data file not found")

#         df = pd.read_csv(data_file_path)

#         if df.empty:
#             return {"oddeven_stats": {}}

#         # Get the last row of the dataframe
#         last_row = df.iloc[[-1]].to_dict(orient="records")[0]

#         # Extract Odd and Even statistics from the last row
#         last_odd_statistic = last_row.get('odd_statistic', None)
#         last_even_statistic = last_row.get('even_statistic', None)

#         # Return the last row statistics
#         return {
#             "last_odd_statistic": last_odd_statistic,
#             "last_even_statistic": last_even_statistic
#         }
#     except Exception as e:
#         raise HTTPException(status_code=500, detail=str(e))

# # New endpoint for Low-High statistics
# @router.get("/get-lowhigh-stats")
# def get_lowhigh_stats():
#     try:
#         if not os.path.exists(data_file_path):
#             raise HTTPException(status_code=404, detail="Data file not found")

#         df = pd.read_csv(data_file_path)

#         if df.empty:
#             return {"lowhigh_stats": {}}

#         # Get the last row of the dataframe
#         last_row = df.iloc[[-1]].to_dict(orient="records")[0]

#         # Extract Low and High statistics from the last row
#         last_high_statistic = last_row.get('high_statistic', None)
#         last_low_statistic = last_row.get('low_statistic', None)

#         # Return the last row statistics
#         return {
#             "last_high_statistic": last_high_statistic,
#             "last_low_statistic": last_low_statistic
#         }
#     except Exception as e:
#         raise HTTPException(status_code=500, detail=str(e))







from fastapi import APIRouter, HTTPException
import pandas as pd
import os

# Initialize the router
router = APIRouter()

# Path to the saved CSV file
data_file_path = os.path.join("data", "roulette_data.csv")

@router.get("/get-last-row")
def get_last_row():
    try:
        if not os.path.exists(data_file_path):
            raise HTTPException(status_code=404, detail="Data file not found")

        df = pd.read_csv(data_file_path)

        if df.empty:
            return {"last_row": None}

        # Get the last row of the dataframe
        last_row = df.iloc[[-1]].to_dict(orient="records")[0]
        return {"last_row": last_row}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.delete("/remove-last-draw")
def remove_last_draw():
    try:
        if not os.path.exists(data_file_path):
            return {"message": "Data file not found. Nothing to remove."}

        df = pd.read_csv(data_file_path)

        if df.empty:
            return {"message": "Dataframe is empty. Nothing to remove."}
            # return get_last_60_stats()
            # return {
            #     "red_statistics": [],
            #     "black_statistics": [],
            #     "odd_statistics": [],
            #     "even_statistics": [],
            #     "low_statistics": [],
            #     "high_statistics": []
            # }

        # Remove the last row
        df = df.iloc[:-1]

        # Save the updated dataframe back to the file
        df.to_csv(data_file_path, index=False)

        return get_last_60_stats()
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/get-redblack-stats")
def get_redblack_stats():
    try:
        if not os.path.exists(data_file_path):
            raise HTTPException(status_code=404, detail="Data file not found")

        df = pd.read_csv(data_file_path)

        if df.empty:
            return {"redblack_stats": {}}

        # Get the last row of the dataframe
        last_row = df.iloc[[-1]].to_dict(orient="records")[0]

        # Extract Red and Black statistics from the last row
        last_red_statistic = last_row.get('red_statistic', None)
        last_black_statistic = last_row.get('black_statistic', None)

        # Return the last row statistics
        return {
            "last_red_statistic": last_red_statistic,
            "last_black_statistic": last_black_statistic
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# New endpoint for Odd-Even statistics
@router.get("/get-oddeven-stats")
def get_oddeven_stats():
    try:
        if not os.path.exists(data_file_path):
            raise HTTPException(status_code=404, detail="Data file not found")

        df = pd.read_csv(data_file_path)

        if df.empty:
            return {"oddeven_stats": {}}

        # Get the last row of the dataframe
        last_row = df.iloc[[-1]].to_dict(orient="records")[0]

        # Extract Odd and Even statistics from the last row
        last_odd_statistic = last_row.get('odd_statistic', None)
        last_even_statistic = last_row.get('even_statistic', None)

        # Return the last row statistics
        return {
            "last_odd_statistic": last_odd_statistic,
            "last_even_statistic": last_even_statistic
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# New endpoint for Low-High statistics
@router.get("/get-lowhigh-stats")
def get_lowhigh_stats():
    try:
        if not os.path.exists(data_file_path):
            raise HTTPException(status_code=404, detail="Data file not found")

        df = pd.read_csv(data_file_path)

        if df.empty:
            return {"lowhigh_stats": {}}

        # Get the last row of the dataframe
        last_row = df.iloc[[-1]].to_dict(orient="records")[0]

        # Extract Low and High statistics from the last row
        last_high_statistic = last_row.get('high_statistic', None)
        last_low_statistic = last_row.get('low_statistic', None)

        # Return the last row statistics
        return {
            "last_high_statistic": last_high_statistic,
            "last_low_statistic": last_low_statistic
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/get-last-60-stats")
def get_last_60_stats():
    try:
        if not os.path.exists(data_file_path):
            raise HTTPException(status_code=404, detail="Data file not found")
        
        df = pd.read_csv(data_file_path)

        if df.empty:
            return {
                "red_statistics": [],
                "black_statistics": [],
                "odd_statistics": [],
                "even_statistics": [],
                "low_statistics": [],
                "high_statistics": []
            }

        # Get the last 60 rows of each statistic
        red_statistics = df['red_statistic'].tail(60).tolist()
        black_statistics = df['black_statistic'].tail(60).tolist()
        odd_statistics = df['odd_statistic'].tail(60).tolist()
        even_statistics = df['even_statistic'].tail(60).tolist()
        low_statistics = df['low_statistic'].tail(60).tolist()
        high_statistics = df['high_statistic'].tail(60).tolist()

        return {
            "red_statistics": red_statistics,
            "black_statistics": black_statistics,
            "odd_statistics": odd_statistics,
            "even_statistics": even_statistics,
            "low_statistics": low_statistics,
            "high_statistics": high_statistics
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))