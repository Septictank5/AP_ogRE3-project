"""
Looks through data object to double-check it makes sense. Will fail for missing or duplicate definitions or
duplicate claims and give warnings for unused and unignored locations or warps.
"""
import logging
from typing import List

from .data import data


_ignorable_locations = {
    # Trick House
    "HIDDEN_ITEM_TRICK_HOUSE_NUGGET",
    "ITEM_TRICK_HOUSE_PUZZLE_1_ORANGE_MAIL",
    "ITEM_TRICK_HOUSE_PUZZLE_2_HARBOR_MAIL",
    "ITEM_TRICK_HOUSE_PUZZLE_2_WAVE_MAIL",
    "ITEM_TRICK_HOUSE_PUZZLE_3_SHADOW_MAIL",
    "ITEM_TRICK_HOUSE_PUZZLE_3_WOOD_MAIL",
    "ITEM_TRICK_HOUSE_PUZZLE_4_MECH_MAIL",
    "ITEM_TRICK_HOUSE_PUZZLE_6_GLITTER_MAIL",
    "ITEM_TRICK_HOUSE_PUZZLE_7_TROPIC_MAIL",
    "ITEM_TRICK_HOUSE_PUZZLE_8_BEAD_MAIL",

    # Battle Frontier
    "ITEM_ARTISAN_CAVE_1F_CARBOS",
    "ITEM_ARTISAN_CAVE_B1F_HP_UP",
    "HIDDEN_ITEM_ARTISAN_CAVE_B1F_CALCIUM",
    "HIDDEN_ITEM_ARTISAN_CAVE_B1F_IRON",
    "HIDDEN_ITEM_ARTISAN_CAVE_B1F_PROTEIN",
    "HIDDEN_ITEM_ARTISAN_CAVE_B1F_ZINC",

    # Event islands
    "HIDDEN_ITEM_NAVEL_ROCK_TOP_SACRED_ASH"
}

_ignorable_warps = {
    # Trick House
    "MAP_ROUTE110_TRICK_HOUSE_PUZZLE2:0,1/MAP_ROUTE110_TRICK_HOUSE_ENTRANCE:2!",
    "MAP_ROUTE110_TRICK_HOUSE_PUZZLE2:2/MAP_ROUTE110_TRICK_HOUSE_END:0!",
    "MAP_ROUTE110_TRICK_HOUSE_PUZZLE3:0,1/MAP_ROUTE110_TRICK_HOUSE_ENTRANCE:2!",
    "MAP_ROUTE110_TRICK_HOUSE_PUZZLE3:2/MAP_ROUTE110_TRICK_HOUSE_END:0!",
    "MAP_ROUTE110_TRICK_HOUSE_PUZZLE4:0,1/MAP_ROUTE110_TRICK_HOUSE_ENTRANCE:2!",
    "MAP_ROUTE110_TRICK_HOUSE_PUZZLE4:2/MAP_ROUTE110_TRICK_HOUSE_END:0!",
    "MAP_ROUTE110_TRICK_HOUSE_PUZZLE5:0,1/MAP_ROUTE110_TRICK_HOUSE_ENTRANCE:2!",
    "MAP_ROUTE110_TRICK_HOUSE_PUZZLE5:2/MAP_ROUTE110_TRICK_HOUSE_END:0!",
    "MAP_ROUTE110_TRICK_HOUSE_PUZZLE6:0,1/MAP_ROUTE110_TRICK_HOUSE_ENTRANCE:2!",
    "MAP_ROUTE110_TRICK_HOUSE_PUZZLE6:2/MAP_ROUTE110_TRICK_HOUSE_END:0!",
    "MAP_ROUTE110_TRICK_HOUSE_PUZZLE7:0,1/MAP_ROUTE110_TRICK_HOUSE_ENTRANCE:2!",
    "MAP_ROUTE110_TRICK_HOUSE_PUZZLE7:10/MAP_ROUTE110_TRICK_HOUSE_PUZZLE7:9",
    "MAP_ROUTE110_TRICK_HOUSE_PUZZLE7:11/MAP_ROUTE110_TRICK_HOUSE_PUZZLE7:12",
    "MAP_ROUTE110_TRICK_HOUSE_PUZZLE7:12/MAP_ROUTE110_TRICK_HOUSE_PUZZLE7:11",
    "MAP_ROUTE110_TRICK_HOUSE_PUZZLE7:2/MAP_ROUTE110_TRICK_HOUSE_END:0!",
    "MAP_ROUTE110_TRICK_HOUSE_PUZZLE7:3/MAP_ROUTE110_TRICK_HOUSE_PUZZLE7:4",
    "MAP_ROUTE110_TRICK_HOUSE_PUZZLE7:4/MAP_ROUTE110_TRICK_HOUSE_PUZZLE7:3",
    "MAP_ROUTE110_TRICK_HOUSE_PUZZLE7:5/MAP_ROUTE110_TRICK_HOUSE_PUZZLE7:6",
    "MAP_ROUTE110_TRICK_HOUSE_PUZZLE7:6/MAP_ROUTE110_TRICK_HOUSE_PUZZLE7:5",
    "MAP_ROUTE110_TRICK_HOUSE_PUZZLE7:7/MAP_ROUTE110_TRICK_HOUSE_PUZZLE7:8",
    "MAP_ROUTE110_TRICK_HOUSE_PUZZLE7:8/MAP_ROUTE110_TRICK_HOUSE_PUZZLE7:7",
    "MAP_ROUTE110_TRICK_HOUSE_PUZZLE7:9/MAP_ROUTE110_TRICK_HOUSE_PUZZLE7:10",
    "MAP_ROUTE110_TRICK_HOUSE_PUZZLE8:0,1/MAP_ROUTE110_TRICK_HOUSE_ENTRANCE:2!",
    "MAP_ROUTE110_TRICK_HOUSE_PUZZLE8:2/MAP_ROUTE110_TRICK_HOUSE_END:0!",

    # Department store elevator
    "MAP_LILYCOVE_CITY_DEPARTMENT_STORE_ELEVATOR:0,1/MAP_DYNAMIC:-1!",
    "MAP_LILYCOVE_CITY_DEPARTMENT_STORE_1F:3/MAP_LILYCOVE_CITY_DEPARTMENT_STORE_ELEVATOR:0!",
    "MAP_LILYCOVE_CITY_DEPARTMENT_STORE_2F:2/MAP_LILYCOVE_CITY_DEPARTMENT_STORE_ELEVATOR:0!",
    "MAP_LILYCOVE_CITY_DEPARTMENT_STORE_3F:2/MAP_LILYCOVE_CITY_DEPARTMENT_STORE_ELEVATOR:0!",
    "MAP_LILYCOVE_CITY_DEPARTMENT_STORE_4F:2/MAP_LILYCOVE_CITY_DEPARTMENT_STORE_ELEVATOR:0!",
    "MAP_LILYCOVE_CITY_DEPARTMENT_STORE_5F:1/MAP_LILYCOVE_CITY_DEPARTMENT_STORE_ELEVATOR:0!",

    # Intro truck
    "MAP_INSIDE_OF_TRUCK:0,1,2/MAP_DYNAMIC:-1!",

    # Battle Frontier
    "MAP_BATTLE_FRONTIER_BATTLE_ARENA_LOBBY:0/MAP_BATTLE_FRONTIER_OUTSIDE_EAST:1",
    "MAP_BATTLE_FRONTIER_BATTLE_DOME_CORRIDOR:0,1/MAP_BATTLE_FRONTIER_OUTSIDE_WEST:1!",
    "MAP_BATTLE_FRONTIER_BATTLE_DOME_LOBBY:0,1/MAP_BATTLE_FRONTIER_OUTSIDE_WEST:1",
    "MAP_BATTLE_FRONTIER_BATTLE_DOME_PRE_BATTLE_ROOM:0,1/MAP_BATTLE_FRONTIER_OUTSIDE_WEST:1!",
    "MAP_BATTLE_FRONTIER_BATTLE_FACTORY_LOBBY:0,1/MAP_BATTLE_FRONTIER_OUTSIDE_WEST:2",
    "MAP_BATTLE_FRONTIER_BATTLE_PALACE_BATTLE_ROOM:0,1/MAP_BATTLE_FRONTIER_BATTLE_PALACE_CORRIDOR:2",
    "MAP_BATTLE_FRONTIER_BATTLE_PALACE_CORRIDOR:0,1/MAP_BATTLE_FRONTIER_BATTLE_PALACE_LOBBY:2",
    "MAP_BATTLE_FRONTIER_BATTLE_PALACE_CORRIDOR:2/MAP_BATTLE_FRONTIER_BATTLE_PALACE_BATTLE_ROOM:0",
    "MAP_BATTLE_FRONTIER_BATTLE_PALACE_CORRIDOR:3/MAP_BATTLE_FRONTIER_BATTLE_PALACE_BATTLE_ROOM:0!",
    "MAP_BATTLE_FRONTIER_BATTLE_PALACE_LOBBY:0,1/MAP_BATTLE_FRONTIER_OUTSIDE_EAST:2",
    "MAP_BATTLE_FRONTIER_BATTLE_PALACE_LOBBY:2/MAP_BATTLE_FRONTIER_BATTLE_PALACE_CORRIDOR:0",
    "MAP_BATTLE_FRONTIER_BATTLE_PIKE_LOBBY:0,1,2/MAP_BATTLE_FRONTIER_OUTSIDE_WEST:0",
    "MAP_BATTLE_FRONTIER_BATTLE_PYRAMID_LOBBY:0/MAP_BATTLE_FRONTIER_OUTSIDE_EAST:3",
    "MAP_BATTLE_FRONTIER_BATTLE_TOWER_BATTLE_ROOM:0,1/MAP_BATTLE_FRONTIER_BATTLE_TOWER_LOBBY:2",
    "MAP_BATTLE_FRONTIER_BATTLE_TOWER_LOBBY:0,1/MAP_BATTLE_FRONTIER_OUTSIDE_EAST:0",
    "MAP_BATTLE_FRONTIER_BATTLE_TOWER_LOBBY:2/MAP_BATTLE_FRONTIER_BATTLE_TOWER_BATTLE_ROOM:0",
    "MAP_BATTLE_FRONTIER_EXCHANGE_SERVICE_CORNER:0,1,2/MAP_BATTLE_FRONTIER_OUTSIDE_EAST:6",
    "MAP_BATTLE_FRONTIER_LOUNGE1:0/MAP_BATTLE_FRONTIER_OUTSIDE_EAST:5",
    "MAP_BATTLE_FRONTIER_LOUNGE2:0,1/MAP_BATTLE_FRONTIER_OUTSIDE_WEST:3",
    "MAP_BATTLE_FRONTIER_LOUNGE3:0/MAP_BATTLE_FRONTIER_OUTSIDE_EAST:9",
    "MAP_BATTLE_FRONTIER_LOUNGE4:0/MAP_BATTLE_FRONTIER_OUTSIDE_WEST:6",
    "MAP_BATTLE_FRONTIER_LOUNGE5:0,1/MAP_BATTLE_FRONTIER_OUTSIDE_EAST:7",
    "MAP_BATTLE_FRONTIER_LOUNGE6:0/MAP_BATTLE_FRONTIER_OUTSIDE_EAST:8",
    "MAP_BATTLE_FRONTIER_LOUNGE7:0/MAP_BATTLE_FRONTIER_OUTSIDE_WEST:7",
    "MAP_BATTLE_FRONTIER_LOUNGE8:0/MAP_BATTLE_FRONTIER_OUTSIDE_EAST:10",
    "MAP_BATTLE_FRONTIER_LOUNGE9:0,1/MAP_BATTLE_FRONTIER_OUTSIDE_EAST:11",
    "MAP_BATTLE_FRONTIER_MART:0,1/MAP_BATTLE_FRONTIER_OUTSIDE_WEST:4",
    "MAP_BATTLE_FRONTIER_OUTSIDE_EAST:0/MAP_BATTLE_FRONTIER_BATTLE_TOWER_LOBBY:0",
    "MAP_BATTLE_FRONTIER_OUTSIDE_EAST:1/MAP_BATTLE_FRONTIER_BATTLE_ARENA_LOBBY:0",
    "MAP_BATTLE_FRONTIER_OUTSIDE_EAST:10/MAP_BATTLE_FRONTIER_LOUNGE8:0",
    "MAP_BATTLE_FRONTIER_OUTSIDE_EAST:11/MAP_BATTLE_FRONTIER_LOUNGE9:0",
    "MAP_BATTLE_FRONTIER_OUTSIDE_EAST:12/MAP_BATTLE_FRONTIER_POKEMON_CENTER_1F:0",
    "MAP_BATTLE_FRONTIER_OUTSIDE_EAST:13/MAP_ARTISAN_CAVE_1F:0",
    "MAP_BATTLE_FRONTIER_OUTSIDE_EAST:2/MAP_BATTLE_FRONTIER_BATTLE_PALACE_LOBBY:0",
    "MAP_BATTLE_FRONTIER_OUTSIDE_EAST:3/MAP_BATTLE_FRONTIER_BATTLE_PYRAMID_LOBBY:0",
    "MAP_BATTLE_FRONTIER_OUTSIDE_EAST:4/MAP_BATTLE_FRONTIER_RANKING_HALL:0",
    "MAP_BATTLE_FRONTIER_OUTSIDE_EAST:5/MAP_BATTLE_FRONTIER_LOUNGE1:0",
    "MAP_BATTLE_FRONTIER_OUTSIDE_EAST:6/MAP_BATTLE_FRONTIER_EXCHANGE_SERVICE_CORNER:0",
    "MAP_BATTLE_FRONTIER_OUTSIDE_EAST:7/MAP_BATTLE_FRONTIER_LOUNGE5:0",
    "MAP_BATTLE_FRONTIER_OUTSIDE_EAST:8/MAP_BATTLE_FRONTIER_LOUNGE6:0",
    "MAP_BATTLE_FRONTIER_OUTSIDE_EAST:9/MAP_BATTLE_FRONTIER_LOUNGE3:0",
    "MAP_BATTLE_FRONTIER_OUTSIDE_WEST:0/MAP_BATTLE_FRONTIER_BATTLE_PIKE_LOBBY:0",
    "MAP_BATTLE_FRONTIER_OUTSIDE_WEST:1/MAP_BATTLE_FRONTIER_BATTLE_DOME_LOBBY:0",
    "MAP_BATTLE_FRONTIER_OUTSIDE_WEST:10/MAP_ARTISAN_CAVE_B1F:0",
    "MAP_BATTLE_FRONTIER_OUTSIDE_WEST:2/MAP_BATTLE_FRONTIER_BATTLE_FACTORY_LOBBY:0",
    "MAP_BATTLE_FRONTIER_OUTSIDE_WEST:3/MAP_BATTLE_FRONTIER_LOUNGE2:0",
    "MAP_BATTLE_FRONTIER_OUTSIDE_WEST:4/MAP_BATTLE_FRONTIER_MART:0",
    "MAP_BATTLE_FRONTIER_OUTSIDE_WEST:5/MAP_BATTLE_FRONTIER_SCOTTS_HOUSE:0",
    "MAP_BATTLE_FRONTIER_OUTSIDE_WEST:6/MAP_BATTLE_FRONTIER_LOUNGE4:0",
    "MAP_BATTLE_FRONTIER_OUTSIDE_WEST:7/MAP_BATTLE_FRONTIER_LOUNGE7:0",
    "MAP_BATTLE_FRONTIER_OUTSIDE_WEST:8/MAP_BATTLE_FRONTIER_RECEPTION_GATE:0",
    "MAP_BATTLE_FRONTIER_OUTSIDE_WEST:9/MAP_BATTLE_FRONTIER_RECEPTION_GATE:1",
    "MAP_BATTLE_FRONTIER_POKEMON_CENTER_1F:0,1/MAP_BATTLE_FRONTIER_OUTSIDE_EAST:12",
    "MAP_BATTLE_FRONTIER_POKEMON_CENTER_1F:2/MAP_BATTLE_FRONTIER_POKEMON_CENTER_2F:0",
    "MAP_BATTLE_FRONTIER_POKEMON_CENTER_2F:0/MAP_BATTLE_FRONTIER_POKEMON_CENTER_1F:2",
    "MAP_BATTLE_FRONTIER_RANKING_HALL:0,1/MAP_BATTLE_FRONTIER_OUTSIDE_EAST:4",
    "MAP_BATTLE_FRONTIER_RECEPTION_GATE:0/MAP_BATTLE_FRONTIER_OUTSIDE_WEST:8",
    "MAP_BATTLE_FRONTIER_RECEPTION_GATE:1/MAP_BATTLE_FRONTIER_OUTSIDE_WEST:9",
    "MAP_BATTLE_FRONTIER_SCOTTS_HOUSE:0,1/MAP_BATTLE_FRONTIER_OUTSIDE_WEST:5",

    "MAP_ARTISAN_CAVE_1F:0/MAP_BATTLE_FRONTIER_OUTSIDE_EAST:13",
    "MAP_ARTISAN_CAVE_1F:1/MAP_ARTISAN_CAVE_B1F:1",
    "MAP_ARTISAN_CAVE_B1F:0/MAP_BATTLE_FRONTIER_OUTSIDE_WEST:10",
    "MAP_ARTISAN_CAVE_B1F:1/MAP_ARTISAN_CAVE_1F:1",

    # Terra Cave and Marine Cave
    "MAP_TERRA_CAVE_ENTRANCE:0/MAP_DYNAMIC:-1!",
    "MAP_TERRA_CAVE_END:0/MAP_TERRA_CAVE_ENTRANCE:1",
    "MAP_TERRA_CAVE_ENTRANCE:1/MAP_TERRA_CAVE_END:0",
    "MAP_ROUTE113:1/MAP_TERRA_CAVE_ENTRANCE:0!",
    "MAP_ROUTE113:2/MAP_TERRA_CAVE_ENTRANCE:0!",
    "MAP_ROUTE114:3/MAP_TERRA_CAVE_ENTRANCE:0!",
    "MAP_ROUTE114:4/MAP_TERRA_CAVE_ENTRANCE:0!",
    "MAP_ROUTE115:1/MAP_TERRA_CAVE_ENTRANCE:0!",
    "MAP_ROUTE115:2/MAP_TERRA_CAVE_ENTRANCE:0!",
    "MAP_ROUTE116:3/MAP_TERRA_CAVE_ENTRANCE:0!",
    "MAP_ROUTE116:4/MAP_TERRA_CAVE_ENTRANCE:0!",
    "MAP_ROUTE118:0/MAP_TERRA_CAVE_ENTRANCE:0!",
    "MAP_ROUTE118:1/MAP_TERRA_CAVE_ENTRANCE:0!",

    "MAP_UNDERWATER_MARINE_CAVE:0/MAP_DYNAMIC:-1!",
    "MAP_MARINE_CAVE_END:0/MAP_MARINE_CAVE_ENTRANCE:0",
    "MAP_MARINE_CAVE_ENTRANCE:0/MAP_MARINE_CAVE_END:0",
    "MAP_UNDERWATER_ROUTE105:0/MAP_UNDERWATER_MARINE_CAVE:0!",
    "MAP_UNDERWATER_ROUTE105:1/MAP_UNDERWATER_MARINE_CAVE:0!",
    "MAP_UNDERWATER_ROUTE125:0/MAP_UNDERWATER_MARINE_CAVE:0!",
    "MAP_UNDERWATER_ROUTE125:1/MAP_UNDERWATER_MARINE_CAVE:0!",
    "MAP_UNDERWATER_ROUTE127:0/MAP_UNDERWATER_MARINE_CAVE:0!",
    "MAP_UNDERWATER_ROUTE127:1/MAP_UNDERWATER_MARINE_CAVE:0!",
    "MAP_UNDERWATER_ROUTE129:0/MAP_UNDERWATER_MARINE_CAVE:0!",
    "MAP_UNDERWATER_ROUTE129:1/MAP_UNDERWATER_MARINE_CAVE:0!",

    # Event islands
    "MAP_BIRTH_ISLAND_EXTERIOR:0/MAP_BIRTH_ISLAND_HARBOR:0",
    "MAP_BIRTH_ISLAND_HARBOR:0/MAP_BIRTH_ISLAND_EXTERIOR:0",

    "MAP_FARAWAY_ISLAND_ENTRANCE:0,1/MAP_FARAWAY_ISLAND_INTERIOR:0,1",
    "MAP_FARAWAY_ISLAND_INTERIOR:0,1/MAP_FARAWAY_ISLAND_ENTRANCE:0,1",

    "MAP_SOUTHERN_ISLAND_EXTERIOR:0,1/MAP_SOUTHERN_ISLAND_INTERIOR:0,1",
    "MAP_SOUTHERN_ISLAND_INTERIOR:0,1/MAP_SOUTHERN_ISLAND_EXTERIOR:0,1",

    "MAP_NAVEL_ROCK_B1F:0/MAP_NAVEL_ROCK_ENTRANCE:0",
    "MAP_NAVEL_ROCK_B1F:1/MAP_NAVEL_ROCK_FORK:1",
    "MAP_NAVEL_ROCK_BOTTOM:0/MAP_NAVEL_ROCK_DOWN11:0",
    "MAP_NAVEL_ROCK_DOWN01:0/MAP_NAVEL_ROCK_FORK:2",
    "MAP_NAVEL_ROCK_DOWN01:1/MAP_NAVEL_ROCK_DOWN02:0",
    "MAP_NAVEL_ROCK_DOWN02:0/MAP_NAVEL_ROCK_DOWN01:1",
    "MAP_NAVEL_ROCK_DOWN02:1/MAP_NAVEL_ROCK_DOWN03:0",
    "MAP_NAVEL_ROCK_DOWN03:0/MAP_NAVEL_ROCK_DOWN02:1",
    "MAP_NAVEL_ROCK_DOWN03:1/MAP_NAVEL_ROCK_DOWN04:0",
    "MAP_NAVEL_ROCK_DOWN04:0/MAP_NAVEL_ROCK_DOWN03:1",
    "MAP_NAVEL_ROCK_DOWN04:1/MAP_NAVEL_ROCK_DOWN05:0",
    "MAP_NAVEL_ROCK_DOWN05:0/MAP_NAVEL_ROCK_DOWN04:1",
    "MAP_NAVEL_ROCK_DOWN05:1/MAP_NAVEL_ROCK_DOWN06:0",
    "MAP_NAVEL_ROCK_DOWN06:0/MAP_NAVEL_ROCK_DOWN05:1",
    "MAP_NAVEL_ROCK_DOWN06:1/MAP_NAVEL_ROCK_DOWN07:0",
    "MAP_NAVEL_ROCK_DOWN07:0/MAP_NAVEL_ROCK_DOWN06:1",
    "MAP_NAVEL_ROCK_DOWN07:1/MAP_NAVEL_ROCK_DOWN08:0",
    "MAP_NAVEL_ROCK_DOWN08:0/MAP_NAVEL_ROCK_DOWN07:1",
    "MAP_NAVEL_ROCK_DOWN08:1/MAP_NAVEL_ROCK_DOWN09:0",
    "MAP_NAVEL_ROCK_DOWN09:0/MAP_NAVEL_ROCK_DOWN08:1",
    "MAP_NAVEL_ROCK_DOWN09:1/MAP_NAVEL_ROCK_DOWN10:0",
    "MAP_NAVEL_ROCK_DOWN10:0/MAP_NAVEL_ROCK_DOWN09:1",
    "MAP_NAVEL_ROCK_DOWN10:1/MAP_NAVEL_ROCK_DOWN11:1",
    "MAP_NAVEL_ROCK_DOWN11:0/MAP_NAVEL_ROCK_BOTTOM:0",
    "MAP_NAVEL_ROCK_DOWN11:1/MAP_NAVEL_ROCK_DOWN10:1",
    "MAP_NAVEL_ROCK_ENTRANCE:0/MAP_NAVEL_ROCK_B1F:0",
    "MAP_NAVEL_ROCK_ENTRANCE:1/MAP_NAVEL_ROCK_EXTERIOR:1",
    "MAP_NAVEL_ROCK_EXTERIOR:0/MAP_NAVEL_ROCK_HARBOR:0",
    "MAP_NAVEL_ROCK_EXTERIOR:1/MAP_NAVEL_ROCK_ENTRANCE:1",
    "MAP_NAVEL_ROCK_FORK:0/MAP_NAVEL_ROCK_UP1:0",
    "MAP_NAVEL_ROCK_FORK:1/MAP_NAVEL_ROCK_B1F:1",
    "MAP_NAVEL_ROCK_FORK:2/MAP_NAVEL_ROCK_DOWN01:0",
    "MAP_NAVEL_ROCK_HARBOR:0/MAP_NAVEL_ROCK_EXTERIOR:0",
    "MAP_NAVEL_ROCK_TOP:0/MAP_NAVEL_ROCK_UP4:1",
    "MAP_NAVEL_ROCK_UP1:0/MAP_NAVEL_ROCK_FORK:0",
    "MAP_NAVEL_ROCK_UP1:1/MAP_NAVEL_ROCK_UP2:0",
    "MAP_NAVEL_ROCK_UP2:0/MAP_NAVEL_ROCK_UP1:1",
    "MAP_NAVEL_ROCK_UP2:1/MAP_NAVEL_ROCK_UP3:0",
    "MAP_NAVEL_ROCK_UP3:0/MAP_NAVEL_ROCK_UP2:1",
    "MAP_NAVEL_ROCK_UP3:1/MAP_NAVEL_ROCK_UP4:0",
    "MAP_NAVEL_ROCK_UP4:0/MAP_NAVEL_ROCK_UP3:1",
    "MAP_NAVEL_ROCK_UP4:1/MAP_NAVEL_ROCK_TOP:0",

    # Secret bases
    "MAP_SECRET_BASE_BROWN_CAVE1:0/MAP_DYNAMIC:-2!",
    "MAP_SECRET_BASE_BROWN_CAVE2:0/MAP_DYNAMIC:-2!",
    "MAP_SECRET_BASE_BROWN_CAVE3:0/MAP_DYNAMIC:-2!",
    "MAP_SECRET_BASE_BROWN_CAVE4:0/MAP_DYNAMIC:-2!",
    "MAP_SECRET_BASE_BLUE_CAVE1:0/MAP_DYNAMIC:-2!",
    "MAP_SECRET_BASE_BLUE_CAVE2:0/MAP_DYNAMIC:-2!",
    "MAP_SECRET_BASE_BLUE_CAVE3:0/MAP_DYNAMIC:-2!",
    "MAP_SECRET_BASE_BLUE_CAVE4:0/MAP_DYNAMIC:-2!",
    "MAP_SECRET_BASE_YELLOW_CAVE1:0/MAP_DYNAMIC:-2!",
    "MAP_SECRET_BASE_YELLOW_CAVE2:0/MAP_DYNAMIC:-2!",
    "MAP_SECRET_BASE_YELLOW_CAVE3:0/MAP_DYNAMIC:-2!",
    "MAP_SECRET_BASE_YELLOW_CAVE4:0/MAP_DYNAMIC:-2!",
    "MAP_SECRET_BASE_RED_CAVE1:0/MAP_DYNAMIC:-2!",
    "MAP_SECRET_BASE_RED_CAVE2:0/MAP_DYNAMIC:-2!",
    "MAP_SECRET_BASE_RED_CAVE3:0/MAP_DYNAMIC:-2!",
    "MAP_SECRET_BASE_RED_CAVE4:0/MAP_DYNAMIC:-2!",
    "MAP_SECRET_BASE_SHRUB1:0/MAP_DYNAMIC:-2!",
    "MAP_SECRET_BASE_SHRUB2:0/MAP_DYNAMIC:-2!",
    "MAP_SECRET_BASE_SHRUB3:0/MAP_DYNAMIC:-2!",
    "MAP_SECRET_BASE_SHRUB4:0/MAP_DYNAMIC:-2!",
    "MAP_SECRET_BASE_TREE1:0/MAP_DYNAMIC:-2!",
    "MAP_SECRET_BASE_TREE2:0/MAP_DYNAMIC:-2!",
    "MAP_SECRET_BASE_TREE3:0/MAP_DYNAMIC:-2!",
    "MAP_SECRET_BASE_TREE4:0/MAP_DYNAMIC:-2!",

    # Multiplayer rooms
    "MAP_RECORD_CORNER:0,1,2,3/MAP_DYNAMIC:-1!",

    "MAP_UNION_ROOM:0,1/MAP_DYNAMIC:-1!",
    "MAP_PACIFIDLOG_TOWN_POKEMON_CENTER_2F:1/MAP_UNION_ROOM:0!",
    "MAP_MAUVILLE_CITY_POKEMON_CENTER_2F:1/MAP_UNION_ROOM:0!",
    "MAP_PETALBURG_CITY_POKEMON_CENTER_2F:1/MAP_UNION_ROOM:0!",
    "MAP_EVER_GRANDE_CITY_POKEMON_CENTER_2F:1/MAP_UNION_ROOM:0!",
    "MAP_EVER_GRANDE_CITY_POKEMON_LEAGUE_2F:1/MAP_UNION_ROOM:0!",
    "MAP_DEWFORD_TOWN_POKEMON_CENTER_2F:1/MAP_UNION_ROOM:0!",
    "MAP_MOSSDEEP_CITY_POKEMON_CENTER_2F:1/MAP_UNION_ROOM:0!",
    "MAP_OLDALE_TOWN_POKEMON_CENTER_2F:1/MAP_UNION_ROOM:0!",
    "MAP_SLATEPORT_CITY_POKEMON_CENTER_2F:1/MAP_UNION_ROOM:0!",
    "MAP_RUSTBORO_CITY_POKEMON_CENTER_2F:1/MAP_UNION_ROOM:0!",
    "MAP_BATTLE_FRONTIER_POKEMON_CENTER_2F:1/MAP_UNION_ROOM:0!",
    "MAP_LILYCOVE_CITY_POKEMON_CENTER_2F:1/MAP_UNION_ROOM:0!",
    "MAP_FORTREE_CITY_POKEMON_CENTER_2F:1/MAP_UNION_ROOM:0!",
    "MAP_FALLARBOR_TOWN_POKEMON_CENTER_2F:1/MAP_UNION_ROOM:0!",
    "MAP_LAVARIDGE_TOWN_POKEMON_CENTER_2F:1/MAP_UNION_ROOM:0!",
    "MAP_SOOTOPOLIS_CITY_POKEMON_CENTER_2F:1/MAP_UNION_ROOM:0!",
    "MAP_VERDANTURF_TOWN_POKEMON_CENTER_2F:1/MAP_UNION_ROOM:0!",

    "MAP_TRADE_CENTER:0,1/MAP_DYNAMIC:-1!",
    "MAP_PACIFIDLOG_TOWN_POKEMON_CENTER_2F:2/MAP_TRADE_CENTER:0!",
    "MAP_MAUVILLE_CITY_POKEMON_CENTER_2F:2/MAP_TRADE_CENTER:0!",
    "MAP_PETALBURG_CITY_POKEMON_CENTER_2F:2/MAP_TRADE_CENTER:0!",
    "MAP_EVER_GRANDE_CITY_POKEMON_CENTER_2F:2/MAP_TRADE_CENTER:0!",
    "MAP_EVER_GRANDE_CITY_POKEMON_LEAGUE_2F:2/MAP_TRADE_CENTER:0!",
    "MAP_DEWFORD_TOWN_POKEMON_CENTER_2F:2/MAP_TRADE_CENTER:0!",
    "MAP_MOSSDEEP_CITY_POKEMON_CENTER_2F:2/MAP_TRADE_CENTER:0!",
    "MAP_OLDALE_TOWN_POKEMON_CENTER_2F:2/MAP_TRADE_CENTER:0!",
    "MAP_SLATEPORT_CITY_POKEMON_CENTER_2F:2/MAP_TRADE_CENTER:0!",
    "MAP_RUSTBORO_CITY_POKEMON_CENTER_2F:2/MAP_TRADE_CENTER:0!",
    "MAP_BATTLE_FRONTIER_POKEMON_CENTER_2F:2/MAP_TRADE_CENTER:0!",
    "MAP_LILYCOVE_CITY_POKEMON_CENTER_2F:2/MAP_TRADE_CENTER:0!",
    "MAP_FORTREE_CITY_POKEMON_CENTER_2F:2/MAP_TRADE_CENTER:0!",
    "MAP_FALLARBOR_TOWN_POKEMON_CENTER_2F:2/MAP_TRADE_CENTER:0!",
    "MAP_LAVARIDGE_TOWN_POKEMON_CENTER_2F:2/MAP_TRADE_CENTER:0!",
    "MAP_SOOTOPOLIS_CITY_POKEMON_CENTER_2F:2/MAP_TRADE_CENTER:0!",
    "MAP_VERDANTURF_TOWN_POKEMON_CENTER_2F:2/MAP_TRADE_CENTER:0!",

    "MAP_BATTLE_COLOSSEUM_2P:0,1/MAP_DYNAMIC:-1!",
    "MAP_BATTLE_COLOSSEUM_4P:0,1,2,3/MAP_DYNAMIC:-1!",

    # Unused content
    "MAP_CAVE_OF_ORIGIN_UNUSED_RUBY_SAPPHIRE_MAP1:0/MAP_CAVE_OF_ORIGIN_1F:1!",
    "MAP_CAVE_OF_ORIGIN_UNUSED_RUBY_SAPPHIRE_MAP1:1/MAP_CAVE_OF_ORIGIN_UNUSED_RUBY_SAPPHIRE_MAP2:0",
    "MAP_CAVE_OF_ORIGIN_UNUSED_RUBY_SAPPHIRE_MAP2:0/MAP_CAVE_OF_ORIGIN_UNUSED_RUBY_SAPPHIRE_MAP1:1",
    "MAP_CAVE_OF_ORIGIN_UNUSED_RUBY_SAPPHIRE_MAP2:1/MAP_CAVE_OF_ORIGIN_UNUSED_RUBY_SAPPHIRE_MAP3:0",
    "MAP_CAVE_OF_ORIGIN_UNUSED_RUBY_SAPPHIRE_MAP3:0/MAP_CAVE_OF_ORIGIN_UNUSED_RUBY_SAPPHIRE_MAP2:1",
    "MAP_CAVE_OF_ORIGIN_UNUSED_RUBY_SAPPHIRE_MAP3:1/MAP_CAVE_OF_ORIGIN_B1F:0!",
    "MAP_LILYCOVE_CITY_UNUSED_MART:0,1/MAP_LILYCOVE_CITY:0!"
}


def validate_regions() -> bool:
    error_messages: List[str] = []
    warn_messages: List[str] = []
    failed = False

    def error(message: str) -> None:
        nonlocal failed
        failed = True
        error_messages.append(message)

    def warn(message: str) -> None:
        warn_messages.append(message)

    # Check regions
    for name, region in data.regions.items():
        for region_exit in region.exits:
            if region_exit not in data.regions:
                error(f"Pokemon Emerald: Region [{region_exit}] referenced by [{name}] was not defined")

    # Check warps
    for warp_source, warp_dest in data.warp_map.items():
        if warp_source in _ignorable_warps:
            continue

        if warp_dest is None:
            error(f"Pokemon Emerald: Warp [{warp_source}] has no destination")
        elif not data.warps[warp_dest].connects_to(data.warps[warp_source]) and not data.warps[warp_source].is_one_way:
            error(f"Pokemon Emerald: Warp [{warp_source}] appears to be a one-way warp but was not marked as one")

    # Check locations
    claimed_locations = [location for region in data.regions.values() for location in region.locations]
    claimed_locations_set = set()
    for location_name in claimed_locations:
        if location_name in claimed_locations_set:
            error(f"Pokemon Emerald: Location [{location_name}] was claimed by multiple regions")
        claimed_locations_set.add(location_name)

    for location_name in data.locations:
        if location_name not in claimed_locations and location_name not in _ignorable_locations:
            warn(f"Pokemon Emerald: Location [{location_name}] was not claimed by any region")

    warn_messages.sort()
    error_messages.sort()

    for message in warn_messages:
        logging.warning(message)
    for message in error_messages:
        logging.error(message)

    logging.debug("Pokemon Emerald sanity check done. Found %s errors and %s warnings.", len(error_messages), len(warn_messages))

    return not failed
