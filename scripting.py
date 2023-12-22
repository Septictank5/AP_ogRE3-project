from enum import IntEnum

class Resi3LocationCategory(IntEnum):
    PICKUP = 0


class Resi3LocationData:
    def __init__(self, name, default, category):
        self.name = name
        self.default = default
        self.category = category

location_tables = {
    "R100:Warehouse Save Room": [
        Resi3LocationData("182: Warehouse Key (BackDoor)", "Warehouse Key (BackDoor)", Resi3LocationCategory.PICKUP),
        Resi3LocationData("244: GunPowder A", "GunPowder A", Resi3LocationCategory.PICKUP),
        Resi3LocationData("306: GunPowder A", "GunPowder A", Resi3LocationCategory.PICKUP),
        Resi3LocationData("368: Ink Ribbon", "Ink Ribbon", Resi3LocationCategory.PICKUP),
        Resi3LocationData("432: Game Instruction A", "Game Instruction A", Resi3LocationCategory.PICKUP),
    ],
    "R101:Warehouse": [
        Resi3LocationData("204: First Aid Spray", "First Aid Spray", Resi3LocationCategory.PICKUP),
        Resi3LocationData("242: HG bullets", "HG bullets", Resi3LocationCategory.PICKUP),
        Resi3LocationData("914: GunPowder A", "GunPowder A", Resi3LocationCategory.PICKUP),
        Resi3LocationData("976: GunPowder A", "GunPowder A", Resi3LocationCategory.PICKUP),
        Resi3LocationData("1038: GunPowder B", "GunPowder B", Resi3LocationCategory.PICKUP),
        Resi3LocationData("1100: GunPowder B", "GunPowder B", Resi3LocationCategory.PICKUP),
        Resi3LocationData("1162: DOCUMENT", "DOCUMENT", Resi3LocationCategory.PICKUP),
    ],
    "R102:Warehouse Alley": [
    ],
    "R103:Warehouse Street": [
        Resi3LocationData("224: GunPowder B", "GunPowder B", Resi3LocationCategory.PICKUP),
    ],
    "R104:Basement Alley": [
        Resi3LocationData("526: Green Herb", "Green Herb", Resi3LocationCategory.PICKUP),
        Resi3LocationData("596: Green Herb", "Green Herb", Resi3LocationCategory.PICKUP),
        Resi3LocationData("666: Lighter Oil", "Lighter Oil", Resi3LocationCategory.PICKUP),
        Resi3LocationData("736: Benelli SG", "Benelli SG", Resi3LocationCategory.PICKUP),
    ],
    "R105:Bar Jack Alley": [
        Resi3LocationData("140: Ink Ribbon", "Ink Ribbon", Resi3LocationCategory.PICKUP),
    ],
    "R106:Bar Jack Street": [
        Resi3LocationData("974: DOCUMENT", "DOCUMENT", Resi3LocationCategory.PICKUP),
        Resi3LocationData("1036: Green Herb", "Green Herb", Resi3LocationCategory.PICKUP),
        Resi3LocationData("1058: Green Herb", "Green Herb", Resi3LocationCategory.PICKUP),
    ],
    "R107:Bar Jack": [
        Resi3LocationData("820: Lighter Case", "Lighter Case", Resi3LocationCategory.PICKUP),
        Resi3LocationData("850: HG bullets", "HG bullets", Resi3LocationCategory.PICKUP),
        Resi3LocationData("920: DOCUMENT", "DOCUMENT", Resi3LocationCategory.PICKUP),
    ],
    "R108:Barricade Alley": [
        Resi3LocationData("1262: Red Herb", "Red Herb", Resi3LocationCategory.PICKUP),
        Resi3LocationData("1324: Red Herb", "Red Herb", Resi3LocationCategory.PICKUP),
        Resi3LocationData("1394: DOCUMENT", "DOCUMENT", Resi3LocationCategory.PICKUP),
    ],
    "R109:Hydrant Alley": [
    ],
    "R10A:RPD Street": [
    ],
    "R10B:Alleyway Outside Pharmacy": [
        Resi3LocationData("986: Square Crank", "Square Crank", Resi3LocationCategory.PICKUP),
    ],
    "R10C:Hydrant Save": [
        Resi3LocationData("286: GunPowder A", "GunPowder A", Resi3LocationCategory.PICKUP),
        Resi3LocationData("348: GunPowder B", "GunPowder B", Resi3LocationCategory.PICKUP),
    ],
    "R10D:Scenario Start": [
    ],
    "R10E:Back Alley": [
        Resi3LocationData("468: Blue Herb", "Blue Herb", Resi3LocationCategory.PICKUP),
        Resi3LocationData("530: Blue Herb", "Blue Herb", Resi3LocationCategory.PICKUP),
    ],
    "R10F:Boutique": [
    ],
    "R110:RPD Front": [
        Resi3LocationData("210: Brad's Card Case", "Brad's Card Case", Resi3LocationCategory.PICKUP),
    ],
    "R111:RPD Hall": [
        Resi3LocationData("322: HG bullets", "HG bullets", Resi3LocationCategory.PICKUP),
        Resi3LocationData("384: Green Herb", "Green Herb", Resi3LocationCategory.PICKUP),
        Resi3LocationData("446: Green Herb", "Green Herb", Resi3LocationCategory.PICKUP),
        Resi3LocationData("508: Green Herb", "Green Herb", Resi3LocationCategory.PICKUP),
        Resi3LocationData("570: DOCUMENT", "DOCUMENT", Resi3LocationCategory.PICKUP),
    ],
    "R112:RPD Big Office": [
        Resi3LocationData("154: SG shells", "SG shells", Resi3LocationCategory.PICKUP),
        Resi3LocationData("864: DOCUMENT", "DOCUMENT", Resi3LocationCategory.PICKUP),
        Resi3LocationData("934: DOCUMENT", "DOCUMENT", Resi3LocationCategory.PICKUP),
    ],
    "R113:RPD Evidence Room": [
        Resi3LocationData("488: Emblem Key", "Emblem Key", Resi3LocationCategory.PICKUP),
        Resi3LocationData("600: GunPowder B", "GunPowder B", Resi3LocationCategory.PICKUP),
        Resi3LocationData("686: Blue Gem", "Blue Gem", Resi3LocationCategory.PICKUP),
    ],
    "R114:RPD Stairs 1F": [
        Resi3LocationData("282: Green Herb", "Green Herb", Resi3LocationCategory.PICKUP),
        Resi3LocationData("344: Green Herb", "Green Herb", Resi3LocationCategory.PICKUP),
    ],
    "R115:RPD Corridor": [
        Resi3LocationData("946: Red Herb", "Red Herb", Resi3LocationCategory.PICKUP),
        Resi3LocationData("1008: Red Herb", "Red Herb", Resi3LocationCategory.PICKUP),
    ],
    "R116:RPD Meeting Room": [
        Resi3LocationData("24: Jill's STARS Card", "Jill's STARS Card", Resi3LocationCategory.PICKUP),
        Resi3LocationData("228: SG shells", "SG shells", Resi3LocationCategory.PICKUP),
        Resi3LocationData("292: Ink Ribbon", "Ink Ribbon", Resi3LocationCategory.PICKUP),
    ],
    "R117:RPD Dark Room": [
        Resi3LocationData("156: Ink Ribbon", "Ink Ribbon", Resi3LocationCategory.PICKUP),
        Resi3LocationData("218: GunPowder A", "GunPowder A", Resi3LocationCategory.PICKUP),
        Resi3LocationData("240: DOCUMENT", "DOCUMENT", Resi3LocationCategory.PICKUP),
    ],
    "R118:RPD Stairs 2F": [
    ],
    "R119:RPD STARS Corridor": [
        Resi3LocationData("190: Red Herb", "Red Herb", Resi3LocationCategory.PICKUP),
        Resi3LocationData("252: Red Herb", "Red Herb", Resi3LocationCategory.PICKUP),
    ],
    "R11A:STARS Office": [
        Resi3LocationData("158: S&W magnum", "S&W magnum", Resi3LocationCategory.PICKUP),
        Resi3LocationData("224: GL(burst)", "GL(burst)", Resi3LocationCategory.PICKUP),
        Resi3LocationData("288: Lockpick", "Lockpick", Resi3LocationCategory.PICKUP),
        Resi3LocationData("350: HG bullets", "HG bullets", Resi3LocationCategory.PICKUP),
        Resi3LocationData("412: First Aid Spray", "First Aid Spray", Resi3LocationCategory.PICKUP),
        Resi3LocationData("438: DOCUMENT", "DOCUMENT", Resi3LocationCategory.PICKUP),
    ],
    "R11B:Pharmacy Room 1": [
        Resi3LocationData("2050: DOCUMENT", "DOCUMENT", Resi3LocationCategory.PICKUP),
        Resi3LocationData("2142: First Aid Spray", "First Aid Spray", Resi3LocationCategory.PICKUP),
        Resi3LocationData("2164: Ink Ribbon", "Ink Ribbon", Resi3LocationCategory.PICKUP),
        Resi3LocationData("2226: DOCUMENT", "DOCUMENT", Resi3LocationCategory.PICKUP),
    ],
    "R11C:Pharmacy Room 2": [
        Resi3LocationData("144: Additive", "Additive", Resi3LocationCategory.PICKUP),
        Resi3LocationData("308: GunPowder A", "GunPowder A", Resi3LocationCategory.PICKUP),
        Resi3LocationData("370: GunPowder A", "GunPowder A", Resi3LocationCategory.PICKUP),
        Resi3LocationData("432: GunPowder A", "GunPowder A", Resi3LocationCategory.PICKUP),
        Resi3LocationData("558: GunPowder B", "GunPowder B", Resi3LocationCategory.PICKUP),
        Resi3LocationData("620: GunPowder B", "GunPowder B", Resi3LocationCategory.PICKUP),
        Resi3LocationData("682: GunPowder B", "GunPowder B", Resi3LocationCategory.PICKUP),
    ],
    "R11D:Warehouse Alley 2": [
    ],
    "R11E:Warehouse Street 2": [
        Resi3LocationData("314: GunPowder B", "GunPowder B", Resi3LocationCategory.PICKUP),
    ],
    "R11F:Basement Alley 2": [
        Resi3LocationData("1494: Green Herb", "Green Herb", Resi3LocationCategory.PICKUP),
        Resi3LocationData("1564: Green Herb", "Green Herb", Resi3LocationCategory.PICKUP),
        Resi3LocationData("1634: Benelli SG", "Benelli SG", Resi3LocationCategory.PICKUP),
    ],
    "R120:Bar Jack Alley 2": [
        Resi3LocationData("3652: GL rounds(burst)", "GL rounds(burst)", Resi3LocationCategory.PICKUP),
        Resi3LocationData("3714: GL rounds(burst)", "GL rounds(burst)", Resi3LocationCategory.PICKUP),
        Resi3LocationData("3776: GL rounds(burst)", "GL rounds(burst)", Resi3LocationCategory.PICKUP),
        Resi3LocationData("3838: Ink Ribbon", "Ink Ribbon", Resi3LocationCategory.PICKUP),
    ],
    "R121:Bar Jack Street 2": [
        Resi3LocationData("1910: DOCUMENT", "DOCUMENT", Resi3LocationCategory.PICKUP),
    ],
    "R122:Barricade Alley 2": [
        Resi3LocationData("696: Red Herb", "Red Herb", Resi3LocationCategory.PICKUP),
        Resi3LocationData("758: Red Herb", "Red Herb", Resi3LocationCategory.PICKUP),
        Resi3LocationData("828: DOCUMENT", "DOCUMENT", Resi3LocationCategory.PICKUP),
    ],
    "R123:Hydrant Alley 2": [
    ],
    "R124:RPD Street 2": [
    ],
    "R125:RPD Front 2": [
    ],
    "R200:Bus Street": [
        Resi3LocationData("2712: GunPowder B", "GunPowder B", Resi3LocationCategory.PICKUP),
    ],
    "R201:Parking Lot": [
        Resi3LocationData("136: Power Cable", "Power Cable", Resi3LocationCategory.PICKUP),
    ],
    "R202:Parking Lot Back": [
        Resi3LocationData("2086: GL rounds(burst)", "GL rounds(burst)", Resi3LocationCategory.PICKUP),
    ],
    "R203:Construction Site": [
        Resi3LocationData("966: Battery", "Battery", Resi3LocationCategory.PICKUP),
        Resi3LocationData("1028: GunPowder A", "GunPowder A", Resi3LocationCategory.PICKUP),
        Resi3LocationData("1090: DOCUMENT", "DOCUMENT", Resi3LocationCategory.PICKUP),
    ],
    "R204:Power Station Front": [
        Resi3LocationData("1924: HG bullets", "HG bullets", Resi3LocationCategory.PICKUP),
    ],
    "R205:Restaurant Front": [
        Resi3LocationData("1180: Bronze Book", "Bronze Book", Resi3LocationCategory.PICKUP),
        Resi3LocationData("1354: Bronze Compass", "Bronze Compass", Resi3LocationCategory.PICKUP),
        Resi3LocationData("1564: Green Herb", "Green Herb", Resi3LocationCategory.PICKUP),
        Resi3LocationData("1626: Green Herb", "Green Herb", Resi3LocationCategory.PICKUP),
    ],
    "R206:Shopping Alley": [
    ],
    "R207:Press Street": [
        Resi3LocationData("3390: HG bullets", "HG bullets", Resi3LocationCategory.PICKUP),
    ],
    "R208:Municipal Alley": [
        Resi3LocationData("3470: Green Herb", "Green Herb", Resi3LocationCategory.PICKUP),
        Resi3LocationData("3532: Green Herb", "Green Herb", Resi3LocationCategory.PICKUP),
        Resi3LocationData("3594: Green Herb", "Green Herb", Resi3LocationCategory.PICKUP),
        Resi3LocationData("3666: Bronze Book", "Bronze Book", Resi3LocationCategory.PICKUP),
        Resi3LocationData("3894: Battery", "Battery", Resi3LocationCategory.PICKUP),
    ],
    "R209:Party Alley": [
        Resi3LocationData("2110: GunPowder B", "GunPowder B", Resi3LocationCategory.PICKUP),
    ],
    "R20A:Grave Digger Alley": [
        Resi3LocationData("64: Green Herb", "Green Herb", Resi3LocationCategory.PICKUP),
        Resi3LocationData("126: Green Herb", "Green Herb", Resi3LocationCategory.PICKUP),
    ],
    "R20B:Train Station": [
        Resi3LocationData("470: SG shells", "SG shells", Resi3LocationCategory.PICKUP),
    ],
    "R20C:Cable Car": [
        Resi3LocationData("1030: DOCUMENT", "DOCUMENT", Resi3LocationCategory.PICKUP),
        Resi3LocationData("1096: Wrench", "Wrench", Resi3LocationCategory.PICKUP),
        Resi3LocationData("1248: GL rounds(flame)", "GL rounds(flame)", Resi3LocationCategory.PICKUP),
    ],
    "R20D:Stagla Gas": [
        Resi3LocationData("226: First Aid Spray", "First Aid Spray", Resi3LocationCategory.PICKUP),
        Resi3LocationData("334: GunPowder A", "GunPowder A", Resi3LocationCategory.PICKUP),
        Resi3LocationData("396: GunPowder A", "GunPowder A", Resi3LocationCategory.PICKUP),
        Resi3LocationData("458: GunPowder A", "GunPowder A", Resi3LocationCategory.PICKUP),
        Resi3LocationData("688: Machine Oil", "Machine Oil", Resi3LocationCategory.PICKUP),
    ],
    "R20E:Stagla Gas Outside": [
        Resi3LocationData("4850: Red Herb", "Red Herb", Resi3LocationCategory.PICKUP),
        Resi3LocationData("4912: Red Herb", "Red Herb", Resi3LocationCategory.PICKUP),
    ],
    "R20F:Press Offices": [
        Resi3LocationData("448: GunPowder A", "GunPowder A", Resi3LocationCategory.PICKUP),
        Resi3LocationData("510: GunPowder A", "GunPowder A", Resi3LocationCategory.PICKUP),
        Resi3LocationData("574: Red Herb", "Red Herb", Resi3LocationCategory.PICKUP),
        Resi3LocationData("636: Red Herb", "Red Herb", Resi3LocationCategory.PICKUP),
        Resi3LocationData("698: DOCUMENT", "DOCUMENT", Resi3LocationCategory.PICKUP),
        Resi3LocationData("760: DOCUMENT", "DOCUMENT", Resi3LocationCategory.PICKUP),
        Resi3LocationData("2806: Green Gem", "Green Gem", Resi3LocationCategory.PICKUP),
    ],
    "R210:Press Entrance": [
        Resi3LocationData("322: DOCUMENT", "DOCUMENT", Resi3LocationCategory.PICKUP),
        Resi3LocationData("384: First Aid Spray", "First Aid Spray", Resi3LocationCategory.PICKUP),
        Resi3LocationData("446: Ink Ribbon", "Ink Ribbon", Resi3LocationCategory.PICKUP),
    ],
    "R211:Restaurant": [
        Resi3LocationData("970: Fire Hook", "Fire Hook", Resi3LocationCategory.PICKUP),
        Resi3LocationData("1194: GunPowder A", "GunPowder A", Resi3LocationCategory.PICKUP),
        Resi3LocationData("1256: GunPowder A", "GunPowder A", Resi3LocationCategory.PICKUP),
        Resi3LocationData("1320: DOCUMENT", "DOCUMENT", Resi3LocationCategory.PICKUP),
    ],
    "R212:Restaurant Basement": [
        Resi3LocationData("318: Green Gem", "Green Gem", Resi3LocationCategory.PICKUP),
    ],
    "R213:Power Station Access": [
        Resi3LocationData("288: Red Herb", "Red Herb", Resi3LocationCategory.PICKUP),
        Resi3LocationData("350: Red Herb", "Red Herb", Resi3LocationCategory.PICKUP),
    ],
    "R214:Power Station": [
        Resi3LocationData("632: GL(burst)", "GL(burst)", Resi3LocationCategory.PICKUP),
        Resi3LocationData("698: S&W magnum", "S&W magnum", Resi3LocationCategory.PICKUP),
        Resi3LocationData("762: Fuse", "Fuse", Resi3LocationCategory.PICKUP),
        Resi3LocationData("870: GunPowder B", "GunPowder B", Resi3LocationCategory.PICKUP),
        Resi3LocationData("932: GunPowder B", "GunPowder B", Resi3LocationCategory.PICKUP),
        Resi3LocationData("994: GunPowder B", "GunPowder B", Resi3LocationCategory.PICKUP),
    ],
    "R215:Cable Car Moving": [
        Resi3LocationData("926: DOCUMENT", "DOCUMENT", Resi3LocationCategory.PICKUP),
    ],
    "R216:Shopping Save": [
        Resi3LocationData("194: SG shells", "SG shells", Resi3LocationCategory.PICKUP),
        Resi3LocationData("256: Rusted Crank", "Rusted Crank", Resi3LocationCategory.PICKUP),
    ],
    "R217:Stagla Escape": [
        Resi3LocationData("5352: Red Herb", "Red Herb", Resi3LocationCategory.PICKUP),
        Resi3LocationData("5414: Red Herb", "Red Herb", Resi3LocationCategory.PICKUP),
    ],
    "R218:Fire Hose Alley": [
        Resi3LocationData("936: Fire Hose", "Fire Hose", Resi3LocationCategory.PICKUP),
        Resi3LocationData("1520: Green Herb", "Green Herb", Resi3LocationCategory.PICKUP),
        Resi3LocationData("1582: Green Herb", "Green Herb", Resi3LocationCategory.PICKUP),
        Resi3LocationData("1644: Green Herb", "Green Herb", Resi3LocationCategory.PICKUP),
        Resi3LocationData("1708: Blue Herb", "Blue Herb", Resi3LocationCategory.PICKUP),
        Resi3LocationData("1770: Blue Herb", "Blue Herb", Resi3LocationCategory.PICKUP),
    ],
    "R219:Press Entrance 2": [
        Resi3LocationData("292: DOCUMENT", "DOCUMENT", Resi3LocationCategory.PICKUP),
        Resi3LocationData("354: First Aid Spray", "First Aid Spray", Resi3LocationCategory.PICKUP),
        Resi3LocationData("416: Ink Ribbon", "Ink Ribbon", Resi3LocationCategory.PICKUP),
    ],
    "R21A:Parasite Alley": [
        Resi3LocationData("1288: HG bullets", "HG bullets", Resi3LocationCategory.PICKUP),
        Resi3LocationData("1310: DOCUMENT", "DOCUMENT", Resi3LocationCategory.PICKUP),
    ],
    "R21B:Parking Lot Save": [
        Resi3LocationData("156: HG bullets", "HG bullets", Resi3LocationCategory.PICKUP),
        Resi3LocationData("218: Ink Ribbon", "Ink Ribbon", Resi3LocationCategory.PICKUP),
    ],
    "R300:ClockTower Chapel": [
        Resi3LocationData("2636: GunPowder A", "GunPowder A", Resi3LocationCategory.PICKUP),
        Resi3LocationData("2698: GunPowder A", "GunPowder A", Resi3LocationCategory.PICKUP),
        Resi3LocationData("2760: GunPowder B", "GunPowder B", Resi3LocationCategory.PICKUP),
        Resi3LocationData("2822: GunPowder B", "GunPowder B", Resi3LocationCategory.PICKUP),
        Resi3LocationData("2914: Clock Tower Key(Winder)", "Clock Tower Key(Winder)", Resi3LocationCategory.PICKUP),
        Resi3LocationData("2980: Clock Tower Key(Bezel)", "Clock Tower Key(Bezel)", Resi3LocationCategory.PICKUP),
    ],
    "R301:ClockTower Piano Room": [
    ],
    "R302:ClockTower Dining Room": [
        Resi3LocationData("412: GL rounds(burst)", "GL rounds(burst)", Resi3LocationCategory.PICKUP),
    ],
    "R303:ClockTower Outdoor": [
        Resi3LocationData("286: Green Herb", "Green Herb", Resi3LocationCategory.PICKUP),
        Resi3LocationData("308: Green Herb", "Green Herb", Resi3LocationCategory.PICKUP),
        Resi3LocationData("330: Green Herb", "Green Herb", Resi3LocationCategory.PICKUP),
        Resi3LocationData("352: Blue Herb", "Blue Herb", Resi3LocationCategory.PICKUP),
        Resi3LocationData("374: Blue Herb", "Blue Herb", Resi3LocationCategory.PICKUP),
    ],
    "R304:ClockTower Hall 1F": [
        Resi3LocationData("398: DOCUMENT", "DOCUMENT", Resi3LocationCategory.PICKUP),
        Resi3LocationData("470: Mine Thrower", "Mine Thrower", Resi3LocationCategory.PICKUP),
        Resi3LocationData("536: SG shells", "SG shells", Resi3LocationCategory.PICKUP),
        Resi3LocationData("560: DOCUMENT", "DOCUMENT", Resi3LocationCategory.PICKUP),
        Resi3LocationData("786: DOCUMENT", "DOCUMENT", Resi3LocationCategory.PICKUP),
        Resi3LocationData("848: First Aid Spray", "First Aid Spray", Resi3LocationCategory.PICKUP),
    ],
    "R305:ClockTower Bedroom": [
        Resi3LocationData("480: Clock Tower Key(Bezel)", "Clock Tower Key(Bezel)", Resi3LocationCategory.PICKUP),
        Resi3LocationData("506: Clock Tower Key(Winder)", "Clock Tower Key(Winder)", Resi3LocationCategory.PICKUP),
        Resi3LocationData("782: GunPowder B", "GunPowder B", Resi3LocationCategory.PICKUP),
        Resi3LocationData("844: GunPowder B", "GunPowder B", Resi3LocationCategory.PICKUP),
        Resi3LocationData("906: GunPowder A", "GunPowder A", Resi3LocationCategory.PICKUP),
        Resi3LocationData("968: GunPowder A", "GunPowder A", Resi3LocationCategory.PICKUP),
    ],
    "R306:ClockTower Chess Room": [
    ],
    "R307:ClockTower Library": [
        Resi3LocationData("316: GL rounds(burst)", "GL rounds(burst)", Resi3LocationCategory.PICKUP),
        Resi3LocationData("436: DOCUMENT", "DOCUMENT", Resi3LocationCategory.PICKUP),
        Resi3LocationData("458: Ink Ribbon", "Ink Ribbon", Resi3LocationCategory.PICKUP),
    ],
    "R308:Chronos Corridor": [
        Resi3LocationData("180: GL rounds(burst)", "GL rounds(burst)", Resi3LocationCategory.PICKUP),
    ],
    "R309:Chronos Room": [
        Resi3LocationData("3158: Amber ball", "Amber ball", Resi3LocationCategory.PICKUP),
        Resi3LocationData("3260: MineThrower rounds", "MineThrower rounds", Resi3LocationCategory.PICKUP),
        Resi3LocationData("3326: SG shells", "SG shells", Resi3LocationCategory.PICKUP),
        Resi3LocationData("3390: Gold Gear", "Gold Gear", Resi3LocationCategory.PICKUP),
        Resi3LocationData("10176: DOCUMENT", "DOCUMENT", Resi3LocationCategory.PICKUP),
    ],
    "R30A:ClockTower Hall 2F": [
    ],
    "R30B:Tower Outdoor": [
        Resi3LocationData("1322: Red Herb", "Red Herb", Resi3LocationCategory.PICKUP),
        Resi3LocationData("1384: Red Herb", "Red Herb", Resi3LocationCategory.PICKUP),
    ],
    "R30C:ClockTower": [
        Resi3LocationData("278: MineThrower rounds", "MineThrower rounds", Resi3LocationCategory.PICKUP),
        Resi3LocationData("344: GunPowder A", "GunPowder A", Resi3LocationCategory.PICKUP),
        Resi3LocationData("406: GunPowder A", "GunPowder A", Resi3LocationCategory.PICKUP),
        Resi3LocationData("474: GunPowder A", "GunPowder A", Resi3LocationCategory.PICKUP),
        Resi3LocationData("536: GunPowder A", "GunPowder A", Resi3LocationCategory.PICKUP),
        Resi3LocationData("600: Chronos Chain", "Chronos Chain", Resi3LocationCategory.PICKUP),
        Resi3LocationData("698: Silver Gear", "Silver Gear", Resi3LocationCategory.PICKUP),
        Resi3LocationData("760: Ink Ribbon", "Ink Ribbon", Resi3LocationCategory.PICKUP),
    ],
    "R30D:ClockTower Nemesis Fight": [
    ],
    "R30E:ClockTower Hall 1F 2": [
        Resi3LocationData("112: DOCUMENT", "DOCUMENT", Resi3LocationCategory.PICKUP),
        Resi3LocationData("184: Mine Thrower", "Mine Thrower", Resi3LocationCategory.PICKUP),
        Resi3LocationData("250: SG shells", "SG shells", Resi3LocationCategory.PICKUP),
        Resi3LocationData("274: DOCUMENT", "DOCUMENT", Resi3LocationCategory.PICKUP),
        Resi3LocationData("500: DOCUMENT", "DOCUMENT", Resi3LocationCategory.PICKUP),
        Resi3LocationData("562: First Aid Spray", "First Aid Spray", Resi3LocationCategory.PICKUP),
    ],
    "R30F:ClockTower Piano&Dining": [
        Resi3LocationData("464: GL rounds(burst)", "GL rounds(burst)", Resi3LocationCategory.PICKUP),
    ],
    "R310:ClockTower Chapel 2": [
    ],
    "R311:ClockTower Bedroom 2": [
    ],
    "R312:ClockTower Chess Room 2": [
    ],
    "R313:ClockTower Library 2": [
        Resi3LocationData("304: DOCUMENT", "DOCUMENT", Resi3LocationCategory.PICKUP),
        Resi3LocationData("326: Ink Ribbon", "Ink Ribbon", Resi3LocationCategory.PICKUP),
    ],
    "R314:Chronos Corridor 2": [
    ],
    "R315:Chronos Room 2": [
        Resi3LocationData("194: DOCUMENT", "DOCUMENT", Resi3LocationCategory.PICKUP),
    ],
    "R316:ClockTower Hall 1F 3": [
        Resi3LocationData("596: DOCUMENT", "DOCUMENT", Resi3LocationCategory.PICKUP),
        Resi3LocationData("668: Mine Thrower", "Mine Thrower", Resi3LocationCategory.PICKUP),
        Resi3LocationData("734: SG shells", "SG shells", Resi3LocationCategory.PICKUP),
        Resi3LocationData("758: DOCUMENT", "DOCUMENT", Resi3LocationCategory.PICKUP),
        Resi3LocationData("984: DOCUMENT", "DOCUMENT", Resi3LocationCategory.PICKUP),
        Resi3LocationData("1046: First Aid Spray", "First Aid Spray", Resi3LocationCategory.PICKUP),
    ],
    "R317:ClockTower Piano Room 2": [
        Resi3LocationData("712: GL rounds(burst)", "GL rounds(burst)", Resi3LocationCategory.PICKUP),
    ],
    "R400:Hospital Street": [
    ],
    "R401:Office Save": [
        Resi3LocationData("308: Ink Ribbon", "Ink Ribbon", Resi3LocationCategory.PICKUP),
        Resi3LocationData("370: Park Key(front)", "Park Key(front)", Resi3LocationCategory.PICKUP),
        Resi3LocationData("448: MineThrower rounds", "MineThrower rounds", Resi3LocationCategory.PICKUP),
        Resi3LocationData("510: MineThrower rounds", "MineThrower rounds", Resi3LocationCategory.PICKUP),
        Resi3LocationData("536: GL rounds(burst)", "GL rounds(burst)", Resi3LocationCategory.PICKUP),
        Resi3LocationData("598: GL rounds(burst)", "GL rounds(burst)", Resi3LocationCategory.PICKUP),
        Resi3LocationData("626: GL rounds(burst)", "GL rounds(burst)", Resi3LocationCategory.PICKUP),
        Resi3LocationData("688: GL rounds(burst)", "GL rounds(burst)", Resi3LocationCategory.PICKUP),
        Resi3LocationData("712: DOCUMENT", "DOCUMENT", Resi3LocationCategory.PICKUP),
    ],
    "R402:Hospital Hall": [
        Resi3LocationData("312: Red Herb", "Red Herb", Resi3LocationCategory.PICKUP),
        Resi3LocationData("374: Red Herb", "Red Herb", Resi3LocationCategory.PICKUP),
    ],
    "R403:Reception": [
        Resi3LocationData("144: Ink Ribbon", "Ink Ribbon", Resi3LocationCategory.PICKUP),
        Resi3LocationData("206: First Aid Spray", "First Aid Spray", Resi3LocationCategory.PICKUP),
    ],
    "R404:Staff Room": [
        Resi3LocationData("510: Tape Recorder", "Tape Recorder", Resi3LocationCategory.PICKUP),
        Resi3LocationData("572: DOCUMENT", "DOCUMENT", Resi3LocationCategory.PICKUP),
        Resi3LocationData("634: HG bullets", "HG bullets", Resi3LocationCategory.PICKUP),
        Resi3LocationData("696: DOCUMENT", "DOCUMENT", Resi3LocationCategory.PICKUP),
        Resi3LocationData("758: Blue Herb", "Blue Herb", Resi3LocationCategory.PICKUP),
    ],
    "R405:4F Corridor": [
    ],
    "R406:Room 402": [
        Resi3LocationData("476: Vaccine Base", "Vaccine Base", Resi3LocationCategory.PICKUP),
    ],
    "R407:Room 401": [
        Resi3LocationData("1302: Green Herb", "Green Herb", Resi3LocationCategory.PICKUP),
        Resi3LocationData("1364: Green Herb", "Green Herb", Resi3LocationCategory.PICKUP),
    ],
    "R408:Data Room": [
        Resi3LocationData("322: HG bullets", "HG bullets", Resi3LocationCategory.PICKUP),
        Resi3LocationData("408: Sickroom Key", "Sickroom Key", Resi3LocationCategory.PICKUP),
        Resi3LocationData("470: DOCUMENT", "DOCUMENT", Resi3LocationCategory.PICKUP),
    ],
    "R409:B3 Corridor": [
    ],
    "R40A:Laboratory": [
        Resi3LocationData("456: HG bullets", "HG bullets", Resi3LocationCategory.PICKUP),
        Resi3LocationData("528: Green Herb", "Green Herb", Resi3LocationCategory.PICKUP),
        Resi3LocationData("590: Green Herb", "Green Herb", Resi3LocationCategory.PICKUP),
    ],
    "R40B:Synthesis Room": [
        Resi3LocationData("532: Vaccine Medium", "Vaccine Medium", Resi3LocationCategory.PICKUP),
        Resi3LocationData("704: Medium Base", "Medium Base", Resi3LocationCategory.PICKUP),
        Resi3LocationData("794: DOCUMENT", "DOCUMENT", Resi3LocationCategory.PICKUP),
    ],
    "R40C:Park Entrance": [
    ],
    "R40D:Fountain Room": [
        Resi3LocationData("3992: DOCUMENT", "DOCUMENT", Resi3LocationCategory.PICKUP),
        Resi3LocationData("4014: Green Herb", "Green Herb", Resi3LocationCategory.PICKUP),
        Resi3LocationData("4036: Green Herb", "Green Herb", Resi3LocationCategory.PICKUP),
        Resi3LocationData("4058: Green Herb", "Green Herb", Resi3LocationCategory.PICKUP),
        Resi3LocationData("4080: Blue Herb", "Blue Herb", Resi3LocationCategory.PICKUP),
        Resi3LocationData("4102: Blue Herb", "Blue Herb", Resi3LocationCategory.PICKUP),
    ],
    "R40E:Lake Passageway": [
    ],
    "R40F:Factory Approach": [
        Resi3LocationData("238: Magnum bullets", "Magnum bullets", Resi3LocationCategory.PICKUP),
        Resi3LocationData("302: Park Key(Graveyard)", "Park Key(Graveyard)", Resi3LocationCategory.PICKUP),
        Resi3LocationData("324: DOCUMENT", "DOCUMENT", Resi3LocationCategory.PICKUP),
    ],
    "R410:Fountain Tunnel": [
    ],
    "R411:Graveyard": [
        Resi3LocationData("178: Red Herb", "Red Herb", Resi3LocationCategory.PICKUP),
        Resi3LocationData("240: Red Herb", "Red Herb", Resi3LocationCategory.PICKUP),
    ],
    "R412:Graveyard Cabin": [
        Resi3LocationData("290: Iron Pipe", "Iron Pipe", Resi3LocationCategory.PICKUP),
        Resi3LocationData("392: GunPowder A", "GunPowder A", Resi3LocationCategory.PICKUP),
        Resi3LocationData("454: GunPowder A", "GunPowder A", Resi3LocationCategory.PICKUP),
        Resi3LocationData("516: GunPowder B", "GunPowder B", Resi3LocationCategory.PICKUP),
        Resi3LocationData("578: GunPowder B", "GunPowder B", Resi3LocationCategory.PICKUP),
    ],
    "R413:Graveyard Save": [
        Resi3LocationData("156: First Aid Spray", "First Aid Spray", Resi3LocationCategory.PICKUP),
    ],
    "R414:Graveyard Secret": [
        Resi3LocationData("112: Park Key(Rear)", "Park Key(Rear)", Resi3LocationCategory.PICKUP),
        Resi3LocationData("174: GL rounds(burst)", "GL rounds(burst)", Resi3LocationCategory.PICKUP),
        Resi3LocationData("266: Ink Ribbon", "Ink Ribbon", Resi3LocationCategory.PICKUP),
        Resi3LocationData("336: DOCUMENT", "DOCUMENT", Resi3LocationCategory.PICKUP),
        Resi3LocationData("398: DOCUMENT", "DOCUMENT", Resi3LocationCategory.PICKUP),
    ],
    "R415:Grave Digger Pit": [
    ],
    "R416:R416": [
    ],
    "R417:Hospital Street 2": [
    ],
    "R500:Factory 1F": [
        Resi3LocationData("956: Green Herb", "Green Herb", Resi3LocationCategory.PICKUP),
        Resi3LocationData("1018: Green Herb", "Green Herb", Resi3LocationCategory.PICKUP),
    ],
    "R501:Factory Save 1F": [
        Resi3LocationData("288: Ink Ribbon", "Ink Ribbon", Resi3LocationCategory.PICKUP),
        Resi3LocationData("350: First Aid Spray", "First Aid Spray", Resi3LocationCategory.PICKUP),
        Resi3LocationData("412: DOCUMENT", "DOCUMENT", Resi3LocationCategory.PICKUP),
        Resi3LocationData("474: Facility Key(no barcode)", "Facility Key(no barcode)", Resi3LocationCategory.PICKUP),
        Resi3LocationData("538: GunPowder A", "GunPowder A", Resi3LocationCategory.PICKUP),
        Resi3LocationData("600: GunPowder A", "GunPowder A", Resi3LocationCategory.PICKUP),
        Resi3LocationData("662: GunPowder A", "GunPowder A", Resi3LocationCategory.PICKUP),
        Resi3LocationData("724: GunPowder B", "GunPowder B", Resi3LocationCategory.PICKUP),
        Resi3LocationData("786: GunPowder B", "GunPowder B", Resi3LocationCategory.PICKUP),
        Resi3LocationData("848: GunPowder B", "GunPowder B", Resi3LocationCategory.PICKUP),
    ],
    "R502:Boiler Room": [
        Resi3LocationData("752: GL rounds(burst)", "GL rounds(burst)", Resi3LocationCategory.PICKUP),
        Resi3LocationData("814: GL rounds(burst)", "GL rounds(burst)", Resi3LocationCategory.PICKUP),
        Resi3LocationData("1020: Rocket Launcher", "Rocket Launcher", Resi3LocationCategory.PICKUP),
        Resi3LocationData("1084: Blue Herb", "Blue Herb", Resi3LocationCategory.PICKUP),
        Resi3LocationData("1146: Blue Herb", "Blue Herb", Resi3LocationCategory.PICKUP),
    ],
    "R503:Treatment Control": [
        Resi3LocationData("1564: Green Herb", "Green Herb", Resi3LocationCategory.PICKUP),
        Resi3LocationData("1626: Green Herb", "Green Herb", Resi3LocationCategory.PICKUP),
        Resi3LocationData("1688: Green Herb", "Green Herb", Resi3LocationCategory.PICKUP),
        Resi3LocationData("1750: DOCUMENT", "DOCUMENT", Resi3LocationCategory.PICKUP),
        Resi3LocationData("1812: System Disk", "System Disk", Resi3LocationCategory.PICKUP),
    ],
    "R504:Factory B1": [
    ],
    "R505:Factory B1 Save": [
        Resi3LocationData("166: DOCUMENT", "DOCUMENT", Resi3LocationCategory.PICKUP),
        Resi3LocationData("228: Water Sample", "Water Sample", Resi3LocationCategory.PICKUP),
        Resi3LocationData("362: Ink Ribbon", "Ink Ribbon", Resi3LocationCategory.PICKUP),
    ],
    "R506:Water Puzzle": [
        Resi3LocationData("870: GunPowder A", "GunPowder A", Resi3LocationCategory.PICKUP),
        Resi3LocationData("932: GunPowder A", "GunPowder A", Resi3LocationCategory.PICKUP),
        Resi3LocationData("994: GunPowder A", "GunPowder A", Resi3LocationCategory.PICKUP),
        Resi3LocationData("1056: GunPowder B", "GunPowder B", Resi3LocationCategory.PICKUP),
        Resi3LocationData("1118: GunPowder B", "GunPowder B", Resi3LocationCategory.PICKUP),
        Resi3LocationData("1180: GunPowder B", "GunPowder B", Resi3LocationCategory.PICKUP),
        Resi3LocationData("1244: First Aid Spray", "First Aid Spray", Resi3LocationCategory.PICKUP),
        Resi3LocationData("1306: Facility Key(barcode)", "Facility Key(barcode)", Resi3LocationCategory.PICKUP),
    ],
    "R507:Toxic Pool Room": [
        Resi3LocationData("2994: SG shells", "SG shells", Resi3LocationCategory.PICKUP),
        Resi3LocationData("3056: SG shells", "SG shells", Resi3LocationCategory.PICKUP),
    ],
    "R508:Disposal Access": [
    ],
    "R509:Disposal Chamber": [
        Resi3LocationData("134: Card Key", "Card Key", Resi3LocationCategory.PICKUP),
    ],
    "R50A:Communications Room": [
        Resi3LocationData("250: Magnum bullets", "Magnum bullets", Resi3LocationCategory.PICKUP),
        Resi3LocationData("272: First Aid Spray", "First Aid Spray", Resi3LocationCategory.PICKUP),
    ],
    "R50B:Hatch Escape Path": [
        Resi3LocationData("902: DOCUMENT", "DOCUMENT", Resi3LocationCategory.PICKUP),
        Resi3LocationData("964: SG shells", "SG shells", Resi3LocationCategory.PICKUP),
        Resi3LocationData("1026: SG shells", "SG shells", Resi3LocationCategory.PICKUP),
    ],
    "R50C:Car Cemetary": [
        Resi3LocationData("66: DOCUMENT", "DOCUMENT", Resi3LocationCategory.PICKUP),
    ],
    "R50D:Paracelsus Room": [
    ],
    "R50E:Chopper Departure": [
    ],
    "R50F:Escape Elevator": [
    ],
    "R510:Factory Access": [
    ]
}

code_data = 'room_table = [\n'
for key in location_tables:
    code_data += f'\t"{key}",\n'

print(code_data)
