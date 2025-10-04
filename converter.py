import os

html_dir = "html"
bf_dir = "bf"
os.makedirs(bf_dir, exist_ok=True)

def text_to_bf(text: str) -> str:
    result = []
    last_val = 0
    text = text.replace('\r\n', '\n')
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

        if file == "index.html":
            # Safely split by cards
            parts = []
            start = 0
            # Split after every <div class="card">
            while True:
                idx = content.find('<div class="card', start)
                if idx == -1:
                    parts.append(content[start:])  # remainder
                    break
                if idx != start:
                    parts.append(content[start:idx])
                start = idx
            # Now write each chunk to a separate .bf
            for i, part in enumerate(parts):
                bf_file = os.path.join(bf_dir, f"index_part{i+1}.bf")
                bf_code = text_to_bf(part)
                with open(bf_file, "w", encoding="utf-8") as f:
                    f.write(bf_code)
                print(f"[✓] Converted {file} → index_part{i+1}.bf")
        else:
            bf_file = os.path.join(bf_dir, file.replace(".html", ".bf"))
            bf_code = text_to_bf(content)
            with open(bf_file, "w", encoding="utf-8") as f:
                f.write(bf_code)
            print(f"[✓] Converted {file} → {bf_file}")
