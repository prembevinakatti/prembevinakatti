#!/usr/bin/env python3
"""
Developer OS - Animated Hero SVG Banner Generator
Features:
- Left Panel: TECH STACK MATRIX with Central Radial Hub (FULL STACK DEVELOPER)
  surrounded by 12 connected technology nodes with rotating orbits & pulse animations.
- Right Panel: SYSTEM.INFO with Colorful Technology Badge Tags (Shield-style Pill Badges).
- Dark Obsidian & Light Mode support.
"""

import os
import math

def get_tech_nodes():
    """Returns the 12 radial technology nodes in clockwise order starting from Top."""
    return [
        {"id": "react", "name": "React", "color": "#61DAFB", "bg": "#0D1E30", "border": "#22D3EE"},
        {"id": "docker", "name": "Docker", "color": "#2496ED", "bg": "#0B1C2E", "border": "#38BDF8"},
        {"id": "rn", "name": "React\nNative", "color": "#61DAFB", "bg": "#0D1E30", "border": "#22D3EE"},
        {"id": "node", "name": "Node.js", "color": "#22C55E", "bg": "#0B2316", "border": "#10B981"},
        {"id": "express", "name": "Express.js", "color": "#F0F6FC", "bg": "#161B22", "border": "#8B949E"},
        {"id": "ts", "name": "TypeScript", "color": "#38BDF8", "bg": "#0F2338", "border": "#3178C6"},
        {"id": "js", "name": "JavaScript", "color": "#FBBF24", "bg": "#28200C", "border": "#F59E0B"},
        {"id": "mongo", "name": "MongoDB", "color": "#10B981", "bg": "#0A2417", "border": "#059669"},
        {"id": "postgres", "name": "PostgreSQL", "color": "#38BDF8", "bg": "#0D2035", "border": "#0284C7"},
        {"id": "tailwind", "name": "Tailwind CSS", "color": "#06B6D4", "bg": "#09222B", "border": "#22D3EE"},
        {"id": "redux", "name": "Redux", "color": "#A78BFA", "bg": "#1D1633", "border": "#7C3AED"},
        {"id": "aws", "name": "AWS", "color": "#F59E0B", "bg": "#261A0A", "border": "#D97706"},
    ]

def render_node_icon(node_id, nx, ny, color):
    parts = []
    if node_id in ("react", "rn"):
        parts.append(f'<ellipse cx="{nx}" cy="{ny}" rx="8.5" ry="3.2" fill="none" stroke="{color}" stroke-width="1"/>')
        parts.append(f'<ellipse cx="{nx}" cy="{ny}" rx="8.5" ry="3.2" fill="none" stroke="{color}" stroke-width="1" transform="rotate(60 {nx} {ny})"/>')
        parts.append(f'<ellipse cx="{nx}" cy="{ny}" rx="8.5" ry="3.2" fill="none" stroke="{color}" stroke-width="1" transform="rotate(120 {nx} {ny})"/>')
        parts.append(f'<circle cx="{nx}" cy="{ny}" r="1.4" fill="{color}"/>')
    elif node_id == "docker":
        parts.append(f'<rect x="{nx-4.5}" y="{ny-3.5}" width="2.2" height="1.8" fill="{color}"/>')
        parts.append(f'<rect x="{nx-1.8}" y="{ny-3.5}" width="2.2" height="1.8" fill="{color}"/>')
        parts.append(f'<rect x="{nx+0.9}" y="{ny-3.5}" width="2.2" height="1.8" fill="{color}"/>')
        parts.append(f'<rect x="{nx-1.8}" y="{ny-5.8}" width="2.2" height="1.8" fill="{color}"/>')
        parts.append(f'<rect x="{nx+0.9}" y="{ny-5.8}" width="2.2" height="1.8" fill="{color}"/>')
        parts.append(f'<path d="M {nx-6} {ny-1} Q {nx-4} {ny+4.5} {nx+5} {ny+3.5} Q {nx+6} {ny} {nx+4} {ny-1} Z" fill="none" stroke="{color}" stroke-width="1"/>')
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

def render_badge_pill(x, y, text, bg_color, text_color="#FFFFFF", logo_prefix=None):
    """Renders a sleek, crisp shield-style badge tag."""
    # Approximate text width
    w = len(text) * 5.8 + 14
    if logo_prefix:
        w += 14
        
    parts = []
    # Badge Chassis
    parts.append(f'<rect x="{x}" y="{y}" width="{w:.1f}" height="17" rx="3" fill="{bg_color}"/>')
    
    cur_text_x = x + 7
    if logo_prefix:
        # Prefix box
        parts.append(f'<rect x="{x}" y="{y}" width="16" height="17" rx="3" fill="#000000" fill-opacity="0.25"/>')
        parts.append(f'<text x="{x+8}" y="{y+11.5}" class="mono" font-size="7.5" font-weight="800" fill="{text_color}" text-anchor="middle">{logo_prefix}</text>')
        cur_text_x = x + 21
        parts.append(f'<text x="{cur_text_x}" y="{y+11.5}" class="mono" font-size="7.5" font-weight="700" fill="{text_color}">{text}</text>')
    else:
        parts.append(f'<text x="{cur_text_x}" y="{y+11.5}" class="mono" font-size="7.5" font-weight="700" fill="{text_color}">{text}</text>')
        
    return "\n".join(parts), w

def generate_banner_svg(is_dark=True, output_path="assets/dark.svg"):
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    
    # Left Panel: x=18, y=62, w=344, h=382
    cx = 18 + 344 / 2  # 190
    cy = 62 + 382 / 2  # 253
    
    # Palette
    if is_dark:
        bg_color = "#08090D"          # Deep obsidian black
        card_bg = "#0F1117"           # Card chassis
        terminal_border = "#21262D"   # Neutral dark border
        grid_line = "#161B22"         # Background grid
        header_bg = "#0B0D13"         # Header
        title_color = "#22D3EE"       # Cyan glow
        accent_emerald = "#10B981"    # Emerald
        accent_purple = "#A78BFA"     # Purple
        text_primary = "#F0F6FC"      # Clean white
        text_secondary = "#8B949E"    # Muted slate
        text_label = "#6E7681"        # Gray label
        pill_bg = "#161B22"
        pill_border = "#30363D"
        divider_color = "#21262D"
        hub_bg = "#0B1526"
        hub_border = "#22D3EE"
        ray_color = "#22D3EE"
    else:
        bg_color = "#F8FAFC"
        card_bg = "#FFFFFF"
        terminal_border = "#CBD5E1"
        grid_line = "#E2E8F0"
        header_bg = "#F1F5F9"
        title_color = "#0284C7"
        accent_emerald = "#059669"
        accent_purple = "#7C3AED"
        text_primary = "#0F172A"
        text_secondary = "#475569"
        text_label = "#64748B"
        pill_bg = "#F1F5F9"
        pill_border = "#94A3B8"
        divider_color = "#E2E8F0"
        hub_bg = "#EFF6FF"
        hub_border = "#0284C7"
        ray_color = "#0284C7"

    nodes = get_tech_nodes()
    radius = 104  # Orbit distance
    
    svg_parts = []
    svg_parts.append('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 880 460" width="100%" height="100%">')
    
    # Defs & CSS Animations
    svg_parts.append(f"""
    <defs>
        <linearGradient id="hubGrad" x1="0%" y1="0%" x2="100%" y2="100%">
            <stop offset="0%" stop-color="{hub_bg}" stop-opacity="0.95"/>
            <stop offset="100%" stop-color="#070C18" stop-opacity="0.95"/>
        </linearGradient>
        <pattern id="gridPat" width="20" height="20" patternUnits="userSpaceOnUse">
            <path d="M 20 0 L 0 0 0 20" fill="none" stroke="{grid_line}" stroke-width="0.6" stroke-opacity="0.4"/>
        </pattern>
        <radialGradient id="centerGlow" cx="50%" cy="50%" r="50%">
            <stop offset="0%" stop-color="{title_color}" stop-opacity="0.25"/>
            <stop offset="100%" stop-color="{title_color}" stop-opacity="0"/>
        </radialGradient>
    </defs>
    <style><![CDATA[
        .mono {{ 
            font-family: 'JetBrains Mono', 'Cascadia Code', 'Fira Code', ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, monospace;
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
    
    # Outer Chassis
    svg_parts.append(f'<rect width="880" height="460" rx="14" fill="{bg_color}" stroke="{terminal_border}" stroke-width="1.2"/>')
    svg_parts.append(f'<rect x="1" y="1" width="878" height="458" rx="13" fill="url(#gridPat)"/>')
    
    # Header Bar
    svg_parts.append(f'<rect x="0" y="0" width="880" height="48" rx="14" fill="{header_bg}" stroke="{terminal_border}" stroke-width="1"/>')
    svg_parts.append(f'<line x1="0" y1="48" x2="880" y2="48" stroke="{terminal_border}" stroke-width="1"/>')
    
    # Controls
    svg_parts.append('<circle cx="26" cy="24" r="5.5" fill="#FF5F56"/>')
    svg_parts.append('<circle cx="44" cy="24" r="5.5" fill="#FFBD2E"/>')
    svg_parts.append('<circle cx="62" cy="24" r="5.5" fill="#27C93F"/>')
    svg_parts.append(f'<text x="88" y="29" class="mono" font-size="12" font-weight="600" fill="{text_secondary}">term://onkar.os/profile.sh <tspan fill="{title_color}">--live</tspan></text>')
    
    # Handle Pill & Live Telemetry
    svg_parts.append(f'<rect x="660" y="12" width="134" height="24" rx="12" fill="{pill_bg}" stroke="{pill_border}" stroke-width="0.8"/>')
    svg_parts.append(f'<text x="727" y="28" class="mono" font-size="11" font-weight="600" fill="{title_color}" text-anchor="middle">@prembevinakatti</text>')
    svg_parts.append(f'<circle class="live-dot" cx="818" cy="24" r="4.5" fill="{accent_emerald}"/>')
    svg_parts.append(f'<text x="829" y="28" class="mono" font-size="10.5" font-weight="700" fill="{accent_emerald}">LIVE</text>')
    
    # ==================== LEFT PANEL: TECH.STACK MATRIX ====================
    svg_parts.append(f'<rect x="18" y="62" width="344" height="382" rx="10" fill="{card_bg}" stroke="{terminal_border}" stroke-width="1"/>')
    svg_parts.append(f'<rect x="18" y="62" width="344" height="30" rx="10" fill="{pill_bg}"/>')
    svg_parts.append(f'<line x1="18" y1="92" x2="362" y2="92" stroke="{terminal_border}" stroke-width="0.8"/>')
    svg_parts.append(f'<text x="32" y="82" class="mono" font-size="11" font-weight="700" fill="{title_color}">[ TECH.STACK ]</text>')
    svg_parts.append(f'<text x="348" y="82" class="mono" font-size="9" fill="{text_label}" text-anchor="end">RADAR.MATRIX // 240 FPS</text>')
    
    # Corner HUD
    svg_parts.append(f'<path d="M 28 108 L 28 100 L 36 100" fill="none" stroke="{title_color}" stroke-width="1" opacity="0.6"/>')
    svg_parts.append(f'<text x="40" y="108" class="mono" font-size="8" fill="{text_label}">Trx: 0xAF7E // STK_OK</text>')
    svg_parts.append(f'<path d="M 352 108 L 352 100 L 344 100" fill="none" stroke="{title_color}" stroke-width="1" opacity="0.6"/>')
    svg_parts.append(f'<text x="340" y="108" class="mono" font-size="8" font-weight="700" fill="{accent_emerald}" text-anchor="end">LIVE_SYNC</text>')
    
    # Geometry
    svg_parts.append(f'<circle cx="{cx}" cy="{cy}" r="130" fill="url(#centerGlow)"/>')
    svg_parts.append(f'<circle cx="{cx}" cy="{cy}" r="{radius}" fill="none" stroke="{terminal_border}" stroke-width="0.8" opacity="0.6"/>')
    svg_parts.append(f'<circle class="orbit-ring-1" cx="{cx}" cy="{cy}" r="76" fill="none" stroke="{title_color}" stroke-width="0.8" stroke-dasharray="4 6" opacity="0.4"/>')
    svg_parts.append(f'<circle class="orbit-ring-2" cx="{cx}" cy="{cy}" r="52" fill="none" stroke="{accent_purple}" stroke-width="0.8" stroke-dasharray="2 4" opacity="0.5"/>')
    
    node_positions = []
    for i, node in enumerate(nodes):
        angle = -math.pi / 2 + (2 * math.pi / len(nodes)) * i
        nx = cx + radius * math.cos(angle)
        ny = cy + radius * math.sin(angle)
        node_positions.append((nx, ny, angle, node))
        
    hub_radius = 38
    node_radius = 13.5
    for nx, ny, angle, node in node_positions:
        x1 = cx + hub_radius * math.cos(angle)
        y1 = cy + hub_radius * math.sin(angle)
        x2 = cx + (radius - node_radius) * math.cos(angle)
        y2 = cy + (radius - node_radius) * math.sin(angle)
        svg_parts.append(f'<line class="connector-ray" x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}" stroke="{title_color}" stroke-width="0.9" opacity="0.6"/>')
        svg_parts.append(f'<circle cx="{x1:.1f}" cy="{y1:.1f}" r="1.5" fill="{title_color}"/>')
    
    # Center Hub
    svg_parts.append(f'<g class="center-hub">')
    svg_parts.append(f'<circle cx="{cx}" cy="{cy}" r="{hub_radius+4}" fill="none" stroke="{title_color}" stroke-width="0.8" stroke-dasharray="6 3" opacity="0.5"/>')
    svg_parts.append(f'<circle cx="{cx}" cy="{cy}" r="{hub_radius}" fill="url(#hubGrad)" stroke="{hub_border}" stroke-width="1.4"/>')
    svg_parts.append(f'<text x="{cx}" y="{cy-10}" class="mono" font-size="10" font-weight="800" fill="{title_color}" text-anchor="middle" letter-spacing="0.5">FULL</text>')
    svg_parts.append(f'<text x="{cx}" y="{cy+3}" class="mono" font-size="10" font-weight="800" fill="{title_color}" text-anchor="middle" letter-spacing="0.5">STACK</text>')
    svg_parts.append(f'<text x="{cx}" y="{cy+15}" class="mono" font-size="7.5" font-weight="700" fill="{text_primary}" text-anchor="middle" letter-spacing="0.8">DEVELOPER</text>')
    svg_parts.append(f'</g>')
    
    # Nodes
    for nx, ny, angle, node in node_positions:
        nid = node["id"]
        ncolor = node["color"]
        nbg = node["bg"]
        nborder = node["border"]
        
        svg_parts.append(f'<circle cx="{nx:.1f}" cy="{ny:.1f}" r="{node_radius}" fill="{nbg}" stroke="{nborder}" stroke-width="1.2"/>')
        svg_parts.append(render_node_icon(nid, nx, ny, ncolor))
        
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
            svg_parts.append(f'<text x="{lx:.1f}" y="{ly+y_shift:.1f}" class="mono" font-size="8" font-weight="600" fill="{text_primary}" text-anchor="{anchor}">{label_lines[0]}</text>')
        else:
            svg_parts.append(f'<text x="{lx:.1f}" y="{ly+y_shift-4:.1f}" class="mono" font-size="7.5" font-weight="600" fill="{text_primary}" text-anchor="{anchor}">{label_lines[0]}</text>')
            svg_parts.append(f'<text x="{lx:.1f}" y="{ly+y_shift+5:.1f}" class="mono" font-size="7.5" font-weight="600" fill="{text_primary}" text-anchor="{anchor}">{label_lines[1]}</text>')

    # Bottom Status Pill on Left
    svg_parts.append(f'<path d="M 28 406 L 28 414 L 36 414" fill="none" stroke="{title_color}" stroke-width="1" opacity="0.6"/>')
    svg_parts.append(f'<path d="M 352 406 L 352 414 L 344 414" fill="none" stroke="{title_color}" stroke-width="1" opacity="0.6"/>')
    svg_parts.append(f'<circle cx="44" cy="425" r="3" fill="{accent_emerald}"/>')
    svg_parts.append(f'<text x="52" y="428" class="mono" font-size="9" font-weight="700" fill="{title_color}">12+ CORE TECHNOLOGIES</text>')
    svg_parts.append(f'<text x="210" y="428" class="mono" font-size="9" fill="{text_label}">//</text>')
    svg_parts.append(f'<text x="235" y="428" class="mono" font-size="9" font-weight="700" fill="{accent_emerald}">STACK: ACTIVE</text>')

    # ==================== RIGHT PANEL: SYSTEM.INFO WITH BADGE TAGS ====================
    svg_parts.append(f'<rect x="376" y="62" width="486" height="382" rx="10" fill="{card_bg}" stroke="{terminal_border}" stroke-width="1"/>')
    svg_parts.append(f'<rect x="376" y="62" width="486" height="30" rx="10" fill="{pill_bg}"/>')
    svg_parts.append(f'<line x1="376" y1="92" x2="862" y2="92" stroke="{terminal_border}" stroke-width="0.8"/>')
    svg_parts.append(f'<text x="392" y="82" class="mono" font-size="11" font-weight="700" fill="{title_color}">[ SYSTEM.INFO ]</text>')
    svg_parts.append(f'<text x="848" y="82" class="mono" font-size="9.5" font-weight="600" fill="{accent_emerald}" text-anchor="end">STATUS: ACTIVE // 240 FPS</text>')
    
    # Section 1: Profile identity
    rows_meta = [
        ("Subject", "Onkar Bevinakatti", title_color, "700"),
        ("Role", "Full Stack &amp; Blockchain Engineer", text_primary, "500"),
        ("Origin", "India [IST / UTC+5:30]", text_secondary, "500"),
        ("Status", "SHIPPING // Web3 &amp; Full-Stack", accent_emerald, "600"),
        ("ToolChain", "Git · Docker · VS Code · Linux · AWS", text_secondary, "500"),
    ]
    
    label_x = 394
    val_x = 512
    cur_y = 114
    for label, val, color, weight in rows_meta:
        svg_parts.append(f'<text x="{label_x}" y="{cur_y}" class="mono" font-size="10.5" font-weight="600" fill="{text_label}">{label}</text>')
        leader_start = label_x + len(label) * 7.2 + 8
        leader_end = val_x - 10
        if leader_start < leader_end:
            svg_parts.append(f'<line x1="{leader_start:.1f}" y1="{cur_y - 3.5}" x2="{leader_end:.1f}" y2="{cur_y - 3.5}" stroke="{divider_color}" stroke-width="1" stroke-dasharray="2 3"/>')
        svg_parts.append(f'<text x="{val_x}" y="{cur_y}" class="mono" font-size="10.5" font-weight="{weight}" fill="{color}">{val}</text>')
        cur_y += 18
        
    svg_parts.append(f'<line x1="394" y1="{cur_y - 6}" x2="846" y2="{cur_y - 6}" stroke="{divider_color}" stroke-width="1" stroke-dasharray="3 3"/>')
    cur_y += 4
    
    # Section 2: CATEGORIZED TECH STACK WITH COLORFUL BADGE TAGS
    badge_categories = [
        ("Core.Lang", [
            ("TypeScript", "#3178C6", "#FFFFFF", "TS"),
            ("JavaScript", "#F7DF1E", "#000000", "JS"),
            ("Solidity", "#363636", "#FFFFFF", None),
            ("Python", "#3776AB", "#FFFFFF", None),
            ("C++", "#00599C", "#FFFFFF", None),
            ("SQL", "#4479A1", "#FFFFFF", None),
        ]),
        ("Core.Frontend", [
            ("React.js", "#0284C7", "#FFFFFF", None),
            ("Next.js", "#000000", "#FFFFFF", None),
            ("React Native", "#0369A1", "#FFFFFF", None),
            ("Tailwind", "#06B6D4", "#FFFFFF", None),
            ("Redux", "#764ABC", "#FFFFFF", None),
            ("Vite", "#646CFF", "#FFFFFF", None),
        ]),
        ("Core.Backend", [
            ("Node.js", "#339933", "#FFFFFF", None),
            ("Express", "#161B22", "#FFFFFF", "ex"),
            ("FastAPI", "#009688", "#FFFFFF", None),
            ("Ethers.js", "#2535A0", "#FFFFFF", None),
            ("Web3.js", "#F16822", "#FFFFFF", None),
            ("Polygon", "#8247E5", "#FFFFFF", None),
        ]),
        ("Core.Database", [
            ("PostgreSQL", "#4169E1", "#FFFFFF", None),
            ("MongoDB", "#47A248", "#FFFFFF", None),
            ("Redis", "#DC382D", "#FFFFFF", None),
            ("Supabase", "#3ECF8E", "#0D1117", None),
            ("Firebase", "#FFCA28", "#0D1117", None),
        ]),
        ("Core.Infra", [
            ("AWS", "#232F3E", "#FF9900", None),
            ("Docker", "#2496ED", "#FFFFFF", None),
            ("Vercel", "#000000", "#FFFFFF", None),
            ("Actions", "#2088FF", "#FFFFFF", None),
            ("Git", "#F05032", "#FFFFFF", None),
        ]),
    ]
    
    badge_start_x = 480
    for label, badges in badge_categories:
        svg_parts.append(f'<text x="{label_x}" y="{cur_y+11}" class="mono" font-size="10" font-weight="600" fill="{text_label}">{label}</text>')
        bx = badge_start_x
        by = cur_y - 2
        for b_text, b_bg, b_fg, b_logo in badges:
            b_svg, b_width = render_badge_pill(bx, by, b_text, b_bg, b_fg, b_logo)
            svg_parts.append(b_svg)
            bx += b_width + 4
        cur_y += 21.5
        
    svg_parts.append(f'<line x1="394" y1="{cur_y - 4}" x2="846" y2="{cur_y - 4}" stroke="{divider_color}" stroke-width="1" stroke-dasharray="3 3"/>')
    cur_y += 6
    
    # Section 3: Grid Uplinks
    rows_grid = [
        ("Grid.Mail", "onkarbevinakatti09@gmail.com", text_secondary),
        ("Grid.Portfolio", "https://onkarportfolio.onrender.com", title_color),
        ("Grid.LinkedIn", "linkedin.com/in/onkar-bevinakatti-6515b8292", text_primary),
        ("Grid.GitHub", "github.com/prembevinakatti", accent_purple),
    ]
    for label, val, color in rows_grid:
        svg_parts.append(f'<text x="{label_x}" y="{cur_y}" class="mono" font-size="10" font-weight="600" fill="{text_label}">{label}</text>')
        leader_start = label_x + len(label) * 7.2 + 8
        leader_end = val_x - 10
        if leader_start < leader_end:
            svg_parts.append(f'<line x1="{leader_start:.1f}" y1="{cur_y - 3.5}" x2="{leader_end:.1f}" y2="{cur_y - 3.5}" stroke="{divider_color}" stroke-width="1" stroke-dasharray="2 3"/>')
        svg_parts.append(f'<text x="{val_x}" y="{cur_y}" class="mono" font-size="10" font-weight="500" fill="{color}">{val}</text>')
        cur_y += 15.5

    svg_parts.append('</svg>')
    
    svg_content = "\n".join(svg_parts)
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(svg_content)
        
    file_size_kb = os.path.getsize(output_path) / 1024
    print(f"[+] Generated {output_path} ({file_size_kb:.1f} KB)")
    return output_path

if __name__ == "__main__":
    generate_banner_svg(is_dark=True, output_path="assets/dark.svg")
    generate_banner_svg(is_dark=False, output_path="assets/light.svg")
