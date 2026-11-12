"""Native-resolution poses for the profile sprite. Coordinates are in source pixels."""

from PIL import Image, ImageDraw, ImageOps

CELL = (58, 68)
CENTER = 29
GROUND = 64
BASE_NAMES = ("front", "three-quarter", "side", "back", "walk-a", "walk-b", "walk-c")
ACTION_NAMES = ("idle", "wave", "think", "phone", "pocket", "look", "typing", "result", "celebrate")

INK = "#171317"
WINE = "#502e34"
WINE_LIGHT = "#633b42"
WINE_SHADE = "#322528"
SKIN = "#efa879"
SKIN_LIGHT = "#fac094"
TROUSERS = "#393437"
SHOE = "#f8eddf"
SOLE = "#b9a9a3"

# One foot moves back three pixels per frame during stance, compensating
# for the actor's forward motion. The opposite foot is four frames ahead.
STEP = 3
FOOT_X = (8, 5, 2, -1, -4, -7, -4, 2)
FOOT_LIFT = (0, 0, 0, 0, 0, 3, 7, 4)
BODY_Y = (0, 1, 0, -1, 0, 1, 0, -1)


def read_sheet(path, names, columns):
    width, height = CELL
    with Image.open(path) as source:
        sheet = source.convert("RGBA")
    frames = {}
    for i, name in enumerate(names):
        row, col = divmod(i, columns)
        left, top = col * width, row * height
        frames[name] = sheet.crop((left, top, left + width, top + height))
    return frames


def arm(draw, shoulder, elbow, hand, color, hand_color):
    draw.line((shoulder, elbow, hand), fill=INK, width=7, joint="curve")
    draw.line((shoulder, elbow, hand), fill=color, width=5, joint="curve")
    x, y = hand
    draw.rectangle((x - 2, y - 1, x + 2, y + 2), fill=INK)
    draw.rectangle((x - 1, y, x + 1, y + 1), fill=hand_color)


def leg(draw, hip, phase, near):
    shoe_x = CENTER + FOOT_X[phase]
    shoe_y = GROUND - 1 - FOOT_LIFT[phase]
    hip_x, hip_y = hip
    knee = ((hip_x + shoe_x) // 2 + (2 if FOOT_LIFT[phase] else 0), (hip_y + shoe_y) // 2)
    ankle = (shoe_x, shoe_y - 4)
    draw.line((hip, knee, ankle), fill=INK, width=9, joint="curve")
    draw.line((hip, knee, ankle), fill=TROUSERS if near else "#2c292d", width=7, joint="curve")
    draw.line((knee, ankle), fill="#494248" if near else "#393437", width=2)

    x, y = shoe_x, shoe_y
    draw.polygon([(x - 4, y), (x - 4, y - 4), (x + 1, y - 4), (x + 2, y - 3),
                  (x + 5, y - 2), (x + 5, y), (x + 4, y + 1), (x - 3, y + 1)], fill=INK)
    draw.rectangle((x - 3, y - 2, x + 4, y), fill=SHOE if near else "#d4c3b5")
    draw.line((x - 3, y, x + 4, y), fill=SOLE)
    draw.line((x - 1, y - 3, x + 1, y - 3), fill="#e8dacb")


def walk_pose(side, phase, settling=False):
    frame = Image.new("RGBA", CELL)
    draw = ImageDraw.Draw(frame)
    body_y = BODY_Y[phase] + (4 if settling else 0)
    near_arm = -FOOT_X[phase] // 2
    far_arm = -FOOT_X[(phase + 4) % 8] // 2

    arm(draw, (32, 32 + body_y), (32 + far_arm, 39 + body_y),
        (32 + far_arm * 2, 45 + body_y), WINE_SHADE, "#ab654a")
    leg(draw, (30, 44 + body_y), (phase + 4) % 8, near=False)
    leg(draw, (27, 44 + body_y), phase, near=True)

    # The original side-facing face, hair and collar are the same across the gait.
    body = side.crop((0, 0, CELL[0], 45))
    ImageDraw.Draw(body).rectangle((0, 33, 25, 44), fill=(0, 0, 0, 0))
    frame.alpha_composite(body, (0, body_y))
    draw = ImageDraw.Draw(frame)
    arm(draw, (27, 33 + body_y), (27 + near_arm, 39 + body_y),
        (27 + near_arm * 2, 46 + body_y), WINE, SKIN)
    return frame


def blink_pose(idle):
    frame = idle.copy()
    draw = ImageDraw.Draw(frame)
    for x in (23, 32):
        draw.rectangle((x, 18, x + 3, 21), fill=SKIN_LIGHT)
        draw.line((x, 20, x + 2, 20), fill=INK)
    return frame


def breathe_pose(idle):
    frame = idle.copy()
    head = idle.crop((0, 0, CELL[0], 28))
    ImageDraw.Draw(frame).rectangle((0, 0, CELL[0] - 1, 26), fill=(0, 0, 0, 0))
    frame.alpha_composite(head.crop((0, 1, CELL[0], 28)), (0, 0))
    return frame


def wave_pose(wave):
    frame = wave.copy()
    palm = wave.crop((11, 22, 19, 31))
    ImageDraw.Draw(frame).rectangle((11, 22, 18, 29), fill=(0, 0, 0, 0))
    frame.alpha_composite(palm, (10, 22))
    return frame


def idea_pose(think):
    frame = think.copy()
    draw = ImageDraw.Draw(frame)
    draw.polygon([(46, 8), (47, 10), (49, 11), (47, 12), (46, 14),
                  (45, 12), (43, 11), (45, 10)], fill="#cf936e")
    draw.point((46, 11), fill="#fff0cf")
    return frame


def phone_tap(phone):
    frame = phone.copy()
    ImageDraw.Draw(frame).line((37, 31, 39, 30), fill=SKIN_LIGHT, width=1)
    return frame


def laptop_pose(typing, opening):
    frame = typing.copy()
    draw = ImageDraw.Draw(frame)
    # Keep the seated pose and the workbench as the hinge moves.
    draw.rectangle((37, 36, 53, 46), fill=(0, 0, 0, 0))
    draw.line((34, 47, 47, 47), fill=INK, width=2)
    draw.line((35, 46, 46, 46), fill="#635963")
    if opening:
        draw.polygon([(36, 46), (42, 41), (50, 41), (47, 46)], fill=INK)
        draw.polygon([(39, 45), (43, 42), (48, 42), (46, 45)], fill="#494248")
    return frame


def typing_tap(typing):
    frame = typing.copy()
    draw = ImageDraw.Draw(frame)
    draw.line((30, 44, 33, 44), fill=SKIN_LIGHT)
    draw.line((33, 45, 35, 45), fill=SKIN)
    return frame


def build_poses(sprites):
    base = read_sheet(sprites / "base-poses.png", BASE_NAMES, 4)
    poses = read_sheet(sprites / "action-poses.png", ACTION_NAMES, 3)
    poses.update({
        "side": base["side"],
        "blink": blink_pose(poses["idle"]),
        "breathe": breathe_pose(poses["idle"]),
        "wave-left": wave_pose(poses["wave"]),
        "look-left": ImageOps.mirror(poses["look"]),
        "idea": idea_pose(poses["think"]),
        "phone-tap": phone_tap(poses["phone"]),
        "settle": walk_pose(base["side"], 2, settling=True),
        "laptop-closed": laptop_pose(poses["typing"], opening=False),
        "laptop-opening": laptop_pose(poses["typing"], opening=True),
        "typing-tap": typing_tap(poses["typing"]),
    })
    for phase in range(8):
        side = base["walk-a" if phase in (1, 2) else "walk-c" if phase in (5, 6) else "side"]
        frame = walk_pose(side, phase)
        poses[f"walk-{phase}"] = frame
        poses[f"walk-left-{phase}"] = ImageOps.mirror(frame)
    return poses
