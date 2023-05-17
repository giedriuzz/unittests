def kmi(svoris: int, ugis: float) -> float:
    kmi = svoris / (ugis * ugis)

    if kmi > 12 and kmi <= 100:
        return kmi
    if kmi <= 12 or kmi > 100:
        raise ValueError("BMI ton low or to big")


# print(kmi(20, 1.40))
