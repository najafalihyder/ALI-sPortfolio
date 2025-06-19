#-- Func for Units of numbers 
def unit_numbers(number):
    for unit in ["", "K", "M", "B", "T"]:
        if abs(number) < 1000:
            return f"{number:.2f}{unit}"
        
        number /= 1000
    return f"{number:,.2f}E+"


# -- Func for highlighted coins
def highlight_change(val):
    if val > 5:
        return f"🟢 +{val:.2f}%"
    elif val < -5:
        return f"🔴 {val:.2f}%"
    else:
        return f"⚪️ {val:.2f}%"


