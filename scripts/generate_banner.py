#!/usr/bin/env python3
"""
Developer OS - Animated Hero SVG Banner Generator
Features:
- Left Panel: Continuous 3-Phase Neural Morphing Animation:
  Phase 1 (0s-4.5s): Onkar's High-Definition Dithered Face Portrait (Floyd-Steinberg Dots with Shimmer)
  Phase 2 (4.5s-9.0s): Next.js Vector Engine (Glowing Circle with N stem & Orbitals)
  Phase 3 (9.0s-13.5s): React Atomic Core (Rotating Orbital Ellipses & Nucleus)
- Right Panel: Pristine SYSTEM.INFO Terminal Dashboard.
"""

import os
import math
from PIL import Image
import numpy as np

def generate_portrait_dither_svg(image_path="data/portrait.png", panel_w=344, panel_h=382, dither_color="#22D3EE"):
    img = Image.open(image_path).convert("L")
    w = 88
    h = int(w * img.height / img.width)
    img_resized = img.resize((w, h), Image.Resampling.LANCZOS)
    dithered = img_resized.convert("1", dither=Image.Dither.FLOYDSTEINBERG)
    arr = np.array(dithered)
    
    pixel_size = 2.7
    offset_x = 18 + (panel_w - w * pixel_size) / 2
    offset_y = 62 + 28 + (panel_h - 40 - h * pixel_size) / 2
    
    # 40 shimmer groups
    groups = [[] for _ in range(40)]
    for y in range(h):
        for x in range(w):
            if arr[y, x]:  # Person foreground pixel (True / White)
                px = offset_x + x * pixel_size
                py = offset_y + y * pixel_size
                grp_idx = (x * 7 + y * 13) % 40
                groups[grp_idx].append((px, py))
                
    svg_groups = []
    for i, grp in enumerate(groups):
        if not grp:
            continue
        rects = "".join([f'<rect x="{px:.1f}" y="{py:.1f}" width="{pixel_size-0.5:.1f}" height="{pixel_size-0.5:.1f}" rx="0.5"/>' for px, py in grp])
        svg_groups.append(f'<g class="dither-grp-{i}">{rects}</g>')
        
    return "\n".join(svg_groups)

def generate_banner_svg(is_dark=True, output_path="assets/dark.svg"):
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    
    cx = 190
    cy = 248
    
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

    portrait_dots = generate_portrait_dither_svg("data/portrait.png", 344, 382, dither_fill)
    
    # CSS Shimmer & 3-Phase Animation
    shimmer_rules = []
    for i in range(40):
        delay = (i * 0.07) % 2.5
        shimmer_rules.append(f'.dither-grp-{i} {{ animation: dotTwinkle 2.8s infinite ease-in-out {delay:.2f}s; fill: {dither_fill}; }}')
        
    svg = []
    svg.append('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 880 460" width="100%" height="100%">')
    
    svg.append(f"""
    <defs>
        <pattern id="gridPat" width="20" height="20" patternUnits="userSpaceOnUse">
            <path d="M 20 0 L 0 0 0 20" fill="none" stroke="{grid_line}" stroke-width="0.6" stroke-opacity="0.4"/>
        </pattern>
        <radialGradient id="portGlow" cx="50%" cy="50%" r="50%">
            <stop offset="0%" stop-color="{title_color}" stop-opacity="0.22"/>
            <stop offset="100%" stop-color="{title_color}" stop-opacity="0"/>
        </radialGradient>
        <linearGradient id="nextGrad" x1="0%" y1="0%" x2="100%" y2="100%">
            <stop offset="0%" stop-color="#F0F6FC"/>
            <stop offset="70%" stop-color="#22D3EE"/>
            <stop offset="100%" stop-color="#08090D"/>
        </linearGradient>
    </defs>
    <style><![CDATA[
        .mono {{ 
            font-family: 'JetBrains Mono', 'Cascadia Code', 'Fira Code', ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, monospace;
            text-rendering: geometricPrecision;
            -webkit-font-smoothing: antialiased;
        }}
        .sans {{ font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif; }}
        
        /* 14-Second 3-Phase Animation */
        @keyframes phasePortrait {{
            0%, 30%   {{ opacity: 1; transform: scale(1); }}
            34%, 96%  {{ opacity: 0; transform: scale(0.96); pointer-events: none; }}
            100%      {{ opacity: 1; transform: scale(1); }}
        }}
        @keyframes phaseNextjs {{
            0%, 30%   {{ opacity: 0; transform: scale(0.94); pointer-events: none; }}
            34%, 63%  {{ opacity: 1; transform: scale(1); }}
            67%, 100% {{ opacity: 0; transform: scale(0.94); pointer-events: none; }}
        }}
        @keyframes phaseReact {{
            0%, 63%   {{ opacity: 0; transform: scale(0.94); pointer-events: none; }}
            67%, 96%  {{ opacity: 1; transform: scale(1); }}
            100%      {{ opacity: 0; transform: scale(0.94); pointer-events: none; }}
        }}
        
        @keyframes rotateClockwise {{
            from {{ transform: rotate(0deg); }}
            to   {{ transform: rotate(360deg); }}
        }}
        @keyframes rotateCounter {{
            from {{ transform: rotate(360deg); }}
            to   {{ transform: rotate(0deg); }}
        }}
        
        @keyframes dotTwinkle {{
            0%, 100% {{ opacity: 0.85; }}
            50%      {{ opacity: 0.40; }}
        }}
        @keyframes pulseLive {{
            0%, 100% {{ opacity: 1; transform: scale(1); }}
            50%      {{ opacity: 0.35; transform: scale(0.85); }}
        }}
        
        .layer-portrait {{ transform-origin: {cx}px {cy}px; animation: phasePortrait 14s infinite ease-in-out; }}
        .layer-nextjs   {{ transform-origin: {cx}px {cy}px; animation: phaseNextjs 14s infinite ease-in-out; }}
        .layer-react    {{ transform-origin: {cx}px {cy}px; animation: phaseReact 14s infinite ease-in-out; }}
        
        .react-orbit-1 {{ transform-origin: {cx}px {cy}px; animation: rotateClockwise 12s linear infinite; }}
        .react-orbit-2 {{ transform-origin: {cx}px {cy}px; animation: rotateCounter 14s linear infinite; }}
        .react-orbit-3 {{ transform-origin: {cx}px {cy}px; animation: rotateClockwise 16s linear infinite; }}
        .nextjs-ring   {{ transform-origin: {cx}px {cy}px; animation: rotateClockwise 20s linear infinite; }}
        
        {chr(10).join(shimmer_rules)}
        .live-dot {{ animation: pulseLive 2s infinite ease-in-out; transform-origin: 820px 24px; }}
        
        @media (prefers-reduced-motion: reduce) {{
            .layer-portrait, .layer-nextjs, .layer-react, .react-orbit-1, .react-orbit-2, .react-orbit-3, .nextjs-ring {{
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
    
    # Live Pill
    svg.append(f'<rect x="660" y="12" width="134" height="24" rx="12" fill="{pill_bg}" stroke="{pill_border}" stroke-width="0.8"/>')
    svg.append(f'<text x="727" y="28" class="mono" font-size="11" font-weight="600" fill="{title_color}" text-anchor="middle">@prembevinakatti</text>')
    svg.append(f'<circle class="live-dot" cx="818" cy="24" r="4.5" fill="{accent_emerald}"/>')
    svg.append(f'<text x="829" y="28" class="mono" font-size="10.5" font-weight="700" fill="{accent_emerald}">LIVE</text>')
    
    # ==================== LEFT PANEL: 3-PHASE ANIMATED AVATAR ====================
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
    
    # Radial Background Glow
    svg.append(f'<circle cx="{cx}" cy="{cy}" r="125" fill="url(#portGlow)"/>')
    
    # ---------------- PHASE 1: HIGH-DEF DITHERED PORTRAIT ----------------
    svg.append(f'<g class="layer-portrait">')
    svg.append(portrait_dots)
    svg.append(f'<text x="{cx}" y="400" class="mono" font-size="9" font-weight="700" fill="{title_color}" text-anchor="middle" letter-spacing="1">ONKAR BEVINAKATTI</text>')
    svg.append(f'</g>')
    
    # ---------------- PHASE 2: NEXT.JS VECTOR CORE ----------------
    svg.append(f'<g class="layer-nextjs">')
    # Orbit ring
    svg.append(f'<circle class="nextjs-ring" cx="{cx}" cy="{cy}" r="88" fill="none" stroke="{title_color}" stroke-width="1" stroke-dasharray="6 8" opacity="0.5"/>')
    svg.append(f'<circle cx="{cx}" cy="{cy}" r="74" fill="#000000" stroke="{title_color}" stroke-width="2"/>')
    # Next.js N Logo Geometry
    svg.append(f'<g transform="translate({cx-36}, {cy-36})">')
    svg.append('<path d="M 16 16 L 16 56 M 56 16 L 56 46" stroke="#FFFFFF" stroke-width="7" stroke-linecap="round"/>')
    svg.append('<line x1="16" y1="16" x2="54" y2="56" stroke="url(#nextGrad)" stroke-width="7" stroke-linecap="round"/>')
    svg.append('</g>')
    svg.append(f'<text x="{cx}" y="{cy+54}" class="mono" font-size="14" font-weight="800" fill="#FFFFFF" text-anchor="middle" letter-spacing="1">NEXT.JS</text>')
    svg.append(f'<text x="{cx}" y="400" class="mono" font-size="9" font-weight="700" fill="{title_color}" text-anchor="middle" letter-spacing="1">RUNTIME // PRODUCTION_ENGINE</text>')
    svg.append(f'</g>')
    
    # ---------------- PHASE 3: REACT ATOMIC CORE ----------------
    svg.append(f'<g class="layer-react">')
    # Rotating React Atom Orbits
    svg.append(f'<g class="react-orbit-1">')
    svg.append(f'<ellipse cx="{cx}" cy="{cy}" rx="78" ry="28" fill="none" stroke="#61DAFB" stroke-width="2.2" stroke-dasharray="12 4"/>')
    svg.append(f'<circle cx="{cx+78}" cy="{cy}" r="4" fill="#61DAFB"/>')
    svg.append(f'</g>')
    svg.append(f'<g class="react-orbit-2">')
    svg.append(f'<ellipse cx="{cx}" cy="{cy}" rx="78" ry="28" fill="none" stroke="#61DAFB" stroke-width="2.2" transform="rotate(60 {cx} {cy})"/>')
    svg.append(f'<circle cx="{cx+39}" cy="{cy+67}" r="4" fill="#22D3EE"/>')
    svg.append(f'</g>')
    svg.append(f'<g class="react-orbit-3">')
    svg.append(f'<ellipse cx="{cx}" cy="{cy}" rx="78" ry="28" fill="none" stroke="#61DAFB" stroke-width="2.2" transform="rotate(120 {cx} {cy})"/>')
    svg.append(f'<circle cx="{cx-39}" cy="{cy+67}" r="4" fill="#61DAFB"/>')
    svg.append(f'</g>')
    # React Nucleus
    svg.append(f'<circle cx="{cx}" cy="{cy}" r="14" fill="#61DAFB" opacity="0.9"/>')
    svg.append(f'<circle cx="{cx}" cy="{cy}" r="8" fill="#FFFFFF"/>')
    svg.append(f'<text x="{cx}" y="{cy+54}" class="mono" font-size="14" font-weight="800" fill="#61DAFB" text-anchor="middle" letter-spacing="1">REACT.JS</text>')
    svg.append(f'<text x="{cx}" y="400" class="mono" font-size="9" font-weight="700" fill="{title_color}" text-anchor="middle" letter-spacing="1">FRONTEND // ATOMIC_CORE</text>')
    svg.append(f'</g>')
    
    # Bottom Status Pill on Left
    svg.append(f'<path d="M 28 416 L 28 424 L 36 424" fill="none" stroke="{title_color}" stroke-width="1" opacity="0.6"/>')
    svg.append(f'<path d="M 352 416 L 352 424 L 344 424" fill="none" stroke="{title_color}" stroke-width="1" opacity="0.6"/>')
    svg.append(f'<circle cx="44" cy="432" r="3" fill="{accent_emerald}"/>')
    svg.append(f'<text x="52" y="435" class="mono" font-size="9" font-weight="700" fill="{title_color}">PORTRAIT ➔ NEXT.JS ➔ REACT</text>')
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
