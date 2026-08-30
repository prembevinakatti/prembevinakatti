#!/usr/bin/env python3
"""
Generate Developer OS Styled GitHub Telemetry & Language Cards
Matches the cyberpunk / dark aesthetic with cyan highlights, HUD accents, and real user metrics.
"""

import os

def generate_github_stats_svg(output_path="assets/github_stats.svg"):
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    
    width = 430
    height = 200
    
    svg = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" width="100%" height="100%">
  <defs>
    <linearGradient id="cardBg" x1="0" y1="0" x2="430" y2="200" gradientUnits="userSpaceOnUse">
      <stop offset="0%" stop-color="#0D1117"/>
      <stop offset="100%" stop-color="#0B132B"/>
    </linearGradient>
    <filter id="cyanGlow" x="-20%" y="-20%" width="140%" height="140%">
      <feGaussianBlur stdDeviation="2" result="blur"/>
      <feMerge>
        <feMergeNode in="blur"/>
        <feMergeNode in="SourceGraphic"/>
      </feMerge>
    </filter>
  </defs>
  
  <style>
    .title {{ font-family: 'JetBrains Mono', 'Segoe UI', monospace, sans-serif; font-size: 15px; font-weight: 800; fill: #22D3EE; }}
    .stat-label {{ font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; font-size: 13px; font-weight: 500; fill: #8B949E; }}
    .stat-val {{ font-family: 'JetBrains Mono', monospace; font-size: 14px; font-weight: 700; fill: #F0F6FC; }}
    .rank-circle {{ font-family: 'JetBrains Mono', monospace; font-size: 26px; font-weight: 900; fill: #22D3EE; }}
    .rank-sub {{ font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif; font-size: 10px; font-weight: 600; fill: #10B981; }}
  </style>

  <!-- Base Card -->
  <rect x="1" y="1" width="{width-2}" height="{height-2}" rx="8" fill="url(#cardBg)" stroke="#21262D" stroke-width="1.2"/>
  
  <!-- Top Left HUD Bracket -->
  <path d="M 6 18 L 6 6 L 18 6" fill="none" stroke="#22D3EE" stroke-width="1.5" opacity="0.8"/>
  <path d="M {width-6} {height-18} L {width-6} {height-6} L {width-18} {height-6}" fill="none" stroke="#22D3EE" stroke-width="1.5" opacity="0.8"/>

  <!-- Title -->
  <g transform="translate(25, 30)">
    <text x="0" y="0" class="title">⚡ GitHub Telemetry</text>
    <line x1="0" y1="8" x2="380" y2="8" stroke="#30363D" stroke-width="1"/>
    <line x1="0" y1="8" x2="140" y2="8" stroke="#22D3EE" stroke-width="1.5"/>
  </g>

  <!-- Stats Grid -->
  <g transform="translate(25, 62)">
    <!-- Total Contributions -->
    <g transform="translate(0, 0)">
      <circle cx="6" cy="6" r="4" fill="#22D3EE"/>
      <text x="18" y="10" class="stat-label">Total Contributions:</text>
      <text x="195" y="10" class="stat-val">1,585+</text>
    </g>
    
    <!-- Current Streak -->
    <g transform="translate(0, 26)">
      <circle cx="6" cy="6" r="4" fill="#10B981"/>
      <text x="18" y="10" class="stat-label">Active Streak:</text>
      <text x="195" y="10" class="stat-val">72 Days 🔥</text>
    </g>

    <!-- Public Repos -->
    <g transform="translate(0, 52)">
      <circle cx="6" cy="6" r="4" fill="#38BDF8"/>
      <text x="18" y="10" class="stat-label">Public Repositories:</text>
      <text x="195" y="10" class="stat-val">40 Repos</text>
    </g>

    <!-- Total Forks & Stars -->
    <g transform="translate(0, 78)">
      <circle cx="6" cy="6" r="4" fill="#F59E0B"/>
      <text x="18" y="10" class="stat-label">Repository Forks:</text>
      <text x="195" y="10" class="stat-val">2 Forks</text>
    </g>

    <!-- System Status -->
    <g transform="translate(0, 104)">
      <circle cx="6" cy="6" r="4" fill="#A78BFA"/>
      <text x="18" y="10" class="stat-label">System Runtime:</text>
      <text x="195" y="10" class="stat-val" fill="#10B981">100% Optimal</text>
    </g>
  </g>

  <!-- Right Side Rank Badge -->
  <g transform="translate(345, 115)">
    <circle cx="0" cy="0" r="36" fill="#0D1117" stroke="#22D3EE" stroke-width="2.5" filter="url(#cyanGlow)"/>
    <circle cx="0" cy="0" r="30" fill="#070D18" stroke="#30363D" stroke-width="1"/>
    <text x="0" y="8" text-anchor="middle" class="rank-circle">A+</text>
    <text x="0" y="21" text-anchor="middle" class="rank-sub">RANK</text>
  </g>
</svg>
"""
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(svg.strip())
    print(f"[+] Generated {output_path}")

def generate_top_langs_svg(output_path="assets/top_languages.svg"):
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    
    width = 430
    height = 200
    
    langs = [
        {"name": "JavaScript", "pct": 65.7, "color": "#F7DF1E"},
        {"name": "TypeScript", "pct": 14.8, "color": "#3178C6"},
        {"name": "CSS / Styling", "pct": 8.6, "color": "#563D7C"},
        {"name": "Python", "pct": 4.4, "color": "#3572A5"},
        {"name": "HTML", "pct": 4.2, "color": "#E34C26"},
        {"name": "Solidity / Others", "pct": 2.3, "color": "#AA6746"},
    ]
    
    svg = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" width="100%" height="100%">
  <defs>
    <linearGradient id="cardBg2" x1="0" y1="0" x2="430" y2="200" gradientUnits="userSpaceOnUse">
      <stop offset="0%" stop-color="#0D1117"/>
      <stop offset="100%" stop-color="#0B132B"/>
    </linearGradient>
    <clipPath id="barClip">
      <rect x="25" y="48" width="380" height="10" rx="5"/>
    </clipPath>
  </defs>
  
  <style>
    .title {{ font-family: 'JetBrains Mono', 'Segoe UI', monospace, sans-serif; font-size: 15px; font-weight: 800; fill: #22D3EE; }}
    .lang-name {{ font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; font-size: 12px; font-weight: 600; fill: #F0F6FC; }}
    .lang-pct {{ font-family: 'JetBrains Mono', monospace; font-size: 12px; font-weight: 500; fill: #8B949E; }}
  </style>

  <!-- Base Card -->
  <rect x="1" y="1" width="{width-2}" height="{height-2}" rx="8" fill="url(#cardBg2)" stroke="#21262D" stroke-width="1.2"/>
  
  <!-- Top Left HUD Bracket -->
  <path d="M 6 18 L 6 6 L 18 6" fill="none" stroke="#22D3EE" stroke-width="1.5" opacity="0.8"/>
  <path d="M {width-6} {height-18} L {width-6} {height-6} L {width-18} {height-6}" fill="none" stroke="#22D3EE" stroke-width="1.5" opacity="0.8"/>

  <!-- Title -->
  <g transform="translate(25, 30)">
    <text x="0" y="0" class="title">🛠️ Most Used Languages</text>
    <line x1="0" y1="8" x2="380" y2="8" stroke="#30363D" stroke-width="1"/>
    <line x1="0" y1="8" x2="160" y2="8" stroke="#22D3EE" stroke-width="1.5"/>
  </g>

  <!-- Multi-Color Progress Bar -->
  <g clip-path="url(#barClip)">
"""
    # Build segmented bar
    cur_x = 25
    total_bar_w = 380
    for l in langs:
        w = (l["pct"] / 100.0) * total_bar_w
        svg += f'    <rect x="{cur_x:.1f}" y="48" width="{w:.1f}" height="10" fill="{l["color"]}"/>\n'
        cur_x += w

    svg += """  </g>

  <!-- Language Grid (2 Columns) -->
  <g transform="translate(25, 76)">
"""
    # Column 1 (Left 3)
    for i, l in enumerate(langs[:3]):
        y = i * 26 + 12
        svg += f"""    <g transform="translate(0, {y})">
      <circle cx="5" cy="5" r="4.5" fill="{l["color"]}"/>
      <text x="18" y="9" class="lang-name">{l["name"]}</text>
      <text x="120" y="9" class="lang-pct">{l["pct"]}%</text>
    </g>
"""
    # Column 2 (Right 3)
    for i, l in enumerate(langs[3:]):
        y = i * 26 + 12
        svg += f"""    <g transform="translate(195, {y})">
      <circle cx="5" cy="5" r="4.5" fill="{l["color"]}"/>
      <text x="18" y="9" class="lang-name">{l["name"]}</text>
      <text x="120" y="9" class="lang-pct">{l["pct"]}%</text>
    </g>
"""

    svg += """  </g>
</svg>
"""
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(svg.strip())
    print(f"[+] Generated {output_path}")

if __name__ == "__main__":
    generate_github_stats_svg()
    generate_top_langs_svg()
