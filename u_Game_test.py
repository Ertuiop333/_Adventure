# import u_Logic

# player = Fighter(10, "Bob", Sprite(Pixel(Vector(0, 0), "B")), Vector(0, 0))


# def check_player_position() -> Vector:
#     """
#     >>> check_player_position()
#     (0, 0)
#     """
#     return player.position.x, player.position.y

import u_Physics as p
import s_Terminal as Terminal

Terminal.reset_in_game_screen(".", " ", 3, 3)

con = True
x = 0
y = 0
while con:
    a = p.Collisions.Area(
        p.Types.Vector(int(input("o1: ")), int(input("o2: "))),
        p.Types.Vector(int(input("e1: ")), int(input("e2: "))),
    )

    print(
        f"origin : ({a.origin.x}, {a.origin.y})\nextent : ({a.extent.x}, {a.extent.y})"
    )

    b = p.Collisions.Area(
        p.Types.Vector(int(input("o1: ")), int(input("o2: "))),
        p.Types.Vector(int(input("e1: ")), int(input("e2: "))),
    )

    Terminal.screen_data[x][y] = str(p.__is_area1_intersecting_with_area2(a, b))[0]

    print("this is a modification worth your time!")

    x += 1
    if x >= len(Terminal.screen_data):
        x = 0
        y += 1

        if y >= len(Terminal.screen_data[0]):
            d = Terminal.screen_data[x][y - 1]
            Terminal.reset_in_game_screen()
            Terminal.screen_data[0][0] = d
            x = 1
            y = 0

    Terminal.update_in_game_screen()

    print(
        f"origin : ({b.origin.x}, {b.origin.y})\nextent : ({b.extent.x}, {b.extent.y})"
    )
    print(
        f"origin : ({b.origin.x}, {b.origin.y})\nextent : ({b.extent.x}, {b.extent.y})"
    )

    i = input("quit? (y/n)")
    if i == "y" or len(i) > 10:
        con = False
