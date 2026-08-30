#!/usr/bin/env python3
"""
Developer OS - Animated Hero SVG Banner Generator (Refined Dark Obsidian Edition)
Features:
- True Dark Obsidian palette (eliminating heavy blue wash)
- Serpentine Floyd-Steinberg 1-bit dithering with user portrait
- Travellers particle morphing (ETH ➔ React ➔ TypeScript)
- Razor-sharp, naturally proportioned typography (no glyph-stretching distortion)
- Precision terminal grid hierarchy
"""

import os
import math
import random
import numpy as np
from PIL import Image, ImageOps, ImageEnhance

def prepare_portrait(raw_path="data/portrait_raw.png", target_path="data/portrait.png"):
    """Crops and tone-maps the user portrait for optimal dithering."""
    if not os.path.exists(raw_path):
        return
    
    img = Image.open(raw_path)
    w, h = img.size
    # Crop head and shoulders
    crop_box = (0, 10, w, 620)
    cropped = img.crop(crop_box)
    
    if cropped.mode == 'RGBA':
        r, g, b, a = cropped.split()
        rgb = Image.merge('RGB', (r, g, b))
        gray = ImageOps.grayscale(rgb)
        alpha = np.array(a) / 255.0
    else:
        gray = ImageOps.grayscale(cropped)
        alpha = np.ones(gray.size[::-1])
        
    gray_resized = gray.resize((300, 340), Image.Resampling.LANCZOS)
    alpha_resized = Image.fromarray((alpha * 255).astype(np.uint8)).resize((300, 340), Image.Resampling.LANCZOS)
    
    g_arr = np.array(gray_resized, dtype=np.float32)
    a_arr = np.array(alpha_resized, dtype=np.float32) / 255.0
    
    boosted = g_arr.copy()
    mask = a_arr > 0.2
    # Tone curve: preserve facial clarity and lift darks for visible dithering
    boosted[mask] = np.clip((boosted[mask] / 255.0) ** 0.85 * 255.0 + 35.0, 0, 255)
    boosted[~mask] = 0.0
    
    result_img = Image.fromarray(boosted.astype(np.uint8))
    result_img.save(target_path)
    print(f"[+] Prepared user portrait at {target_path}")

def dither_floyd_steinberg_serpentine(image_path="data/portrait.png", target_w=300, target_h=340, step=2):
    """Serpentine Floyd-Steinberg dithering with anti-grid noise."""
    if not os.path.exists(image_path):
        prepare_portrait()
        
    img = Image.open(image_path).convert("L")
    img = img.resize((target_w // step, target_h // step), Image.Resampling.LANCZOS)
    
    arr = np.array(img, dtype=np.float32)
    arr = arr / 255.0
    arr = np.clip((arr - 0.45) * 1.35 + 0.45, 0.0, 1.0) * 255.0
    
    h, w = arr.shape
    dithered = arr.copy()
    
    for y in range(h):
        is_l2r = (y % 2 == 0)
        x_range = range(w) if is_l2r else range(w - 1, -1, -1)
        for x in x_range:
            old_val = dithered[y, x]
            new_val = 255.0 if old_val > 128.0 else 0.0
            dithered[y, x] = new_val
            error = old_val - new_val
            
            if is_l2r:
                if x + 1 < w:
                    dithered[y, x + 1] += error * (7.0 / 16.0)
                if y + 1 < h:
                    if x - 1 >= 0:
                        dithered[y + 1, x - 1] += error * (3.0 / 16.0)
                    dithered[y + 1, x] += error * (5.0 / 16.0)
                    if x + 1 < w:
                        dithered[y + 1, x + 1] += error * (1.0 / 16.0)
            else:
                if x - 1 >= 0:
                    dithered[y, x - 1] += error * (7.0 / 16.0)
                if y + 1 < h:
                    if x + 1 < w:
                        dithered[y + 1, x + 1] += error * (3.0 / 16.0)
                    dithered[y + 1, x] += error * (5.0 / 16.0)
                    if x - 1 >= 0:
                        dithered[y + 1, x - 1] += error * (1.0 / 16.0)

    points = []
    rng = random.Random(42)
    for y in range(h):
        for x in range(w):
            if dithered[y, x] > 128:
                real_x = x * step + 1 + (rng.uniform(-0.35, 0.35))
                real_y = y * step + 1 + (rng.uniform(-0.35, 0.35))
                noise_score = (math.sin(x * 0.45) * math.cos(y * 0.35) + rng.uniform(0, 1.0))
                points.append((round(real_x, 2), round(real_y, 2), noise_score))
                
    return points

def sample_logo_1_ethereum(n_points=850, cx=190, cy=245, radius=90):
    pts = []
    rng = random.Random(101)
    top = (cx, cy - radius)
    mid_l = (cx - radius * 0.72, cy)
    mid_r = (cx + radius * 0.72, cy)
    center_front = (cx, cy + radius * 0.15)
    bottom = (cx, cy + radius * 0.95)
    
    segments = [
        (top, mid_l, 130),
        (top, mid_r, 130),
        (top, center_front, 150),
        (mid_l, center_front, 95),
        (mid_r, center_front, 95),
        (center_front, bottom, 120),
        (mid_l, bottom, 105),
        (mid_r, bottom, 105)
    ]
    for (p1, p2, count) in segments:
        for _ in range(count):
            t = rng.random()
            pts.append((round(p1[0] + (p2[0] - p1[0]) * t + rng.uniform(-0.8, 0.8), 2),
                        round(p1[1] + (p2[1] - p1[1]) * t + rng.uniform(-0.8, 0.8), 2)))
    while len(pts) < n_points:
        p = rng.choice(pts)
        pts.append((round(p[0] + rng.uniform(-1, 1), 2), round(p[1] + rng.uniform(-1, 1), 2)))
    return pts[:n_points]

def sample_logo_2_react(n_points=850, cx=190, cy=245, rx=85, ry=32):
    pts = []
    rng = random.Random(202)
    nucleus_count = 140
    for _ in range(nucleus_count):
        r = rng.uniform(0, 16)
        ang = rng.uniform(0, 2 * math.pi)
        pts.append((round(cx + r * math.cos(ang), 2), round(cy + r * math.sin(ang), 2)))
    orbit_pts_each = (n_points - nucleus_count) // 3
    for rot in [0, math.pi / 3, 2 * math.pi / 3]:
        for _ in range(orbit_pts_each):
            theta = rng.uniform(0, 2 * math.pi)
            ex = rx * math.cos(theta)
            ey = ry * math.sin(theta)
            rot_x = ex * math.cos(rot) - ey * math.sin(rot)
            rot_y = ex * math.sin(rot) + ey * math.cos(rot)
            pts.append((round(cx + rot_x + rng.uniform(-0.8, 0.8), 2), round(cy + rot_y + rng.uniform(-0.8, 0.8), 2)))
    while len(pts) < n_points:
        p = rng.choice(pts)
        pts.append((round(p[0] + rng.uniform(-1, 1), 2), round(p[1] + rng.uniform(-1, 1), 2)))
    return pts[:n_points]

def sample_logo_3_typescript(n_points=850, cx=190, cy=245, size=130):
    pts = []
    rng = random.Random(303)
    hex_pts = []
    for i in range(6):
        angle = math.pi / 6 + i * (math.pi / 3)
        hex_pts.append((cx + size * 0.68 * math.cos(angle), cy + size * 0.68 * math.sin(angle)))
    hex_count = 390
    per_edge = hex_count // 6
    for i in range(6):
        p1 = hex_pts[i]
        p2 = hex_pts[(i + 1) % 6]
        for _ in range(per_edge):
            t = rng.random()
            pts.append((round(p1[0] + (p2[0] - p1[0]) * t + rng.uniform(-0.8, 0.8), 2),
                        round(p1[1] + (p2[1] - p1[1]) * t + rng.uniform(-0.8, 0.8), 2)))
    # T monogram
    for _ in range(110):
        t = rng.random()
        pts.append((round((cx - 42) + 32 * t + rng.uniform(-0.6, 0.6), 2), round(cy - 32 + rng.uniform(-0.6, 0.6), 2)))
    for _ in range(130):
        t = rng.random()
        pts.append((round(cx - 26 + rng.uniform(-0.6, 0.6), 2), round((cy - 32) + 68 * t + rng.uniform(-0.6, 0.6), 2)))
    # S monogram
    for _ in range(210):
        t = rng.random() * 2 * math.pi
        if t < math.pi:
            px = (cx + 22) + 16 * math.cos(t)
            py = (cy - 16) - 16 * math.sin(t)
        else:
            px = (cx + 22) - 16 * math.cos(t)
            py = (cy + 16) + 16 * math.sin(t)
        pts.append((round(px + rng.uniform(-0.8, 0.8), 2), round(py + rng.uniform(-0.8, 0.8), 2)))
    while len(pts) < n_points:
        p = rng.choice(pts)
        pts.append((round(p[0] + rng.uniform(-1, 1), 2), round(p[1] + rng.uniform(-1, 1), 2)))
    return pts[:n_points]

def solve_optimal_transport_matching(source_pts, target_pts):
    unassigned_indices = set(range(len(target_pts)))
    matched_targets = []
    for sx, sy in source_pts:
        best_idx = None
        best_dist = float('inf')
        sample_pool = list(unassigned_indices)[:60] if len(unassigned_indices) > 60 else list(unassigned_indices)
        for idx in sample_pool:
            tx, ty = target_pts[idx]
            d = (sx - tx) ** 2 + (sy - ty) ** 2
            if d < best_dist:
                best_dist = d
                best_idx = idx
        if best_idx is not None:
            unassigned_indices.remove(best_idx)
            matched_targets.append(target_pts[best_idx])
        else:
            matched_targets.append((sx, sy))
    return matched_targets

def generate_banner_svg(is_dark=True, output_path="assets/dark.svg"):
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    
    # 1. Compute Dithered Portrait Points
    portrait_raw = dither_floyd_steinberg_serpentine("data/portrait.png", target_w=300, target_h=340, step=2)
    n_groups = 60
    groups = [[] for _ in range(n_groups)]
    portrait_raw.sort(key=lambda p: p[2])
    for i, (px, py, _) in enumerate(portrait_raw):
        gx = px + 40
        gy = py + 75
        groups[i % n_groups].append((gx, gy))
        
    # 2. Compute 3 Logos & Particle Morphing for Travellers
    n_travellers = 850
    logo1 = sample_logo_1_ethereum(n_travellers, cx=190, cy=245, radius=90)
    logo2_raw = sample_logo_2_react(n_travellers, cx=190, cy=245, rx=85, ry=32)
    logo3_raw = sample_logo_3_typescript(n_travellers, cx=190, cy=245, size=130)
    logo2 = solve_optimal_transport_matching(logo1, logo2_raw)
    logo3 = solve_optimal_transport_matching(logo2, logo3_raw)
    
    # Color palette: TRUE DARK OBSIDIAN (Deep Black/Graphite, no heavy blue wash)
    if is_dark:
        bg_color = "#08090D"          # Obsidian deep black
        card_bg = "#0F1117"           # High-end dark card chassis
        terminal_border = "#21262D"   # Sleek GitHub dark border
        grid_line = "#161B22"         # Subtle neutral dark grid
        header_bg = "#0B0D13"         # Header dark
        title_color = "#22D3EE"       # Cyan glow
        accent_emerald = "#10B981"    # Green accent
        accent_purple = "#A78BFA"     # Purple accent
        text_primary = "#F0F6FC"      # Clean crisp white
        text_secondary = "#8B949E"    # Muted slate
        text_label = "#6E7681"        # Terminal label gray
        dot_color_p1 = "#22D3EE"
        dot_color_p2 = "#A78BFA"
        traveller_color = "#22D3EE"
        pill_bg = "#161B22"
        pill_border = "#30363D"
        divider_color = "#21262D"
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
        dot_color_p1 = "#0369A1"
        dot_color_p2 = "#6D28D9"
        traveller_color = "#0284C7"
        pill_bg = "#F1F5F9"
        pill_border = "#94A3B8"
        divider_color = "#E2E8F0"

    svg_parts = []
    svg_parts.append(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 880 460" width="100%" height="100%">')
    
    svg_parts.append(f"""
    <defs>
        <linearGradient id="pGrad" x1="0%" y1="0%" x2="100%" y2="100%">
            <stop offset="0%" stop-color="{dot_color_p1}"/>
            <stop offset="100%" stop-color="{dot_color_p2}"/>
        </linearGradient>
        <pattern id="gridPat" width="20" height="20" patternUnits="userSpaceOnUse">
            <path d="M 20 0 L 0 0 0 20" fill="none" stroke="{grid_line}" stroke-width="0.6" stroke-opacity="0.4"/>
        </pattern>
    </defs>
    <style><![CDATA[
        .mono {{ 
            font-family: 'JetBrains Mono', 'Cascadia Code', 'Fira Code', ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, monospace;
            text-rendering: geometricPrecision;
            -webkit-font-smoothing: antialiased;
        }}
        .sans {{ font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif; }}
        
        /* Shimmer & Dissolve Animation for Portrait (14s Loop) */
        @keyframes portraitLoop {{
            0%   {{ opacity: 0; transform: scale(0.98); }}
            12%  {{ opacity: 0.95; transform: scale(1); }}
            25%  {{ opacity: 0.95; transform: scale(1); }}
            32%  {{ opacity: 0.15; transform: translateY(-4px) scale(0.97); filter: blur(1px); }}
            88%  {{ opacity: 0.10; transform: translateY(-4px) scale(0.97); filter: blur(1px); }}
            96%  {{ opacity: 0.85; transform: translateY(0) scale(1); filter: none; }}
            100% {{ opacity: 0.95; transform: scale(1); }}
        }}
        
        /* Travellers Morphing Visibility (14s Loop) */
        @keyframes travellerFade {{
            0%   {{ opacity: 0; }}
            28%  {{ opacity: 0; }}
            35%  {{ opacity: 0.95; }}
            88%  {{ opacity: 0.95; }}
            94%  {{ opacity: 0; }}
            100% {{ opacity: 0; }}
        }}
        
        /* Pulse Live Indicator */
        @keyframes pulseLive {{
            0%, 100% {{ opacity: 1; transform: scale(1); }}
            50% {{ opacity: 0.35; transform: scale(0.85); }}
        }}
        
        .live-dot {{ animation: pulseLive 2s infinite ease-in-out; transform-origin: 820px 24px; }}
        .portrait-layer {{ animation: portraitLoop 14s infinite cubic-bezier(0.4, 0, 0.2, 1); transform-origin: 190px 245px; }}
        .traveller-layer {{ animation: travellerFade 14s infinite ease-in-out; }}
    ]]></style>
    """)
    
    # Outer Chassis (Deep Obsidian #08090D)
    svg_parts.append(f'<rect width="880" height="460" rx="14" fill="{bg_color}" stroke="{terminal_border}" stroke-width="1.2"/>')
    svg_parts.append(f'<rect x="1" y="1" width="878" height="458" rx="13" fill="url(#gridPat)"/>')
    
    # Header Bar
    svg_parts.append(f'<rect x="0" y="0" width="880" height="48" rx="14" fill="{header_bg}" stroke="{terminal_border}" stroke-width="1"/>')
    svg_parts.append(f'<line x1="0" y1="48" x2="880" y2="48" stroke="{terminal_border}" stroke-width="1"/>')
    
    # Window Controls (macOS terminal dots)
    svg_parts.append('<circle cx="26" cy="24" r="5.5" fill="#FF5F56"/>')
    svg_parts.append('<circle cx="44" cy="24" r="5.5" fill="#FFBD2E"/>')
    svg_parts.append('<circle cx="62" cy="24" r="5.5" fill="#27C93F"/>')
    
    # Window Title
    svg_parts.append(f'<text x="88" y="29" class="mono" font-size="12" font-weight="600" fill="{text_secondary}">term://onkar.os/profile.sh <tspan fill="{title_color}">--live</tspan></text>')
    
    # Handle Pill & Live Telemetry
    svg_parts.append(f'<rect x="660" y="12" width="134" height="24" rx="12" fill="{pill_bg}" stroke="{pill_border}" stroke-width="0.8"/>')
    svg_parts.append(f'<text x="727" y="28" class="mono" font-size="11" font-weight="600" fill="{title_color}" text-anchor="middle">@prembevinakatti</text>')
    
    svg_parts.append(f'<circle class="live-dot" cx="818" cy="24" r="4.5" fill="{accent_emerald}"/>')
    svg_parts.append(f'<text x="829" y="28" class="mono" font-size="10.5" font-weight="700" fill="{accent_emerald}">LIVE</text>')
    
    # ==================== LEFT PANEL: VISUAL.MAP ====================
    svg_parts.append(f'<rect x="18" y="62" width="344" height="382" rx="10" fill="{card_bg}" stroke="{terminal_border}" stroke-width="1"/>')
    svg_parts.append(f'<rect x="18" y="62" width="344" height="30" rx="10" fill="{pill_bg}"/>')
    svg_parts.append(f'<line x1="18" y1="92" x2="362" y2="92" stroke="{terminal_border}" stroke-width="0.8"/>')
    svg_parts.append(f'<text x="32" y="82" class="mono" font-size="11" font-weight="700" fill="{title_color}">[ VISUAL.MAP ]</text>')
    svg_parts.append(f'<text x="348" y="82" class="mono" font-size="9" fill="{text_label}" text-anchor="end">300x340 // DITHER.FS</text>')
    
    # Layer 1: Dense Dithered Portrait
    svg_parts.append('<g class="portrait-layer">')
    for g_idx, g_pts in enumerate(groups):
        delay = round((g_idx / n_groups) * 1.8, 3)
        d_str = " ".join([f"M{x},{y}h1" for x, y in g_pts])
        svg_parts.append(f'<path d="{d_str}" stroke="url(#pGrad)" stroke-width="1.6" stroke-linecap="round" opacity="0">')
        svg_parts.append(f'  <animate attributeName="opacity" values="0;0.95;0.95;0.1;0.1;0.95" keyTimes="0;0.15;0.25;0.35;0.88;1" dur="14s" begin="{delay}s" repeatCount="indefinite"/>')
        svg_parts.append('</path>')
    svg_parts.append('</g>')
    
    # Layer 2: Travellers (Particle Morphing)
    svg_parts.append('<g class="traveller-layer">')
    for idx in range(n_travellers):
        p1 = logo1[idx]
        p2 = logo2[idx]
        p3 = logo3[idx]
        key_times = "0; 0.28; 0.35; 0.50; 0.55; 0.70; 0.75; 0.88; 0.94; 1"
        cx_vals = f"{p1[0]}; {p1[0]}; {p1[0]}; {p1[0]}; {p2[0]}; {p2[0]}; {p3[0]}; {p3[0]}; {p1[0]}; {p1[0]}"
        cy_vals = f"{p1[1]}; {p1[1]}; {p1[1]}; {p1[1]}; {p2[1]}; {p2[1]}; {p3[1]}; {p3[1]}; {p1[1]}; {p1[1]}"
        
        svg_parts.append(f'<circle cx="{p1[0]}" cy="{p1[1]}" r="1.3" fill="{traveller_color}" opacity="0.9">')
        svg_parts.append(f'  <animate attributeName="cx" values="{cx_vals}" keyTimes="{key_times}" dur="14s" repeatCount="indefinite" calcMode="spline" keySplines="0.4 0 0.2 1; 0.4 0 0.2 1; 0.4 0 0.2 1; 0.4 0 0.2 1; 0.4 0 0.2 1; 0.4 0 0.2 1; 0.4 0 0.2 1; 0.4 0 0.2 1; 0.4 0 0.2 1"/>')
        svg_parts.append(f'  <animate attributeName="cy" values="{cy_vals}" keyTimes="{key_times}" dur="14s" repeatCount="indefinite" calcMode="spline" keySplines="0.4 0 0.2 1; 0.4 0 0.2 1; 0.4 0 0.2 1; 0.4 0 0.2 1; 0.4 0 0.2 1; 0.4 0 0.2 1; 0.4 0 0.2 1; 0.4 0 0.2 1; 0.4 0 0.2 1"/>')
        svg_parts.append('</circle>')
    svg_parts.append('</g>')

    # Map Status Pill
    svg_parts.append(f'<rect x="30" y="412" width="320" height="22" rx="6" fill="{pill_bg}" stroke="{terminal_border}" stroke-width="0.8"/>')
    svg_parts.append(f'<text x="40" y="427" class="mono" font-size="9.5" font-weight="700" fill="{title_color}">MODE</text>')
    svg_parts.append(f'<text x="74" y="427" class="mono" font-size="9.5" fill="{text_secondary}">PARTICLE.MORPH [ETH ➔ REACT ➔ TS]</text>')

    # ==================== RIGHT PANEL: SYSTEM.INFO ====================
    svg_parts.append(f'<rect x="376" y="62" width="486" height="382" rx="10" fill="{card_bg}" stroke="{terminal_border}" stroke-width="1"/>')
    svg_parts.append(f'<rect x="376" y="62" width="486" height="30" rx="10" fill="{pill_bg}"/>')
    svg_parts.append(f'<line x1="376" y1="92" x2="862" y2="92" stroke="{terminal_border}" stroke-width="0.8"/>')
    svg_parts.append(f'<text x="392" y="82" class="mono" font-size="11" font-weight="700" fill="{title_color}">[ SYSTEM.INFO ]</text>')
    svg_parts.append(f'<text x="848" y="82" class="mono" font-size="9.5" font-weight="600" fill="{accent_emerald}" text-anchor="end">STATUS: ACTIVE // 240 FPS</text>')
    
    # Unified, crisp typography grid
    rows = [
        # (Label, Value, ValueColor, Weight, has_divider_after)
        ("Subject", "Onkar Bevinakatti", title_color, "700", False),
        ("Role", "Full Stack &amp; Blockchain Engineer", text_primary, "500", False),
        ("Origin", "India [IST / UTC+5:30]", text_secondary, "500", False),
        ("Status", "SHIPPING // Web3 &amp; Full-Stack", accent_emerald, "600", False),
        ("ToolChain", "Git · Docker · VS Code · Linux · AWS", text_secondary, "500", True),
        
        ("Core.Lang", "TypeScript · Solidity · Python · C++ · SQL", text_primary, "500", False),
        ("Core.Frontend", "React · Next.js · Tailwind CSS · Redux", title_color, "500", False),
        ("Core.Backend", "Node.js · Express · Ethers.js · REST APIs", text_primary, "500", False),
        ("Core.Database", "PostgreSQL · MongoDB · Redis · Supabase", accent_emerald, "500", False),
        ("Core.Infra", "AWS · Docker · Vercel · GitHub Actions", text_secondary, "500", True),
        
        ("Grid.Mail", "onkarbevinakatti09@gmail.com", text_secondary, "500", False),
        ("Grid.Portfolio", "https://onkarportfolio.onrender.com", title_color, "500", False),
        ("Grid.LinkedIn", "linkedin.com/in/onkar-bevinakatti-6515b8292", text_primary, "500", False),
        ("Grid.GitHub", "github.com/prembevinakatti", accent_purple, "500", False),
    ]
    
    label_x = 394
    val_x = 512
    cur_y = 114
    
    for label, val, color, weight, has_div in rows:
        # Label
        svg_parts.append(f'<text x="{label_x}" y="{cur_y}" class="mono" font-size="11" font-weight="600" fill="{text_label}">{label}</text>')
        # Dotted leader
        leader_start = label_x + len(label) * 7.2 + 8
        leader_end = val_x - 10
        if leader_start < leader_end:
            svg_parts.append(f'<line x1="{leader_start:.1f}" y1="{cur_y - 3.5}" x2="{leader_end:.1f}" y2="{cur_y - 3.5}" stroke="{divider_color}" stroke-width="1" stroke-dasharray="2 3"/>')
        # Value
        svg_parts.append(f'<text x="{val_x}" y="{cur_y}" class="mono" font-size="11" font-weight="{weight}" fill="{color}">{val}</text>')
        
        cur_y += 19.5
        if has_div:
            svg_parts.append(f'<line x1="394" y1="{cur_y - 7}" x2="846" y2="{cur_y - 7}" stroke="{divider_color}" stroke-width="1" stroke-dasharray="3 3"/>')
            cur_y += 6

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
