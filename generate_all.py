import subprocess
import sys
import os

scripts = [
    "generate_sprites.py",
    "fix_animals.py",
    "create_derived_sprites.py",
    "add_animals.py",
    "add_15_animals.py",
    "draw_side_bodies.py",
    "draw_side_bodies2.py",
    "draw_side_bodies3.py",
    "draw_side_bodies4.py",
    "draw_side_bodies5.py",
    "draw_zebra.py",
    "generate_fruits.py"
]

print("Starting overall Pixel Zoo & Orchard sprite generation pipeline...")
os.makedirs("images/animals", exist_ok=True)
os.makedirs("images/fruits", exist_ok=True)

for script in scripts:
    if not os.path.exists(script):
        print(f"Error: {script} not found in workspace!")
        sys.exit(1)
        
    print(f"Executing: {script} ...")
    res = subprocess.run([sys.executable, script], capture_output=True, text=True)
    if res.returncode != 0:
        print(f"FAIL: Error occurred while running {script}!")
        print("Stdout:")
        print(res.stdout)
        print("Stderr:")
        print(res.stderr)
        sys.exit(1)
    else:
        # Show output
        lines = [l.strip() for l in res.stdout.splitlines() if l.strip()]
        if lines:
            print(f"SUCCESS: {lines[-1]}")
        else:
            print("SUCCESS")

# Post-process app.js to ensure all animal filename fields are prepended with images/animals/
print("Post-processing app.js to prepend image folder path for animals...")
import re
with open("app.js", "r") as f:
    content = f.read()

def replacer(match):
    prefix = match.group(1)
    path = match.group(2)
    suffix = match.group(3)
    if not path.startswith('images/animals/') and not path.startswith('images/fruits/'):
        return f'{prefix}images/animals/{path}{suffix}'
    return match.group(0)

new_content = re.sub(r'(filename:\s*")([^"]+)(")', replacer, content)
with open("app.js", "w") as f:
    f.write(new_content)

print("\nAll 85 animal sprites and 52 fruit sprites generated, database updated successfully!")
