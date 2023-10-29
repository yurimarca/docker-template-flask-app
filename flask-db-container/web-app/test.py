with open('requirements.txt', 'r') as f:
    lines = f.readlines()

with open('requirements_pip.txt', 'w') as f:
    for line in lines:
        # Skip lines with comments or platform info
        if line.startswith("#") or line.startswith("platform:"):
            continue

        # Process each package line
        if "=" in line:
            parts = line.strip().split("=")
            if len(parts) == 3:  # Conda format with channel
                package, version, _ = parts
                f.write(f"{package}=={version}\n")
            elif len(parts) == 2:  # Conda format without channel
                package, version = parts
                f.write(f"{package}=={version}\n")
