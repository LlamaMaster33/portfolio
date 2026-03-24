import os

bf_dir = "bf"
html_dir = "html"
os.makedirs(html_dir, exist_ok=True)

def bf_to_text(bf_code: str) -> str:
    """Execute Brainfuck code and return output as HTML"""
    tape = [0] * 30000
    ptr = 0
    output = []
    i = 0
    loop_stack = []
    
    while i < len(bf_code):
        cmd = bf_code[i]
        if cmd == '>':
            ptr += 1
        elif cmd == '<':
            ptr -= 1
        elif cmd == '+':
            tape[ptr] = (tape[ptr] + 1) % 256
        elif cmd == '-':
            tape[ptr] = (tape[ptr] - 1) % 256
        elif cmd == '.':
            output.append(chr(tape[ptr]))
        elif cmd == '[':
            if tape[ptr] == 0:
                depth = 1
                while depth > 0:
                    i += 1
                    if bf_code[i] == '[':
                        depth += 1
                    elif bf_code[i] == ']':
                        depth -= 1
            else:
                loop_stack.append(i)
        elif cmd == ']':
            if tape[ptr] != 0:
                i = loop_stack[-1]
            else:
                loop_stack.pop()
        i += 1
    
    return ''.join(output)

# Convert Brainfuck files to HTML
for file in os.listdir(bf_dir):
    if file.endswith(".bf"):
        with open(os.path.join(bf_dir, file), "r", encoding="utf-8") as f:
            bf_code = f.read()
        
        html_filename = file.replace(".bf", ".html")
        html_file = os.path.join(html_dir, html_filename)
        html_content = bf_to_text(bf_code)
        
        with open(html_file, "w", encoding="utf-8") as f:
            f.write(html_content)
        
        print(f"[✓] Converted {file} → {html_filename}")