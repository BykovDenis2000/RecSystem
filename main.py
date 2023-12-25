from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse, HTMLResponse
from recommendation.recomennder import get_recommendations
from data.data_processing import get_data,get_rating_matrix
app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Food recommendation system"}

@app.get("/collaborative/{food_name}")
def get_collaborative_recommendations(food_name: str):
    try:
        collaborative_recommendations = get_recommendations(food_name)
        return HTMLResponse(content=collaborative_recommendations.to_html(), status_code=200)
    except KeyError:
        raise HTTPException(status_code=404, detail="Food not found")

@app.get("/rating")
def get_users():
    try:
        rating = get_data("data/ratings.csv")
        rating_matrix = get_rating_matrix(rating)
        return HTMLResponse(content=rating_matrix.to_html(), status_code=200)
    except KeyError:
        raise HTTPException(status_code=404, detail="Food not found")

@app.get("/food")
def get_users():
    try:
        food = get_data("data/food.csv")
        return HTMLResponse(content=food.to_html(), status_code=200)
    except KeyError:
        raise HTTPException(status_code=404, detail="Food not found")