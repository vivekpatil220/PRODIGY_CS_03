import re

def password_strength_checker(password):
    score = 0
    feedback = []

    length_criteria = len(password) >= 8
    upper_case_criteria = re.search(r'[A-Z]', password)
    lower_case_criteria = re.search(r'[a-z]', password)
    digit_criteria = re.search(r'[0-9]', password)
    special_char_criteria = re.search(r'[\W_]', password)

    if length_criteria:
        score += 1
    else:
        feedback.append("Password should be at least 8 characters long.")

    if upper_case_criteria:
        score += 1
    else:
        feedback.append("Password should include at least one uppercase letter.")

    if lower_case_criteria:
        score += 1
    else:
        feedback.append("Password should include at least one lowercase letter.")

    if digit_criteria:
        score += 1
    else:
        feedback.append("Password should include at least one digit.")

    if special_char_criteria:
        score += 1
    else:
        feedback.append("Password should include at least one special character.")

    if score == 5:
        strength = "Very Strong"
    elif score == 4:
        strength = "Strong"
    elif score == 3:
        strength = "Moderate"
    elif score == 2:
        strength = "Weak"
    else:
        strength = "Very Weak"

    return strength, feedback

if __name__ == "__main__":
    password = input("Enter your password: ")
    strength, feedback = password_strength_checker(password)
    print(f"Password Strength: {strength}")
    if feedback:
        print("Feedback:")
        for comment in feedback:
            print(f"- {comment}")
