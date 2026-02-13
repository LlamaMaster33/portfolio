// Very basic Brainfuck interpreter
function interpretBF(code) {
    const tape = Array(30000).fill(0);
    let ptr = 0, output = "", pc = 0;
    const stack = [];
  
    while (pc < code.length) {
      const cmd = code[pc];
      switch (cmd) {
        case '>': ptr++; break;
        case '<': ptr--; break;
        case '+': tape[ptr] = (tape[ptr] + 1) % 256; break;
        case '-': tape[ptr] = (tape[ptr] + 255) % 256; break;
        case '.': output += String.fromCharCode(tape[ptr]); break;
        case ',': break; // Ignore input for now
        case '[':
          if (tape[ptr] === 0) {
            let open = 1;
            while (open > 0) {
              pc++;
              if (code[pc] === '[') open++;
              else if (code[pc] === ']') open--;
            }
          } else {
            stack.push(pc);
          }
          break;
        case ']':
          if (tape[ptr] !== 0) {
            pc = stack[stack.length - 1];
          } else {
            stack.pop();
          }
          break;
      }
      pc++;
    }
    return output;
  }
  
