#!/usr/bin/env python3
"""
Generate Cyberpunk / Developer OS Section Header SVGs matching the specification:
- Left Cyan Pill Indicator
- Top-Left Corner Accent '┌'
- Section Emoji Icon
- Primary Title (White) + Secondary Subtitle (Cyan)
- Right-aligned System Identifier Tag with Glowing Cyan Beacon Dot
"""

import os

HEADERS = [
    {
        "id": "01_system_identity",
        "icon": "⚡",
        "primary": "SYSTEM_IDENTITY",
        "secondary": "PHILOSOPHY_ARCHITECTURE",
        "tag": "SYS.CORE_KERNEL",
        "filename": "header_01_identity.svg"
    },
    {
        "id": "02_current_runtime",
        "icon": "⚡",
        "primary": "CURRENT_RUNTIME",
        "secondary": "LIVE_FOCUS",
        "tag": "SYS.RUNTIME_STATE",
        "filename": "header_02_runtime.svg"
    },
    {
        "id": "03_experience",
        "icon": "💼",
        "primary": "EXPERIENCE",
        "secondary": "5_INDUSTRIAL_INTERNSHIPS",
        "tag": "SYS.WORK_HISTORY",
        "filename": "header_03_experience.svg"
    },
    {
        "id": "04_technical_arsenal",
        "icon": "🛠️",
        "primary": "TECHNICAL_ARSENAL",
        "secondary": "TECH_STACK_MATRIX",
        "tag": "SYS.TECH_MATRIX",
        "filename": "header_04_tech_stack.svg"
    },
    {
        "id": "05_selected_work",
        "icon": "🚀",
        "primary": "SELECTED_WORK",
        "secondary": "PRODUCTION_BUILDS",
        "tag": "SYS.FLAGSHIP_PROJECTS",
        "filename": "header_05_selected_work.svg"
    },
    {
        "id": "06_achievements",
        "icon": "🏆",
        "primary": "ACHIEVEMENTS",
        "secondary": "HACKATHON_RECORDS",
        "tag": "SYS.AWARDS_LOG",
        "filename": "header_06_achievements.svg"
    },
    {
        "id": "07_credentials",
        "icon": "📄",
        "primary": "CREDENTIALS",
        "secondary": "RESUME_SCANNER",
        "tag": "SYS.VERIFIED_DOCS",
        "filename": "header_07_credentials.svg"
    },
    {
        "id": "08_telemetry",
        "icon": "📊",
        "primary": "TELEMETRY",
        "secondary": "OBSERVABILITY_METRICS",
        "tag": "SYS.GITHUB_STATS",
        "filename": "header_08_telemetry.svg"
    },
    {
        "id": "09_contribution_stream",
        "icon": "🐍",
        "primary": "CONTRIBUTION_STREAM",
        "secondary": "ACTIVITY_GRAPH",
        "tag": "SYS.COMMIT_STREAM",
        "filename": "header_09_contribution.svg"
    },
    {
        "id": "10_network_uplink",
        "icon": "🌐",
        "primary": "NETWORK_UPLINK",
        "secondary": "CONNECT_CHANNELS",
        "tag": "SYS.COMM_CHANNELS",
        "filename": "header_10_network.svg"
    }
]

def generate_header_svg(item, output_dir="assets/headers"):
    os.makedirs(output_dir, exist_ok=True)
    out_path = os.path.join(output_dir, item["filename"])
    
    width = 880
    height = 44
    
    svg = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" width="100%" height="{height}" fill="none">
  <defs>
    <linearGradient id="cardBg_{item['id']}" x1="0" y1="0" x2="880" y2="44" gradientUnits="userSpaceOnUse">
      <stop offset="0%" stop-color="#070D18"/>
      <stop offset="50%" stop-color="#0B1226"/>
      <stop offset="100%" stop-color="#080F1E"/>
    </linearGradient>
    <linearGradient id="cyanPill_{item['id']}" x1="0" y1="0" x2="0" y2="44" gradientUnits="userSpaceOnUse">
      <stop offset="0%" stop-color="#38BDF8"/>
      <stop offset="50%" stop-color="#00D2FF"/>
      <stop offset="100%" stop-color="#0284C7"/>
    </linearGradient>
    <filter id="glow_{item['id']}" x="-50%" y="-50%" width="200%" height="200%">
      <feGaussianBlur in="SourceGraphic" stdDeviation="2.5" result="blur"/>
      <feMerge>
        <feMergeNode in="blur"/>
        <feMergeNode in="SourceGraphic"/>
      </feMerge>
    </filter>
    <clipPath id="clip_{item['id']}">
      <rect x="0" y="0" width="{width}" height="{height}" rx="7" ry="7"/>
    </clipPath>
  </defs>
  <style>
    .title-white {{
      font-family: 'JetBrains Mono', 'Segoe UI', -apple-system, BlinkMacSystemFont, monospace, sans-serif;
      font-size: 14.5px;
      font-weight: 800;
      fill: #FFFFFF;
      letter-spacing: 0.6px;
    }}
    .title-cyan {{
      font-family: 'JetBrains Mono', 'Segoe UI', -apple-system, BlinkMacSystemFont, monospace, sans-serif;
      font-size: 14.5px;
      font-weight: 800;
      fill: #00D2FF;
      letter-spacing: 0.6px;
    }}
    .tag-text {{
      font-family: 'JetBrains Mono', 'Segoe UI', -apple-system, BlinkMacSystemFont, monospace, sans-serif;
      font-size: 11px;
      font-weight: 600;
      fill: #8FA3BF;
      letter-spacing: 1.2px;
    }}
    .emoji-icon {{
      font-size: 17px;
      font-family: 'Apple Color Emoji', 'Segoe UI Emoji', 'Noto Color Emoji', sans-serif;
    }}
  </style>

  <!-- Container Box with Rounded Corners -->
  <g clip-path="url(#clip_{item['id']})">
    <rect x="0" y="0" width="{width}" height="{height}" fill="url(#cardBg_{item['id']})" stroke="#1E293B" stroke-width="1.2" rx="7"/>
    
    <!-- Left Pill Accent Bar -->
    <rect x="0" y="0" width="8" height="{height}" fill="url(#cyanPill_{item['id']})"/>
    
    <!-- Subtle Top Rim Glow -->
    <line x1="8" y1="1" x2="350" y2="1" stroke="#38BDF8" stroke-width="1" opacity="0.25"/>
  </g>

  <!-- Outer Stroke Overlay -->
  <rect x="0.5" y="0.5" width="{width-1}" height="{height-1}" rx="6.5" fill="none" stroke="#1E293B" stroke-width="1"/>

  <!-- Top-Left Corner Accent '┌' -->
  <path d="M 22 13 L 16 13 L 16 19" fill="none" stroke="#38BDF8" stroke-width="1.3" opacity="0.75" stroke-linecap="round" stroke-linejoin="round"/>

  <!-- Emoji Icon -->
  <text x="32" y="28" class="emoji-icon">{item["icon"]}</text>

  <!-- Title: Primary (White) // Secondary (Cyan) -->
  <text x="59" y="27.5">
    <tspan class="title-white">{item["primary"]}</tspan>
    <tspan class="title-cyan"> // {item["secondary"]}</tspan>
  </text>

  <!-- Right System Identifier Tag + Cyan Beacon Dot -->
  <g transform="translate({width - 20}, 0)">
    <text x="-16" y="27.5" text-anchor="end" class="tag-text">{item["tag"]}</text>
    <circle cx="-3" cy="23.5" r="4" fill="#00D2FF" filter="url(#glow_{item['id']})"/>
    <circle cx="-3" cy="23.5" r="1.8" fill="#FFFFFF"/>
  </g>
</svg>
"""
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(svg.strip())
    print(f"[+] Generated {out_path}")

def main():
    for h in HEADERS:
        generate_header_svg(h)

if __name__ == "__main__":
    main()
