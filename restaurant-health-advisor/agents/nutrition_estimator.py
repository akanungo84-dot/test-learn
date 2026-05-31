from utils.ollama_client import ask_llm

PROMPT='''You are a clinical nutritionist. Analyze menu items for Diabetes, High BP, Weight Loss, Heart Disease, CKD and Fitness. Return JSON with product_name, ingredients, calories_estimate, sugar_risk, sodium_risk, glycemic_risk, score and recommendation.'''


def analyze_menu(menu_text:str):
    return ask_llm(PROMPT + '\n\n' + menu_text)
