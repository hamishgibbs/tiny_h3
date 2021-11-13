import subprocess


def latLngToCell(
        resolution: int,
        latitude: float,
        longitude: float,
        h3_exe: str = "h3/build/bin/latLngToCell"):

    res = subprocess.Popen([
        h3_exe,
        "--resolution",
        str(resolution),
        "--latitude",
        str(latitude),
        "--longitude",
        str(longitude)],
        stdout=subprocess.PIPE).communicate()

    # DEV: remove newline character here
    return res[0]


print(latLngToCell(10, 4, 6))
