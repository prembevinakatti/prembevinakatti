#!/usr/bin/env python3
"""
Developer OS - Animated Hero SVG Banner Generator with User Portrait
Features:
- Left Panel: Floyd-Steinberg dithered vector portrait with 60-group shimmer
  plus 850 particle travellers morphing along Ethereum -> React -> TypeScript geometries.
- Right Panel: Pristine SYSTEM.INFO terminal dashboard.
- Dark Obsidian & Light Mode support.
"""

import os
import math
import random
from PIL import Image
import numpy as np

def generate_dithered_portrait_svg_elements(image_path="data/portrait.png", panel_w=344, panel_h=382):
    if not os.path.exists(image_path):
        print(f"[!] {image_path} not found")
        return ""
    
    img = Image.open(image_path).convert("L")
    target_w = 110
    aspect = img.height / img.width
    target_h = int(target_w * aspect)
    img_resized = img.resize((target_w, target_h), Image.Resampling.LANCZOS)
    
    # Floyd-Steinberg dithering
    dithered = img_resized.convert("1", dither=Image.Dither.FLOYDSTEINBERG)
    arr = np.array(dithered)
    
    offset_x = 18 + (panel_w - target_w * 2.7) / 2
    offset_y = 62 + 35 + (panel_h - 40 - target_h * 2.7) / 2
    pixel_size = 2.7
    
    groups = [[] for _ in range(60)]
    for y in range(arr.shape[0]):
        for x in range(arr.shape[1]):
            if not arr[y, x]: # Black/foreground pixel
                px = offset_x + x * pixel_size
                py = offset_y + y * pixel_size
                grp_idx = (x * 7 + y * 13) % 60
                groups[grp_idx].append((px, py))
                
    svg_groups = []
    for i, grp in enumerate(groups):
        if not grp:
            continue
        rects = "".join([f'<rect x="{px:.1f}" y="{py:.1f}" width="{pixel_size-0.2:.1f}" height="{pixel_size-0.2:.1f}" rx="0.4"/>' for px, py in grp])
        svg_groups.append(f'<g class="port-grp-{i}">{rects}</g>')
        
    return "\n".join(svg_groups)

def get_morph_geometries(cx=190, cy=255, n=850):
    """Generate 850 particle trajectories morphing along Ethereum -> React -> TypeScript -> Grid."""
    random.seed(42)
    trajectories = []
    
    # State 1: Ethereum Diamond
    eth_pts = []
    for _ in range(n):
        u = random.random()
        v = random.random()
        if u + v > 1:
            u, v = 1 - u, 1 - v
        if random.random() < 0.65:
            # Top pyramid
            x = cx + (-60 * (1-u-v) + 0 * u + 60 * v) * 0.7
            y = cy - 85 * (1-u-v) + (-10) * u + (-10) * v
        else:
            # Bottom pyramid
            x = cx + (-50 * (1-u-v) + 0 * u + 50 * v) * 0.65
            y = cy + 5 * (1-u-v) + 75 * u + 5 * v
        eth_pts.append((x, y))
        
    # State 2: React Orbital Ellipses
    react_pts = []
    for i in range(n):
        orbit = i % 3
        angle = random.uniform(0, 2 * math.pi)
        a, b = 80, 28
        ex = a * math.cos(angle)
        ey = b * math.sin(angle)
        rot = orbit * (math.pi / 3)
        rx = cx + (ex * math.cos(rot) - ey * math.sin(rot))
        ry = cy + (ex * math.sin(rot) + ey * math.cos(rot))
        react_pts.append((rx, ry))
        
    # State 3: TypeScript TS Cube Box
    ts_pts = []
    for _ in range(n):
        side = random.choice([0, 1, 2, 3])
        t = random.uniform(-65, 65)
        if side == 0:
            tx, ty = cx + t, cy - 65
        elif side == 1:
            tx, ty = cx + 65, cy + t
        elif side == 2:
            tx, ty = cx + t, cy + 65
        else:
            tx, ty = cx - 65, cy + t
        ts_pts.append((tx, ty))
        
    return eth_pts, react_pts, ts_pts

def generate_banner_svg(is_dark=True, output_path="assets/dark.svg"):
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    
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
        dither_fill = "#22D3EE"
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
        dither_fill = "#0284C7"

    dithered_portrait_svg = generate_dithered_portrait_svg_elements("data/portrait.png", 344, 382)
    eth_pts, react_pts, ts_pts = get_morph_geometries(190, 255, 400)
    
    svg = []
    svg.append('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 880 460" width="100%" height="100%">')
    
    # CSS
    shimmer_keyframes = []
    for i in range(60):
        delay = (i * 0.08) % 3.0
        shimmer_keyframes.append(f'.port-grp-{i} {{ animation: portShimmer 3.2s infinite ease-in-out {delay:.2f}s; fill: {dither_fill}; }}')
        
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
        
        @keyframes portShimmer {{
            0%, 100% {{ opacity: 0.85; }}
            50%      {{ opacity: 0.35; }}
        }}
        
        @keyframes pulseLive {{
            0%, 100% {{ opacity: 1; transform: scale(1); }}
            50%      {{ opacity: 0.35; transform: scale(0.85); }}
        }}
        
        {chr(10).join(shimmer_keyframes)}
        .live-dot {{ animation: pulseLive 2s infinite ease-in-out; transform-origin: 820px 24px; }}
        
        @media (prefers-reduced-motion: reduce) {{
            [class^="port-grp-"], .live-dot {{
                animation: none !important;
            }}
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
    
    # Live pill
    svg.append(f'<rect x="660" y="12" width="134" height="24" rx="12" fill="{pill_bg}" stroke="{pill_border}" stroke-width="0.8"/>')
    svg.append(f'<text x="727" y="28" class="mono" font-size="11" font-weight="600" fill="{title_color}" text-anchor="middle">@prembevinakatti</text>')
    svg.append(f'<circle class="live-dot" cx="818" cy="24" r="4.5" fill="{accent_emerald}"/>')
    svg.append(f'<text x="829" y="28" class="mono" font-size="10.5" font-weight="700" fill="{accent_emerald}">LIVE</text>')
    
    # ==================== LEFT PANEL: USER PORTRAIT / VISUAL MAP ====================
    svg.append(f'<rect x="18" y="62" width="344" height="382" rx="10" fill="{card_bg}" stroke="{terminal_border}" stroke-width="1"/>')
    svg.append(f'<rect x="18" y="62" width="344" height="30" rx="10" fill="{pill_bg}"/>')
    svg.append(f'<line x1="18" y1="92" x2="362" y2="92" stroke="{terminal_border}" stroke-width="0.8"/>')
    svg.append(f'<text x="32" y="82" class="mono" font-size="11" font-weight="700" fill="{title_color}">[ VISUAL.IDENTITY ]</text>')
    svg.append(f'<text x="348" y="82" class="mono" font-size="9" fill="{text_label}" text-anchor="end">DITHER.MATRIX // 60 FPS</text>')
    
    # Corner HUD
    svg.append(f'<path d="M 28 108 L 28 100 L 36 100" fill="none" stroke="{title_color}" stroke-width="1" opacity="0.6"/>')
    svg.append(f'<text x="40" y="108" class="mono" font-size="8" fill="{text_label}">Trx: 0xAF7E // ONKAR_OK</text>')
    svg.append(f'<path d="M 352 108 L 352 100 L 344 100" fill="none" stroke="{title_color}" stroke-width="1" opacity="0.6"/>')
    svg.append(f'<text x="340" y="108" class="mono" font-size="8" font-weight="700" fill="{accent_emerald}" text-anchor="end">LIVE_SYNC</text>')
    
    # Glow & Dithered Portrait
    svg.append(f'<circle cx="190" cy="255" r="120" fill="url(#portGlow)"/>')
    svg.append(dithered_portrait_svg)
    
    # Bottom Status Pill on Left
    svg.append(f'<path d="M 28 406 L 28 414 L 36 414" fill="none" stroke="{title_color}" stroke-width="1" opacity="0.6"/>')
    svg.append(f'<path d="M 352 406 L 352 414 L 344 414" fill="none" stroke="{title_color}" stroke-width="1" opacity="0.6"/>')
    svg.append(f'<circle cx="44" cy="425" r="3" fill="{accent_emerald}"/>')
    svg.append(f'<text x="52" y="428" class="mono" font-size="9" font-weight="700" fill="{title_color}">NEURAL VECTOR AVATAR</text>')
    svg.append(f'<text x="210" y="428" class="mono" font-size="9" fill="{text_label}">//</text>')
    svg.append(f'<text x="235" y="428" class="mono" font-size="9" font-weight="700" fill="{accent_emerald}">ENGINE: ACTIVE</text>')

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
