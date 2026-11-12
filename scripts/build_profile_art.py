"""Render the README animation, its still alternative and the editable pose atlas."""

from base64 import b64encode
from dataclasses import dataclass
from io import BytesIO
import json
from pathlib import Path

from PIL import Image, ImageDraw

from sprite_poses import CELL, CENTER, GROUND, STEP, build_poses

ROOT = Path(__file__).resolve().parents[1]
ASSETS = ROOT / "assets"
SPRITES = ASSETS / "pixel-character/sprites"
ANIMATIONS = ASSETS / "pixel-character/animations"
BRANDING = ASSETS / "branding"
SCENE = (384, 134)
SCALE = 2
FLOOR = 112
DESK_X = 305
DESK_POSES = {"laptop-closed", "laptop-opening", "typing", "typing-tap", "result"}


@dataclass(frozen=True)
class Cel:
    pose: str
    x: int
    milliseconds: int


def hold(x, *poses):
    return [Cel(name, x, milliseconds) for name, milliseconds in poses]


def walk(start, end):
    step = STEP if end > start else -STEP
    prefix = "walk" if step > 0 else "walk-left"
    return [
        Cel(f"{prefix}-{index % 8}", x, 100)
        for index, x in enumerate(range(start + step, end + step, step))
    ]


def storyboard():
    return [
        *hold(74, ("idle", 850), ("breathe", 450)),
        *walk(74, 134),
        *hold(134, ("look", 720), ("look-left", 700), ("think", 1150), ("idea", 850)),
        *walk(134, 215),
        *hold(215, ("pocket", 420), ("phone", 1250), ("phone-tap", 180),
              ("phone", 900), ("pocket", 420), ("side", 240)),
        *walk(215, DESK_X),
        *hold(DESK_X, ("settle", 180), ("laptop-closed", 380), ("laptop-opening", 200)),
        *hold(DESK_X, *([("typing", 370), ("typing-tap", 170)] * 6)),
        *hold(DESK_X, ("result", 1400), ("laptop-opening", 240), ("laptop-closed", 360),
              ("settle", 190), ("celebrate", 690), ("idle", 350)),
        *walk(DESK_X, 152),
        *hold(152, ("idle", 260), ("wave", 340), ("wave-left", 240),
              ("wave", 320), ("wave-left", 240), ("wave", 530),
              ("idle", 920), ("blink", 100), ("breathe", 670)),
        *walk(152, 74),
        *hold(74, ("idle", 750), ("blink", 100)),
    ]


def room():
    art = Image.new("RGB", SCENE, "#201a27")
    draw = ImageDraw.Draw(art)
    draw.rectangle((2, 2, 381, 111), fill="#2c2333")
    draw.rectangle((3, 3, 380, 12), fill="#312637")
    draw.line((3, 13, 380, 13), fill="#422f40")
    draw.rectangle((3, 96, 380, 111), fill="#28212f")
    draw.line((3, 106, 380, 106), fill="#4e3945")
    draw.line((3, 109, 380, 109), fill="#1a1721")

    # Window with a sunset cityscape and a muted crescent.
    draw.rectangle((109, 16, 286, 94), fill="#160f1c")
    draw.rectangle((112, 19, 283, 91), fill="#6b526b")
    draw.rectangle((115, 21, 280, 87), fill="#42364f")
    for top, bottom, color in ((25, 40, "#493950"), (41, 51, "#574157"),
                               (52, 62, "#69485f"), (63, 72, "#815568"),
                               (73, 87, "#8f6070")):
        draw.rectangle((115, top, 280, bottom), fill=color)
    draw.polygon([(215, 29), (224, 29), (228, 33), (228, 40), (224, 44),
                  (215, 44), (211, 40), (211, 33)], fill="#dfb59c")
    draw.polygon([(218, 28), (226, 28), (230, 32), (230, 37), (226, 40),
                  (220, 40), (216, 36), (216, 31)], fill="#493950")
    for x, y in ((128, 30), (139, 43), (161, 31), (192, 48), (201, 28),
                 (244, 34), (254, 49), (269, 28)):
        draw.point((x, y), fill="#bd8b9a")
    draw.line((125, 54, 151, 54), fill="#946276")
    draw.line((235, 56, 264, 56), fill="#aa7482")
    draw.line((169, 62, 198, 62), fill="#a77483")
    for x, top, width in ((116, 70, 13), (130, 66, 14), (146, 74, 12), (160, 69, 20),
                          (182, 76, 13), (198, 70, 12), (214, 65, 20), (237, 73, 14),
                          (253, 66, 11), (267, 71, 13)):
        draw.rectangle((x, top, x + width - 1, 87), fill="#4c3b51")
        draw.line((x + 2, top + 3, x + width - 3, top + 3), fill="#61495e")
    for x, top, width in ((118, 77, 14), (135, 81, 12), (150, 76, 18), (173, 79, 12),
                          (188, 82, 12), (204, 74, 18), (226, 79, 11), (239, 77, 15),
                          (257, 80, 12), (272, 75, 8)):
        draw.rectangle((x, top, x + width - 1, 88), fill="#302739")
        for light in range(x + 3, x + width - 1, 5):
            draw.point((light, top + 4), fill="#c3937d")
            if top < 78:
                draw.point((light, top + 8), fill="#835c71")
    for x in (169, 225):
        draw.rectangle((x, 20, x + 2, 89), fill="#322638")
        draw.line((x + 2, 20, x + 2, 89), fill="#9c7086")
    draw.rectangle((112, 89, 283, 91), fill="#503647")
    draw.line((112, 92, 283, 92), fill="#886276")

    # Left doorway, amber task light, and storage.
    draw.rectangle((16, 23, 61, 111), fill="#17131c")
    draw.rectangle((19, 26, 58, 111), fill="#4e3545")
    draw.rectangle((22, 29, 55, 110), fill="#291f2e")
    draw.rectangle((26, 35, 51, 75), fill="#67475b")
    draw.rectangle((28, 37, 49, 73), fill="#402e43")
    draw.line((40, 37, 40, 73), fill="#725465")
    draw.line((28, 57, 49, 57), fill="#725465")
    draw.rectangle((45, 87, 50, 88), fill="#bc906f")
    draw.line((22, 107, 55, 107), fill="#593c4b")
    draw.rectangle((67, 31, 95, 33), fill="#473240")
    draw.polygon([(74, 34), (87, 34), (93, 39), (93, 43), (68, 43), (68, 39)], fill="#865866")
    draw.line((70, 43, 91, 43), fill="#dca689")
    draw.rectangle((77, 44, 84, 45), fill="#f0c3a2")
    draw.rectangle((66, 76, 100, 79), fill="#18131d")
    draw.line((66, 76, 100, 76), fill="#92626d")
    for x, y, color in ((70, 66, "#9b6c7b"), (75, 63, "#6a657e"),
                         (80, 68, "#ae7a64"), (85, 65, "#654d68")):
        draw.rectangle((x, y, x + 3, 75), fill=color)
        draw.point((x + 1, y + 2), fill="#c49889")

    # A tiny terminal and a shelf above the workstation.
    draw.rectangle((304, 22, 360, 48), fill="#1a1521")
    draw.rectangle((306, 24, 358, 46), fill="#6e526a")
    draw.rectangle((308, 26, 356, 44), fill="#262031")
    draw.line([(312, 30), (315, 32), (312, 34)], fill="#d8a58e")
    draw.line((318, 34, 323, 34), fill="#d8a58e")
    for x, y, width, color in ((327, 31, 21, "#73586f"), (315, 38, 12, "#94758c"),
                               (331, 38, 14, "#664b68"), (348, 38, 5, "#9c6375")):
        draw.line((x, y, x + width, y), fill=color)
    draw.rectangle((309, 63, 369, 66), fill="#1a1521")
    draw.line((309, 63, 369, 63), fill="#a27178")
    draw.rectangle((314, 56, 326, 62), fill="#584258")
    draw.line((314, 56, 326, 56), fill="#8c6f83")
    draw.rectangle((330, 52, 339, 62), fill="#684354")
    draw.line((330, 53, 339, 53), fill="#ad7f85")
    draw.polygon([(356, 56), (367, 56), (365, 62), (358, 62)], fill="#a17270")
    for points in ([(362, 56), (360, 51), (357, 50)], [(362, 56), (363, 49), (366, 47)],
                   [(364, 55), (368, 52), (370, 52)]):
        draw.line(points, fill="#9aa58c", width=2)

    draw.rectangle((2, FLOOR, 381, 130), fill="#29232f")
    draw.line((2, FLOOR, 381, FLOOR), fill="#ad7b7d")
    draw.line((2, FLOOR + 1, 381, FLOOR + 1), fill="#6e505f")
    draw.line((2, 120, 381, 120), fill="#372a3b")
    draw.line((2, 130, 381, 130), fill="#493546")
    for x in range(10, 382, 30):
        draw.line((x, 121, x + 7, 129), fill="#362a39")
    draw.rectangle((0, 0, 383, 133), outline="#72546c")
    draw.rectangle((1, 1, 382, 132), outline="#1a1521")
    return art.convert("RGBA")


def empty_desk():
    props = Image.new("RGBA", CELL)
    draw = ImageDraw.Draw(props)
    draw.rectangle((30, 48, 51, 51), fill="#1c141b")
    draw.line((31, 49, 50, 49), fill="#996752")
    for x in (34, 45):
        draw.rectangle((x, 51, x + 3, 63), fill="#1c141b")
        draw.line((x + 1, 51, x + 1, 62), fill="#855340")
    draw.line((35, 47, 47, 47), fill="#635963", width=2)
    draw.rectangle((12, 52, 22, 54), fill="#1c141b")
    draw.line((13, 53, 21, 53), fill="#996752")
    for x in (13, 20):
        draw.rectangle((x, 54, x + 2, 63), fill="#1c141b")
        draw.line((x + 1, 55, x + 1, 62), fill="#855340")
    draw.line((14, 59, 21, 59), fill="#855340")
    return props


def render_frame(backdrop, desk, poses, cel):
    scene = backdrop.copy()
    if cel.pose not in DESK_POSES:
        scene.alpha_composite(desk, (DESK_X - CENTER, FLOOR - GROUND))
    shadow = ImageDraw.Draw(scene)
    shadow.line((cel.x - 10, FLOOR + 1, cel.x + 10, FLOOR + 1), fill="#442f3c")
    scene.alpha_composite(poses[cel.pose], (cel.x - CENTER, FLOOR - GROUND))
    return scene.convert("RGB")


def scale_up(image):
    return image.resize((image.width * SCALE, image.height * SCALE), Image.Resampling.NEAREST)


def gif_frames(frames):
    # Use one deterministic palette across frames, with no temporal dithering.
    colors = sorted({color for frame in frames for _, color in frame.getcolors(maxcolors=frame.width * frame.height)})
    if len(colors) > 255:
        raise ValueError(f"GIF palette has {len(colors)} colors, leaving no transparency index")
    transparent_color = next((0, 0, blue) for blue in range(256) if (0, 0, blue) not in colors)
    palette_data = bytes(channel for color in (*colors, transparent_color) for channel in color)
    indices = {color: index for index, color in enumerate(colors)}
    indexed = []
    for frame in frames:
        exact = Image.new("P", frame.size)
        exact.putpalette(palette_data)
        exact.putdata([indices[color] for color in frame.get_flattened_data()])
        indexed.append(scale_up(exact))
    return indexed, palette_data, len(colors)


def export_atlas(poses):
    columns = 8
    width, height = CELL
    rows = (len(poses) + columns - 1) // columns
    atlas = Image.new("RGBA", (columns * width, rows * height))
    index = {}
    for i, (name, frame) in enumerate(poses.items()):
        row, col = divmod(i, columns)
        x, y = col * width, row * height
        atlas.alpha_composite(frame, (x, y))
        index[name] = {"x": x, "y": y}
    atlas.save(SPRITES / "atlas.png", optimize=True)
    manifest = {"width": width, "height": height, "anchor": [CENTER, GROUND], "poses": index}
    (SPRITES / "atlas.json").write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")
    return atlas, manifest


def data_png(image):
    buffer = BytesIO()
    image.save(buffer, format="PNG", optimize=True)
    return "data:image/png;base64," + b64encode(buffer.getvalue()).decode("ascii")


def export_preview(timeline, atlas, manifest, backdrop, desk):
    chapters = (
        ("walk", "walk-0", "look"),
        ("look", "look", "pocket"),
        ("phone", "pocket", "side"),
        ("code", "settle", "walk-left-0"),
        ("wave", "wave", "walk-left-0"),
    )
    actions = {"all": [0, len(timeline)]}
    for name, start_pose, end_pose in chapters:
        start = next(i for i, cel in enumerate(timeline) if cel.pose == start_pose)
        end = next(i for i in range(start + 1, len(timeline)) if timeline[i].pose == end_pose)
        actions[name] = [start, end]
    data = {
        "atlas": manifest, "spritePng": data_png(atlas), "roomPng": data_png(backdrop),
        "deskPng": data_png(desk), "floor": FLOOR, "deskX": DESK_X,
        "deskPoses": sorted(DESK_POSES), "actions": actions,
        "frames": [[cel.pose, cel.x, cel.milliseconds] for cel in timeline],
    }
    template = (ROOT / "scripts/estudio.template.html").read_text(encoding="utf-8")
    page = template.replace("<!--ART_DATA-->", json.dumps(data, separators=(",", ":")))
    (ROOT / "docs/estudio.html").write_text(page, encoding="utf-8")


def main():
    poses = build_poses(SPRITES)
    timeline = storyboard()
    backdrop = room()
    desk = empty_desk()
    frames = [render_frame(backdrop, desk, poses, cel) for cel in timeline]
    scale_up(frames[0]).save(BRANDING / "studio.png", optimize=True)
    gif, palette, transparency = gif_frames(frames)
    gif[0].save(ANIMATIONS / "studio.gif", save_all=True, append_images=gif[1:], loop=0,
                duration=[cel.milliseconds for cel in timeline], disposal=1, optimize=True,
                palette=palette, transparency=transparency)
    wave = poses["wave"].crop(poses["wave"].getbbox())
    scale_up(wave).save(SPRITES / "wave.png", optimize=True)
    atlas, manifest = export_atlas(poses)
    export_preview(timeline, atlas, manifest, backdrop, desk)


if __name__ == "__main__":
    main()
