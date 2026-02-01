import os

project_structure = {
    "docs": ["problem-statement.md", "system-architecture.md", "gas-analysis.md", "roadmap.md"],
    "hardware": ["components-list.md", "circuit-diagram.png", "sensor-details.md"],
    "firmware/esp32": ["main.ino"],
    "firmware/arduino": ["main.ino"],
    "cloud": ["api-design.md", "dashboard-ui.md"],
    "images": ["system-block-diagram.png", "flowchart.png"],
}

root_files = ["README.md", "LICENSE"]

for folder, files in project_structure.items():
    os.makedirs(folder, exist_ok=True)
    for f in files:
        path = os.path.join(folder, f)
        if not os.path.exists(path):
            open(path, 'a').close()

for f in root_files:
    if not os.path.exists(f):
        open(f, 'a').close()
