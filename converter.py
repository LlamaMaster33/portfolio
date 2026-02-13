
import os

html_dir = "html"
bf_dir = "bf"
os.makedirs(bf_dir, exist_ok=True)

def text_to_bf(text: str) -> str:
    result = []
    last_val = 0
    # Normalize line endings and handle non-ASCII
    text = text.replace('\r\n', '\n')
    text = text.replace('©', '(c)')  # Replace copyright symbol
    text = ''.join([c if ord(c) < 128 else '?' for c in text])
    
    for c in text:
        val = ord(c)
        diff = val - last_val
        if diff > 0:
            result.append('+' * diff)
        elif diff < 0:
            result.append('-' * (-diff))
        result.append('.')
        last_val = val
    return ''.join(result)

# Convert HTML files
for file in os.listdir(html_dir):
    if file.endswith(".html"):
        with open(os.path.join(html_dir, file), "r", encoding="utf-8") as f:
            content = f.read()
        
        # Just convert the whole file to one .bf
        bf_filename = file.replace(".html", ".bf")
        bf_file = os.path.join(bf_dir, bf_filename)
        bf_code = text_to_bf(content)
        
        with open(bf_file, "w", encoding="utf-8") as f:
            f.write(bf_code)
        
        print(f"[✓] Converted {file} → {bf_filename}")
