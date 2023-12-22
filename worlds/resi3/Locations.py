from enum import IntEnum
from typing import Optional, NamedTuple, Dict
from BaseClasses import Location, Region


class Resi3LocationCategory(IntEnum):
    PICKUP = 0
    NPC = 1
    NEMESIS = 2


class Resi3LocationData(NamedTuple):
    name: str
    default_item: str
    category: Resi3LocationCategory


class Resi3Location(Location):
    game: str = "Resident Evil 3"
    category: Resi3LocationCategory
    default_item_name: str

    def __init__(
            self,
            player: int,
            name: str,
            address: Optional[int] = None,
            parent: Optional[Region] = None):
        super().__init__(player, name, address, parent)

    room_table = [
        "Warehouse",
        "Trailer",
        "Basement Alley",
        "Bar Jack Street",
        "Bar Jack",
        "Barricade Alley",
        "Alleyway Outside Pharmacy",
        "Hydrant Save",
        "Back Alley",
        "RPD Front",
        "RPD Hall",
        "RPD Big Office",
        "RPD Evidence Room",
        "RPD Stairs 1F",
        "RPD Corridor",
        "RPD Meeting Room",
        "RPD Dark Room",
        "RPD Stairs 2F",
        "RPD STARS Corridor",
        "STARS Office",
        "Pharmacy Room 1",
        "Pharmacy Room 2",
        "Warehouse Alley 2",
        "Warehouse Street 2",
        "Bar Jack Alley 2",
        "Bar Jack Alley Loot",
        "Hydrant Alley 2",
        "RPD Street 2",
        "Bus Street",
        "Parking Lot",
        "Parking Lot Back",
        "Construction Site",
        "Power Station Front",
        "Restaurant Front",
        "Shopping Alley",
        "Press Street",
        "Municipal Alley",
        "Party Alley",
        "Grave Digger Alley",
        "Train Station",
        "Cable Car",
        "Stagla Gas",
        "Stagla Gas Outside",
        "Press Offices",
        "Press Entrance",
        "Restaurant",
        "Restaurant Basement",
        "Power Station Access",
        "Power Station",
        "Cable Car Moving",
        "Shopping Save",
        "Stagla Escape",
        "Fire Hose Alley",
        "Press Entrance 2",
        "Parasite Alley",
        "Parking Lot Save",
        "ClockTower Chapel",
        "ClockTower Piano Room",
        "ClockTower Dining Room",
        "ClockTower Outdoor",
        "ClockTower Hall 1F",
        "ClockTower Bedroom",
        "ClockTower Chess Room",
        "ClockTower Library",
        "Chronos Corridor",
        "ClockTower Hall 2F",
        "Tower Outdoor",
        "ClockTower",
        "Chronos Room 2",
        "ClockTower Piano Room 2",
        "Hospital Street",
        "Office Save",
        "Hospital Hall",
        "Reception",
        "Staff Room",
        "4F Corridor",
        "Room 402",
        "Room 401",
        "Data Room",
        "B3 Corridor",
        "Laboratory",
        "Synthesis Room",
        "Park Entrance",
        "Fountain Room",
        "Lake Passageway",
        "Factory Approach",
        "Fountain Tunnel",
        "Graveyard",
        "Graveyard Cabin",
        "Graveyard Save",
        "Graveyard Secret",
        "Factory 1F",
        "Factory Path",
        "Factory Save 1F",
        "Boiler Room",
        "Treatment Control",
        "Factory B1",
        "Factory B1 Save",
        "Water Puzzle",
        "Toxic Pool Room",
        "Disposal Access",
        "Disposal Chamber",
        "Communications Room",
        "Hatch Escape Path",
        "Car Cemetary",
        "Chopper Departure",
    ]

    @staticmethod
    def get_name_to_id() -> dict:
        base_id = 100000
        offset = 100
        output = {}

        for index, roomname in enumerate(Resi3Location.room_table):
            output.update({location.name: ID for ID, location in enumerate(location_tables[roomname],
                                                                           base_id + index * offset)})

        return output


location_tables = {
    "Warehouse": [
        Resi3LocationData("R101-204: First Aid Spray", "First Aid Spray", Resi3LocationCategory.PICKUP),
        Resi3LocationData("R101-242: HG bullets", "Warehouse Key (BackDoor)", Resi3LocationCategory.PICKUP),
        ],
    "Trailer": [
        Resi3LocationData("R101-914: GunPowder A", "GunPowder A", Resi3LocationCategory.PICKUP),
        Resi3LocationData("R101-976: GunPowder A", "GunPowder A", Resi3LocationCategory.PICKUP),
        Resi3LocationData("R101-1038: GunPowder B", "GunPowder B", Resi3LocationCategory.PICKUP),
        Resi3LocationData("R101-1100: GunPowder B", "GunPowder B", Resi3LocationCategory.PICKUP),
        Resi3LocationData("R101-1162: DOCUMENT", "DOCUMENT", Resi3LocationCategory.PICKUP),
    ],
    "Basement Alley": [
        Resi3LocationData("R104-526: Green Herb", "Green Herb", Resi3LocationCategory.PICKUP),
        Resi3LocationData("R104-596: Green Herb", "Green Herb", Resi3LocationCategory.PICKUP),
        Resi3LocationData("R104-666: Lighter Oil", "Lighter Oil", Resi3LocationCategory.PICKUP),
        Resi3LocationData("R104-736: Benelli SG", "Benelli SG", Resi3LocationCategory.PICKUP),
    ],
    "Bar Jack Street": [
        Resi3LocationData("R106-974: DOCUMENT", "DOCUMENT", Resi3LocationCategory.PICKUP),
        Resi3LocationData("R106-1036: Green Herb", "Green Herb", Resi3LocationCategory.PICKUP),
        Resi3LocationData("R106-1058: Green Herb", "Green Herb", Resi3LocationCategory.PICKUP),
    ],
    "Bar Jack": [
        Resi3LocationData("R107-820: Lighter Case", "Lighter Case", Resi3LocationCategory.PICKUP),
        Resi3LocationData("R107-850: HG bullets", "HG bullets", Resi3LocationCategory.PICKUP),
        Resi3LocationData("R107-920: DOCUMENT", "DOCUMENT", Resi3LocationCategory.PICKUP),
    ],
    "Barricade Alley": [
        Resi3LocationData("R108-1262: Red Herb", "Red Herb", Resi3LocationCategory.PICKUP),
        Resi3LocationData("R108-1324: Red Herb", "Red Herb", Resi3LocationCategory.PICKUP),
        Resi3LocationData("R108-1394: DOCUMENT", "DOCUMENT", Resi3LocationCategory.PICKUP),
    ],
    "Alleyway Outside Pharmacy": [
        Resi3LocationData("R10B-986: Square Crank", "Square Crank", Resi3LocationCategory.PICKUP),
    ],
    "Hydrant Save": [
        Resi3LocationData("R10C-286: GunPowder A", "GunPowder A", Resi3LocationCategory.PICKUP),
        Resi3LocationData("R10C-348: GunPowder B", "GunPowder B", Resi3LocationCategory.PICKUP),
    ],
    "Back Alley": [
        Resi3LocationData("R10E-468: Blue Herb", "Blue Herb", Resi3LocationCategory.PICKUP),
        Resi3LocationData("R10E-530: Blue Herb", "Blue Herb", Resi3LocationCategory.PICKUP),
    ],
    "RPD Front": [
    ],
    "RPD Hall": [
        Resi3LocationData("R111-322: HG bullets", "HG bullets", Resi3LocationCategory.PICKUP),
        Resi3LocationData("R111-384: Green Herb", "Green Herb", Resi3LocationCategory.PICKUP),
        Resi3LocationData("R111-446: Green Herb", "Green Herb", Resi3LocationCategory.PICKUP),
        Resi3LocationData("R111-508: Green Herb", "Green Herb", Resi3LocationCategory.PICKUP),
        Resi3LocationData("R111-570: DOCUMENT", "DOCUMENT", Resi3LocationCategory.PICKUP),
    ],
    "RPD Big Office": [
        Resi3LocationData("R112-154: SG shells", "SG shells", Resi3LocationCategory.PICKUP),
        Resi3LocationData("R112-864: DOCUMENT", "DOCUMENT", Resi3LocationCategory.PICKUP),
        Resi3LocationData("R112-934: DOCUMENT", "DOCUMENT", Resi3LocationCategory.PICKUP),
    ],
    "RPD Evidence Room": [
        Resi3LocationData("R113-488: Emblem Key", "Emblem Key", Resi3LocationCategory.PICKUP),
        Resi3LocationData("R113-600: GunPowder B", "GunPowder B", Resi3LocationCategory.PICKUP),
        Resi3LocationData("R113-686: Blue Gem", "Blue Gem", Resi3LocationCategory.PICKUP),
    ],
    "RPD Stairs 1F": [
        Resi3LocationData("R114-282: Green Herb", "Green Herb", Resi3LocationCategory.PICKUP),
        Resi3LocationData("R114-344: Green Herb", "Green Herb", Resi3LocationCategory.PICKUP),
    ],
    "RPD Corridor": [
        Resi3LocationData("R115-946: Red Herb", "Red Herb", Resi3LocationCategory.PICKUP),
        Resi3LocationData("R115-1008: Red Herb", "Red Herb", Resi3LocationCategory.PICKUP),
    ],
    "RPD Meeting Room": [
        Resi3LocationData("R116-24: Jill's STARS Card", "Jill's STARS Card", Resi3LocationCategory.PICKUP),
        Resi3LocationData("R116-228: SG shells", "SG shells", Resi3LocationCategory.PICKUP),
        Resi3LocationData("R116-292: Ink Ribbon", "Ink Ribbon", Resi3LocationCategory.PICKUP),
    ],
    "RPD Dark Room": [
        Resi3LocationData("R117-156: Ink Ribbon", "Ink Ribbon", Resi3LocationCategory.PICKUP),
        Resi3LocationData("R117-218: GunPowder A", "GunPowder A", Resi3LocationCategory.PICKUP),
        Resi3LocationData("R117-240: DOCUMENT", "DOCUMENT", Resi3LocationCategory.PICKUP),
    ],
    "RPD Stairs 2F": [
    ],
    "RPD STARS Corridor": [
    ],
    "STARS Office": [
        Resi3LocationData("R11A-158: S&W magnum", "S&W magnum", Resi3LocationCategory.PICKUP),
        Resi3LocationData("R11A-224: GL(burst)", "GL(burst)", Resi3LocationCategory.PICKUP),
        Resi3LocationData("R11A-288: Lockpick", "Lockpick", Resi3LocationCategory.PICKUP),
        Resi3LocationData("R11A-350: HG bullets", "HG bullets", Resi3LocationCategory.PICKUP),
        Resi3LocationData("R11A-412: First Aid Spray", "First Aid Spray", Resi3LocationCategory.PICKUP),
        Resi3LocationData("R11A-438: DOCUMENT", "DOCUMENT", Resi3LocationCategory.PICKUP),
    ],
    "Pharmacy Room 1": [
        Resi3LocationData("R11B-2050: DOCUMENT", "DOCUMENT", Resi3LocationCategory.PICKUP),
        Resi3LocationData("R11B-2142: First Aid Spray", "First Aid Spray", Resi3LocationCategory.PICKUP),
        Resi3LocationData("R11B-2164: Ink Ribbon", "Ink Ribbon", Resi3LocationCategory.PICKUP),
        Resi3LocationData("R11B-2226: DOCUMENT", "DOCUMENT", Resi3LocationCategory.PICKUP),
    ],
    "Pharmacy Room 2": [
        Resi3LocationData("R11C-144: Additive", "Additive", Resi3LocationCategory.PICKUP),
        Resi3LocationData("R11C-308: GunPowder A", "GunPowder A", Resi3LocationCategory.PICKUP),
        Resi3LocationData("R11C-370: GunPowder A", "GunPowder A", Resi3LocationCategory.PICKUP),
        Resi3LocationData("R11C-432: GunPowder A", "GunPowder A", Resi3LocationCategory.PICKUP),
        Resi3LocationData("R11C-558: GunPowder B", "GunPowder B", Resi3LocationCategory.PICKUP),
        Resi3LocationData("R11C-620: GunPowder B", "GunPowder B", Resi3LocationCategory.PICKUP),
        Resi3LocationData("R11C-682: GunPowder B", "GunPowder B", Resi3LocationCategory.PICKUP),
    ],
    "Warehouse Alley 2": [
    ],
    "Warehouse Street 2": [
    ],
    "Bar Jack Alley 2": [
    ],
    "Bar Jack Alley Loot": [
        Resi3LocationData("R120-3652: GL rounds(burst)", "GL rounds(burst)", Resi3LocationCategory.PICKUP),
        Resi3LocationData("R120-3714: GL rounds(burst)", "GL rounds(burst)", Resi3LocationCategory.PICKUP),
        Resi3LocationData("R120-3776: GL rounds(burst)", "GL rounds(burst)", Resi3LocationCategory.PICKUP),
    ],
    "Hydrant Alley 2": [
    ],
    "RPD Street 2": [
    ],
    "Bus Street": [
        Resi3LocationData("R200-2712: GunPowder B", "GunPowder B", Resi3LocationCategory.PICKUP),
    ],
    "Parking Lot": [
        Resi3LocationData("R201-136: Power Cable", "Power Cable", Resi3LocationCategory.PICKUP),
    ],
    "Parking Lot Back": [
        Resi3LocationData("R202-2086: GL rounds(burst)", "GL rounds(burst)", Resi3LocationCategory.PICKUP),
    ],
    "Construction Site": [
        Resi3LocationData("R203-1028: GunPowder A", "GunPowder A", Resi3LocationCategory.PICKUP),
        Resi3LocationData("R203-1090: DOCUMENT", "DOCUMENT", Resi3LocationCategory.PICKUP),
    ],
    "Power Station Front": [
        Resi3LocationData("R204-1924: HG bullets", "HG bullets", Resi3LocationCategory.PICKUP),
    ],
    "Restaurant Front": [
        Resi3LocationData("R205-1180: Bronze Book", "HG bullets", Resi3LocationCategory.PICKUP),
        Resi3LocationData("R205-1354: Bronze Compass", "Bronze Compass", Resi3LocationCategory.PICKUP),
        Resi3LocationData("R205-1564: Green Herb", "Green Herb", Resi3LocationCategory.PICKUP),
        Resi3LocationData("R205-1626: Green Herb", "Green Herb", Resi3LocationCategory.PICKUP),
    ],
    "Shopping Alley": [
    ],
    "Press Street": [
        Resi3LocationData("R207-3390: HG bullets", "HG bullets", Resi3LocationCategory.PICKUP),
    ],
    "Municipal Alley": [
        Resi3LocationData("R208-3470: Green Herb", "Green Herb", Resi3LocationCategory.PICKUP),
        Resi3LocationData("R208-3532: Green Herb", "Green Herb", Resi3LocationCategory.PICKUP),
        Resi3LocationData("R208-3594: Green Herb", "Green Herb", Resi3LocationCategory.PICKUP),
        Resi3LocationData("R208-3666: Bronze Book", "Bronze Book", Resi3LocationCategory.PICKUP),
        Resi3LocationData("R208-3894: Battery", "Battery", Resi3LocationCategory.PICKUP),
    ],
    "Party Alley": [
        Resi3LocationData("R209-2110: GunPowder B", "GunPowder B", Resi3LocationCategory.PICKUP),
    ],
    "Grave Digger Alley": [
        Resi3LocationData("R20A-64: Green Herb", "Green Herb", Resi3LocationCategory.PICKUP),
        Resi3LocationData("R20A-126: Green Herb", "Green Herb", Resi3LocationCategory.PICKUP),
    ],
    "Train Station": [
        Resi3LocationData("R20B-470: SG shells", "SG shells", Resi3LocationCategory.PICKUP),
    ],
    "Cable Car": [
        Resi3LocationData("R20C-1030: DOCUMENT", "DOCUMENT", Resi3LocationCategory.PICKUP),
        Resi3LocationData("R20C-1096: Wrench", "Wrench", Resi3LocationCategory.PICKUP),
        Resi3LocationData("R20C-1248: GL rounds(flame)", "GL rounds(flame)", Resi3LocationCategory.PICKUP),
    ],
    "Stagla Gas": [
        Resi3LocationData("R20D-226: First Aid Spray", "First Aid Spray", Resi3LocationCategory.PICKUP),
        Resi3LocationData("R20D-688: Machine Oil", "Machine Oil", Resi3LocationCategory.PICKUP),
    ],
    "Stagla Gas Outside": [
        Resi3LocationData("R20E-4850: Red Herb", "Red Herb", Resi3LocationCategory.PICKUP),
        Resi3LocationData("R20E-4912: Red Herb", "Red Herb", Resi3LocationCategory.PICKUP),
    ],
    "Press Offices": [
        Resi3LocationData("R20F-448: GunPowder A", "GunPowder A", Resi3LocationCategory.PICKUP),
        Resi3LocationData("R20F-510: GunPowder A", "GunPowder A", Resi3LocationCategory.PICKUP),
        Resi3LocationData("R20F-698: DOCUMENT", "DOCUMENT", Resi3LocationCategory.PICKUP),
        Resi3LocationData("R20F-760: DOCUMENT", "DOCUMENT", Resi3LocationCategory.PICKUP),
        Resi3LocationData("R20F-2806: Green Gem", "Green Gem", Resi3LocationCategory.PICKUP),
    ],
    "Press Entrance": [
        Resi3LocationData("R210-322: DOCUMENT", "DOCUMENT", Resi3LocationCategory.PICKUP),
        Resi3LocationData("R210-384: First Aid Spray", "First Aid Spray", Resi3LocationCategory.PICKUP),
        Resi3LocationData("R210-446: Ink Ribbon", "Ink Ribbon", Resi3LocationCategory.PICKUP),
    ],
    "Restaurant": [
        Resi3LocationData("R211-970: Fire Hook", "Fire Hook", Resi3LocationCategory.PICKUP),
        Resi3LocationData("R211-1320: DOCUMENT", "DOCUMENT", Resi3LocationCategory.PICKUP),
    ],
    "Restaurant Basement": [
    ],
    "Power Station Access": [
    ],
    "Power Station": [
        Resi3LocationData("R214-762: Fuse", "Fuse", Resi3LocationCategory.PICKUP),
    ],
    "Cable Car Moving": [
        Resi3LocationData("R215-926: DOCUMENT", "DOCUMENT", Resi3LocationCategory.PICKUP),
    ],
    "Shopping Save": [
        Resi3LocationData("R216-194: SG shells", "SG shells", Resi3LocationCategory.PICKUP),
        Resi3LocationData("R216-256: Rusted Crank", "Rusted Crank", Resi3LocationCategory.PICKUP),
    ],
    "Stagla Escape": [
        Resi3LocationData("R217-5352: Red Herb", "Red Herb", Resi3LocationCategory.PICKUP),
        Resi3LocationData("R217-5414: Red Herb", "Red Herb", Resi3LocationCategory.PICKUP),
    ],
    "Fire Hose Alley": [
        Resi3LocationData("R218-936: Fire Hose", "Fire Hose", Resi3LocationCategory.PICKUP),
        Resi3LocationData("R218-1520: Green Herb", "Green Herb", Resi3LocationCategory.PICKUP),
        Resi3LocationData("R218-1582: Green Herb", "Green Herb", Resi3LocationCategory.PICKUP),
        Resi3LocationData("R218-1644: Green Herb", "Green Herb", Resi3LocationCategory.PICKUP),
        Resi3LocationData("R218-1708: Blue Herb", "Blue Herb", Resi3LocationCategory.PICKUP),
        Resi3LocationData("R218-1770: Blue Herb", "Blue Herb", Resi3LocationCategory.PICKUP),
    ],
    "Press Entrance 2": [
        Resi3LocationData("R219-292: DOCUMENT", "DOCUMENT", Resi3LocationCategory.PICKUP),
        Resi3LocationData("R219-354: First Aid Spray", "First Aid Spray", Resi3LocationCategory.PICKUP),
        Resi3LocationData("R219-416: Ink Ribbon", "Ink Ribbon", Resi3LocationCategory.PICKUP),
    ],
    "Parasite Alley": [
        Resi3LocationData("R21A-1288: HG bullets", "HG bullets", Resi3LocationCategory.PICKUP),
        Resi3LocationData("R21A-1310: DOCUMENT", "DOCUMENT", Resi3LocationCategory.PICKUP),
    ],
    "Parking Lot Save": [
        Resi3LocationData("R21B-156: HG bullets", "HG bullets", Resi3LocationCategory.PICKUP),
        Resi3LocationData("R21B-218: Ink Ribbon", "Ink Ribbon", Resi3LocationCategory.PICKUP),
    ],
    "ClockTower Chapel": [
        Resi3LocationData("R300-2636: GunPowder A", "Clock Tower Key(Winder)", Resi3LocationCategory.PICKUP),
        Resi3LocationData("R300-2698: GunPowder A", "GunPowder A", Resi3LocationCategory.PICKUP),
        Resi3LocationData("R300-2760: GunPowder B", "GunPowder B", Resi3LocationCategory.PICKUP),
        Resi3LocationData("R300-2822: GunPowder B", "GunPowder B", Resi3LocationCategory.PICKUP),
    ],
    "ClockTower Piano Room": [
    ],
    "ClockTower Dining Room": [
        Resi3LocationData("R302-412: GL rounds(burst)", "GL rounds(burst)", Resi3LocationCategory.PICKUP),
    ],
    "ClockTower Outdoor": [
        Resi3LocationData("R303-286: Green Herb", "Green Herb", Resi3LocationCategory.PICKUP),
        Resi3LocationData("R303-308: Green Herb", "Green Herb", Resi3LocationCategory.PICKUP),
        Resi3LocationData("R303-330: Green Herb", "Green Herb", Resi3LocationCategory.PICKUP),
        Resi3LocationData("R303-352: Blue Herb", "Blue Herb", Resi3LocationCategory.PICKUP),
        Resi3LocationData("R303-374: Blue Herb", "Blue Herb", Resi3LocationCategory.PICKUP),
    ],
    "ClockTower Hall 1F": [
        Resi3LocationData("R304-398: DOCUMENT", "DOCUMENT", Resi3LocationCategory.PICKUP),
        Resi3LocationData("R304-470: Mine Thrower", "Mine Thrower", Resi3LocationCategory.PICKUP),
        Resi3LocationData("R304-536: SG shells", "SG shells", Resi3LocationCategory.PICKUP),
        Resi3LocationData("R304-560: DOCUMENT", "DOCUMENT", Resi3LocationCategory.PICKUP),
        Resi3LocationData("R304-786: DOCUMENT", "DOCUMENT", Resi3LocationCategory.PICKUP),
        Resi3LocationData("R304-848: First Aid Spray", "First Aid Spray", Resi3LocationCategory.PICKUP),
    ],
    "ClockTower Bedroom": [
    ],
    "ClockTower Chess Room": [
    ],
    "ClockTower Library": [
        Resi3LocationData("R307-316: GL rounds(burst)", "GL rounds(burst)", Resi3LocationCategory.PICKUP),
        Resi3LocationData("R307-436: DOCUMENT", "DOCUMENT", Resi3LocationCategory.PICKUP),
        Resi3LocationData("R307-458: Ink Ribbon", "Ink Ribbon", Resi3LocationCategory.PICKUP),
    ],
    "Chronos Corridor": [
        Resi3LocationData("R308-180: GL rounds(burst)", "GL rounds(burst)", Resi3LocationCategory.PICKUP),
    ],
    "ClockTower Hall 2F": [
    ],
    "Tower Outdoor": [
        Resi3LocationData("R30B-1322: Red Herb", "Red Herb", Resi3LocationCategory.PICKUP),
        Resi3LocationData("R30B-1384: Red Herb", "Red Herb", Resi3LocationCategory.PICKUP),
    ],
    "ClockTower": [
        Resi3LocationData("R30C-278: MineThrower rounds", "Chronos Chain", Resi3LocationCategory.PICKUP),
        Resi3LocationData("R30C-344: GunPowder A", "GunPowder A", Resi3LocationCategory.PICKUP),
        Resi3LocationData("R30C-406: GunPowder A", "GunPowder A", Resi3LocationCategory.PICKUP),
        Resi3LocationData("R30C-474: GunPowder A", "GunPowder A", Resi3LocationCategory.PICKUP),
        Resi3LocationData("R30C-536: GunPowder A", "GunPowder A", Resi3LocationCategory.PICKUP),
        Resi3LocationData("R30C-698: Silver Gear", "GunPowder C", Resi3LocationCategory.PICKUP),
        Resi3LocationData("R30C-760: Ink Ribbon", "Ink Ribbon", Resi3LocationCategory.PICKUP),
    ],
    "Chronos Room 2": [
        Resi3LocationData("R315-194: DOCUMENT", "DOCUMENT", Resi3LocationCategory.PICKUP),
    ],
    "ClockTower Piano Room 2": [
        Resi3LocationData("R317-712: GL rounds(burst)", "GL rounds(burst)", Resi3LocationCategory.PICKUP),
    ],
    "Hospital Street": [
    ],
    "Office Save": [
        Resi3LocationData("R401-308: Ink Ribbon", "Ink Ribbon", Resi3LocationCategory.PICKUP),
        Resi3LocationData("R401-370: Park Key(front)", "Park Key(front)", Resi3LocationCategory.PICKUP),
        Resi3LocationData("R401-448: MineThrower rounds", "MineThrower rounds", Resi3LocationCategory.PICKUP),
        Resi3LocationData("R401-510: MineThrower rounds", "MineThrower rounds", Resi3LocationCategory.PICKUP),
        Resi3LocationData("R401-536: GL rounds(burst)", "GL rounds(burst)", Resi3LocationCategory.PICKUP),
        Resi3LocationData("R401-598: GL rounds(burst)", "GL rounds(burst)", Resi3LocationCategory.PICKUP),
        Resi3LocationData("R401-626: GL rounds(burst)", "GL rounds(burst)", Resi3LocationCategory.PICKUP),
        Resi3LocationData("R401-688: GL rounds(burst)", "GL rounds(burst)", Resi3LocationCategory.PICKUP),
        Resi3LocationData("R401-712: DOCUMENT", "DOCUMENT", Resi3LocationCategory.PICKUP),
    ],
    "Hospital Hall": [
        Resi3LocationData("R402-312: Red Herb", "Red Herb", Resi3LocationCategory.PICKUP),
        Resi3LocationData("R402-374: Red Herb", "Red Herb", Resi3LocationCategory.PICKUP),
    ],
    "Reception": [
        Resi3LocationData("R403-144: Ink Ribbon", "Ink Ribbon", Resi3LocationCategory.PICKUP),
        Resi3LocationData("R403-206: First Aid Spray", "First Aid Spray", Resi3LocationCategory.PICKUP),
    ],
    "Staff Room": [
        Resi3LocationData("R404-510: Tape Recorder", "Tape Recorder", Resi3LocationCategory.PICKUP),
        Resi3LocationData("R404-572: DOCUMENT", "DOCUMENT", Resi3LocationCategory.PICKUP),
        Resi3LocationData("R404-634: HG bullets", "HG bullets", Resi3LocationCategory.PICKUP),
        Resi3LocationData("R404-696: DOCUMENT", "DOCUMENT", Resi3LocationCategory.PICKUP),
        Resi3LocationData("R404-758: Blue Herb", "Blue Herb", Resi3LocationCategory.PICKUP),
    ],
    "4F Corridor": [
    ],
    "Room 402": [
        Resi3LocationData("R406-476: Vaccine Base", "GunPowder B", Resi3LocationCategory.PICKUP),
    ],
    "Room 401": [
        Resi3LocationData("R407-1302: Green Herb", "Green Herb", Resi3LocationCategory.PICKUP),
        Resi3LocationData("R407-1364: Green Herb", "Green Herb", Resi3LocationCategory.PICKUP),
    ],
    "Data Room": [
        Resi3LocationData("R408-322: HG bullets", "HG bullets", Resi3LocationCategory.PICKUP),
        Resi3LocationData("R408-408: Sickroom Key", "Sickroom Key", Resi3LocationCategory.PICKUP),
        Resi3LocationData("R408-470: DOCUMENT", "DOCUMENT", Resi3LocationCategory.PICKUP),
    ],
    "B3 Corridor": [
    ],
    "Laboratory": [
        Resi3LocationData("R40A-456: HG bullets", "HG bullets", Resi3LocationCategory.PICKUP),
        Resi3LocationData("R40A-528: Green Herb", "Green Herb", Resi3LocationCategory.PICKUP),
        Resi3LocationData("R40A-590: Green Herb", "Green Herb", Resi3LocationCategory.PICKUP),
    ],
    "Synthesis Room": [
        Resi3LocationData("R40B-704: Medium Base", "GunPowder A", Resi3LocationCategory.PICKUP),
        Resi3LocationData("R40B-794: DOCUMENT", "DOCUMENT", Resi3LocationCategory.PICKUP),
    ],
    "Park Entrance": [
    ],
    "Fountain Room": [
        Resi3LocationData("R40D-3992: DOCUMENT", "DOCUMENT", Resi3LocationCategory.PICKUP),
        Resi3LocationData("R40D-4014: Green Herb", "Green Herb", Resi3LocationCategory.PICKUP),
        Resi3LocationData("R40D-4036: Green Herb", "Green Herb", Resi3LocationCategory.PICKUP),
        Resi3LocationData("R40D-4058: Green Herb", "Green Herb", Resi3LocationCategory.PICKUP),
        Resi3LocationData("R40D-4080: Blue Herb", "Blue Herb", Resi3LocationCategory.PICKUP),
        Resi3LocationData("R40D-4102: Blue Herb", "Blue Herb", Resi3LocationCategory.PICKUP),
    ],
    "Lake Passageway": [
    ],
    "Factory Approach": [
        Resi3LocationData("R40F-238: Magnum bullets", "Magnum bullets", Resi3LocationCategory.PICKUP),
        Resi3LocationData("R40F-302: Park Key(Graveyard)", "Park Key(Graveyard)", Resi3LocationCategory.PICKUP),
        Resi3LocationData("R40F-324: DOCUMENT", "DOCUMENT", Resi3LocationCategory.PICKUP),
    ],
    "Fountain Tunnel": [
    ],
    "Graveyard": [
        Resi3LocationData("R411-178: Red Herb", "Red Herb", Resi3LocationCategory.PICKUP),
        Resi3LocationData("R411-240: Red Herb", "Red Herb", Resi3LocationCategory.PICKUP),
    ],
    "Graveyard Cabin": [
        Resi3LocationData("R412-290: Iron Pipe", "Iron Pipe", Resi3LocationCategory.PICKUP),
        Resi3LocationData("R412-392: GunPowder A", "GunPowder A", Resi3LocationCategory.PICKUP),
        Resi3LocationData("R412-454: GunPowder A", "GunPowder A", Resi3LocationCategory.PICKUP),
        Resi3LocationData("R412-516: GunPowder B", "GunPowder B", Resi3LocationCategory.PICKUP),
        Resi3LocationData("R412-578: GunPowder B", "GunPowder B", Resi3LocationCategory.PICKUP),
    ],
    "Graveyard Save": [
        Resi3LocationData("R413-156: First Aid Spray", "First Aid Spray", Resi3LocationCategory.PICKUP),
    ],
    "Graveyard Secret": [
        Resi3LocationData("R414-112: Park Key(Rear)", "GunPowder C", Resi3LocationCategory.PICKUP),
        Resi3LocationData("R414-174: GL rounds(burst)", "GL rounds(burst)", Resi3LocationCategory.PICKUP),
        Resi3LocationData("R414-266: Ink Ribbon", "Ink Ribbon", Resi3LocationCategory.PICKUP),
        Resi3LocationData("R414-336: DOCUMENT", "DOCUMENT", Resi3LocationCategory.PICKUP),
        Resi3LocationData("R414-398: DOCUMENT", "DOCUMENT", Resi3LocationCategory.PICKUP),
    ],
    "Factory 1F": [
    ],
    "Factory Path": [
        Resi3LocationData("R500-956: Green Herb", "Green Herb", Resi3LocationCategory.PICKUP),
        Resi3LocationData("R500-1018: Green Herb", "Green Herb", Resi3LocationCategory.PICKUP),
    ],
    "Factory Save 1F": [
        Resi3LocationData("R501-288: Ink Ribbon", "Ink Ribbon", Resi3LocationCategory.PICKUP),
        Resi3LocationData("R501-350: First Aid Spray", "First Aid Spray", Resi3LocationCategory.PICKUP),
        Resi3LocationData("R501-412: DOCUMENT", "DOCUMENT", Resi3LocationCategory.PICKUP),
        Resi3LocationData("R501-474: Facility Key(no barcode)", "Facility Key(no barcode)", Resi3LocationCategory.PICKUP),
        Resi3LocationData("R501-538: GunPowder A", "GunPowder A", Resi3LocationCategory.PICKUP),
        Resi3LocationData("R501-600: GunPowder A", "GunPowder A", Resi3LocationCategory.PICKUP),
        Resi3LocationData("R501-662: GunPowder A", "GunPowder A", Resi3LocationCategory.PICKUP),
        Resi3LocationData("R501-724: GunPowder B", "GunPowder B", Resi3LocationCategory.PICKUP),
        Resi3LocationData("R501-786: GunPowder B", "GunPowder B", Resi3LocationCategory.PICKUP),
        Resi3LocationData("R501-848: GunPowder B", "GunPowder B", Resi3LocationCategory.PICKUP),
    ],
    "Boiler Room": [
        Resi3LocationData("R502-1084: Blue Herb", "Blue Herb", Resi3LocationCategory.PICKUP),
        Resi3LocationData("R502-1146: Blue Herb", "Blue Herb", Resi3LocationCategory.PICKUP),
    ],
    "Treatment Control": [
        Resi3LocationData("R503-1564: Green Herb", "Green Herb", Resi3LocationCategory.PICKUP),
        Resi3LocationData("R503-1626: Green Herb", "Green Herb", Resi3LocationCategory.PICKUP),
        Resi3LocationData("R503-1688: Green Herb", "Green Herb", Resi3LocationCategory.PICKUP),
        Resi3LocationData("R503-1750: DOCUMENT", "DOCUMENT", Resi3LocationCategory.PICKUP),
        Resi3LocationData("R503-1812: System Disk", "System Disk", Resi3LocationCategory.PICKUP),
    ],
    "Factory B1": [
    ],
    "Factory B1 Save": [
        Resi3LocationData("R505-166: DOCUMENT", "DOCUMENT", Resi3LocationCategory.PICKUP),
        Resi3LocationData("R505-228: Water Sample", "Water Sample", Resi3LocationCategory.PICKUP),
        Resi3LocationData("R505-362: Ink Ribbon", "Ink Ribbon", Resi3LocationCategory.PICKUP),
    ],
    "Water Puzzle": [
        Resi3LocationData("R506-870: GunPowder A", "GunPowder A", Resi3LocationCategory.PICKUP),
        Resi3LocationData("R506-932: GunPowder A", "GunPowder A", Resi3LocationCategory.PICKUP),
        Resi3LocationData("R506-994: GunPowder A", "GunPowder A", Resi3LocationCategory.PICKUP),
        Resi3LocationData("R506-1056: GunPowder B", "GunPowder B", Resi3LocationCategory.PICKUP),
        Resi3LocationData("R506-1118: GunPowder B", "GunPowder B", Resi3LocationCategory.PICKUP),
        Resi3LocationData("R506-1180: GunPowder B", "GunPowder B", Resi3LocationCategory.PICKUP),
        Resi3LocationData("R506-1244: First Aid Spray", "First Aid Spray", Resi3LocationCategory.PICKUP),
        Resi3LocationData("R506-1306: Facility Key(barcode)", "Facility Key(barcode)", Resi3LocationCategory.PICKUP),
    ],
    "Toxic Pool Room": [
        Resi3LocationData("R507-2994: SG shells", "SG shells", Resi3LocationCategory.PICKUP),
        Resi3LocationData("R507-3056: SG shells", "SG shells", Resi3LocationCategory.PICKUP),
    ],
    "Disposal Access": [
    ],
    "Disposal Chamber": [
        Resi3LocationData("R509-134: Card Key", "Card Key", Resi3LocationCategory.PICKUP),
    ],
    "Communications Room": [
        Resi3LocationData("R50A-250: Magnum bullets", "Magnum bullets", Resi3LocationCategory.PICKUP),
        Resi3LocationData("R50A-272: First Aid Spray", "First Aid Spray", Resi3LocationCategory.PICKUP),
    ],
    "Hatch Escape Path": [
        Resi3LocationData("R50B-902: DOCUMENT", "DOCUMENT", Resi3LocationCategory.PICKUP),
        Resi3LocationData("R50B-964: SG shells", "SG shells", Resi3LocationCategory.PICKUP),
        Resi3LocationData("R50B-1026: SG shells", "SG shells", Resi3LocationCategory.PICKUP),
    ],
    "Car Cemetary": [
        Resi3LocationData("R50C-66: DOCUMENT", "DOCUMENT", Resi3LocationCategory.PICKUP),
        Resi3LocationData("MadeVictory", "EVENT", Resi3LocationCategory.PICKUP),
    ],
    "Chopper Departure": [
    ],
}
