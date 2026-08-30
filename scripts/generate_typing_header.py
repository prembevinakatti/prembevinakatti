#!/usr/bin/env python3
"""
Generate a Guaranteed High-Visibility Animated Typist Header SVG:
- Pure Bright White (#FFFFFF) Title
- Fully visible under all conditions (Dark & Light)
- Native SMIL Typewriter Animation + Blinking Cyan Cursor
- Smooth cycling dynamic subtitles (every 3.5s)
- Zero emojis / Zero horizontal line separators
"""

import os

def generate_typing_header(output_path="assets/typing_header.svg"):
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    
    sub_lines = [
        "Builder of 40+ Production Web &amp; Mobile Projects",
        "Full-Stack &amp; Blockchain Engineer",
        "Specializing in High-Throughput &amp; Distributed Systems",
        "Architecting MERN, Next.js, Cloud &amp; AI Pipelines",
        "5 Industrial Internships &amp; 2x Hackathon Winner"
    ]
    
    width = 880
    height = 95
    
    svg = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" width="100%" height="{height}" fill="none">
  <defs>
    <style>
      .main-title {{
        font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif;
        font-size: 30px;
        font-weight: 800;
        fill: #FFFFFF !important;
        letter-spacing: -0.2px;
      }}

      .sub-title {{
        font-family: 'JetBrains Mono', 'Cascadia Code', ui-monospace, SFMono-Regular, Menlo, monospace;
        font-size: 15.5px;
        font-weight: 600;
        fill: #22D3EE !important;
        letter-spacing: 0.2px;
      }}

      .cursor-title {{
        font-family: -apple-system, BlinkMacSystemFont, monospace, sans-serif;
        font-size: 28px;
        font-weight: 300;
        fill: #22D3EE !important;
      }}

      /* Subtitle rotation keyframes (5 states over 17.5s cycle = 3.5s per line) */
      @keyframes subCycle0 {{
        0% {{ opacity: 0; transform: translateY(5px); }}
        3% {{ opacity: 1; transform: translateY(0); }}
        17% {{ opacity: 1; transform: translateY(0); }}
        20% {{ opacity: 0; transform: translateY(-5px); }}
        100% {{ opacity: 0; }}
      }}
      @keyframes subCycle1 {{
        0%, 20% {{ opacity: 0; transform: translateY(5px); }}
        23% {{ opacity: 1; transform: translateY(0); }}
        37% {{ opacity: 1; transform: translateY(0); }}
        40% {{ opacity: 0; transform: translateY(-5px); }}
        100% {{ opacity: 0; }}
      }}
      @keyframes subCycle2 {{
        0%, 40% {{ opacity: 0; transform: translateY(5px); }}
        43% {{ opacity: 1; transform: translateY(0); }}
        57% {{ opacity: 1; transform: translateY(0); }}
        60% {{ opacity: 0; transform: translateY(-5px); }}
        100% {{ opacity: 0; }}
      }}
      @keyframes subCycle3 {{
        0%, 60% {{ opacity: 0; transform: translateY(5px); }}
        63% {{ opacity: 1; transform: translateY(0); }}
        77% {{ opacity: 1; transform: translateY(0); }}
        80% {{ opacity: 0; transform: translateY(-5px); }}
        100% {{ opacity: 0; }}
      }}
      @keyframes subCycle4 {{
        0%, 80% {{ opacity: 0; transform: translateY(5px); }}
        83% {{ opacity: 1; transform: translateY(0); }}
        97% {{ opacity: 1; transform: translateY(0); }}
        100% {{ opacity: 0; transform: translateY(-5px); }}
      }}

      .line-0 {{ animation: subCycle0 17.5s infinite ease-in-out; }}
      .line-1 {{ animation: subCycle1 17.5s infinite ease-in-out; }}
      .line-2 {{ animation: subCycle2 17.5s infinite ease-in-out; }}
      .line-3 {{ animation: subCycle3 17.5s infinite ease-in-out; }}
      .line-4 {{ animation: subCycle4 17.5s infinite ease-in-out; }}
    </style>

    <!-- SMIL animated clip-path for robust cross-browser typewriter reveal -->
    <clipPath id="titleTypingClip">
      <rect x="0" y="0" width="500" height="50">
        <animate attributeName="width"
                 values="0; 0; 480; 480; 0"
                 keyTimes="0; 0.05; 0.35; 0.92; 1"
                 dur="9s"
                 repeatCount="indefinite" />
      </rect>
    </clipPath>
  </defs>

  <!-- Title Center Group (starts at x=200 for exact center alignment) -->
  <g transform="translate(200, 38)">
    <!-- Clipped Animated Text (Pure Bright White #FFFFFF) -->
    <g clip-path="url(#titleTypingClip)">
      <text x="0" y="0" class="main-title" fill="#FFFFFF">Hello, I'm Onkar Bevinakatti!</text>
    </g>

    <!-- Cursor following the typing animation and blinking -->
    <g>
      <animateTransform attributeName="transform"
                        type="translate"
                        values="0 0; 0 0; 475 0; 475 0; 0 0"
                        keyTimes="0; 0.05; 0.35; 0.92; 1"
                        dur="9s"
                        repeatCount="indefinite" />
      <text x="12" y="-1" class="cursor-title" fill="#22D3EE">
        |
        <animate attributeName="opacity" values="1;0;1" dur="0.75s" repeatCount="indefinite"/>
      </text>
    </g>
  </g>

  <!-- Continuously Changing Dynamic Subtitle Lines (Centered at x=440, no separator line) -->
  <g transform="translate(440, 76)">
    <text x="0" y="0" text-anchor="middle" class="sub-title line-0" fill="#22D3EE">{sub_lines[0]}</text>
    <text x="0" y="0" text-anchor="middle" class="sub-title line-1" fill="#22D3EE">{sub_lines[1]}</text>
    <text x="0" y="0" text-anchor="middle" class="sub-title line-2" fill="#22D3EE">{sub_lines[2]}</text>
    <text x="0" y="0" text-anchor="middle" class="sub-title line-3" fill="#22D3EE">{sub_lines[3]}</text>
    <text x="0" y="0" text-anchor="middle" class="sub-title line-4" fill="#22D3EE">{sub_lines[4]}</text>
  </g>
</svg>
"""
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(svg.strip())
    print(f"[+] Generated {output_path}")

if __name__ == "__main__":
    generate_typing_header()
