#!/usr/bin/env python3
"""
Developer OS - Animated Dotted Particle Morphing Hero Banner
Features:
- Left Panel: Pure Dotted Particle Morphing Matrix (750 Animated Vector Dots)
  State 1 (0.0s - 2.8s): Onkar's Facial Portrait (High-Definition Dotted Silhouette, Eyes, Smile, Hair)
  State 2 (3.3s - 6.1s): Next.js Dotted Vector Logo (Outer Ring + N Letter)
  State 3 (6.6s - 9.5s): React Dotted Atomic Core (3 Rotating Ellipses + Central Nucleus)
  Loop (9.5s - 10.0s): Smooth Spline Return to Portrait
- Right Panel: Pristine SYSTEM.INFO Terminal Dashboard.
"""

import os
import math
import random
from PIL import Image, ImageFilter, ImageOps
import numpy as np

def extract_portrait_dots(image_path="data/portrait.png", cx=190, cy=246, n_points=720):
    img = Image.open(image_path).convert("L")
    img = ImageOps.autocontrast(img)
    
    target_w, target_h = 100, int(100 * img.height / img.width)
    img_res = img.resize((target_w, target_h), Image.Resampling.LANCZOS)
    
    edges = img_res.filter(ImageFilter.FIND_EDGES)
    arr_edges = np.array(edges).astype(float)
    arr_tones = np.array(img_res).astype(float)
    
    # Combined probability: Edge features (70%) + Tone features (30%)
    # Invert tones so dark features (eyes, hair, lines, smile) have high intensity
    inv_tones = 255.0 - arr_tones
    inv_tones[arr_tones < 20] = 0 # filter out pure background
    
    weights = (arr_edges * 0.75) + (inv_tones * 0.35)
    weights[weights < 25] = 0 # threshold out noise
    
    total = np.sum(weights)
    if total == 0:
        probs = np.ones(weights.size) / weights.size
    else:
        probs = (weights / total).flatten()
        
    np.random.seed(42)
    indices = np.random.choice(weights.size, size=n_points, p=probs, replace=True)
    
    scale = 1.95
    off_x = cx - (target_w * scale) / 2
    off_y = cy - (target_h * scale) / 2 - 4
    
    pts = []
    for idx in indices:
        y, x = divmod(idx, target_w)
        px = off_x + x * scale + random.uniform(-0.5, 0.5)
        py = off_y + y * scale + random.uniform(-0.5, 0.5)
        pts.append((round(px, 1), round(py, 1)))
        
    return pts

def generate_nextjs_dots(cx=190, cy=246, n_points=720):
    pts = []
    r_outer = 74
    
    # 1. Outer Circle (36% of dots)
    n_circle = int(n_points * 0.36)
    for i in range(n_circle):
        th = 2 * math.pi * (i / n_circle)
        x = cx + r_outer * math.cos(th)
        y = cy + r_outer * math.sin(th)
        pts.append((round(x, 1), round(y, 1)))
        
    # 2. Left Vertical Stem of N (18% of dots)
    n_left = int(n_points * 0.18)
    for i in range(n_left):
        t = i / n_left
        x = cx - 32 + random.uniform(-1.2, 1.2)
        y = cy - 46 + t * 92
        pts.append((round(x, 1), round(y, 1)))
        
    # 3. Diagonal Stroke of N (32% of dots)
    n_diag = int(n_points * 0.32)
    for i in range(n_diag):
        t = i / n_diag
        x = cx - 32 + t * 64 + random.uniform(-1.2, 1.2)
        y = cy - 46 + t * 92 + random.uniform(-0.8, 0.8)
        pts.append((round(x, 1), round(y, 1)))
        
    # 4. Right Vertical Stem of N (remainder)
    n_right = n_points - len(pts)
    for i in range(n_right):
        t = i / n_right
        x = cx + 32 + random.uniform(-1.2, 1.2)
        y = cy - 46 + t * 56
        pts.append((round(x, 1), round(y, 1)))
        
    return pts

def generate_react_dots(cx=190, cy=246, n_points=720):
    pts = []
    
    # 1. Nucleus Center (14% of dots)
    n_core = int(n_points * 0.14)
    for _ in range(n_core):
        r = random.uniform(0, 13)
        th = random.uniform(0, 2 * math.pi)
        pts.append((round(cx + r * math.cos(th), 1), round(cy + r * math.sin(th), 1)))
        
    # 2. Three Orbital Ellipses (86% of dots)
    rem = n_points - len(pts)
    pts_per_orbit = rem // 3
    a, b = 84, 28
    
    for orbit in range(3):
        rot = orbit * (math.pi / 3) # 0 deg, 60 deg, 120 deg
        count = pts_per_orbit if orbit < 2 else (n_points - len(pts))
        for i in range(count):
            th = 2 * math.pi * (i / count)
            ex = a * math.cos(th) + random.uniform(-1.0, 1.0)
            ey = b * math.sin(th) + random.uniform(-0.8, 0.8)
            rx = cx + (ex * math.cos(rot) - ey * math.sin(rot))
            ry = cy + (ex * math.sin(rot) + ey * math.cos(rot))
            pts.append((round(rx, 1), round(ry, 1)))
            
    return pts

def generate_banner_svg(is_dark=True, output_path="assets/dark.svg"):
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    
    cx = 190
    cy = 246
    n_points = 720
    
    # Generate the 3 Dotted Morphing States
    pts_portrait = extract_portrait_dots("data/portrait.png", cx, cy, n_points)
    pts_nextjs = generate_nextjs_dots(cx, cy, n_points)
    pts_react = generate_react_dots(cx, cy, n_points)
    
    # Palette
    if is_dark:
        bg_color = "#08090D"
        card_bg = "#0F1117"
        terminal_border = "#21262D"
        grid_line = "#161B22"
        header_bg = "#0B0D13"
        title_color = "#22D3EE"
        accent_emerald = "#10B981"
        accent_purple = "#A78BFA"
        text_primary = "#F0F6FC"
        text_secondary = "#8B949E"
        text_label = "#6E7681"
        pill_bg = "#161B22"
        pill_border = "#30363D"
        divider_color = "#21262D"
        dot_primary = "#22D3EE"
        dot_highlight = "#38BDF8"
        dot_accent = "#10B981"
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
        dot_primary = "#0284C7"
        dot_highlight = "#0EA5E9"
        dot_accent = "#059669"

    svg = []
    svg.append('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 880 460" width="100%" height="100%">')
    
    svg.append(f"""
    <defs>
        <pattern id="gridPat" width="20" height="20" patternUnits="userSpaceOnUse">
            <path d="M 20 0 L 0 0 0 20" fill="none" stroke="{grid_line}" stroke-width="0.6" stroke-opacity="0.4"/>
        </pattern>
        <radialGradient id="portGlow" cx="50%" cy="50%" r="50%">
            <stop offset="0%" stop-color="{title_color}" stop-opacity="0.2"/>
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
        
        @keyframes pulseLive {{
            0%, 100% {{ opacity: 1; transform: scale(1); }}
            50%      {{ opacity: 0.35; transform: scale(0.85); }}
        }}
        
        @keyframes labelPortrait {{
            0%, 28%   {{ opacity: 1; }}
            33%, 95%  {{ opacity: 0; }}
            100%      {{ opacity: 1; }}
        }}
        @keyframes labelNextjs {{
            0%, 28%   {{ opacity: 0; }}
            33%, 61%  {{ opacity: 1; }}
            66%, 100% {{ opacity: 0; }}
        }}
        @keyframes labelReact {{
            0%, 61%   {{ opacity: 0; }}
            66%, 95%  {{ opacity: 1; }}
            100%      {{ opacity: 0; }}
        }}
        
        .lbl-port {{ animation: labelPortrait 10s infinite ease-in-out; }}
        .lbl-next {{ animation: labelNextjs 10s infinite ease-in-out; }}
        .lbl-react {{ animation: labelReact 10s infinite ease-in-out; }}
        .live-dot {{ animation: pulseLive 2s infinite ease-in-out; transform-origin: 820px 24px; }}
        
        @media (prefers-reduced-motion: reduce) {{
            animate {{ display: none !important; }}
            .lbl-port, .lbl-next, .lbl-react, .live-dot {{ animation: none !important; }}
        }}
    ]]></style>
    """)
    
    # Outer Chassis
    svg.append(f'<rect width="880" height="460" rx="14" fill="{bg_color}" stroke="{terminal_border}" stroke-width="1.2"/>')
    svg.append(f'<rect x="1" y="1" width="878" height="458" rx="13" fill="url(#gridPat)"/>')
    
    # Header Bar
    svg.append(f'<rect x="0" y="0" width="880" height="48" rx="14" fill="{header_bg}" stroke="{terminal_border}" stroke-width="1"/>')
    svg.append(f'<line x1="0" y1="48" x2="880" y2="48" stroke="{terminal_border}" stroke-width="1"/>')
    svg.append('<circle cx="26" cy="24" r="5.5" fill="#FF5F56"/>')
    svg.append('<circle cx="44" cy="24" r="5.5" fill="#FFBD2E"/>')
    svg.append('<circle cx="62" cy="24" r="5.5" fill="#27C93F"/>')
    svg.append(f'<text x="88" y="29" class="mono" font-size="12" font-weight="600" fill="{text_secondary}">term://onkar.os/profile.sh <tspan fill="{title_color}">--live</tspan></text>')
    
    # Live Pill
    svg.append(f'<rect x="660" y="12" width="134" height="24" rx="12" fill="{pill_bg}" stroke="{pill_border}" stroke-width="0.8"/>')
    svg.append(f'<text x="727" y="28" class="mono" font-size="11" font-weight="600" fill="{title_color}" text-anchor="middle">@prembevinakatti</text>')
    svg.append(f'<circle class="live-dot" cx="818" cy="24" r="4.5" fill="{accent_emerald}"/>')
    svg.append(f'<text x="829" y="28" class="mono" font-size="10.5" font-weight="700" fill="{accent_emerald}">LIVE</text>')
    
    # ==================== LEFT PANEL: 100% DOTTED PARTICLE MATRIX ====================
    svg.append(f'<rect x="18" y="62" width="344" height="382" rx="10" fill="{card_bg}" stroke="{terminal_border}" stroke-width="1"/>')
    svg.append(f'<rect x="18" y="62" width="344" height="30" rx="10" fill="{pill_bg}"/>')
    svg.append(f'<line x1="18" y1="92" x2="362" y2="92" stroke="{terminal_border}" stroke-width="0.8"/>')
    svg.append(f'<text x="32" y="82" class="mono" font-size="11" font-weight="700" fill="{title_color}">[ VISUAL.IDENTITY ]</text>')
    svg.append(f'<text x="348" y="82" class="mono" font-size="9" fill="{text_label}" text-anchor="end">DOT.MATRIX // 60 FPS</text>')
    
    # Corner HUD
    svg.append(f'<path d="M 28 108 L 28 100 L 36 100" fill="none" stroke="{title_color}" stroke-width="1" opacity="0.6"/>')
    svg.append(f'<text x="40" y="108" class="mono" font-size="8" fill="{text_label}">Trx: 0xAF7E // ONKAR_OK</text>')
    svg.append(f'<path d="M 352 108 L 352 100 L 344 100" fill="none" stroke="{title_color}" stroke-width="1" opacity="0.6"/>')
    svg.append(f'<text x="340" y="108" class="mono" font-size="8" font-weight="700" fill="{accent_emerald}" text-anchor="end">LIVE_SYNC</text>')
    
    # Radial Background Glow
    svg.append(f'<circle cx="{cx}" cy="{cy}" r="125" fill="url(#portGlow)"/>')
    
    # Render 720 Morphing Particle Dots
    dur = "10s"
    key_times = "0; 0.28; 0.33; 0.61; 0.66; 0.95; 1"
    splines = "0.4 0 0.2 1; 0.4 0 0.2 1; 0.4 0 0.2 1; 0.4 0 0.2 1; 0.4 0 0.2 1; 0.4 0 0.2 1"
    
    svg.append('<g id="dotted-particle-matrix">')
    for i in range(n_points):
        p_port = pts_portrait[i]
        p_next = pts_nextjs[i]
        p_react = pts_react[i]
        
        # Color distribution
        if i % 7 == 0:
            c = dot_accent
            r = 1.7
        elif i % 5 == 0:
            c = dot_highlight
            r = 1.7
        else:
            c = dot_primary
            r = 1.5
            
        vx = f"{p_port[0]}; {p_port[0]}; {p_next[0]}; {p_next[0]}; {p_react[0]}; {p_react[0]}; {p_port[0]}"
        vy = f"{p_port[1]}; {p_port[1]}; {p_next[1]}; {p_next[1]}; {p_react[1]}; {p_react[1]}; {p_port[1]}"
        
        svg.append(f'<circle cx="{p_port[0]}" cy="{p_port[1]}" r="{r}" fill="{c}" opacity="0.92">')
        svg.append(f'  <animate attributeName="cx" dur="{dur}" repeatCount="indefinite" values="{vx}" keyTimes="{key_times}" calcMode="spline" keySplines="{splines}"/>')
        svg.append(f'  <animate attributeName="cy" dur="{dur}" repeatCount="indefinite" values="{vy}" keyTimes="{key_times}" calcMode="spline" keySplines="{splines}"/>')
        svg.append('</circle>')
        
    svg.append('</g>')
    
    # Dynamic State Text Indicator
    svg.append(f'<path d="M 28 416 L 28 424 L 36 424" fill="none" stroke="{title_color}" stroke-width="1" opacity="0.6"/>')
    svg.append(f'<path d="M 352 416 L 352 424 L 344 424" fill="none" stroke="{title_color}" stroke-width="1" opacity="0.6"/>')
    svg.append(f'<circle cx="44" cy="432" r="3" fill="{accent_emerald}"/>')
    
    # Alternating State Labels
    svg.append(f'<text x="52" y="435" class="mono lbl-port" font-size="9" font-weight="700" fill="{title_color}">IDENTITY // ONKAR BEVINAKATTI</text>')
    svg.append(f'<text x="52" y="435" class="mono lbl-next" font-size="9" font-weight="700" fill="{title_color}">RUNTIME // NEXT.JS CORE</text>')
    svg.append(f'<text x="52" y="435" class="mono lbl-react" font-size="9" font-weight="700" fill="{title_color}">FRONTEND // REACT ATOM</text>')
    
    svg.append(f'<text x="270" y="435" class="mono" font-size="9" fill="{text_label}">//</text>')
    svg.append(f'<text x="290" y="435" class="mono" font-size="9" font-weight="700" fill="{accent_emerald}">ACTIVE</text>')

    # ==================== RIGHT PANEL: SYSTEM.INFO ====================
    svg.append(f'<rect x="376" y="62" width="486" height="382" rx="10" fill="{card_bg}" stroke="{terminal_border}" stroke-width="1"/>')
    svg.append(f'<rect x="376" y="62" width="486" height="30" rx="10" fill="{pill_bg}"/>')
    svg.append(f'<line x1="376" y1="92" x2="862" y2="92" stroke="{terminal_border}" stroke-width="0.8"/>')
    svg.append(f'<text x="392" y="82" class="mono" font-size="11" font-weight="700" fill="{title_color}">[ SYSTEM.INFO ]</text>')
    svg.append(f'<text x="848" y="82" class="mono" font-size="9.5" font-weight="600" fill="{accent_emerald}" text-anchor="end">STATUS: ACTIVE // 240 FPS</text>')
    
    rows = [
        ("Subject", "Onkar Bevinakatti", title_color, "700", False),
        ("Role", "Full Stack &amp; Blockchain Engineer", text_primary, "500", False),
        ("Origin", "India [IST / UTC+5:30]", text_secondary, "500", False),
        ("Status", "SHIPPING // Web3 &amp; Full-Stack", accent_emerald, "600", False),
        ("ToolChain", "Git · Docker · VS Code · Linux · AWS", text_secondary, "500", True),
        
        ("Core.Lang", "TypeScript · Solidity · Python · C++ · SQL", text_primary, "500", False),
        ("Core.Frontend", "React · Next.js · React Native · Tailwind · Redux", title_color, "500", False),
        ("Core.Backend", "Node.js · Express · Ethers.js · REST APIs", text_primary, "500", False),
        ("Core.Database", "PostgreSQL · MongoDB · Redis · Supabase", accent_emerald, "500", False),
        ("Core.Infra", "AWS · Docker · Vercel · Render · GitHub Actions", text_secondary, "500", True),
        
        ("Grid.Mail", "onkarbevinakatti09@gmail.com", text_secondary, "500", False),
        ("Grid.Portfolio", "https://onkarportfolio.onrender.com", title_color, "500", False),
        ("Grid.LinkedIn", "linkedin.com/in/onkar-bevinakatti-6515b8292", text_primary, "500", False),
        ("Grid.GitHub", "github.com/prembevinakatti", accent_purple, "500", False),
    ]
    
    label_x = 394
    val_x = 512
    cur_y = 114
    
    for label, val, color, weight, has_div in rows:
        svg.append(f'<text x="{label_x}" y="{cur_y}" class="mono" font-size="11" font-weight="600" fill="{text_label}">{label}</text>')
        leader_start = label_x + len(label) * 7.2 + 8
        leader_end = val_x - 10
        if leader_start < leader_end:
            svg.append(f'<line x1="{leader_start:.1f}" y1="{cur_y - 3.5}" x2="{leader_end:.1f}" y2="{cur_y - 3.5}" stroke="{divider_color}" stroke-width="1" stroke-dasharray="2 3"/>')
        svg.append(f'<text x="{val_x}" y="{cur_y}" class="mono" font-size="11" font-weight="{weight}" fill="{color}">{val}</text>')
        
        cur_y += 19.5
        if has_div:
            svg.append(f'<line x1="394" y1="{cur_y - 7}" x2="846" y2="{cur_y - 7}" stroke="{divider_color}" stroke-width="1" stroke-dasharray="3 3"/>')
            cur_y += 6

    svg.append('</svg>')
    
    svg_content = "\n".join(svg)
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(svg_content)
        
    print(f"[+] Generated {output_path} ({len(svg_content)/1024:.1f} KB)")
    return output_path

if __name__ == "__main__":
    generate_banner_svg(is_dark=True, output_path="assets/dark.svg")
    generate_banner_svg(is_dark=False, output_path="assets/light.svg")
