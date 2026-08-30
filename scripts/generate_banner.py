#!/usr/bin/env python3
"""
Developer OS - Animated Hero SVG Banner Generator
Synthesizes dark.svg and light.svg for GitHub profile README.
Features:
- Serpentine Floyd-Steinberg 1-bit dithering
- 60-group interleaved shimmer reveal (per-dot organic noise to eliminate grid trap)
- Travellers layer with optimal-transport particle morphing between 3 tech logos
- SYSTEM.INFO terminal dashboard with precision dotted leaders and lengthAdjust
- Dark & Light mode color schemes
"""

import os
import math
import random
import numpy as np
from PIL import Image, ImageDraw, ImageFilter

def create_default_portrait_if_missing(filepath="data/portrait.png", width=300, height=340):
    """Generates a high-detail cybernetic/developer head-and-shoulders baseline if no custom photo is provided."""
    if os.path.exists(filepath):
        return
    
    img = Image.new("L", (width, height), 0)
    draw = ImageDraw.Draw(img)
    
    # Head & shoulders geometric model with soft lighting
    center_x = width // 2
    # Shoulders
    draw.ellipse([center_x - 120, 230, center_x + 120, 420], fill=140)
    draw.polygon([(center_x - 130, 340), (center_x + 130, 340), (center_x + 90, 240), (center_x - 90, 240)], fill=160)
    
    # Neck
    draw.rectangle([center_x - 32, 170, center_x + 32, 250], fill=180)
    
    # Head / Jaw
    draw.ellipse([center_x - 65, 80, center_x + 65, 210], fill=210)
    # Hair
    draw.ellipse([center_x - 72, 60, center_x + 72, 150], fill=60)
    draw.rectangle([center_x - 70, 75, center_x + 70, 110], fill=50)
    
    # Face features (subtle contrast for dithering)
    # Eyes
    draw.ellipse([center_x - 38, 128, center_x - 18, 142], fill=70)
    draw.ellipse([center_x + 18, 128, center_x + 38, 142], fill=70)
    draw.ellipse([center_x - 30, 131, center_x - 24, 139], fill=240)
    draw.ellipse([center_x + 24, 131, center_x + 30, 139], fill=240)
    # Eyebrows
    draw.line([center_x - 42, 120, center_x - 14, 122], fill=40, width=4)
    draw.line([center_x + 14, 122, center_x + 42, 120], fill=40, width=4)
    # Nose ridge & shadow
    draw.line([center_x - 2, 130, center_x - 4, 160], fill=160, width=3)
    draw.polygon([(center_x - 8, 160), (center_x + 6, 160), (center_x - 1, 153)], fill=130)
    # Mouth
    draw.line([center_x - 22, 182, center_x + 22, 182], fill=110, width=3)
    draw.line([center_x - 14, 190, center_x + 14, 190], fill=150, width=2)
    # Glasses / Cybernetic HUD rim (stylish tech accent)
    draw.rounded_rectangle([center_x - 45, 120, center_x - 10, 148], radius=4, outline=250, width=2)
    draw.rounded_rectangle([center_x + 10, 120, center_x + 45, 148], radius=4, outline=250, width=2)
    draw.line([center_x - 10, 132, center_x + 10, 132], fill=250, width=2)

    # Soft ambient blur for photographic dithering gradients
    img = img.filter(ImageFilter.GaussianBlur(radius=1.2))
    img.save(filepath)
    print(f"[+] Created synthetic reference portrait at {filepath}")

def dither_floyd_steinberg_serpentine(image_path, target_w=300, target_h=340, step=2):
    """
    Applies serpentine Floyd-Steinberg dithering with moderate contrast tuning
    and converts pixels into coordinate points with per-dot anti-grid noise.
    """
    img = Image.open(image_path).convert("L")
    img = img.resize((target_w // step, target_h // step), Image.Resampling.LANCZOS)
    
    # Moderate contrast curve
    arr = np.array(img, dtype=np.float32)
    # Normalize 0..1
    arr = arr / 255.0
    # Contrast adjustment: midpoint 0.5, gentle S-curve
    arr = np.clip((arr - 0.45) * 1.35 + 0.45, 0.0, 1.0) * 255.0
    
    h, w = arr.shape
    dithered = arr.copy()
    
    # Serpentine Floyd-Steinberg
    for y in range(h):
        is_left_to_right = (y % 2 == 0)
        x_range = range(w) if is_left_to_right else range(w - 1, -1, -1)
        for x in x_range:
            old_val = dithered[y, x]
            new_val = 255.0 if old_val > 128.0 else 0.0
            dithered[y, x] = new_val
            error = old_val - new_val
            
            if is_left_to_right:
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

    # Collect active points (foreground dots)
    points = []
    rng = random.Random(42)
    for y in range(h):
        for x in range(w):
            if dithered[y, x] > 128:  # Lit dot
                real_x = x * step + 1 + (rng.uniform(-0.35, 0.35))
                real_y = y * step + 1 + (rng.uniform(-0.35, 0.35))
                # Anti-grid noise score for interleaved grouping
                noise_score = (math.sin(x * 0.45) * math.cos(y * 0.35) + rng.uniform(0, 1.0))
                points.append((round(real_x, 2), round(real_y, 2), noise_score))
                
    return points

def sample_logo_1_ethereum(n_points=900, cx=150, cy=170, radius=95):
    """Samples points along Ethereum / Solidity diamond geometry."""
    pts = []
    rng = random.Random(101)
    
    # 3D faceted diamond vertices
    top = (cx, cy - radius)
    mid_l = (cx - radius * 0.72, cy)
    mid_r = (cx + radius * 0.72, cy)
    center_front = (cx, cy + radius * 0.15)
    bottom = (cx, cy + radius * 0.95)
    
    segments = [
        # Upper pyramid
        (top, mid_l, 140),
        (top, mid_r, 140),
        (top, center_front, 160),
        (mid_l, center_front, 100),
        (mid_r, center_front, 100),
        # Lower inverted pyramid
        (center_front, bottom, 130),
        (mid_l, bottom, 110),
        (mid_r, bottom, 110)
    ]
    
    for (p1, p2, count) in segments:
        for _ in range(count):
            t = rng.random()
            # slight jitter for vector particle look
            jitter_x = rng.uniform(-0.9, 0.9)
            jitter_y = rng.uniform(-0.9, 0.9)
            px = p1[0] + (p2[0] - p1[0]) * t + jitter_x
            py = p1[1] + (p2[1] - p1[1]) * t + jitter_y
            pts.append((round(px, 2), round(py, 2)))
            
    while len(pts) < n_points:
        p = rng.choice(pts)
        pts.append((round(p[0] + rng.uniform(-1, 1), 2), round(p[1] + rng.uniform(-1, 1), 2)))
    return pts[:n_points]

def sample_logo_2_react(n_points=900, cx=150, cy=170, rx=85, ry=32):
    """Samples points along React atomic orbital geometry."""
    pts = []
    rng = random.Random(202)
    
    # Core nucleus
    nucleus_count = 150
    for _ in range(nucleus_count):
        r = rng.uniform(0, 16)
        ang = rng.uniform(0, 2 * math.pi)
        pts.append((round(cx + r * math.cos(ang), 2), round(cy + r * math.sin(ang), 2)))
        
    # 3 Elliptical orbits rotated at 0, 60, 120 deg
    orbit_pts_each = (n_points - nucleus_count) // 3
    for rot in [0, math.pi / 3, 2 * math.pi / 3]:
        for _ in range(orbit_pts_each):
            theta = rng.uniform(0, 2 * math.pi)
            ex = rx * math.cos(theta)
            ey = ry * math.sin(theta)
            # rotate
            rot_x = ex * math.cos(rot) - ey * math.sin(rot)
            rot_y = ex * math.sin(rot) + ey * math.cos(rot)
            jx = rng.uniform(-0.8, 0.8)
            jy = rng.uniform(-0.8, 0.8)
            pts.append((round(cx + rot_x + jx, 2), round(cy + rot_y + jy, 2)))
            
    while len(pts) < n_points:
        p = rng.choice(pts)
        pts.append((round(p[0] + rng.uniform(-1, 1), 2), round(p[1] + rng.uniform(-1, 1), 2)))
    return pts[:n_points]

def sample_logo_3_typescript(n_points=900, cx=150, cy=170, size=130):
    """Samples points along TypeScript / Tech Hexagonal Shield geometry."""
    pts = []
    rng = random.Random(303)
    
    # Hexagon outer boundary
    hex_pts = []
    for i in range(6):
        angle = math.pi / 6 + i * (math.pi / 3)
        hex_pts.append((cx + size * 0.68 * math.cos(angle), cy + size * 0.68 * math.sin(angle)))
        
    # Sample edges of hexagon
    hex_count = 420
    per_edge = hex_count // 6
    for i in range(6):
        p1 = hex_pts[i]
        p2 = hex_pts[(i + 1) % 6]
        for _ in range(per_edge):
            t = rng.random()
            pts.append((round(p1[0] + (p2[0] - p1[0]) * t + rng.uniform(-0.8, 0.8), 2),
                        round(p1[1] + (p2[1] - p1[1]) * t + rng.uniform(-0.8, 0.8), 2)))
            
    # 'TS' monogram inside
    # T: top bar (cx-42, cy-32) to (cx-10, cy-32), stem down to (cx-26, cy+36)
    for _ in range(120):
        t = rng.random()
        pts.append((round((cx - 42) + 32 * t + rng.uniform(-0.6, 0.6), 2), round(cy - 32 + rng.uniform(-0.6, 0.6), 2)))
    for _ in range(140):
        t = rng.random()
        pts.append((round(cx - 26 + rng.uniform(-0.6, 0.6), 2), round((cy - 32) + 68 * t + rng.uniform(-0.6, 0.6), 2)))
        
    # S: upper curve, middle bar, lower curve
    for _ in range(220):
        t = rng.random() * 2 * math.pi
        if t < math.pi: # top curve
            px = (cx + 22) + 16 * math.cos(t)
            py = (cy - 16) - 16 * math.sin(t)
        else: # bottom curve
            px = (cx + 22) - 16 * math.cos(t)
            py = (cy + 16) + 16 * math.sin(t)
        pts.append((round(px + rng.uniform(-0.8, 0.8), 2), round(py + rng.uniform(-0.8, 0.8), 2)))
        
    while len(pts) < n_points:
        p = rng.choice(pts)
        pts.append((round(p[0] + rng.uniform(-1, 1), 2), round(p[1] + rng.uniform(-1, 1), 2)))
    return pts[:n_points]

def solve_optimal_transport_matching(source_pts, target_pts):
    """
    Greedy nearest neighbor matching to compute smooth morph paths
    from source points to target points with minimal particle travel distance.
    """
    available_targets = list(range(len(target_pts)))
    target_np = np.array(target_pts)
    matched_targets = []
    
    # Fast KD-like greedy pairing
    unassigned_indices = set(range(len(target_pts)))
    
    for sx, sy in source_pts:
        best_idx = None
        best_dist = float('inf')
        # Check subset of unassigned to maintain high performance
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
    """
    Assembles the complete SVG banner with embedded SMIL/CSS animations,
    dithered portrait layer (interleaved shimmer), and traveller particle morphing.
    """
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    
    # Ensure portrait exists
    portrait_path = "data/portrait.png"
    create_default_portrait_if_missing(portrait_path)
    
    # 1. Compute Dithered Portrait Points
    portrait_raw = dither_floyd_steinberg_serpentine(portrait_path, target_w=300, target_h=340, step=2)
    # Group into 60 interleaved shimmer groups
    n_groups = 60
    groups = [[] for _ in range(n_groups)]
    
    # Sort with noise score to interleave naturally across the entire image
    portrait_raw.sort(key=lambda p: p[2])
    for i, (px, py, _) in enumerate(portrait_raw):
        # Shift coordinate into Left Terminal Panel: Box x=30, y=70, w=320, h=350 -> center portrait at x=40, y=75
        gx = px + 40
        gy = py + 75
        groups[i % n_groups].append((gx, gy))
        
    # 2. Compute 3 Logos & Particle Morphing for Travellers
    n_travellers = 850
    # Center inside the VISUAL.MAP panel (cx=190, cy=245)
    logo1 = sample_logo_1_ethereum(n_travellers, cx=190, cy=245, radius=90)
    logo2_raw = sample_logo_2_react(n_travellers, cx=190, cy=245, rx=85, ry=32)
    logo3_raw = sample_logo_3_typescript(n_travellers, cx=190, cy=245, size=130)
    
    # Match paths: Logo 1 -> Logo 2 -> Logo 3
    logo2 = solve_optimal_transport_matching(logo1, logo2_raw)
    logo3 = solve_optimal_transport_matching(logo2, logo3_raw)
    
    # Color tokens
    if is_dark:
        bg_color = "#0A101F"
        card_bg = "#0D1527"
        terminal_border = "#1E293B"
        grid_line = "#172554"
        title_color = "#22D3EE"
        accent_emerald = "#10B981"
        accent_purple = "#A78BFA"
        text_primary = "#F8FAFC"
        text_secondary = "#94A3B8"
        text_muted = "#475569"
        dot_color_p1 = "#38BDF8"
        dot_color_p2 = "#818CF8"
        traveller_color = "#22D3EE"
        pill_bg = "#1E293B"
        pill_border = "#0891B2"
    else:
        bg_color = "#F8FAFC"
        card_bg = "#FFFFFF"
        terminal_border = "#CBD5E1"
        grid_line = "#E2E8F0"
        title_color = "#0284C7"
        accent_emerald = "#059669"
        accent_purple = "#7C3AED"
        text_primary = "#0F172A"
        text_secondary = "#475569"
        text_muted = "#94A3B8"
        dot_color_p1 = "#0369A1"
        dot_color_p2 = "#6D28D9"
        traveller_color = "#0284C7"
        pill_bg = "#F1F5F9"
        pill_border = "#94A3B8"

    # SVG Canvas Dimensions: 880 × 460
    svg_parts = []
    svg_parts.append(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 880 460" width="100%" height="100%">')
    
    # Embedded Stylesheet
    svg_parts.append("""
    <defs>
        <linearGradient id="pGrad" x1="0%" y1="0%" x2="100%" y2="100%">
            <stop offset="0%" stop-color="{p1}"/>
            <stop offset="100%" stop-color="{p2}"/>
        </linearGradient>
        <linearGradient id="cardGrad" x1="0%" y1="0%" x2="0%" y2="100%">
            <stop offset="0%" stop-color="{cbg}" stop-opacity="0.95"/>
            <stop offset="100%" stop-color="{cbg}" stop-opacity="0.85"/>
        </linearGradient>
        <pattern id="gridPat" width="20" height="20" patternUnits="userSpaceOnUse">
            <path d="M 20 0 L 0 0 0 20" fill="none" stroke="{grid}" stroke-width="0.5" stroke-opacity="0.35"/>
        </pattern>
    </defs>
    <style><![CDATA[
        .mono {{ font-family: 'JetBrains Mono', 'Fira Code', ui-monospace, SFMono-Regular, monospace; }}
        .sans {{ font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif; }}
        
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
        
        .live-dot {{ animation: pulseLive 2s infinite ease-in-out; transform-origin: 820px 32px; }}
        .portrait-layer {{ animation: portraitLoop 14s infinite cubic-bezier(0.4, 0, 0.2, 1); transform-origin: 190px 245px; }}
        .traveller-layer {{ animation: travellerFade 14s infinite ease-in-out; }}
    ]]></style>
    """.format(
        p1=dot_color_p1, p2=dot_color_p2, cbg=card_bg, grid=grid_line
    ))
    
    # Outer Chassis
    svg_parts.append(f'<rect width="880" height="460" rx="16" fill="{bg_color}" stroke="{terminal_border}" stroke-width="1.5"/>')
    svg_parts.append(f'<rect x="1" y="1" width="878" height="458" rx="15" fill="url(#gridPat)"/>')
    
    # Header Bar
    svg_parts.append(f'<rect x="0" y="0" width="880" height="52" rx="16" fill="{card_bg}" stroke="{terminal_border}" stroke-width="1"/>')
    svg_parts.append(f'<line x1="0" y1="52" x2="880" y2="52" stroke="{terminal_border}" stroke-width="1.2"/>')
    
    # Window Controls (macOS terminal style dots)
    svg_parts.append('<circle cx="28" cy="26" r="6" fill="#EF4444"/>')
    svg_parts.append('<circle cx="48" cy="26" r="6" fill="#F59E0B"/>')
    svg_parts.append('<circle cx="68" cy="26" r="6" fill="#10B981"/>')
    
    # Window Title
    svg_parts.append(f'<text x="96" y="31" class="mono" font-size="13" font-weight="600" fill="{text_secondary}">term://onkar.os/profile.sh <tspan fill="{title_color}">--live</tspan></text>')
    
    # Handle Pill & Live Telemetry
    svg_parts.append(f'<rect x="650" y="15" width="138" height="24" rx="12" fill="{pill_bg}" stroke="{pill_border}" stroke-width="0.8"/>')
    svg_parts.append(f'<text x="719" y="31" class="mono" font-size="11" font-weight="600" fill="{title_color}" text-anchor="middle">@prembevinakatti</text>')
    
    svg_parts.append(f'<circle class="live-dot" cx="818" cy="27" r="4.5" fill="{accent_emerald}"/>')
    svg_parts.append(f'<text x="830" y="31" class="mono" font-size="10" font-weight="700" fill="{accent_emerald}">LIVE</text>')
    
    # ==================== LEFT PANEL: VISUAL.MAP ====================
    svg_parts.append(f'<rect x="22" y="68" width="340" height="372" rx="10" fill="{card_bg}" stroke="{terminal_border}" stroke-width="1"/>')
    svg_parts.append(f'<rect x="22" y="68" width="340" height="30" rx="10" fill="{pill_bg}"/>')
    svg_parts.append(f'<line x1="22" y1="98" x2="362" y2="98" stroke="{terminal_border}" stroke-width="0.8"/>')
    svg_parts.append(f'<text x="36" y="88" class="mono" font-size="11" font-weight="700" fill="{title_color}">[ VISUAL.MAP ]</text>')
    svg_parts.append(f'<text x="348" y="88" class="mono" font-size="9" fill="{text_muted}" text-anchor="end">300x340 // DITHER.FS</text>')
    
    # Layer 1: Dense Dithered Portrait (with 60 interleaved shimmer delay groups)
    svg_parts.append('<g class="portrait-layer">')
    for g_idx, g_pts in enumerate(groups):
        delay = round((g_idx / n_groups) * 1.8, 3)
        d_str = " ".join([f"M{x},{y}h1" for x, y in g_pts])
        svg_parts.append(f'<path d="{d_str}" stroke="url(#pGrad)" stroke-width="1.6" stroke-linecap="round" opacity="0">')
        svg_parts.append(f'  <animate attributeName="opacity" values="0;0.95;0.95;0.1;0.1;0.95" keyTimes="0;0.15;0.25;0.35;0.88;1" dur="14s" begin="{delay}s" repeatCount="indefinite"/>')
        svg_parts.append('</path>')
    svg_parts.append('</g>')
    
    # Layer 2: Travellers (Particle Morphing: Logo 1 -> Logo 2 -> Logo 3)
    svg_parts.append('<g class="traveller-layer">')
    # Loop timing breakdown:
    # 0s..4s: Hidden
    # 4.5s..7.0s: Logo 1 (Ethereum)
    # 7.5s..9.8s: Logo 2 (React)
    # 10.3s..12.5s: Logo 3 (TypeScript Hex)
    # 13.0s..14.0s: Return
    for idx in range(n_travellers):
        p1 = logo1[idx]
        p2 = logo2[idx]
        p3 = logo3[idx]
        
        # SMIL motion path interpolation
        key_times = "0; 0.28; 0.35; 0.50; 0.55; 0.70; 0.75; 0.88; 0.94; 1"
        cx_vals = f"{p1[0]}; {p1[0]}; {p1[0]}; {p1[0]}; {p2[0]}; {p2[0]}; {p3[0]}; {p3[0]}; {p1[0]}; {p1[0]}"
        cy_vals = f"{p1[1]}; {p1[1]}; {p1[1]}; {p1[1]}; {p2[1]}; {p2[1]}; {p3[1]}; {p3[1]}; {p1[1]}; {p1[1]}"
        
        svg_parts.append(f'<circle cx="{p1[0]}" cy="{p1[1]}" r="1.4" fill="{traveller_color}" opacity="0.9">')
        svg_parts.append(f'  <animate attributeName="cx" values="{cx_vals}" keyTimes="{key_times}" dur="14s" repeatCount="indefinite" calcMode="spline" keySplines="0.4 0 0.2 1; 0.4 0 0.2 1; 0.4 0 0.2 1; 0.4 0 0.2 1; 0.4 0 0.2 1; 0.4 0 0.2 1; 0.4 0 0.2 1; 0.4 0 0.2 1; 0.4 0 0.2 1"/>')
        svg_parts.append(f'  <animate attributeName="cy" values="{cy_vals}" keyTimes="{key_times}" dur="14s" repeatCount="indefinite" calcMode="spline" keySplines="0.4 0 0.2 1; 0.4 0 0.2 1; 0.4 0 0.2 1; 0.4 0 0.2 1; 0.4 0 0.2 1; 0.4 0 0.2 1; 0.4 0 0.2 1; 0.4 0 0.2 1; 0.4 0 0.2 1"/>')
        svg_parts.append('</circle>')
    svg_parts.append('</g>')

    # Map Status Pill
    svg_parts.append(f'<rect x="36" y="405" width="312" height="24" rx="6" fill="{pill_bg}" stroke="{terminal_border}" stroke-width="0.8"/>')
    svg_parts.append(f'<text x="46" y="421" class="mono" font-size="10" fill="{title_color}">MODE</text>')
    svg_parts.append(f'<text x="80" y="421" class="mono" font-size="10" fill="{text_secondary}">PARTICLE.MORPH [ETH ➔ REACT ➔ TS]</text>')

    # ==================== RIGHT PANEL: SYSTEM.INFO ====================
    svg_parts.append(f'<rect x="378" y="68" width="480" height="372" rx="10" fill="{card_bg}" stroke="{terminal_border}" stroke-width="1"/>')
    svg_parts.append(f'<rect x="378" y="68" width="480" height="30" rx="10" fill="{pill_bg}"/>')
    svg_parts.append(f'<line x1="378" y1="98" x2="858" y2="98" stroke="{terminal_border}" stroke-width="0.8"/>')
    svg_parts.append(f'<text x="394" y="88" class="mono" font-size="11" font-weight="700" fill="{title_color}">[ SYSTEM.INFO ]</text>')
    svg_parts.append(f'<text x="844" y="88" class="mono" font-size="9" fill="{accent_emerald}" text-anchor="end">STATUS: ACTIVE // 240 FPS</text>')
    
    # System Info Fields with Precision Dotted Leaders & SVG Spacing
    rows_section1 = [
        ("Subject", "ONKAR BEVINAKATTI"),
        ("Role", "FULL STACK &amp; BLOCKCHAIN ENGINEER"),
        ("Origin", "INDIA [IST / UTC+5:30]"),
        ("Status", "SHIPPING // WEB3 &amp; FULL-STACK"),
        ("ToolChain", "GIT · DOCKER · VS CODE · LINUX"),
    ]
    
    rows_section2 = [
        ("Core.Lang", "TYPESCRIPT · JAVASCRIPT · SOLIDITY · PYTHON"),
        ("Core.Frontend", "REACT · NEXT.JS · TAILWIND · REDUX"),
        ("Core.Backend", "NODE.JS · EXPRESS · ETHERS.JS · REST"),
        ("Core.Database", "POSTGRESQL · MONGODB · REDIS"),
        ("Core.Infra", "DOCKER · VERCEL · GITHUB ACTIONS"),
    ]
    
    rows_section3 = [
        ("Grid.Mail", "onkarbevinakatti09@gmail.com"),
        ("Grid.Portfolio", "https://onkarportfolio.onrender.com"),
        ("Grid.LinkedIn", "linkedin.com/in/onkar-bevinakatti-6515b8292"),
        ("Grid.GitHub", "github.com/prembevinakatti"),
    ]
    
    # Render Section 1
    cur_y = 122
    for label, val in rows_section1:
        svg_parts.append(f'<text x="396" y="{cur_y}" class="mono" font-size="11" fill="{text_secondary}">{label}</text>')
        # Dotted leader line
        svg_parts.append(f'<line x1="490" y1="{cur_y - 3}" x2="560" y2="{cur_y - 3}" stroke="{text_muted}" stroke-width="1" stroke-dasharray="2 4" opacity="0.6"/>')
        val_color = title_color if label == "Subject" else (accent_emerald if label == "Status" else text_primary)
        svg_parts.append(f'<text x="570" y="{cur_y}" class="mono" font-size="11" font-weight="600" fill="{val_color}" textLength="270" lengthAdjust="spacingAndGlyphs">{val}</text>')
        cur_y += 20
        
    # Divider 1
    svg_parts.append(f'<line x1="396" y1="{cur_y - 8}" x2="840" y2="{cur_y - 8}" stroke="{terminal_border}" stroke-width="0.8" stroke-dasharray="3 3"/>')
    cur_y += 8
    
    # Render Section 2 (Core Stacks)
    for label, val in rows_section2:
        svg_parts.append(f'<text x="396" y="{cur_y}" class="mono" font-size="11" fill="{text_secondary}">{label}</text>')
        svg_parts.append(f'<line x1="510" y1="{cur_y - 3}" x2="545" y2="{cur_y - 3}" stroke="{text_muted}" stroke-width="1" stroke-dasharray="2 4" opacity="0.6"/>')
        val_color = accent_purple if "Lang" in label or "Frontend" in label else text_primary
        svg_parts.append(f'<text x="555" y="{cur_y}" class="mono" font-size="10.5" font-weight="500" fill="{val_color}" textLength="285" lengthAdjust="spacingAndGlyphs">{val}</text>')
        cur_y += 20
        
    # Divider 2
    svg_parts.append(f'<line x1="396" y1="{cur_y - 8}" x2="840" y2="{cur_y - 8}" stroke="{terminal_border}" stroke-width="0.8" stroke-dasharray="3 3"/>')
    cur_y += 8
    
    # Render Section 3 (Grid Networks)
    for label, val in rows_section3:
        svg_parts.append(f'<text x="396" y="{cur_y}" class="mono" font-size="11" fill="{text_secondary}">{label}</text>')
        svg_parts.append(f'<line x1="510" y1="{cur_y - 3}" x2="545" y2="{cur_y - 3}" stroke="{text_muted}" stroke-width="1" stroke-dasharray="2 4" opacity="0.6"/>')
        svg_parts.append(f'<text x="555" y="{cur_y}" class="mono" font-size="10.5" font-weight="500" fill="{title_color}" textLength="285" lengthAdjust="spacingAndGlyphs">{val}</text>')
        cur_y += 20

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
