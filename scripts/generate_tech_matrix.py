#!/usr/bin/env python3
"""
Generate a dedicated, standalone TECH STACK MATRIX Terminal Card SVG
for Section 04 (TECHNICAL ARSENAL).
Combines the radial 12-node animated radar on the left with structured technical categories on the right.
"""

import os
import math

def get_tech_nodes():
    return [
        {"id": "react", "name": "React", "color": "#61DAFB", "bg": "#0D1E30", "border": "#22D3EE"},
        {"id": "nextjs", "name": "Next.js", "color": "#F0F6FC", "bg": "#161B22", "border": "#8B949E"},
        {"id": "rn", "name": "React\nNative", "color": "#61DAFB", "bg": "#0D1E30", "border": "#22D3EE"},
        {"id": "node", "name": "Node.js", "color": "#22C55E", "bg": "#0B2316", "border": "#10B981"},
        {"id": "express", "name": "Express.js", "color": "#F0F6FC", "bg": "#161B22", "border": "#8B949E"},
        {"id": "ts", "name": "TypeScript", "color": "#38BDF8", "bg": "#0F2338", "border": "#3178C6"},
        {"id": "js", "name": "JavaScript", "color": "#FBBF24", "bg": "#28200C", "border": "#F59E0B"},
        {"id": "mongo", "name": "MongoDB", "color": "#10B981", "bg": "#0A2417", "border": "#059669"},
        {"id": "supabase", "name": "Supabase", "color": "#3ECF8E", "bg": "#0D251D", "border": "#10B981"},
        {"id": "tailwind", "name": "Tailwind CSS", "color": "#06B6D4", "bg": "#09222B", "border": "#22D3EE"},
        {"id": "redux", "name": "Redux", "color": "#A78BFA", "bg": "#1D1633", "border": "#7C3AED"},
        {"id": "aws", "name": "AWS", "color": "#F59E0B", "bg": "#261A0A", "border": "#D97706"},
    ]

def render_node_icon(node_id, nx, ny, color):
    parts = []
    if node_id in ("react", "rn"):
        parts.append(f'<ellipse cx="{nx}" cy="{ny}" rx="8" ry="3" fill="none" stroke="{color}" stroke-width="1"/>')
        parts.append(f'<ellipse cx="{nx}" cy="{ny}" rx="8" ry="3" fill="none" stroke="{color}" stroke-width="1" transform="rotate(60 {nx} {ny})"/>')
        parts.append(f'<ellipse cx="{nx}" cy="{ny}" rx="8" ry="3" fill="none" stroke="{color}" stroke-width="1" transform="rotate(120 {nx} {ny})"/>')
        parts.append(f'<circle cx="{nx}" cy="{ny}" r="1.3" fill="{color}"/>')
    elif node_id == "nextjs":
        parts.append(f'<text x="{nx}" y="{ny+3.2}" class="mono" font-size="7.5" font-weight="800" fill="{color}" text-anchor="middle">N</text>')
        parts.append(f'<circle cx="{nx}" cy="{ny}" r="6.5" fill="none" stroke="{color}" stroke-width="1"/>')
    elif node_id == "node":
        parts.append(f'<polygon points="{nx},{ny-6.5} {nx+5.5},{ny-3.2} {nx+5.5},{ny+3.2} {nx},{ny+6.5} {nx-5.5},{ny+3.2} {nx-5.5},{ny-3.2}" fill="none" stroke="{color}" stroke-width="1.1"/>')
        parts.append(f'<text x="{nx}" y="{ny+2.8}" class="mono" font-size="6.5" font-weight="700" fill="{color}" text-anchor="middle">JS</text>')
    elif node_id == "express":
        parts.append(f'<text x="{nx}" y="{ny+3.2}" class="mono" font-size="7.5" font-weight="700" fill="{color}" text-anchor="middle">ex</text>')
    elif node_id in ("ts", "js"):
        label = "TS" if node_id == "ts" else "JS"
        parts.append(f'<rect x="{nx-6}" y="{ny-6}" width="12" height="12" rx="2" fill="{color}"/>')
        parts.append(f'<text x="{nx}" y="{ny+3.2}" class="mono" font-size="7" font-weight="800" fill="#0D1117" text-anchor="middle">{label}</text>')
    elif node_id == "mongo":
        parts.append(f'<path d="M {nx} {ny-6} C {nx-4.5} {ny-1.5} {nx-3.5} {ny+3.5} {nx} {ny+6} C {nx+3.5} {ny+3.5} {nx+4.5} {ny-1.5} {nx} {ny-6} Z" fill="none" stroke="{color}" stroke-width="1.1"/>')
        parts.append(f'<line x1="{nx}" y1="{ny-4.5}" x2="{nx}" y2="{ny+5}" stroke="{color}" stroke-width="0.8"/>')
    elif node_id == "postgres":
        parts.append(f'<path d="M {nx-5.5} {ny-3.5} C {nx-5.5} {ny-6.5} {nx+5.5} {ny-6.5} {nx+5.5} {ny-3.5} C {nx+5.5} {ny+3.5} {nx} {ny+6} {nx-5.5} {ny+3.5} Z" fill="none" stroke="{color}" stroke-width="1.1"/>')
        parts.append(f'<circle cx="{nx-1.8}" cy="{ny-1.8}" r="0.9" fill="{color}"/>')
    elif node_id == "tailwind":
        parts.append(f'<path d="M {nx-5} {ny-1.5} C {nx-3} {ny-4} {nx-1} {ny-4} {nx} {ny-1.5} C {nx+1} {ny+1} {nx+3} {ny+1} {nx+5} {ny-1.5}" fill="none" stroke="{color}" stroke-width="1.1" stroke-linecap="round"/>')
        parts.append(f'<path d="M {nx-4} {ny+1.5} C {nx-2} {ny-1} {nx} {ny-1} {nx+1} {ny+1.5} C {nx+2} {ny+4} {nx+4} {ny+4} {nx+6} {ny+1.5}" fill="none" stroke="{color}" stroke-width="1.1" stroke-linecap="round"/>')
    elif node_id == "redux":
        parts.append(f'<circle cx="{nx}" cy="{ny}" r="5.5" fill="none" stroke="{color}" stroke-width="1" stroke-dasharray="2.5 1.5"/>')
        parts.append(f'<circle cx="{nx-2.5}" cy="{ny-1.8}" r="1.2" fill="{color}"/>')
        parts.append(f'<circle cx="{nx+2.5}" cy="{ny-1.8}" r="1.2" fill="{color}"/>')
        parts.append(f'<circle cx="{nx}" cy="{ny+2.5}" r="1.2" fill="{color}"/>')
    elif node_id == "aws":
        parts.append(f'<text x="{nx}" y="{ny+1}" class="mono" font-size="6.5" font-weight="800" fill="{color}" text-anchor="middle">aws</text>')
        parts.append(f'<path d="M {nx-4.5} {ny+3.2} Q {nx} {ny+5.2} {nx+4.5} {ny+3.2}" fill="none" stroke="{color}" stroke-width="0.9"/>')
    return "\n".join(parts)

def generate_matrix_card(is_dark=True, output_path="assets/tech_matrix_dark.svg"):
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    
    # 880 × 420
    cx = 210
    cy = 230
    radius = 106
    hub_radius = 38
    node_radius = 13.5
    
    bg_color = "#08090D" if is_dark else "#F8FAFC"
    card_bg = "#0F1117" if is_dark else "#FFFFFF"
    terminal_border = "#21262D" if is_dark else "#CBD5E1"
    grid_line = "#161B22" if is_dark else "#E2E8F0"
    header_bg = "#0B0D13" if is_dark else "#F1F5F9"
    title_color = "#22D3EE" if is_dark else "#0284C7"
    accent_emerald = "#10B981" if is_dark else "#059669"
    accent_purple = "#A78BFA" if is_dark else "#7C3AED"
    text_primary = "#F0F6FC" if is_dark else "#0F172A"
    text_secondary = "#8B949E" if is_dark else "#475569"
    text_label = "#6E7681" if is_dark else "#64748B"
    pill_bg = "#161B22" if is_dark else "#F1F5F9"
    pill_border = "#30363D" if is_dark else "#94A3B8"
    divider_color = "#21262D" if is_dark else "#E2E8F0"
    hub_bg = "#0B1526" if is_dark else "#EFF6FF"
    hub_border = "#22D3EE" if is_dark else "#0284C7"
    ray_color = "#22D3EE" if is_dark else "#0284C7"

    nodes = get_tech_nodes()
    
    svg = []
    svg.append('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 880 420" width="100%" height="100%">')
    
    svg.append(f"""
    <defs>
        <linearGradient id="hubGrad2" x1="0%" y1="0%" x2="100%" y2="100%">
            <stop offset="0%" stop-color="{hub_bg}" stop-opacity="0.95"/>
            <stop offset="100%" stop-color="#070C18" stop-opacity="0.95"/>
        </linearGradient>
        <pattern id="gridPat2" width="20" height="20" patternUnits="userSpaceOnUse">
            <path d="M 20 0 L 0 0 0 20" fill="none" stroke="{grid_line}" stroke-width="0.6" stroke-opacity="0.4"/>
        </pattern>
        <radialGradient id="centerGlow2" cx="50%" cy="50%" r="50%">
            <stop offset="0%" stop-color="{title_color}" stop-opacity="0.25"/>
            <stop offset="100%" stop-color="{title_color}" stop-opacity="0"/>
        </radialGradient>
    </defs>
    <style><![CDATA[
        .mono {{ 
            font-family: 'JetBrains Mono', 'Cascadia Code', 'Fira Code', ui-monospace, SFMono-Regular, Menlo, monospace;
            text-rendering: geometricPrecision;
            -webkit-font-smoothing: antialiased;
        }}
        .sans {{ font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif; }}
        
        @keyframes rotateClockwise {{
            from {{ transform: rotate(0deg); }}
            to   {{ transform: rotate(360deg); }}
        }}
        @keyframes rotateCounter {{
            from {{ transform: rotate(360deg); }}
            to   {{ transform: rotate(0deg); }}
        }}
        @keyframes pulseGlow {{
            0%, 100% {{ opacity: 0.85; transform: scale(1); }}
            50%      {{ opacity: 1; transform: scale(1.02); }}
        }}
        @keyframes dashFlow {{
            to {{ stroke-dashoffset: -20; }}
        }}
        @keyframes pulseLive {{
            0%, 100% {{ opacity: 1; transform: scale(1); }}
            50%      {{ opacity: 0.35; transform: scale(0.85); }}
        }}
        
        .orbit-ring-1 {{ transform-origin: {cx}px {cy}px; animation: rotateClockwise 30s linear infinite; }}
        .orbit-ring-2 {{ transform-origin: {cx}px {cy}px; animation: rotateCounter 40s linear infinite; }}
        .center-hub   {{ transform-origin: {cx}px {cy}px; animation: pulseGlow 4s ease-in-out infinite; }}
        .connector-ray {{ stroke-dasharray: 4 3; animation: dashFlow 2s linear infinite; }}
        .live-dot     {{ animation: pulseLive 2s infinite ease-in-out; transform-origin: 820px 24px; }}
        
        @media (prefers-reduced-motion: reduce) {{
            .orbit-ring-1, .orbit-ring-2, .center-hub, .connector-ray, .live-dot {{
                animation: none !important;
            }}
        }}
    ]]></style>
    """)
    
    # Chassis
    svg.append(f'<rect width="880" height="420" rx="14" fill="{bg_color}" stroke="{terminal_border}" stroke-width="1.2"/>')
    svg.append(f'<rect x="1" y="1" width="878" height="418" rx="13" fill="url(#gridPat2)"/>')
    
    # Header Bar
    svg.append(f'<rect x="0" y="0" width="880" height="46" rx="14" fill="{header_bg}" stroke="{terminal_border}" stroke-width="1"/>')
    svg.append(f'<line x1="0" y1="46" x2="880" y2="46" stroke="{terminal_border}" stroke-width="1"/>')
    svg.append('<circle cx="26" cy="23" r="5" fill="#FF5F56"/>')
    svg.append('<circle cx="44" cy="23" r="5" fill="#FFBD2E"/>')
    svg.append('<circle cx="62" cy="23" r="5" fill="#27C93F"/>')
    svg.append(f'<text x="88" y="28" class="mono" font-size="12" font-weight="600" fill="{text_secondary}">term://onkar.os/tech_matrix.sh <tspan fill="{title_color}">--active</tspan></text>')
    
    svg.append(f'<circle class="live-dot" cx="818" cy="23" r="4" fill="{accent_emerald}"/>')
    svg.append(f'<text x="829" y="27" class="mono" font-size="10" font-weight="700" fill="{accent_emerald}">LIVE</text>')
    
    # ==================== LEFT: RADIAL MATRIX ====================
    # Radial Background
    svg.append(f'<circle cx="{cx}" cy="{cy}" r="135" fill="url(#centerGlow2)"/>')
    svg.append(f'<circle cx="{cx}" cy="{cy}" r="{radius}" fill="none" stroke="{terminal_border}" stroke-width="0.8" opacity="0.6"/>')
    svg.append(f'<circle class="orbit-ring-1" cx="{cx}" cy="{cy}" r="76" fill="none" stroke="{title_color}" stroke-width="0.8" stroke-dasharray="4 6" opacity="0.4"/>')
    svg.append(f'<circle class="orbit-ring-2" cx="{cx}" cy="{cy}" r="52" fill="none" stroke="{accent_purple}" stroke-width="0.8" stroke-dasharray="2 4" opacity="0.5"/>')
    
    node_positions = []
    for i, node in enumerate(nodes):
        angle = -math.pi / 2 + (2 * math.pi / len(nodes)) * i
        nx = cx + radius * math.cos(angle)
        ny = cy + radius * math.sin(angle)
        node_positions.append((nx, ny, angle, node))
        
    # Connector Rays
    for nx, ny, angle, node in node_positions:
        x1 = cx + hub_radius * math.cos(angle)
        y1 = cy + hub_radius * math.sin(angle)
        x2 = cx + (radius - node_radius) * math.cos(angle)
        y2 = cy + (radius - node_radius) * math.sin(angle)
        svg.append(f'<line class="connector-ray" x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}" stroke="{title_color}" stroke-width="0.9" opacity="0.6"/>')
        svg.append(f'<circle cx="{x1:.1f}" cy="{y1:.1f}" r="1.5" fill="{title_color}"/>')
        
    # Center Hub
    svg.append(f'<g class="center-hub">')
    svg.append(f'<circle cx="{cx}" cy="{cy}" r="{hub_radius+4}" fill="none" stroke="{title_color}" stroke-width="0.8" stroke-dasharray="6 3" opacity="0.5"/>')
    svg.append(f'<circle cx="{cx}" cy="{cy}" r="{hub_radius}" fill="url(#hubGrad2)" stroke="{hub_border}" stroke-width="1.4"/>')
    svg.append(f'<text x="{cx}" y="{cy-10}" class="mono" font-size="10" font-weight="800" fill="{title_color}" text-anchor="middle" letter-spacing="0.5">FULL</text>')
    svg.append(f'<text x="{cx}" y="{cy+3}" class="mono" font-size="10" font-weight="800" fill="{title_color}" text-anchor="middle" letter-spacing="0.5">STACK</text>')
    svg.append(f'<text x="{cx}" y="{cy+15}" class="mono" font-size="7.5" font-weight="700" fill="{text_primary}" text-anchor="middle" letter-spacing="0.8">DEVELOPER</text>')
    svg.append(f'</g>')
    
    # Render Nodes
    for nx, ny, angle, node in node_positions:
        nid = node["id"]
        ncolor = node["color"]
        nbg = node["bg"]
        nborder = node["border"]
        
        svg.append(f'<circle cx="{nx:.1f}" cy="{ny:.1f}" r="{node_radius}" fill="{nbg}" stroke="{nborder}" stroke-width="1.2"/>')
        svg.append(render_node_icon(nid, nx, ny, ncolor))
        
        label_dist = radius + 21
        lx = cx + label_dist * math.cos(angle)
        ly = cy + label_dist * math.sin(angle)
        cos_val = math.cos(angle)
        sin_val = math.sin(angle)
        anchor = "middle"
        if cos_val > 0.4:
            anchor = "start"
            lx += 2
        elif cos_val < -0.4:
            anchor = "end"
            lx -= 2
        y_shift = 3
        if sin_val < -0.7:
            y_shift = -2
        elif sin_val > 0.7:
            y_shift = 8
            
        label_lines = node["name"].split("\n")
        if len(label_lines) == 1:
            svg.append(f'<text x="{lx:.1f}" y="{ly+y_shift:.1f}" class="mono" font-size="8" font-weight="600" fill="{text_primary}" text-anchor="{anchor}">{label_lines[0]}</text>')
        else:
            svg.append(f'<text x="{lx:.1f}" y="{ly+y_shift-4:.1f}" class="mono" font-size="7.5" font-weight="600" fill="{text_primary}" text-anchor="{anchor}">{label_lines[0]}</text>')
            svg.append(f'<text x="{lx:.1f}" y="{ly+y_shift+5:.1f}" class="mono" font-size="7.5" font-weight="600" fill="{text_primary}" text-anchor="{anchor}">{label_lines[1]}</text>')

    # Bottom Status Pill on Left
    svg.append(f'<rect x="40" y="375" width="340" height="26" rx="6" fill="{pill_bg}" stroke="{terminal_border}" stroke-width="0.8"/>')
    svg.append(f'<circle cx="56" cy="388" r="3.5" fill="{accent_emerald}"/>')
    svg.append(f'<text x="66" y="392" class="mono" font-size="9" font-weight="700" fill="{title_color}">12+ CORE TECHNOLOGIES</text>')
    svg.append(f'<text x="235" y="392" class="mono" font-size="9" fill="{text_label}">//</text>')
    svg.append(f'<text x="260" y="392" class="mono" font-size="9" font-weight="700" fill="{accent_emerald}">STACK: ACTIVE</text>')

    # ==================== RIGHT: CATEGORIZED ARSENAL ====================
    rx = 430
    svg.append(f'<rect x="{rx}" y="62" width="430" height="340" rx="10" fill="{card_bg}" stroke="{terminal_border}" stroke-width="1"/>')
    svg.append(f'<rect x="{rx}" y="62" width="430" height="30" rx="10" fill="{pill_bg}"/>')
    svg.append(f'<line x1="{rx}" y1="92" x2="{rx+430}" y2="92" stroke="{terminal_border}" stroke-width="0.8"/>')
    svg.append(f'<text x="{rx+16}" y="82" class="mono" font-size="11" font-weight="700" fill="{title_color}">[ ARSENAL.CATEGORIES ]</text>')
    svg.append(f'<text x="{rx+414}" y="82" class="mono" font-size="9" font-weight="600" fill="{accent_emerald}" text-anchor="end">PRODUCTION_READY</text>')
    
    categories = [
        ("LANGUAGES", "TypeScript · JavaScript · Solidity · Python · C++ · REST", "#22D3EE"),
        ("FRONTEND &amp; MOBILE", "React.js · Next.js · React Native · Tailwind CSS · Redux · Vite", "#38BDF8"),
        ("BACKEND &amp; WEB3", "Node.js · Express.js · FastAPI · Ethers.js · Web3.js · Polygon", "#10B981"),
        ("DATABASE &amp; CACHE", "MongoDB · Redis · Supabase · Firebase", "#A78BFA"),
        ("CLOUD &amp; DEVOPS", "AWS · Vercel · Render · GitHub Actions · Git", "#F59E0B"),
    ]
    
    cy_cat = 120
    for title, stack, color in categories:
        svg.append(f'<circle cx="{rx+18}" cy="{cy_cat-4}" r="3" fill="{color}"/>')
        svg.append(f'<text x="{rx+28}" y="{cy_cat}" class="mono" font-size="10.5" font-weight="700" fill="{color}">{title}</text>')
        svg.append(f'<text x="{rx+28}" y="{cy_cat+18}" class="mono" font-size="10" font-weight="500" fill="{text_primary}">{stack}</text>')
        svg.append(f'<line x1="{rx+18}" y1="{cy_cat+32}" x2="{rx+412}" y2="{cy_cat+32}" stroke="{divider_color}" stroke-width="0.8" stroke-dasharray="2 3"/>')
        cy_cat += 54
        
    svg.append('</svg>')
    
    with open(output_path, "w", encoding="utf-8") as f:
        f.write("\n".join(svg))
    print(f"[+] Generated {output_path}")

if __name__ == "__main__":
    generate_matrix_card(is_dark=True, output_path="assets/tech_matrix_dark.svg")
    generate_matrix_card(is_dark=False, output_path="assets/tech_matrix_light.svg")
