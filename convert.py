import json

def hex_to_rgb(hex_color):
    hex_color = hex_color.strip().lstrip("#")
    return tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))

with open("model.json", "r") as f:
    parts = json.load(f)

lines = [
    'local model = Instance.new("Model")',
    'model.Name = "VortexModel"',
    'model.Parent = workspace',
    '',
    'local parts = {'
]

for p in parts:
    pos = p["P"]
    rot = p["R"]
    size = p["S"]
    r, g, b = hex_to_rgb(p["C"])
    tr = p["Tr"]

    lines.append(
        f'\t{{P = Vector3.new({pos[0]}, {pos[1]}, {pos[2]}), '
        f'R = Vector3.new({rot[0]}, {rot[1]}, {rot[2]}), '
        f'S = Vector3.new({size[0]}, {size[1]}, {size[2]}), '
        f'C = Color3.fromRGB({r}, {g}, {b}), '
        f'Tr = {tr}}},'
    )

lines.extend([
    '}',
    '',
    'for _, data in ipairs(parts) do',
    '\tlocal part = Instance.new("Part")',
    '\tpart.Size = data.S',
    '\tpart.CFrame = CFrame.new(data.P) * CFrame.Angles(',
    '\t\tmath.rad(data.R.X),',
    '\t\tmath.rad(data.R.Y),',
    '\t\tmath.rad(data.R.Z)',
    '\t)',
    '\tpart.Color = data.C',
    '\tpart.Transparency = data.Tr',
    '\tpart.Anchored = true',
    '\tpart.TopSurface = Enum.SurfaceType.Studs',
    '\tpart.BottomSurface = Enum.SurfaceType.Studs',
    '\tpart.LeftSurface = Enum.SurfaceType.Studs',
    '\tpart.RightSurface = Enum.SurfaceType.Studs',
    '\tpart.FrontSurface = Enum.SurfaceType.Studs',
    '\tpart.BackSurface = Enum.SurfaceType.Studs',
    '\tpart.Parent = model',
    'end'
])

with open("output.txt", "w", newline="\n") as f:
    f.write("\n".join(lines))

print("copy output.txt into your roblox studio command bar, then run it for the model")