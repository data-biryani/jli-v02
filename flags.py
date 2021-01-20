import attr

@attr.s
class Flags:
    judge: str = False
    judgment: str = False
    text: bool = False
