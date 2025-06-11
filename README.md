# 💳 Credit Card Validator [Difficult Level]

A Python program that checks if a credit card number is valid using the **Luhn Algorithm**. This is a logic-focused project that’s perfect for intermediate Python learners!

---

## ✨ Features

- 🔢 Accepts credit card numbers (with or without spaces/dashes)
- 🧹 Cleans input automatically
- 🔁 Applies the Luhn Algorithm
- ✅ Tells if a number is **VALID** or **INVALID**

---

## 📋 What You Learn

- 📌 String and digit handling
- 🔄 Slicing and looping through numbers
- 🧠 Step-by-step algorithm logic
- ✖️ Modulo and integer math
- 💡 Real-world application of validation techniques

---

## ▶️ How to Run

1. Make sure Python is installed.
2. Save the code in a file like `credit_card_validator.py`.
3. Open terminal and run:

```bash
python credit_card_validator.py

Enter a credit card #: 4012 8888 8888 1881
VALID

Enter a credit card #: 1234-5678-9876-5432
INVALID
```

---

## 🧮 How the Luhn Algorithm Works

- 🧼 Remove spaces/dashes from input
- ➕ Add all digits in odd positions from the right
- 🔄 Double all digits in even positions from the right
- 🔟 If doubling gives a two-digit number, add its digits
- ➕ Add both sums
- ✅ If the final total is divisible by 10 → VALID, else INVALID

---

## 🙋‍♀️ Made By

Challenging mini project by **Tanvi** 🌸  
A great logic exercise for improving Python problem-solving skills!
