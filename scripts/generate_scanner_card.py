#!/usr/bin/env python3
"""
Generate a cybernetic Terminal HUD Resume Scanner SVG for GitHub README.
Encodes exact Google Drive link with terminal chassis, glowing laser line,
HUD corner brackets, and aligned metadata.
"""

import os
import base64
import qrcode
from io import BytesIO

def generate_scanner_svg(output_path="assets/resume_scanner.svg"):
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    
    resume_url = "https://drive.google.com/file/d/1tNLVWYCM9jyN3SjJYti5hJNV8vS5z_zY/view?usp=drivesdk"
    
    # Generate high-res QR code
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=8,
        border=3,
    )
    qr.add_data(resume_url)
    qr.make(fit=True)
    
    qr_img = qr.make_image(fill_color="#0D1117", back_color="#FFFFFF").convert("RGBA")
    
    buffer = BytesIO()
    qr_img.save(buffer, format="PNG")
    qr_b64 = base64.b64encode(buffer.getvalue()).decode("utf-8")
    
    svg = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 880 340" width="100%" height="100%">
    <defs>
        <linearGradient id="scanLaser" x1="0%" y1="0%" x2="100%" y2="0%">
            <stop offset="0%" stop-color="#22D3EE" stop-opacity="0.1"/>
            <stop offset="50%" stop-color="#22D3EE" stop-opacity="0.9"/>
            <stop offset="100%" stop-color="#22D3EE" stop-opacity="0.1"/>
        </linearGradient>
        <linearGradient id="btnGrad" x1="0%" y1="0%" x2="100%" y2="0%">
            <stop offset="0%" stop-color="#2563EB"/>
            <stop offset="100%" stop-color="#3B82F6"/>
        </linearGradient>
    </defs>
    
    <style><![CDATA[
        .mono {{ font-family: 'JetBrains Mono', 'Cascadia Code', ui-monospace, SFMono-Regular, Menlo, monospace; }}
        .sans {{ font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif; }}
        
        @keyframes laserSweep {{
            0%, 100% {{ transform: translateY(0px); opacity: 0.8; }}
            50% {{ transform: translateY(140px); opacity: 1; }}
        }}
        
        .laser-line {{
            animation: laserSweep 3s infinite ease-in-out;
        }}
    ]]></style>

    <!-- Outer Chassis -->
    <rect width="880" height="340" rx="12" fill="#08090D" stroke="#21262D" stroke-width="1.2"/>
    
    <!-- ==================== LEFT: TERMINAL QR HUD ==================== -->
    <g transform="translate(24, 20)">
        <!-- Terminal Box -->
        <rect width="250" height="300" rx="10" fill="#0F1117" stroke="#21262D" stroke-width="1"/>
        
        <!-- Terminal Header -->
        <circle cx="16" cy="18" r="4" fill="#FF5F56"/>
        <circle cx="28" cy="18" r="4" fill="#FFBD2E"/>
        <circle cx="40" cy="18" r="4" fill="#27C93F"/>
        <text x="54" y="22" class="mono" font-size="9" font-weight="700" fill="#22D3EE">RESUME.SCAN // CV_TELEMETRY</text>
        <line x1="0" y1="34" x2="250" y2="34" stroke="#21262D" stroke-width="0.8"/>
        
        <!-- QR Container -->
        <rect x="35" y="48" width="180" height="180" rx="8" fill="#FFFFFF"/>
        <image x="40" y="53" width="170" height="170" href="data:image/png;base64,{qr_b64}"/>
        
        <!-- HUD Target Brackets -->
        <!-- Top-Left -->
        <path d="M 28 65 L 28 42 L 51 42" fill="none" stroke="#22D3EE" stroke-width="2.5" stroke-linecap="round"/>
        <!-- Top-Right -->
        <path d="M 222 65 L 222 42 L 199 42" fill="none" stroke="#22D3EE" stroke-width="2.5" stroke-linecap="round"/>
        <!-- Bottom-Left -->
        <path d="M 28 211 L 28 234 L 51 234" fill="none" stroke="#22D3EE" stroke-width="2.5" stroke-linecap="round"/>
        <!-- Bottom-Right -->
        <path d="M 222 211 L 222 234 L 199 234" fill="none" stroke="#22D3EE" stroke-width="2.5" stroke-linecap="round"/>
        
        <!-- Laser Sweep Line -->
        <g class="laser-line">
            <line x1="38" y1="68" x2="212" y2="68" stroke="url(#scanLaser)" stroke-width="2.5"/>
        </g>
        
        <!-- Footer Caption -->
        <text x="125" y="258" class="mono" font-size="9.5" font-weight="700" fill="#F0F6FC" text-anchor="middle">SCAN WITH CAMERA OR CLICK TO OPEN</text>
        <text x="125" y="276" class="mono" font-size="8.5" fill="#6E7681" text-anchor="middle">Google Drive Verified // PDF v2026</text>
    </g>

    <!-- ==================== RIGHT: CREDENTIALS INFO ==================== -->
    <g transform="translate(300, 36)">
        <!-- Heading -->
        <text x="0" y="20" class="sans" font-size="16" font-weight="700" fill="#F0F6FC">
            <tspan fill="#F59E0B">⚡ </tspan>Instant CV Access // PDF Document
        </text>
        
        <text x="0" y="48" class="sans" font-size="12.5" fill="#8B949E">
            Point your smartphone camera at the scanner matrix or click below to view the
        </text>
        <text x="0" y="68" class="sans" font-size="12.5" fill="#8B949E">
            official verified resume on Google Drive.
        </text>
        
        <!-- Bullet Items -->
        <g transform="translate(0, 96)">
            <!-- Bullet 1 -->
            <circle cx="4" cy="4" r="2.5" fill="#22D3EE"/>
            <text x="16" y="8" class="sans" font-size="12.5" font-weight="700" fill="#F0F6FC">Current Role: <tspan font-weight="400" fill="#CBD5E1">Full Stack Developer Intern @ IIIT Dharwad Research Park</tspan></text>
            
            <!-- Bullet 2 -->
            <circle cx="4" cy="30" r="2.5" fill="#22D3EE"/>
            <text x="16" y="34" class="sans" font-size="12.5" font-weight="700" fill="#F0F6FC">Core Specialization: <tspan font-weight="400" fill="#CBD5E1">Full-Stack Web, React Native, AI-Assisted Backends</tspan></text>
            
            <!-- Bullet 3 -->
            <circle cx="4" cy="56" r="2.5" fill="#22D3EE"/>
            <text x="16" y="60" class="sans" font-size="12.5" font-weight="700" fill="#F0F6FC">Education: <tspan font-weight="400" fill="#CBD5E1">B.E. Computer Science &amp; Engineering (CGPA: 9.00 // 2027)</tspan></text>
            
            <!-- Bullet 4 -->
            <circle cx="4" cy="82" r="2.5" fill="#22D3EE"/>
            <text x="16" y="86" class="sans" font-size="12.5" font-weight="700" fill="#F0F6FC">Track Record: <tspan font-weight="400" fill="#CBD5E1">5 Industrial Internships · 2x Hackathon Winner</tspan></text>
        </g>
        
        <!-- CTA Button -->
        <g transform="translate(0, 222)">
            <rect width="310" height="42" rx="6" fill="url(#btnGrad)"/>
            <!-- Google Drive Triangle Logo -->
            <path d="M 22 28 L 30 14 L 38 28 Z" fill="none" stroke="#FFFFFF" stroke-width="2"/>
            <text x="46" y="26" class="mono" font-size="11.5" font-weight="700" fill="#FFFFFF">OPEN RESUME ON GOOGLE DRIVE</text>
        </g>
    </g>
</svg>"""
    
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(svg)
    print(f"[+] Generated {output_path}")

if __name__ == "__main__":
    generate_scanner_svg("assets/resume_scanner.svg")
