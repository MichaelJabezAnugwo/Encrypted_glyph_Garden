# Encrypted Glyph Garden

**Aesthetic Encryption Series – Experiment 003**

This project transforms encrypted text into a living field of animated glyphs — abstract, symbolic shapes that pulse, rotate, and shimmer in response to the hidden structure of a message. Each glyph is a visual echo of a character, a fragment of meaning rendered in motion and color.

---

## Concept

In cryptography, encryption hides meaning. In art, abstraction reveals it. This sketch bridges both worlds.

Instead of decrypting a message, we **visualize its encrypted structure**. Each character in a string becomes a glyph — a symbolic, animated form — whose shape, color, and behavior are derived from the character’s ASCII value. The result is a **glyph garden**: a calm or chaotic field of encrypted symbols, animated in real time.

This is not a cipher to be cracked. It’s a **visual language of secrecy** — expressive, non-literal, and deeply personal.

---

## How It Works

1. **Input**: A string of text (e.g., `"I dream in encrypted color"`)
2. **Encoding**:
   - Each character is converted to its ASCII value
   - Values are grouped and mapped to:
     - Rotation angle
     - Rotation speed
     - Shape type (circle, arc, or line)
     - Size
     - Color (via modular RGB mapping)
3. **Glyph Generation**:
   - Glyphs are arranged in an 8×8 grid
   - Each glyph is centered in its cell and animated independently
4. **Animation**:
   - Glyphs rotate continuously
   - Shapes pulse in size using sine wave modulation
   - The entire field evolves over time, revealing the rhythm of the encrypted input

---

## Tools Used

- **Processing.py** – Python mode in [Processing](https://processing.org/)
- **Built-in Python functions** – For ASCII conversion and math
- **No external libraries** – Fully compatible with Processing’s native environment

---

## File Structure

├── glyph_garden.pyde       # Main Processing.py sketch 

├── README.md               # Project documentation



---

## How to Run

1. Install [Processing](https://processing.org/download/)
2. Launch Processing and switch to **Python mode**
3. Open `glyph_garden.pyde`
4. Run the sketch
5. Modify the `text_input` variable to visualize your own encrypted message

---

## Visual Examples

| Input Text | Visual Feel |
|------------|-------------|
| `"hello"` | Calm, symmetrical glyphs with soft rotation |
| `"chaos123"` | Jagged, fast-spinning glyphs with high contrast |
| `"I dream in encrypted color"` | Layered, poetic, slow-moving glyphs with blended hues |

Each input creates a unique visual fingerprint — a symbolic representation of the message’s structure, not its meaning.

---
## visual Output

[Screen Recording 2025-12-16 122631.mp4](Screen%20Recording%202025-12-16%20122631.mp4)

![Screenshot 2025-12-16 142027.png](Screenshot%202025-12-16%20142027.png)
---

## Why Glyphs?

A **glyph** is more than a shape — it’s a symbol of meaning. In this sketch, each glyph is:
- A **visual stand-in** for a character
- A **non-literal expression** of encrypted data
- A **living symbol** that moves, pulses, and rotates with intention

This project treats encryption not as a barrier, but as a **canvas**.

---

## Related Projects

- [Encrypted Color Fields](https://github.com/MichaelJabezAnugwo/aesthetic-encryption-color-fields)  
  Visualizing encrypted text as abstract color grids

- [Visual Hash Generator (Bar Chart)](https://github.com/MichaelJabezAnugwo/aesthetic-encryption-bar-charts)  
  SHA-256 hashes rendered as bar charts

---

## Author

**Michael**  
Cybersecurity Professional & creative coder  


---

## License

MIT License — feel free to remix, expand, or build upon this work.

---

## Final Thought

> “A glyph is not a letter. It is a gesture — a mark of presence.  
> In this garden, encryption becomes expression.”
