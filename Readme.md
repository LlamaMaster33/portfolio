# Portfolio Website

A unique portfolio website with a Serial Experiments Lain aesthetic, featuring a boot sequence and content delivered via Brainfuck interpretation.

## Features
- Tokyo Night color scheme
- CRT scanline effects
- Boot sequence (skipped on subsequent visits)
- Brainfuck-encoded content
- Theme toggle (light/dark)
- Keyboard navigation

## Setup

1. Install Python 3
2. Run the converter:
   ```bash
   python converter.py
   ```
3. Open `systembrain.html` in your browser

## Structure
- `html/` - Original HTML content files
- `bf/` - Generated Brainfuck files
- `systembrain.html` - Main entry point
- `interpreter.js` - Brainfuck interpreter
- `converter.py` - HTML to Brainfuck converter

## Navigation
- Click links in header
- Or use arrow keys (Left/Right)
- Or press 1-4 for direct page access