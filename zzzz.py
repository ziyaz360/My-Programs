def MinBoots(trail, boots):
    BootChange = 0
    WearingBoot = 0
    for surface in trail:
        if surface > boots[WearingBoot]:
            WearingBoot += 1
            BootChange += 1
            if WearingBoot >= len(boots):
                return -1
    return BootChange
trail = [3, 2, 1]
boots = [4, 5, 3]
OP = MinBoots(trail, boots)
print(OP)
