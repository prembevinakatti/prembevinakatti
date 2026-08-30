#!/usr/bin/env python3
"""
Generate a 5-Card Telemetry Metrics Status Bar SVG for GitHub README.
Cards:
1. EXPERIENCE: 1.5+ YRS / 5 Internships Completed (Cyan)
2. ACADEMICS: 9.00 CGPA / B.E. Computer Science (Emerald)
3. HACKATHONS: 2x WINNER / Top 10 in 800+ Teams (Purple)
4. PORTFOLIO: 40+ BUILT / Full-Stack & Mobile Apps (Blue/Cyan)
5. DISPATCH: PRODUCTION / Ready to Build & Scale (Amber)
"""

import os

def generate_metrics_svg(output_path="assets/metrics_bar.svg"):
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    
    # 5 Cards across 880 width -> card width 164, gap 15
    cards = [
        {
            "tag": "EXPERIENCE",
            "dot": "#22D3EE",
            "val": "1.5+ YRS",
            "val_color": "#22D3EE",
            "sub": "5 Internships Completed",
            "border": "#0891B2",
            "hud": "#22D3EE"
        },
        {
            "tag": "ACADEMICS",
            "dot": "#10B981",
            "val": "9.00 CGPA",
            "val_color": "#10B981",
            "sub": "B.E. Computer Science",
            "border": "#059669",
            "hud": "#10B981"
        },
        {
            "tag": "HACKATHONS",
            "dot": "#A78BFA",
            "val": "2x WINNER",
            "val_color": "#A78BFA",
            "sub": "Top 10 in 800+ Teams",
            "border": "#7C3AED",
            "hud": "#A78BFA"
        },
        {
            "tag": "PORTFOLIO",
            "dot": "#38BDF8",
            "val": "40+ BUILT",
            "val_color": "#38BDF8",
            "sub": "Full-Stack &amp; Mobile Apps",
            "border": "#0284C7",
            "hud": "#38BDF8"
        },
        {
            "tag": "DISPATCH",
            "dot": "#F59E0B",
            "val": "PRODUCTION",
            "val_color": "#F59E0B",
            "sub": "Ready to Build &amp; Scale",
            "border": "#D97706",
            "hud": "#F59E0B"
        },
    ]
    
    card_w = 164
    card_h = 78
    gap = 15
    
    svg_parts = []
    svg_parts.append('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 880 84" width="100%" height="100%">')
    svg_parts.append("""
    <style><![CDATA[
        .mono { font-family: 'JetBrains Mono', 'Cascadia Code', ui-monospace, SFMono-Regular, Menlo, monospace; }
        .sans { font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif; }
    ]]></style>
    """)
    
    for i, c in enumerate(cards):
        x = i * (card_w + gap)
        y = 3
        
        # Base Card Chassis
        svg_parts.append(f'<rect x="{x}" y="{y}" width="{card_w}" height="{card_h}" rx="7" fill="#0D1117" stroke="#21262D" stroke-width="1"/>')
        
        # Top Accent Header Bar Line
        svg_parts.append(f'<line x1="{x+1}" y1="{y+19}" x2="{x+card_w-1}" y2="{y+19}" stroke="{c["border"]}" stroke-width="1.2" opacity="0.85"/>')
        
        # Tag Dot & Header Label
        svg_parts.append(f'<circle cx="{x+12}" cy="{y+10}" r="3" fill="{c["dot"]}"/>')
        svg_parts.append(f'<text x="{x+20}" y="{y+13}" class="mono" font-size="9" font-weight="700" fill="#94A3B8" letter-spacing="0.5">{c["tag"]}</text>')
        
        # HUD Corner Brackets
        bracket_len = 6
        # Top-Left HUD
        svg_parts.append(f'<path d="M {x+5} {y+28} L {x+5} {y+24} L {x+5+bracket_len} {y+24}" fill="none" stroke="{c["hud"]}" stroke-width="1.2" opacity="0.9"/>')
        # Bottom-Right HUD
        svg_parts.append(f'<path d="M {x+card_w-5} {y+card_h-8} L {x+card_w-5} {y+card_h-4} L {x+card_w-5-bracket_len} {y+card_h-4}" fill="none" stroke="{c["hud"]}" stroke-width="1.2" opacity="0.9"/>')
        
        # Metric Value
        svg_parts.append(f'<text x="{x+12}" y="{y+44}" class="sans" font-size="16" font-weight="800" fill="{c["val_color"]}">{c["val"]}</text>')
        
        # Subtitle
        svg_parts.append(f'<text x="{x+12}" y="{y+63}" class="sans" font-size="9.5" font-weight="500" fill="#8B949E">{c["sub"]}</text>')
        
    svg_parts.append('</svg>')
    
    with open(output_path, "w", encoding="utf-8") as f:
        f.write("\n".join(svg_parts))
    print(f"[+] Generated {output_path}")

if __name__ == "__main__":
    generate_metrics_svg("assets/metrics_bar.svg")
