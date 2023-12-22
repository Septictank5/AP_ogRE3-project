from Options import DefaultOnToggle, Range, Choice, PerGameCommonOptions


class RandomizeFun(DefaultOnToggle):
    """Randomizes weapons (+76 locations)"""
    display_name = "Randomize Fun"

resi3_options = {"enable fun": RandomizeFun}
