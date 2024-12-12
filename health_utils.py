def calculate_bmi(height, weight):
    """Calculate Body Mass Index (BMI) given height in meters and weight in kilograms.
       
       Args:
       height (float): Height in centimeters.
       weight (float): Weight in kilograms.
       Returns:
       float: Calculated BMI.
    """

    BMI = weight / (height ** 2)
    return BMI
def calculate_bmr(height, weight, age, gender):
    """
    Calculate Basal Metabolic Rate (BMR) using the Harris-Benedict equation.

    Args:
    height (float): Height in centimeters.
    weight (float): Weight in kilograms.
    age (int): Age in years.
    gender (str): Gender ('male' or 'female').

    Returns:
    float: Calculated BMR.
    """
    heigh = height  
    if gender == 'male':
        BMR =  88.362 + (13.397 * weight) + (4.799 * heigh) - (5.677 * age)
    if gender == 'female':
        BMR =  447.593 + (9.247 * weight) + (3.098 * heigh) - (4.330 * age)
    return BMR

