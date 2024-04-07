from flask import Flask, request, jsonify
from flask_cors import CORS
import joblib

app = Flask(__name__)
CORS(app)

# Load the model
model = joblib.load('model.pkl')

# Sample meal plans database
MEAL_PLANS = {
    'low_carb': {
        'day1': {'breakfast': 'Scrambled eggs with spinach', 'lunch': 'Grilled chicken salad', 'dinner': 'Stir-fried tofu with vegetables'},
        'day2': {'breakfast': 'Greek yogurt with nuts', 'lunch': 'Turkey and avocado wrap', 'dinner': 'Grilled salmon with asparagus'},
        'day3': {'breakfast': 'Almond flour pancakes', 'lunch': 'Shrimp and avocado salad', 'dinner': 'Baked chicken with roasted Brussels sprouts'},
        'day4': {'breakfast': 'Chia seed pudding', 'lunch': 'Beef lettuce wraps', 'dinner': 'Pan-seared cod with cauliflower mash'},
        'day5': {'breakfast': 'Frittata with mushrooms and feta', 'lunch': 'Cobb salad', 'dinner': 'Lamb chops with grilled zucchini'},
        'day6': {'breakfast': 'Protein smoothie with spinach and avocado', 'lunch': 'Chicken avocado soup', 'dinner': 'Pork tenderloin with sautéed kale'},
        'day7': {'breakfast': 'Coconut yogurt with flaxseeds', 'lunch': 'Egg salad on lettuce', 'dinner': 'Salmon patties with side salad'},
    },
    'plant_based': {
        'day1': {'breakfast': 'Oatmeal with fresh berries', 'lunch': 'Quinoa salad with mixed vegetables', 'dinner': 'Lentil soup'},
        'day2': {'breakfast': 'Smoothie with spinach, banana, and almond milk', 'lunch': 'Chickpea and avocado sandwich', 'dinner': 'Vegetable stir-fry with tofu'},
        'day3': {'breakfast': 'Chia pudding with mixed nuts and berries', 'lunch': 'Vegan sushi rolls', 'dinner': 'Black bean chili'},
        'day4': {'breakfast': 'Avocado toast on whole grain bread', 'lunch': 'Sweet potato and black bean burrito', 'dinner': 'Stuffed bell peppers'},
        'day5': {'breakfast': 'Almond butter and banana smoothie', 'lunch': 'Lentil and beet salad', 'dinner': 'Curried cauliflower soup'},
        'day6': {'breakfast': 'Granola with soy yogurt', 'lunch': 'Falafel wrap with tahini sauce', 'dinner': 'Mushroom and pea risotto'},
        'day7': {'breakfast': 'Peanut butter and jelly on whole grain toast', 'lunch': 'Vegan taco salad', 'dinner': 'Eggplant parmesan with marinara sauce'},
    },
    'high_protein': {
        'day1': {'breakfast': 'Egg omelet with vegetables', 'lunch': 'Chicken Caesar salad', 'dinner': 'Beef stir-fry with broccoli'},
        'day2': {'breakfast': 'Cottage cheese with sliced peaches', 'lunch': 'Tuna salad', 'dinner': 'Pork chops with steamed green beans'},
        'day3': {'breakfast': 'Protein shake with whey protein, banana, and almond milk', 'lunch': 'Turkey burger with sweet potato fries', 'dinner': 'Grilled salmon with quinoa and asparagus'},
        'day4': {'breakfast': 'Greek yogurt with granola and honey', 'lunch': 'Chicken and avocado wrap', 'dinner': 'Lamb skewers with Greek salad'},
        'day5': {'breakfast': 'Scrambled eggs with smoked salmon', 'lunch': 'Quinoa and black bean stuffed bell peppers', 'dinner': 'Chicken tikka masala with cauliflower rice'},
        'day6': {'breakfast': 'Protein pancakes with blueberries', 'lunch': 'Beef and vegetable soup', 'dinner': 'Grilled shrimp with mixed greens salad'},
        'day7': {'breakfast': 'Overnight oats with protein powder and strawberries', 'lunch': 'Salmon salad with mixed greens and vinaigrette', 'dinner': 'Turkey meatballs with spaghetti squash'},
    }
}


@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json(force=True)
    prediction = model.predict([data['features']])
    return jsonify(prediction.tolist())

@app.route('/meal_plans/<plan_type>', methods=['GET'])
def get_meal_plan(plan_type):
    if plan_type not in MEAL_PLANS:
        return jsonify({'error': 'Meal plan type not found'}), 404
    
    return jsonify(MEAL_PLANS[plan_type])

if __name__ == '__main__':
    app.run(debug=True)
