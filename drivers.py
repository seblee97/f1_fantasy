import constants
from f1_objects import Driver

hamilton = Driver(
    name=constants.HAMILTON,
    constructor=constants.MERCEDES,
    price=33.5,
    teammate=constants.BOTTAS,
)
bottas = Driver(
    name=constants.BOTTAS,
    constructor=constants.MERCEDES,
    price=23.6,
    teammate=constants.HAMILTON,
)

verstappen = Driver(
    name=constants.VERSTAPPEN,
    constructor=constants.RED_BULL,
    price=24.8,
    teammate=constants.PEREZ,
)
perez = Driver(
    name=constants.PEREZ,
    constructor=constants.RED_BULL,
    price=18.4,
    teammate=constants.VERSTAPPEN,
)

norris = Driver(
    name=constants.NORRIS,
    constructor=constants.MCLAREN,
    price=13.1,
    teammate=constants.RICCIARDO,
)
ricciardo = Driver(
    name=constants.RICCIARDO,
    constructor=constants.MCLAREN,
    price=16.8,
    teammate=constants.NORRIS,
)

leclerc = Driver(
    name=constants.LECLERC,
    constructor=constants.FERRARI,
    price=16.8,
    teammate=constants.SAINZ,
)
sainz = Driver(
    name=constants.SAINZ,
    constructor=constants.FERRARI,
    price=14.1,
    teammate=constants.LECLERC,
)

tsunoda = Driver(
    name=constants.TSUNODA,
    constructor=constants.ALPHA_TAURI,
    price=8.8,
    teammate=constants.GASLY,
)
gasly = Driver(
    name=constants.GASLY,
    constructor=constants.ALPHA_TAURI,
    price=11.7,
    teammate=constants.TSUNODA,
)

stroll = Driver(
    name=constants.STROLL,
    constructor=constants.ASTON_MARTIN,
    price=13.9,
    teammate=constants.VETTEL,
)
vettel = Driver(
    name=constants.VETTEL,
    constructor=constants.ASTON_MARTIN,
    price=16.2,
    teammate=constants.STROLL,
)

ocon = Driver(
    name=constants.OCON,
    constructor=constants.ALPINE,
    price=10.1,
    teammate=constants.ALONSO,
)
alonso = Driver(
    name=constants.ALONSO,
    constructor=constants.ALPINE,
    price=15.6,
    teammate=constants.OCON,
)

raikkonen = Driver(
    name=constants.RAIKKONEN,
    constructor=constants.ALFA_ROMEO,
    price=9.6,
    teammate=constants.GIOVINAZZI,
)
giovinazzi = Driver(
    name=constants.GIOVINAZZI,
    constructor=constants.ALFA_ROMEO,
    price=7.9,
    teammate=constants.RAIKKONEN,
)

schumacher = Driver(
    name=constants.SCHUMACHER,
    constructor=constants.HAAS,
    price=5.8,
    teammate=constants.MAZEPIN,
)
mazepin = Driver(
    name=constants.MAZEPIN,
    constructor=constants.HAAS,
    price=5.5,
    teammate=constants.SCHUMACHER,
)

russell = Driver(
    name=constants.RUSSELL,
    constructor=constants.WILLIAMS,
    price=6.2,
    teammate=constants.LATIFI,
)
latifi = Driver(
    name=constants.LATIFI,
    constructor=constants.WILLIAMS,
    price=6.5,
    teammate=constants.RUSSELL,
)

all_drivers = [
    hamilton,
    bottas,
    verstappen,
    perez,
    norris,
    ricciardo,
    leclerc,
    sainz,
    tsunoda,
    gasly,
    stroll,
    vettel,
    ocon,
    alonso,
    raikkonen,
    giovinazzi,
    schumacher,
    mazepin,
    russell,
    latifi,
]
