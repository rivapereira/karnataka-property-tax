# 🚗 Karnataka Vehicle Road Tax Estimator

This simple tool helps estimate road tax for vehicles registered in Karnataka, India. Just input vehicle cost, age, fuel type, and district—get instant tax calculations with breakdowns based on Karnataka RTO rules.

---

## 🔧 Features

- 🎯 Calculates tax based on:
  - Vehicle cost
  - Age (age factor discounts)
  - Fuel type (Electric/Petrol/Diesel)
  - Vehicle type (Two/Four-Wheeler)
  - Selected Karnataka district

- 📑 Breaks down:
  - Base tax %
  - Cost-based tax
  - Age discount applied
  - Fixed cess

- 🖌️ Styled with Gradio + custom CSS

---

## 🛠 Built With

- [Gradio](https://www.gradio.app/)  
- [Python 3.x](https://python.org)

---

## 🚀 How to Run

1. Clone this repo:
   ```bash
   git clone https://github.com/yourusername/karnataka-road-tax-estimator.git
   cd karnataka-road-tax-estimator
Install Gradio:

bash
Copy
Edit
pip install gradio
Launch the app:

bash
Copy
Edit
python app.py
📸 Preview

## 🧠 Notes
Rules are based on Karnataka's standard 2023 tax slabs.

Electric vehicles are assumed to have no age discount.

You can update age_factor or cess as new rules apply.

## 📜 License
MIT – free for learning and remixing!

---

Let me know if you want both of these wrapped into `README.md` files + auto-generated `requirements.txt` for each.
