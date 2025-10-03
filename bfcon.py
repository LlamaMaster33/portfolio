# html_to_bf_nested.py
import sys

def bf_for_char(ascii_val, prev_val):
    diff = ascii_val - prev_val
    code = ""

    if diff == 0:
        return "."
    
    # Nested loops for multiples of 10
    if abs(diff) >= 10:
        loops = abs(diff) // 10
        remainder = abs(diff) % 10
        # Outer loop setup
        code += "+" * loops + "["
        if diff > 0:
            code += ">" + "+" * 10 + "<"
        else:
            code += ">" + "-" * 10 + "<"
        code += "]"
        # Remaining difference
        if remainder > 0:
            code += "+" * remainder
        elif remainder < 0:
            code += "-" * (-remainder)
    else:
        if diff > 0:
            code += "+" * diff
        else:
            code += "-" * (-diff)
    
    return code + "."

# Load HTML
with open("index.html", "r", encoding="utf-8") as f:
    html = f.read()

bf_code = ""
prev_val = 0

for c in html:
    ascii_val = ord(c)
    bf_code += bf_for_char(ascii_val, prev_val)
    prev_val = ascii_val

# Save BF
with open("index_nested.bf", "w", encoding="utf-8") as f:
    f.write(bf_code)

print("Nested-loop optimized BF saved as index_nested.bf")
