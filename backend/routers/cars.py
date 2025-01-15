from typing import List, Dict, Any
from math import ceil
from fastapi import APIRouter, Request, Body, HTTPException, BackgroundTasks
from fastapi.encoders import jsonable_encoder
from models import CarBase
from utils.report import report_pipeline
import joblib
import pandas as pd

router = APIRouter()

@router.get("/all", response_description="List all cars")
async def list_all_cars(
    request: Request,
    min_price: int = 0,
    max_price: int = 100000,
    brand: str = "",
    page: int = 1,
) -> Dict[str, Any]:
    RESULTS_PER_PAGE = 25
    skip = (page - 1) * RESULTS_PER_PAGE

    # Construire la requête
    query = {"price": {"$lt": max_price, "$gt": min_price}}
    if brand:
        query["brand"] = brand

    # Compter le total des documents
    total_docs = await request.app.mongodb["cars"].count_documents(query)
    total_pages = ceil(total_docs / RESULTS_PER_PAGE)

    # Exécuter la requête paginée et s'assurer que tous les champs sont inclus
    cursor = (
        request.app.mongodb["cars"]
        .find(
            query,
            {
                "_id": 1,
                "brand": 1,
                "make": 1,
                "year": 1,
                "cm3": 1,
                "km": 1,
                "price": 1
            }
        )
        .sort("km", -1)
        .skip(skip)
        .limit(RESULTS_PER_PAGE)
    )
    
    # Convertir les documents en format approprié
    results = []
    async for doc in cursor:
        car_dict = {
            "id": str(doc["_id"]),
            "brand": doc["brand"],
            "make": doc["make"],
            "year": doc["year"],
            "cm3": doc["cm3"],
            "km": doc["km"],
            "price": doc["price"]
        }
        results.append(car_dict)

    return {
        "results": results,
        "total_pages": total_pages,
        "current_page": page
    }

@router.get("/", response_description="List all cars")
async def list_cars(request: Request) -> List[Dict[str, Any]]:
    cars = []
    for doc in await request.app.mongodb["cars"].find().to_list(length=100):
        cars.append(doc)
    return cars

@router.get("/sample/{n}", response_description="Sample of N cars")
async def get_sample(n: int, request: Request) -> List[Dict[str, Any]]:
    query = [
        {"$match": {"year": {"$gt": 2010}}},
        {"$project": {"_id": 0}},
        {"$sample": {"size": n}},
        {"$sort": {"brand": 1, "make": 1, "year": 1}},
    ]
    full_query = request.app.mongodb["cars"].aggregate(query)
    return [el async for el in full_query]

@router.get("/brand/{val}/{brand}", response_description="Get brand models by val")
async def brand_price(brand: str, val: str, request: Request):
    query = [
        {"$match": {"brand": brand}},
        {"$project": {"_id": 0}},
        {
            "$group": {"_id": {"model": "$make"}, f"avg_{val}": {"$avg": f"${val}"}},
        },
        {"$sort": {f"avg_{val}": 1}},
    ]

    full_query = request.app.mongodb["cars"].aggregate(query)
    return [el async for el in full_query]

@router.get("/brand/count", response_description="Count by brand")
async def brand_count(request: Request):
    query = [{"$group": {"_id": "$brand", "count": {"$sum": 1}}}]
    full_query = request.app.mongodb["cars"].aggregate(query)
    return [el async for el in full_query]

@router.get("/make/count/{brand}", response_description="Count by brand")
async def brand_count(brand: str, request: Request):
    query = [
        {"$match": {"brand": brand}},
        {"$group": {"_id": "$make", "count": {"$sum": 1}}},
        {"$sort": {"count": -1}},
    ]

    full_query = request.app.mongodb["cars"].aggregate(query)
    results = [el async for el in full_query]
    return results

@router.post("/email", response_description="Send email")
async def send_mail(
    background_tasks: BackgroundTasks,
    cars_num: int = Body(...),
    email: str = Body(...),
):
    background_tasks.add_task(report_pipeline, email, cars_num)
    return {"Received": {"email": email, "cars_num": cars_num}}

@router.post("/predict", response_description="Predict price")
async def predict(
    brand: str = Body(...),
    make: str = Body(...),
    year: int = Body(...),
    cm3: int = Body(...),
    km: int = Body(...),
):
    loaded_model = joblib.load("./random_forest_pipe.joblib")
    input_data = {
        "brand": brand,
        "make": make,
        "year": year,
        "cm3": cm3,
        "km": km,
    }
    from_db_df = pd.DataFrame(input_data, index=[0])
    prediction = float(loaded_model.predict(from_db_df)[0])
    return {"prediction": prediction}
