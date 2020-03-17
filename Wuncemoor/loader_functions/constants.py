import tcod as libtcod

def get_constants():
    window_title = 'Wuncemoor: The Eternal Dream'
    
    screen_width = 80
    screen_height = 50
    fps = 60
    
    bar_width = 20
    panel_height = 8
    panel_y = screen_height - panel_height
    
    message_x = bar_width + 2
    message_width = screen_width - bar_width - 2
    message_height = panel_height -1
    
    map_width = 80
    map_height = 42
    
    alpha_width = 150
    alpha_height = 100
    
    room_max_size = 10
    room_min_size = 6
    max_rooms = 3
    
    fov_algorithm = 0
    fov_light_walls = True
    fov_radius = 10
    
    max_monsters_per_room = 3
    max_items_per_room = 2
    
    colors = {
        'dark_wall': libtcod.Color(0, 0, 100),
        'dark_ground': libtcod.Color(50, 50, 150),
        'light_wall': libtcod.Color(130, 110, 50),
        'light_ground': libtcod.Color(200, 180, 50),
        'grass': libtcod.Color(0, 191, 0),
        'water': libtcod.Color(0, 191, 191)
        }
    
    constants = {
        'window_title': window_title,
        'screen_width': screen_width,
        'screen_height': screen_height,
        'bar_width': bar_width,
        'panel_height': panel_height,
        'panel_y': panel_y,
        'message_x': message_x,
        'message_width': message_width,
        'message_height': message_height,
        'alpha_width': alpha_width,
        'alpha_height': alpha_height,
        'map_width': map_width,
        'map_height': map_height,
        'room_max_size': room_max_size,
        'room_min_size': room_min_size,
        'max_rooms': max_rooms,
        'fov_algorithm': fov_algorithm,
        'fov_light_walls': fov_light_walls,
        'fov_radius': fov_radius,
        'max_monsters_per_room': max_monsters_per_room,
        'max_items_per_room': max_items_per_room,
        'colors': colors
        }
    return constants
