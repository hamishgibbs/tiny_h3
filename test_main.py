from main import latLngToCell


def test_latLngToCell():

    res = latLngToCell(
        resolution=10,
        latitude=40.689167,
        longitude=-74.044444
    )

    assert res == b"8a2a1072b59ffff\n"
