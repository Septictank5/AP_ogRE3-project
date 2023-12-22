import settings
import typing
from .Options import RandomizeFun, resi3_options
from .Items import Resi3Item, item_dict, Resi3ItemCategory
from .Locations import Resi3Location, location_tables
from worlds.AutoWorld import World
from worlds.generic.Rules import set_rule, add_rule, forbid_items
from BaseClasses import Region, Entrance, ItemClassification

print("resident evil 3 found")


class Resi3Settings(settings.Group):
    class FolderPath(settings.UserFolderPath):
        """Resident Evil 3 Path"""
        description = "Path to BIOHAZARD(R) 3 PC.exe"

    filepath: FolderPath = FolderPath('')


class Resi3World(World):
    game = "Resident Evil 3"
    options_definitions: resi3_options
    settings: Resi3Settings
    topology_present = True
    base_id = 1234
    item_name_to_id = Resi3Item.get_name_to_id()
    location_name_to_id = Resi3Location.get_name_to_id()

    def create_item(self, name: str) -> Resi3Item:
        match item_dict[name].category:
            case Resi3ItemCategory.WEAPON | Resi3ItemCategory.WEAPONPART:
                classification = ItemClassification.useful
            case Resi3ItemCategory.KEY_ITEM | Resi3ItemCategory.GOAL_ITEM:
                classification = ItemClassification.progression
            # case Resi3ItemCategory.GOAL_ITEM:
            #     classification = ItemClassification.progression_skip_balancing
            case _:
                classification = ItemClassification.filler

        return Resi3Item(name, classification, self.item_name_to_id[name], self.player)

    def create_event(self, event: str) -> Resi3Item:
        return Resi3Item(event, ItemClassification.progression, None, self.player)

    def create_items(self):
        for room, data in location_tables.items():
            for location in data:
                if location.default_item in item_dict:
                    self.multiworld.itempool.append(self.create_item(location.default_item))
                else:
                    continue


    def create_regions(self):

        menu_region = Region("Menu", self.player, self.multiworld)
        self.multiworld.regions.append(menu_region)
        regions = {"Menu": menu_region}

        for entry, locations in location_tables.items():
            new_region = Region(entry, self.player, self.multiworld)
            for location in locations:
                new_location = Resi3Location(self.player, location.name, self.location_name_to_id[location.name], new_region)
                new_region.locations.append(new_location)
            regions.update({entry: new_region})
            self.multiworld.regions.append(new_region)

        def connect(from_region: str, to_region: str):
            connection = Entrance(self.player, f"Go to {to_region}", regions[from_region])
            regions[from_region].exits.append(connection)
            connection.connect(regions[to_region])

        regions["Menu"].exits.append(Entrance(self.player, "New Game", regions["Menu"]))
        self.multiworld.get_entrance("New Game", self.player).connect(regions["Warehouse"])

        connect("Warehouse", "Warehouse Alley 2")
        connect("Warehouse Alley 2", "Warehouse Street 2")

        connect("Warehouse Street 2", "Basement Alley")

        connect("Basement Alley", "Bar Jack Street")

        connect("Bar Jack Street", "Bar Jack Alley 2")

        connect("Bar Jack Alley 2", "Bar Jack")
        connect("Bar Jack Alley 2", "Barricade Alley")

        connect("Barricade Alley", "Hydrant Alley 2")

        connect("Hydrant Alley 2", "RPD Street 2")
        connect("Hydrant Alley 2", "Hydrant Save")
        connect("Hydrant Alley 2", "Back Alley")

        connect("RPD Street 2", "RPD Front")
        connect("RPD Street 2", "Party Alley")

        connect("RPD Front", "RPD Hall")

        connect("RPD Hall", "RPD Big Office")

        connect("RPD Big Office", "RPD Evidence Room")

        connect("RPD Evidence Room", "RPD Stairs 1F")

        connect("RPD Stairs 1F", "RPD Dark Room")
        connect("RPD Stairs 1F", "RPD Stairs 2F")
        connect("RPD Stairs 1F", "RPD Corridor")

        connect("RPD Stairs 2F", "RPD STARS Corridor")

        connect("RPD Corridor", "RPD Meeting Room")

        connect("RPD STARS Corridor", "STARS Office")

        # Make this not jank!!
        connect("STARS Office", "Trailer")

        connect("Bar Jack Alley 2", "Bar Jack Alley Loot")

        connect("Back Alley", "Alleyway Outside Pharmacy")

        connect("Alleyway Outside Pharmacy", "Pharmacy Room 1")

        connect("Pharmacy Room 1", "Pharmacy Room 2")

        # Credits to Reven
        connect("Party Alley", "Fire Hose Alley")
        connect("Fire Hose Alley", "Bus Street")
        # End Credits to Reven

        connect("Bus Street", "Parking Lot")

        connect("Parking Lot", "Parking Lot Save")

        connect("Parking Lot Save", "Parking Lot Back")

        connect("Parking Lot Back", "Construction Site")

        connect("Construction Site", "Power Station Front")
        connect("Construction Site", "Restaurant Front")

        connect("Power Station Front", "Power Station Access")

        connect("Power Station Access", "Power Station")

        connect("Restaurant Front", "Restaurant")
        connect("Restaurant Front", "Shopping Alley")

        connect("Restaurant", "Restaurant Basement")

        connect("Shopping Alley", "Shopping Save")
        connect("Shopping Alley", "Press Street")

        connect("Press Street", "Press Entrance")
        connect("Press Street", "Municipal Alley")

        connect("Press Entrance", "Press Offices")

        connect("Municipal Alley", "Grave Digger Alley")
        connect("Municipal Alley", "Stagla Gas Outside")

        connect("Grave Digger Alley", "Train Station")

        connect("Train Station", "Cable Car")

        connect("Stagla Gas Outside", "Stagla Gas")

        connect("Stagla Gas", "Stagla Escape")

        connect("Cable Car", "Cable Car Moving")
        connect("Cable Car Moving", "ClockTower Bedroom")

        connect("Warehouse", "ClockTower Piano Room")
        connect("ClockTower Piano Room", "ClockTower Chapel")
        connect("ClockTower Piano Room", "ClockTower Dining Room")
        connect("ClockTower Dining Room", "ClockTower Hall 1F")
        connect("ClockTower Hall 1F", "ClockTower Outdoor")
        connect("ClockTower Hall 1F", "ClockTower Hall 2F")
        connect("ClockTower Hall 1F", "ClockTower Library")
        connect("ClockTower Hall 2F", "Tower Outdoor")
        connect("Tower Outdoor", "ClockTower")
        connect("ClockTower Library", "Chronos Corridor")
        connect("Chronos Corridor", "Chronos Room 2")
        connect("Chronos Room 2", "Hospital Street")
        connect("Hospital Street", "Office Save")
        connect("Hospital Street", "Hospital Hall")
        connect("Hospital Street", "Park Entrance")

        connect("Park Entrance", "Lake Passageway")
        connect("Lake Passageway", "Factory Approach")
        connect("Park Entrance", "Fountain Room")
        connect("Fountain Room", "Fountain Tunnel")
        connect("Fountain Tunnel", "Graveyard")
        connect("Graveyard", "Graveyard Cabin")
        connect("Graveyard Cabin", "Graveyard Save")
        connect("Graveyard Cabin", "Graveyard Secret")

        connect("ClockTower Library", "ClockTower Chess Room")
        connect("ClockTower Chess Room", "Boiler Room")

        connect("Hospital Hall", "Reception")
        connect("Reception", "Staff Room")
        connect("Staff Room", "4F Corridor")
        connect("Staff Room", "B3 Corridor")
        connect("4F Corridor", "Room 401")
        connect("4F Corridor", "Room 402")
        connect("4F Corridor", "Data Room")
        connect("B3 Corridor", "Laboratory")
        connect("Laboratory", "Synthesis Room")

        connect("Boiler Room", "Factory Save 1F")
        connect("Factory Save 1F", "Factory 1F")
        connect("Factory 1F", "Treatment Control")
        connect("Factory 1F", "Factory Path")

        connect("Treatment Control", "Toxic Pool Room")
        connect("Treatment Control", "Disposal Access")

        connect("Toxic Pool Room", "Factory B1")

        connect("Factory B1", "Factory B1 Save")

        connect("Factory B1 Save", "Water Puzzle")

        connect("Disposal Access", "Disposal Chamber")

        connect("Factory Path", "Communications Room")
        connect("Communications Room", "Hatch Escape Path")
        connect("Hatch Escape Path", "Car Cemetary")
        connect("Car Cemetary", "Chopper Departure")

    def set_rules(self) -> None:
        set_rule(self.multiworld.get_entrance("Go to Warehouse Alley 2", self.player),
                 lambda state: state.has("Warehouse Key (BackDoor)", self.player))
        add_rule(self.multiworld.get_entrance("Go to Hydrant Alley 2", self.player),
                 lambda state: state.has("Lighter Oil", self.player))
        add_rule(self.multiworld.get_entrance("Go to Hydrant Alley 2", self.player),
                 lambda state: state.has("Lighter Case", self.player))
        set_rule(self.multiworld.get_entrance("Go to Party Alley", self.player),
                 lambda state: state.has("Lockpick", self.player))
        set_rule(self.multiworld.get_entrance("Go to STARS Office", self.player),
                 lambda state: state.has("Emblem Key", self.player))
        set_rule(self.multiworld.get_entrance("Go to Back Alley", self.player),
                 lambda state: state.has("Fire Hose", self.player))
        set_rule(self.multiworld.get_entrance("Go to Restaurant Basement", self.player),
                 lambda state: state.has("Iron Pipe", self.player))
        set_rule(self.multiworld.get_location("R113-600: GunPowder B", self.player),
                 lambda state: state.has("Lockpick", self.player))
        add_rule(self.multiworld.get_entrance("Go to Municipal Alley", self.player),
                 lambda state: state.has("Green Gem", self.player))
        add_rule(self.multiworld.get_entrance("Go to Municipal Alley", self.player),
                 lambda state: state.has("Blue Gem", self.player))
        set_rule(self.multiworld.get_entrance("Go to Power Station Front", self.player),
                 lambda state: state.has("Battery", self.player))
        set_rule(self.multiworld.get_location("R211-970: Fire Hook", self.player),
                 lambda state: state.has("Lockpick", self.player))
        add_rule(self.multiworld.get_entrance("Go to Cable Car Moving", self.player),
                 lambda state: state.has("Additive", self.player))
        add_rule(self.multiworld.get_entrance("Go to Cable Car Moving", self.player),
                 lambda state: state.has("Fuse", self.player))
        add_rule(self.multiworld.get_entrance("Go to Cable Car Moving", self.player),
                 lambda state: state.has("Power Cable", self.player))
        add_rule(self.multiworld.get_entrance("Go to Cable Car Moving", self.player),
                 lambda state: state.has("Wrench", self.player))
        add_rule(self.multiworld.get_entrance("Go to Cable Car Moving", self.player),
                 lambda state: state.has("Machine Oil", self.player))
        add_rule(self.multiworld.get_entrance("Go to Park Entrance", self.player),
                 lambda state: state.has("Park Key(front)", self.player))
        set_rule(self.multiworld.get_entrance("Go to Graveyard Cabin", self.player),
                 lambda state: state.has("Park Key(Graveyard)", self.player))
        set_rule(self.multiworld.get_entrance("Go to Factory 1F", self.player),
                 lambda state: state.has("Park Key(Rear)", self.player))
        set_rule(self.multiworld.get_entrance("Go to Treatment Control", self.player),
                 lambda state: state.has("Facility Key(no barcode)", self.player))
        add_rule(self.multiworld.get_entrance("Go to Disposal Chamber", self.player),
                 lambda state: state.has("System Disk", self.player))
        add_rule(self.multiworld.get_entrance("Go to Disposal Chamber", self.player),
                 lambda state: state.has("Water Sample", self.player))
        set_rule(self.multiworld.get_location("R506-1306: Facility Key(barcode)", self.player),
                 lambda state: state.has("Card Key", self.player))
        set_rule(self.multiworld.get_entrance("Go to Communications Room", self.player),
                 lambda state: state.has("Card Key", self.player))
        set_rule(self.multiworld.get_location("R205-1354: Bronze Compass", self.player),
                 lambda state: state.has("Bronze Book", self.player))
        set_rule(self.multiworld.get_location("R208-3894: Battery", self.player),
                 lambda state: state.has("Bronze Compass", self.player))
        set_rule(self.multiworld.get_location("R113-488: Emblem Key", self.player),
                 lambda state: state.has("Jill's STARS Card", self.player))
        add_rule(self.multiworld.get_entrance("Go to Stagla Gas", self.player),
                 lambda state: state.has("Wrench", self.player))
        add_rule(self.multiworld.get_entrance("Go to Stagla Gas", self.player),
                 lambda state: state.has("Rusted Crank", self.player))
        set_rule(self.multiworld.get_location("R218-936: Fire Hose", self.player),
                 lambda state: state.has("Wrench", self.player))
        set_rule(self.multiworld.get_entrance("Go to ClockTower", self.player),
                 lambda state: state.has("Clock Tower Key(Winder)", self.player))
        set_rule(self.multiworld.get_entrance("Go to Factory Path", self.player),
                 lambda state: state.has("Card Key", self.player))
        add_rule(self.multiworld.get_entrance("Go to Chronos Corridor", self.player),
                 lambda state: state.has("Clock Tower Key(Winder)", self.player))
        add_rule(self.multiworld.get_entrance("Go to Chronos Corridor", self.player),
                 lambda state: state.has("Chronos Chain", self.player))
        set_rule(self.multiworld.get_entrance("Go to Room 402", self.player),
                 lambda state: state.has("Sickroom Key", self.player))
        set_rule(self.multiworld.get_entrance("Go to Bar Jack Alley Loot", self.player),
                 lambda state: state.has("Square Crank", self.player))

    def generate_basic(self) -> None:
        self.multiworld.get_location("MadeVictory", self.player).place_locked_item(self.create_event("Victory"))
        self.multiworld.completion_condition[self.player] = lambda state: state.has("Victory", self.player)

    def generate_output(self, output_directory: str) -> None:
        # path = self.settings.filepath
        # print(path)
        for location in self.multiworld.get_locations(self.player):
            print(location, '-', location.item)


