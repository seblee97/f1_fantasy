import constants
from f1_objects import Constructor

mercedes = Constructor(
    name=constants.MERCEDES, price=38.0, drivers=[constants.HAMILTON, constants.BOTTAS]
)
red_bull = Constructor(
    name=constants.RED_BULL, price=25.9, drivers=[constants.VERSTAPPEN, constants.PEREZ]
)
mclaren = Constructor(
    name=constants.MCLAREN, price=18.9, drivers=[constants.NORRIS, constants.RICCIARDO]
)
ferrari = Constructor(
    name=constants.FERRARI, price=18.1, drivers=[constants.LECLERC, constants.SAINZ]
)
alpha_tauri = Constructor(
    name=constants.ALPHA_TAURI, price=12.7, drivers=[constants.TSUNODA, constants.GASLY]
)
aston_martin = Constructor(
    name=constants.ASTON_MARTIN,
    price=17.6,
    drivers=[constants.STROLL, constants.VETTEL],
)
alpine = Constructor(
    name=constants.ALPINE, price=15.4, drivers=[constants.ALONSO, constants.OCON]
)
alfa_romeo = Constructor(
    name=constants.ALFA_ROMEO,
    price=8.9,
    drivers=[constants.RAIKKONEN, constants.GIOVINAZZI],
)
haas = Constructor(
    name=constants.HAAS, price=6.1, drivers=[constants.SCHUMACHER, constants.MAZEPIN]
)
williams = Constructor(
    name=constants.WILLIAMS, price=6.3, drivers=[constants.RUSSELL, constants.LATIFI]
)

all_constructors = [
    mercedes,
    red_bull,
    mclaren,
    ferrari,
    alpha_tauri,
    aston_martin,
    alpine,
    alfa_romeo,
    haas,
    williams,
]
