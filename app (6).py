import gradio as gr

# List of Karnataka districts
districts_karnataka = [
    "Bagalkot", "Ballari", "Belagavi", "Bengaluru Rural", "Bengaluru Urban",
    "Bidar", "Chamarajanagar", "Chikkaballapur", "Chikkamagaluru",
    "Chitradurga", "Dakshina Kannada", "Davanagere", "Dharwad", "Gadag",
    "Hassan", "Haveri", "Kalaburagi", "Kodagu", "Kolar", "Koppal", "Mandya",
    "Mysuru", "Raichur", "Ramanagara", "Shivamogga", "Tumakuru", "Udupi",
    "Uttara Kannada", "Vijayapura", "Yadgir", "Vijayanagara"
]

def calculate_karnataka_road_tax(district, vehicle_cost, fuel_type, vehicle_age, vehicle_type):
    if not district or vehicle_cost <= 0 or vehicle_age < 0:
        return "⚠️ Please enter valid and complete details."

    # Determine base tax rate
    if fuel_type == "Electric":
        tax_rate = 4
        age_factor = 1  # No age discount for EVs (can be adjusted per latest rules)
    else:
        if vehicle_cost <= 500000:
            tax_rate = 13
        elif vehicle_cost <= 1000000:
            tax_rate = 14
        elif vehicle_cost <= 2000000:
            tax_rate = 17
        else:
            tax_rate = 18

        if vehicle_age < 5:
            age_factor = 0.84
        elif vehicle_age < 10:
            age_factor = 0.59
        elif vehicle_age < 15:
            age_factor = 0.35
        else:
            age_factor = 0.25

    base_tax = (vehicle_cost * tax_rate) / 100
    adjusted_tax = base_tax * age_factor

    # Add cess
    if vehicle_type == "Two-Wheeler":
        additional_cess = 500
    elif vehicle_type == "Four-Wheeler":
        additional_cess = 1000
    else:
        additional_cess = 0

    total_tax = adjusted_tax + additional_cess

    return f"""🧾 Estimated Road Tax for **{district}**: ₹{total_tax:,.2f}  

**Calculation Breakdown:**
- Base tax rate: {tax_rate}%
- Cost-based tax: ₹{base_tax:,.2f}
- Age factor applied: {int(age_factor*100)}%
- Additional cess: ₹{additional_cess}"""

# CSS
custom_css = """
body {
    font-family: 'Inter', sans-serif;
}

.gradio-container {
    padding: 20px;
    max-width: 720px;
    margin: auto;
}


input, select {
    background-color: #fff !important;
    border: 1px solid #ccc !important;
    border-radius: 6px !important;
    padding: 8px !important;
}

textarea {
    font-size: 16px;
}

h1, h2, h3 {
    color: #d62828 !important;
    text-align: center;
}

label {
    font-weight: bold;
    color: #d62828;
}

/* Override Miku theme label color */
.gr-input-label,
.gr-textbox label,
.gr-dropdown label,
.gr-number label {
    color: #d62828 !important;
    font-weight: bold !important;
}


/* Label color override */
.gr-box .gr-label,
.gr-dropdown label,
label {
    color: #d62828 !important;
    font-weight: bold !important;
}

/* Dropdown selected text fix */
select {
    color: #111 !important;
    background-color: #fff !important;
}


"""

with gr.Blocks(theme="NoCrypt/miku@1.2.1") as demo:
    gr.Markdown("## 🚗 Karnataka Vehicle Road Tax Estimator")
    gr.Markdown("Enter your vehicle details to get a road tax estimate based on Karnataka RTO rules.")

    with gr.Column():
        district = gr.Dropdown(districts_karnataka, label="District")
        cost = gr.Number(label="Vehicle Cost (₹)")
        fuel = gr.Dropdown(["Petrol", "Diesel", "Electric"], label="Fuel Type")
        age = gr.Number(label="Vehicle Age (in years)")
        vtype = gr.Dropdown(["Two-Wheeler", "Four-Wheeler"], label="Vehicle Type")
        submit_btn = gr.Button("Calculate Tax 💸", variant="primary")

    output = gr.Markdown()

    submit_btn.click(fn=calculate_karnataka_road_tax, inputs=[district, cost, fuel, age, vtype], outputs=output)

demo.launch()
