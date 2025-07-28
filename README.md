# Your Way TD: customizable Tower Defense

This project is a the result of the Boot.dev Hackathon (July 25 to July 28 2025)
This is a simple, highly customizable Tower Defense game with minimalist graphics.
This was inspired by the pygame Asteroids course on the Boot.dev site, and the collision logic is more-or-less directly lifted from that course. All other code and assets are original.
In the current build, the game plays one level (defined in a confguration file)
Win or lose, the game will exit as soon as the level ends.
Towers, creeps and wave are also defined in confguration files.

## Running the game
### requirements:
* uv
* pygame (can be installed via the provided script)

### setup
Run the provided setup.sh script. This will use uv to create a virtual environment and install pygame
### play
while the virtual environment is active run the command:
> uv run -m src.main [MAP_FILE]

MAP_FILE: an optional parameter that points to a user-provided map file. See the configuration section for details on how to create a map file.

## Customization options
note: distance measurements in the game are currently mixed between pixels and grid squares. A grid square is a 50 pixel square. The path is exactly one grid square wide. The eventual goal is to convert all measurements to grid squares.

### Towers
Towers are defined by json files in the folder `assets/towers`
All files with the `.json` extension will be read and used to generate towers. Files may contain a single json object, or an array of objects.
Towers expect to have the following attributes
* `name`: a unique string that the game uses to identify each tower type
* `type`: a string that identifies the tower's method of attack. Supported types are:
** `hitscan`: a single target in range takes instant damage
** `projectile`: The tower launches a projectile at a target in range
** `AOE`: All targets in range take instant damage
** `slow`: All targets in range stop, and need to get back up to speed.
* `cost`: how much it costs to place the tower
* `damage`: the number of hitpoints of damage that are inflicted on the target(s)
* `cooldown`: the number of frames that pass between shots
* `range`: the tower's range in pixels
* `color`: the color that will be used to draw towers of this type

### Creeps
Creeps are defined by json files in the folder `assets/creeps`
All files with the `.json` extension will be read and used to generate creeps. Files may contain a single json object, or an array of objects.
Creeps expect to have the following attributes:
* `name`: a unique string that the game uses to identify each creep type
* `speed`: how fast the creep moves along the path. Measured in grid squares per second
* `hp`: how much damage the creep takes before dying
* `bounty`: how much the player is paid for kiling this creep
* `color`: the color that will be used to draw creeps of this type

### Waves
The sequence of waves for this level are defined in a single file `assets/waves.json`. This file expects an array of json objects, each representing a single wave.
Each wave has the following attributes:
* `num_creeps`: the number of creeps that will be released during this wave.
* `creep_type`: the name of the creep type that will be unleashed in this wave.
* `production_cooldown`: the number of frames that pass between each creep being released

### Map
The default level map is defined in the file `assets/maps/default_map.txt` The file begins with a 2D array of characters (27x18), representing the x,y grid coordinates of the map. Like pydraw pixels, the grid squares are 0-indexed and begin with 0,0 in the top left corner.

After the map, there is a single pair of numbers, separated by a comma, on the last line of the file. These numbers represent the Creep spawn point, as an x,y grid square.
Characters used to define the map are:
* `n`: part of the path. the next square will be 'north' (above) from this one.
* `s`: part of the path. the next square will be 'south' (below) from this one.
* `w`: part of the path. the next square will be 'west' (left) from this one.
* `e`: part of the path. the next square will be 'east' (right) from this one.
* `z`: part of the path. This is the end of the path. Creeps that reach this square will despawn and damage the player.
* `0`: non-path square. THe player is free to place towers here.
* `p`: 'poison' square. Towers can be placed here, but their firing rate will be halved.