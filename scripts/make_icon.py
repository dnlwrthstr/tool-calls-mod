"""Draw the plugin icon: .claude-plugin/icon.png (512x512 PNG).

Usage (needs Pillow):
    python3 scripts/make_icon.py .claude-plugin/icon.png
"""
import sys
from PIL import Image, ImageDraw
out = sys.argv[1]
N = 2048  # draw large, downsample for smooth edges
img = Image.new("RGBA", (N, N), (0, 0, 0, 0))
d = ImageDraw.Draw(img)
s = N / 512
def R(*v): return [x * s for x in v]
# background tile
d.rounded_rectangle(R(16, 16, 496, 496), radius=96 * s, fill=(28, 30, 38, 255))
# pane frame with title bar
d.rounded_rectangle(R(84, 92, 428, 420), radius=28 * s, fill=(40, 43, 54, 255), outline=(84, 90, 110, 255), width=int(6 * s))
d.rounded_rectangle(R(84, 92, 428, 148), radius=28 * s, fill=(58, 62, 78, 255))
d.rectangle(R(87, 128, 425, 148), fill=(58, 62, 78, 255))
for i, c in enumerate([(240, 110, 90), (240, 190, 80), (110, 200, 120)]):
    x = 116 + i * 30
    d.ellipse(R(x - 8, 112, x + 8, 128), fill=c + (255,))
# rows: three done (dim, check), one running (bright, accent dot)
rows = [(186, 220, False), (240, 180, False), (294, 240, False), (348, 200, True)]
for y, w, running in rows:
    if running:
        d.ellipse(R(116, y - 14, 144, y + 14), fill=(217, 119, 87, 255))
        d.rounded_rectangle(R(166, y - 12, 166 + w, y + 12), radius=12 * s, fill=(236, 238, 244, 255))
    else:
        d.line(R(116, y, 126, y + 10, 144, y - 10), fill=(110, 200, 120, 255), width=int(7 * s), joint="curve")
        d.rounded_rectangle(R(166, y - 10, 166 + w, y + 10), radius=10 * s, fill=(110, 116, 136, 255))
img.resize((512, 512), Image.LANCZOS).save(out, optimize=True)
