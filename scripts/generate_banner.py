#!/usr/bin/env python3
"""
Developer OS - Cyberpunk Workstation Hero Banner Generator
Features:
- Left Panel: Animated Cyber Dev Workspace featuring an ultra-unique animated artwork of
  a developer actively typing on his laptop with exactly 1 laptop and 1 extra vertical monitor,
  neon cyberpunk setup, animated cyber-scan laser, HUD corner reticles, and telemetry badges.
- Right Panel: Pristine SYSTEM.INFO Terminal Dashboard with skills, toolchain, and links.
"""

import os
import base64

def get_coder_gif_b64(gif_path="assets/coder_typing_opt.gif"):
    if not os.path.exists(gif_path):
        gif_path = "assets/coder_typing.gif"
    with open(gif_path, "rb") as f:
        return base64.b64encode(f.read()).decode("utf-8")

def generate_banner_svg(is_dark=True, output_path="assets/dark.svg"):
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    
    gif_b64 = get_coder_gif_b64("assets/coder_typing_opt.gif")
    
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
        badge_bg = "rgba(8, 9, 13, 0.85)"
        badge_border = "#30363D"
        badge_text = "#F0F6FC"
        hud_glow = "#22D3EE"
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
        badge_bg = "rgba(255, 255, 255, 0.88)"
        badge_border = "#CBD5E1"
        badge_text = "#0F172A"
        hud_glow = "#0284C7"

    svg = []
    svg.append('<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" viewBox="0 0 880 460" width="100%" height="100%">')
    
    svg.append(f"""
    <defs>
        <pattern id="gridPat" width="20" height="20" patternUnits="userSpaceOnUse">
            <path d="M 20 0 L 0 0 0 20" fill="none" stroke="{grid_line}" stroke-width="0.6" stroke-opacity="0.4"/>
        </pattern>
        <pattern id="scanlines" width="100" height="4" patternUnits="userSpaceOnUse">
            <line x1="0" y1="0" x2="100" y2="0" stroke="#000000" stroke-width="1.2" stroke-opacity="0.14"/>
        </pattern>
        <linearGradient id="cyberLaser" x1="0%" y1="0%" x2="100%" y2="0%">
            <stop offset="0%" stop-color="{title_color}" stop-opacity="0"/>
            <stop offset="20%" stop-color="{title_color}" stop-opacity="0.8"/>
            <stop offset="50%" stop-color="{accent_emerald}" stop-opacity="1"/>
            <stop offset="80%" stop-color="{title_color}" stop-opacity="0.8"/>
            <stop offset="100%" stop-color="{title_color}" stop-opacity="0"/>
        </linearGradient>
        <clipPath id="devSetupClip">
            <rect x="30" y="118" width="320" height="284" rx="8"/>
        </clipPath>
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
        
        @keyframes scanBeam {{
            0%   {{ transform: translateY(0px); opacity: 0.15; }}
            50%  {{ transform: translateY(280px); opacity: 0.85; }}
            100% {{ transform: translateY(0px); opacity: 0.15; }}
        }}
        
        .live-dot {{ animation: pulseLive 2s infinite ease-in-out; transform-origin: 818px 24px; }}
        .badge-dot {{ animation: pulseLive 2s infinite ease-in-out; transform-origin: 48px 383px; }}
        .scanline-beam {{ animation: scanBeam 4.5s infinite ease-in-out; }}
        
        @media (prefers-reduced-motion: reduce) {{
            .live-dot, .badge-dot, .scanline-beam {{ animation: none !important; }}
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
    
    # ==================== LEFT PANEL: ANIMATED CYBER DEV WORKSTATION ====================
    svg.append(f'<rect x="18" y="62" width="344" height="382" rx="10" fill="{card_bg}" stroke="{terminal_border}" stroke-width="1"/>')
    svg.append(f'<rect x="18" y="62" width="344" height="30" rx="10" fill="{pill_bg}"/>')
    svg.append(f'<line x1="18" y1="92" x2="362" y2="92" stroke="{terminal_border}" stroke-width="0.8"/>')
    svg.append(f'<text x="32" y="82" class="mono" font-size="11" font-weight="700" fill="{title_color}">[ DEV.WORKSPACE ]</text>')
    svg.append(f'<text x="348" y="82" class="mono" font-size="9" font-weight="600" fill="{accent_emerald}" text-anchor="end">CYBER.RIG // LIVE</text>')
    
    # Top HUD Indicators
    svg.append(f'<path d="M 28 108 L 28 100 L 36 100" fill="none" stroke="{title_color}" stroke-width="1.2" opacity="0.8"/>')
    svg.append(f'<text x="40" y="108" class="mono" font-size="8.5" fill="{text_label}">RIG: <tspan fill="{text_primary}" font-weight="600">1x LAPTOP + 1x MONITOR</tspan></text>')
    svg.append(f'<path d="M 352 108 L 352 100 L 344 100" fill="none" stroke="{title_color}" stroke-width="1.2" opacity="0.8"/>')
    svg.append(f'<text x="340" y="108" class="mono" font-size="8.5" font-weight="700" fill="{accent_emerald}" text-anchor="end">TYPING // ACTIVE</text>')
    
    # Image Frame Container with Border
    svg.append(f'<rect x="29" y="117" width="322" height="286" rx="9" fill="{card_bg}" stroke="{terminal_border}" stroke-width="1.2"/>')
    
    # Embedded Animated Typing Coder Artwork (1 Laptop + 1 Monitor)
    svg.append(f'<g clip-path="url(#devSetupClip)">')
    svg.append(f'  <image x="30" y="118" width="320" height="284" preserveAspectRatio="xMidYMid slice" href="data:image/gif;base64,{gif_b64}"/>')
    # Subtle CRT / Monitor Scanlines Texture Overlay
    svg.append(f'  <rect x="30" y="118" width="320" height="284" fill="url(#scanlines)" opacity="0.6"/>')
    # Animated Laser Scanning Beam
    svg.append(f'  <g class="scanline-beam">')
    svg.append(f'    <line x1="30" y1="118" x2="350" y2="118" stroke="url(#cyberLaser)" stroke-width="2.5"/>')
    svg.append(f'  </g>')
    svg.append(f'</g>')
    
    # Cyber Corner Reticles on top of image
    reticle_color = hud_glow
    # Top-Left Reticle
    svg.append(f'<path d="M 34 132 L 34 122 L 44 122" fill="none" stroke="{reticle_color}" stroke-width="2" stroke-linecap="round"/>')
    # Top-Right Reticle
    svg.append(f'<path d="M 346 132 L 346 122 L 336 122" fill="none" stroke="{reticle_color}" stroke-width="2" stroke-linecap="round"/>')
    # Bottom-Left Reticle
    svg.append(f'<path d="M 34 388 L 34 398 L 44 398" fill="none" stroke="{reticle_color}" stroke-width="2" stroke-linecap="round"/>')
    # Bottom-Right Reticle
    svg.append(f'<path d="M 346 388 L 346 398 L 336 398" fill="none" stroke="{reticle_color}" stroke-width="2" stroke-linecap="round"/>')
    
    # Glassmorphism Telemetry HUD Badges overlay on image
    svg.append(f'<rect x="38" y="372" width="138" height="22" rx="4" fill="{badge_bg}" stroke="{badge_border}" stroke-width="0.8"/>')
    svg.append(f'<circle class="badge-dot" cx="48" cy="383" r="3" fill="{accent_emerald}"/>')
    svg.append(f'<text x="56" y="386.5" class="mono" font-size="8" font-weight="700" fill="{badge_text}">SYNTH.RIG // NEON_CORE</text>')
    
    svg.append(f'<rect x="246" y="372" width="96" height="22" rx="4" fill="{badge_bg}" stroke="{badge_border}" stroke-width="0.8"/>')
    svg.append(f'<text x="294" y="386.5" class="mono" font-size="8" font-weight="700" fill="{title_color}" text-anchor="middle">TYPING: 120 WPM</text>')
    
    # Bottom Panel Footer
    svg.append(f'<line x1="18" y1="412" x2="362" y2="412" stroke="{terminal_border}" stroke-width="0.8"/>')
    svg.append(f'<path d="M 28 420 L 28 430 L 38 430" fill="none" stroke="{title_color}" stroke-width="1.2" opacity="0.6"/>')
    svg.append(f'<path d="M 352 420 L 352 430 L 342 430" fill="none" stroke="{title_color}" stroke-width="1.2" opacity="0.6"/>')
    
    svg.append(f'<circle cx="48" cy="427" r="3" fill="{accent_emerald}"/>')
    svg.append(f'<text x="56" y="430.5" class="mono" font-size="9" font-weight="700" fill="{title_color}">IDENTITY // ONKAR BEVINAKATTI</text>')
    svg.append(f'<text x="336" y="430.5" class="mono" font-size="9" font-weight="700" fill="{accent_emerald}" text-anchor="end">LIVE_DEV // 24/7</text>')

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
        ("ToolChain", "Git · VS Code · Linux · AWS · Postman", text_secondary, "500", True),
        
        ("Core.Lang", "TypeScript · Solidity · Python · C++ · JavaScript", text_primary, "500", False),
        ("Core.Frontend", "React · Next.js · React Native · Tailwind · Redux", title_color, "500", False),
        ("Core.Backend", "Node.js · Express · Ethers.js · REST APIs", text_primary, "500", False),
        ("Core.Database", "MongoDB · Redis · Supabase · Firebase", accent_emerald, "500", False),
        ("Core.Infra", "AWS · Vercel · Render · GitHub Actions", text_secondary, "500", True),
        
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
