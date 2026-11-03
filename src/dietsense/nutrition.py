"""Deterministic calculations; demonstration only, not medical advice."""
from dataclasses import dataclass

@dataclass(frozen=True)
class NutritionRecord:
    name: str
    kcal_per_100g: float
    protein_per_100g: float = 0.0
    carbs_per_100g: float = 0.0
    fat_per_100g: float = 0.0


def portion_nutrients(record: NutritionRecord, grams: float) -> dict[str, float]:
    if grams <= 0:
        raise ValueError("grams must be positive")
    if record.kcal_per_100g < 0 or min(record.protein_per_100g,record.carbs_per_100g,record.fat_per_100g)<0:
        raise ValueError("nutrients must be nonnegative")
    factor=grams/100
    return {"kcal": round(factor*record.kcal_per_100g,2),
            "protein_g": round(factor*record.protein_per_100g,2),
            "carbs_g": round(factor*record.carbs_per_100g,2),
            "fat_g": round(factor*record.fat_per_100g,2)}


def mifflin_st_jeor(weight_kg: float,height_cm: float,age: int,sex: str) -> float:
    if weight_kg <= 0 or height_cm <= 0 or age <= 0:
        raise ValueError("weight, height, and age must be positive")
    constants={"male":5,"female":-161}
    if sex not in constants:
        raise ValueError("sex must be male or female for this equation")
    return 10*weight_kg + 6.25*height_cm - 5*age + constants[sex]


def estimate_tdee(bmr:float,activity_factor:float)->float:
    if bmr <= 0 or activity_factor <= 0:
        raise ValueError("bmr and activity_factor must be positive")
    return bmr*activity_factor
