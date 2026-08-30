#!/usr/bin/env python3
"""
Generate Animated Morphing SVG Banner
Particles morph seamlessly between:
1. Onkar's Portrait (Dotted Facial Silhouette)
2. Next.js Dotted Logo ('N' inside circle)
3. React Dotted Atom (3 Orbital Ellipses + Nucleus)
4. Ethereum Dotted Diamond
"""

import os
import math
import random
from PIL import Image
import numpy as np

def extract_portrait_points(image_path="data/portrait.png", cx=190, cy=245, n_points=550):
    """Extracts high-contrast subject points from portrait image without background."""
    img = Image.open(image_path).convert("L")
    w, h = 100, int(100 * img.height / img.width)
    img_resized = img.resize((w, h), Image.Resampling.LANCZOS)
    arr = np.array(img_resized)
    
    # Invert so dark pixels (hair, face features, body) have high values
    inverted = 255 - arr
    
    # Threshold out background
    inverted[inverted < 45] = 0
    
    # Probability distribution based on inverted luminance
    total = np.sum(inverted)
    if total == 0:
        probs = np.ones(inverted.size) / inverted.size
    else:
        probs = (inverted / total).flatten()
        
    indices = np.random.choice(inverted.size, size=n_points, p=probs, replace=True)
    
    scale_x = 2.4
    scale_y = 2.4
    offset_x = cx - (w * scale_x) / 2
    offset_y = cy - (h * scale_y) / 2
    
    portrait_pts = []
    for idx in indices:
        y, x = divmod(idx, w)
        px = offset_x + x * scale_x + random.uniform(-0.8, 0.8)
        py = offset_y + y * scale_y + random.uniform(-0.8, 0.8)
        portrait_pts.append((round(px, 1), round(py, 1)))
        
    return portrait_pts

def generate_nextjs_points(cx=190, cy=245, n_points=550):
    """Generates dotted Next.js logo: circle + N."""
    pts = []
    r_outer = 68
    
    # Outer circle (35% of points)
    n_circle = int(n_points * 0.38)
    for i in range(n_circle):
        angle = 2 * math.pi * (i / n_circle)
        x = cx + r_outer * math.cos(angle)
        y = cy + r_outer * math.sin(angle)
        pts.append((round(x, 1), round(y, 1)))
        
    # Left vertical stem of N (20%)
    n_left = int(n_points * 0.18)
    for i in range(n_left):
        t = i / n_left
        x = cx - 28
        y = cy - 42 + t * 84
        pts.append((round(x, 1), round(y, 1)))
        
    # Diagonal stem of N (30%)
    n_diag = int(n_points * 0.28)
    for i in range(n_diag):
        t = i / n_diag
        x = cx - 28 + t * 56
        y = cy - 42 + t * 84
        pts.append((round(x, 1), round(y, 1)))
        
    # Right vertical stem of N (remainder)
    n_right = n_points - len(pts)
    for i in range(n_right):
        t = i / n_right
        x = cx + 28
        y = cy - 42 + t * 50
        pts.append((round(x, 1), round(y, 1)))
        
    return pts

def generate_react_points(cx=190, cy=245, n_points=550):
    """Generates dotted React atom logo: 3 orbital ellipses + central nucleus."""
    pts = []
    # Nucleus (15%)
    n_core = int(n_points * 0.15)
    for _ in range(n_core):
        r = random.uniform(0, 11)
        th = random.uniform(0, 2 * math.pi)
        pts.append((round(cx + r * math.cos(th), 1), round(cy + r * math.sin(th), 1)))
        
    # 3 Orbital ellipses
    remaining = n_points - len(pts)
    pts_per_orbit = remaining // 3
    a, b = 76, 26
    
    for orbit in range(3):
        rot = orbit * (math.pi / 3)
        count = pts_per_orbit if orbit < 2 else (n_points - len(pts))
        for i in range(count):
            th = 2 * math.pi * (i / count)
            ex = a * math.cos(th)
            ey = b * math.sin(th)
            rx = cx + (ex * math.cos(rot) - ey * math.sin(rot))
            ry = cy + (ex * math.sin(rot) + ey * math.cos(rot))
            pts.append((round(rx, 1), round(ry, 1)))
            
    return pts

def generate_ethereum_points(cx=190, cy=245, n_points=550):
    """Generates dotted Ethereum diamond logo."""
    pts = []
    for _ in range(n_points):
        u, v = random.random(), random.random()
        if u + v > 1:
            u, v = 1 - u, 1 - v
        if random.random() < 0.62:
            # Top pyramid
            x = cx + (-55 * (1-u-v) + 0 * u + 55 * v) * 0.8
            y = cy - 80 * (1-u-v) + (-10) * u + (-10) * v
        else:
            # Bottom pyramid
            x = cx + (-48 * (1-u-v) + 0 * u + 48 * v) * 0.75
            y = cy + 5 * (1-u-v) + 72 * u + 5 * v
        pts.append((round(x, 1), round(y, 1)))
    return pts

def generate_animated_banner(is_dark=True, output_path="assets/dark.svg"):
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    
    cx = 190
    cy = 245
    n_points = 520
    
    # 4 Morphing States
    pts_portrait = extract_portrait_points("data/portrait.png", cx, cy, n_points)
    pts_nextjs = generate_nextjs_points(cx, cy, n_points)
    pts_react = generate_react_points(cx, cy, n_points)
    pts_eth = generate_ethereum_points(cx, cy, n_points)
    
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
        particle_color = "#22D3EE"
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
        particle_color = "#0284C7"

    svg = []
    svg.append('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 880 460" width="100%" height="100%">')
    
    svg.append(f"""
    <defs>
        <pattern id="gridPat" width="20" height="20" patternUnits="userSpaceOnUse">
            <path d="M 20 0 L 0 0 0 20" fill="none" stroke="{grid_line}" stroke-width="0.6" stroke-opacity="0.4"/>
        </pattern>
        <radialGradient id="portGlow" cx="50%" cy="50%" r="50%">
            <stop offset="0%" stop-color="{title_color}" stop-opacity="0.18"/>
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
        .live-dot {{ animation: pulseLive 2s infinite ease-in-out; transform-origin: 820px 24px; }}
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
    
    # ==================== LEFT PANEL: NEURAL MORPHING MATRIX ====================
    svg.append(f'<rect x="18" y="62" width="344" height="382" rx="10" fill="{card_bg}" stroke="{terminal_border}" stroke-width="1"/>')
    svg.append(f'<rect x="18" y="62" width="344" height="30" rx="10" fill="{pill_bg}"/>')
    svg.append(f'<line x1="18" y1="92" x2="362" y2="92" stroke="{terminal_border}" stroke-width="0.8"/>')
    svg.append(f'<text x="32" y="82" class="mono" font-size="11" font-weight="700" fill="{title_color}">[ VISUAL.IDENTITY ]</text>')
    svg.append(f'<text x="348" y="82" class="mono" font-size="9" fill="{text_label}" text-anchor="end">MORPH.MATRIX // 60 FPS</text>')
    
    # Corner HUD
    svg.append(f'<path d="M 28 108 L 28 100 L 36 100" fill="none" stroke="{title_color}" stroke-width="1" opacity="0.6"/>')
    svg.append(f'<text x="40" y="108" class="mono" font-size="8" fill="{text_label}">Trx: 0xAF7E // ONKAR_OK</text>')
    svg.append(f'<path d="M 352 108 L 352 100 L 344 100" fill="none" stroke="{title_color}" stroke-width="1" opacity="0.6"/>')
    svg.append(f'<text x="340" y="108" class="mono" font-size="8" font-weight="700" fill="{accent_emerald}" text-anchor="end">LIVE_SYNC</text>')
    
    # Radial Background Glow & Concentric Rings
    svg.append(f'<circle cx="{cx}" cy="{cy}" r="125" fill="url(#portGlow)"/>')
    svg.append(f'<circle cx="{cx}" cy="{cy}" r="110" fill="none" stroke="{terminal_border}" stroke-width="0.8" opacity="0.4"/>')
    svg.append(f'<circle cx="{cx}" cy="{cy}" r="75" fill="none" stroke="{title_color}" stroke-width="0.8" stroke-dasharray="4 6" opacity="0.3"/>')
    
    # 520 Animated Morphing Particles
    # Timeline (14 seconds):
    # 0s - 3s: Portrait
    # 3.5s - 6.5s: Next.js
    # 7s - 10s: React
    # 10.5s - 13.5s: Ethereum
    # 14s: loop back to Portrait
    dur = "14s"
    splines = "0.4 0 0.2 1; 0.4 0 0.2 1; 0.4 0 0.2 1; 0.4 0 0.2 1; 0.4 0 0.2 1; 0.4 0 0.2 1; 0.4 0 0.2 1; 0.4 0 0.2 1"
    key_times = "0; 0.20; 0.25; 0.45; 0.50; 0.70; 0.75; 0.95; 1"
    
    svg.append('<g id="particle-cloud">')
    for i in range(n_points):
        p1 = pts_portrait[i]
        p2 = pts_nextjs[i]
        p3 = pts_react[i]
        p4 = pts_eth[i]
        
        # Color variation
        if i % 6 == 0:
            c = accent_emerald
            r = 1.8
        elif i % 7 == 0:
            c = accent_purple
            r = 1.8
        else:
            c = particle_color
            r = 1.5
            
        val_x = f"{p1[0]}; {p1[0]}; {p2[0]}; {p2[0]}; {p3[0]}; {p3[0]}; {p4[0]}; {p4[0]}; {p1[0]}"
        val_y = f"{p1[1]}; {p1[1]}; {p2[1]}; {p2[1]}; {p3[1]}; {p3[1]}; {p4[1]}; {p4[1]}; {p1[1]}"
        
        svg.append(f'<circle cx="{p1[0]}" cy="{p1[1]}" r="{r}" fill="{c}" opacity="0.9">')
        svg.append(f'  <animate attributeName="cx" dur="{dur}" repeatCount="indefinite" values="{val_x}" keyTimes="{key_times}" calcMode="spline" keySplines="{splines}"/>')
        svg.append(f'  <animate attributeName="cy" dur="{dur}" repeatCount="indefinite" values="{val_y}" keyTimes="{key_times}" calcMode="spline" keySplines="{splines}"/>')
        svg.append('</circle>')
        
    svg.append('</g>')
    
    # State Indicator Label (Dynamic label showing current morph state)
    svg.append(f'<path d="M 28 406 L 28 414 L 36 414" fill="none" stroke="{title_color}" stroke-width="1" opacity="0.6"/>')
    svg.append(f'<path d="M 352 406 L 352 414 L 344 414" fill="none" stroke="{title_color}" stroke-width="1" opacity="0.6"/>')
    svg.append(f'<circle cx="44" cy="425" r="3" fill="{accent_emerald}"/>')
    svg.append(f'<text x="52" y="428" class="mono" font-size="9" font-weight="700" fill="{title_color}">AVATAR ➔ NEXT.JS ➔ REACT ➔ ETH</text>')
    svg.append(f'<text x="290" y="428" class="mono" font-size="9" fill="{text_label}">//</text>')
    svg.append(f'<text x="306" y="428" class="mono" font-size="9" font-weight="700" fill="{accent_emerald}">LIVE</text>')

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
    generate_animated_banner(is_dark=True, output_path="assets/dark.svg")
    generate_animated_banner(is_dark=False, output_path="assets/light.svg")
