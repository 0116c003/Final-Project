"""CLI for a *fictional* example nutrient record; no external AI/API."""
import argparse,json
from .nutrition import NutritionRecord,portion_nutrients,mifflin_st_jeor,estimate_tdee

def main():
    p=argparse.ArgumentParser(description="DietSense calculation demo (synthetic food data)")
    p.add_argument("--food",choices=["demo_rice"],default="demo_rice")
    p.add_argument("--grams",type=float,default=150)
    p.add_argument("--weight",type=float,default=70)
    p.add_argument("--height",type=float,default=170)
    p.add_argument("--age",type=int,default=25)
    p.add_argument("--sex",choices=["male","female"],default="male")
    p.add_argument("--activity",type=float,default=1.4)
    args=p.parse_args()
    demo=NutritionRecord("demo_rice (fictional)",130,3,28,0.3)
    bmr=mifflin_st_jeor(args.weight,args.height,args.age,args.sex)
    result={"warning":"All example food values are fictional and for code demonstration only.",
        "food":args.food,"portion_g":args.grams,"estimated_nutrients":portion_nutrients(demo,args.grams),
        "estimated_bmr_kcal_day":round(bmr,2),"estimated_tdee_kcal_day":round(estimate_tdee(bmr,args.activity),2)}
    print(json.dumps(result,ensure_ascii=False,indent=2))

if __name__ == "__main__":main()
