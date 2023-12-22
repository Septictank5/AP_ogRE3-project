from enum import IntEnum
from typing import NamedTuple
from BaseClasses import Item


class Resi3ItemCategory(IntEnum):
    DOCUMENT = 0
    TRASH = 1
    AMMO = 2
    GUNPOWDER = 3
    HEALTH = 4
    WEAPONPART = 5
    WEAPON = 6
    KEY_ITEM = 7
    GOAL_ITEM = 8


class Resi3Item(Item):
    game: str = "Resident Evil 3"

    @staticmethod
    def get_name_to_id() -> dict:
        return {item_data.name: id for id, item_data in enumerate(_all_items)}


class Resi3ItemData(NamedTuple):
    name: str
    code: int
    category: Resi3ItemCategory


_all_items = [Resi3ItemData(row[0], row[1], row[2]) for row in [
    ("Knife", 1, Resi3ItemCategory.WEAPON),
    ("Sigpro HG", 2, Resi3ItemCategory.WEAPON),
    ("Beretta HG", 3, Resi3ItemCategory.WEAPON),
    ("Benelli SG", 4, Resi3ItemCategory.WEAPON),
    ("S&W magnum", 5, Resi3ItemCategory.WEAPON),
    ("GL(burst)", 6, Resi3ItemCategory.WEAPON),
    ("GL(flame)", 7, Resi3ItemCategory.WEAPON),
    ("GL(acid)", 8, Resi3ItemCategory.WEAPON),
    ("GL(freeze)", 9, Resi3ItemCategory.WEAPON),
    ("Rocket Launcher", 10, Resi3ItemCategory.WEAPON),
    ("Gatling Gun", 11, Resi3ItemCategory.WEAPON),
    ("Mine Thrower", 12, Resi3ItemCategory.WEAPON),
    ("Sigpro HG(en)", 17, Resi3ItemCategory.WEAPON),
    ("Beretta HG(en)", 18, Resi3ItemCategory.WEAPON),
    ("Benelli SG(en)", 19, Resi3ItemCategory.WEAPON),
    ("HG bullets", 21, Resi3ItemCategory.AMMO),
    ("Magnum bullets", 22, Resi3ItemCategory.AMMO),
    ("SG shells", 23, Resi3ItemCategory.AMMO),
    ("GL rounds(burst)", 24, Resi3ItemCategory.AMMO),
    ("GL rounds(flame)", 25, Resi3ItemCategory.AMMO),
    ("GL rounds(acid)", 26, Resi3ItemCategory.AMMO),
    ("GL rounds(freeze)", 27, Resi3ItemCategory.AMMO),
    ("MineThrower rounds", 28, Resi3ItemCategory.AMMO),
    ("enhanced HG bullets", 30, Resi3ItemCategory.AMMO),
    ("enhanced SG shells", 31, Resi3ItemCategory.AMMO),
    ("First Aid Spray", 32, Resi3ItemCategory.HEALTH),
    ("Green Herb", 33, Resi3ItemCategory.HEALTH),
    ("Blue Herb", 34, Resi3ItemCategory.HEALTH),
    ("Red Herb", 35, Resi3ItemCategory.HEALTH),
    ("FAS box", 42, Resi3ItemCategory.HEALTH),
    ("Square Crank", 43, Resi3ItemCategory.KEY_ITEM),
    ("Jill's STARS Card", 47, Resi3ItemCategory.KEY_ITEM),
    ("Battery", 49, Resi3ItemCategory.KEY_ITEM),
    ("Fire Hook", 50, Resi3ItemCategory.KEY_ITEM),
    ("Power Cable", 51, Resi3ItemCategory.KEY_ITEM),
    ("Fuse", 52, Resi3ItemCategory.KEY_ITEM),
    ("Additive", 54, Resi3ItemCategory.KEY_ITEM),
    ("Brad's STARS Card", 56, Resi3ItemCategory.KEY_ITEM),
    ("Machine Oil", 57, Resi3ItemCategory.KEY_ITEM),
    ("Wrench", 60, Resi3ItemCategory.KEY_ITEM),
    ("Iron Pipe", 61, Resi3ItemCategory.KEY_ITEM),
    ("Fire Hose", 63, Resi3ItemCategory.KEY_ITEM),
    ("Tape Recorder", 64, Resi3ItemCategory.KEY_ITEM),
    ("Lighter Oil", 65, Resi3ItemCategory.KEY_ITEM),
    ("Lighter Case", 66, Resi3ItemCategory.KEY_ITEM),
    ("Green Gem", 68, Resi3ItemCategory.KEY_ITEM),
    ("Blue Gem", 69, Resi3ItemCategory.KEY_ITEM),
    ("Silver Gear", 77, Resi3ItemCategory.KEY_ITEM),
    ("Chronos Gear", 78, Resi3ItemCategory.KEY_ITEM),
    ("Bronze Book", 79, Resi3ItemCategory.KEY_ITEM),
    ("Bronze Compass", 80, Resi3ItemCategory.KEY_ITEM),
    ("Vaccine Base", 82, Resi3ItemCategory.KEY_ITEM),
    ("Vaccine", 85, Resi3ItemCategory.KEY_ITEM),
    ("Medium Base", 88, Resi3ItemCategory.KEY_ITEM),
    ("Eagle Parts A", 89, Resi3ItemCategory.WEAPONPART),
    ("Eagle Parts B", 90, Resi3ItemCategory.WEAPONPART),
    ("M37 Parts A", 91, Resi3ItemCategory.WEAPONPART),
    ("M37 Parts B", 92, Resi3ItemCategory.WEAPONPART),
    ("Chronos Chain", 94, Resi3ItemCategory.KEY_ITEM),
    ("Rusted Crank", 95, Resi3ItemCategory.KEY_ITEM),
    ("Card Key", 96, Resi3ItemCategory.GOAL_ITEM),
    ("GunPowder A", 97, Resi3ItemCategory.GUNPOWDER),
    ("GunPowder B", 98, Resi3ItemCategory.GUNPOWDER),
    ("GunPowder C", 99, Resi3ItemCategory.GUNPOWDER),
    ("Water Sample", 111, Resi3ItemCategory.KEY_ITEM),
    ("System Disk", 112, Resi3ItemCategory.KEY_ITEM),
    ("Lockpick", 114, Resi3ItemCategory.KEY_ITEM),
    ("Warehouse Key (BackDoor)", 115, Resi3ItemCategory.KEY_ITEM),
    ("Sickroom Key", 116, Resi3ItemCategory.KEY_ITEM),
    ("Emblem Key", 117, Resi3ItemCategory.KEY_ITEM),
    ("Clock Tower Key(Winder)", 120, Resi3ItemCategory.KEY_ITEM),
    ("Park Key(front)", 123, Resi3ItemCategory.KEY_ITEM),
    ("Park Key(Graveyard)", 124, Resi3ItemCategory.KEY_ITEM),
    ("Park Key(Rear)", 125, Resi3ItemCategory.KEY_ITEM),
    ("Facility Key(no barcode)", 126, Resi3ItemCategory.KEY_ITEM),
    ("Facility Key(barcode)", 127, Resi3ItemCategory.KEY_ITEM),
    ("Ink Ribbon", 129, Resi3ItemCategory.TRASH),
    ("DOCUMENT", 130, Resi3ItemCategory.TRASH),
]]

item_dict = {item_data.name: item_data for item_data in _all_items}
