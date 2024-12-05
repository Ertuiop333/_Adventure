# import u_Logic

# player = Fighter(10, "Bob", Sprite(Pixel(Vector(0, 0), "B")), Vector(0, 0))


# def check_player_position() -> Vector:
#     """
#     >>> check_player_position()
#     (0, 0)
#     """
#     return player.position.x, player.position.y

import u_Physics as p
import s_Collisions as c
import s_Terminal as Terminal

Terminal.reset_in_game_screen(".", " ", 20, 10)

con = True
x = 0
y = 0
i = 0
while con:
    # a = p.Types.Vector(int(input("posX: ")), int(input("posY: ")))

    # b = p.PhysicsObject(
    #     p.Collisions.Area(
    #         p.Types.Vector(int(input("oX: ")), int(input("oY: "))),
    #         p.Types.Vector(int(input("eX: ")), int(input("eY: "))),
    #     ),
    #     p.Types.Vector(0, 0),
    # )

    object1 = p.PhysicsObject(
        c.empty_box(5, 5),
        p.Types.Vector(0, 0),
    )
    object2 = p.PhysicsObject(
        c.empty_box(5, 5),
        p.Types.Vector(0, 1),
    )

    tests = [
        [
            object1,
            object2,
            False,
        ],
    ]

    # for x in object2.collider.points:
    #     Terminal.screen_data[x.x + object2.position.x][x.y + object2.position.y] = "l"
    for x in object1.collider.points:
        Terminal.screen_data[x.x + object1.position.x][x.y + object1.position.y] = "c"

    result = p.is_object_colliding_with_other_object(tests[i][0], tests[i][1])

    Terminal.screen_data[i][0] = str(result)[0]

    success = "n"
    if result == tests[i][2]:
        success = "Y"

    Terminal.screen_data[i][1] = success

    # x += 1
    # if x >= len(Terminal.screen_data):
    #     x = 0
    #     y += 1

    #     if y >= len(Terminal.screen_data[0]):
    #         d = Terminal.screen_data[x][y - 1]
    #         Terminal.reset_in_game_screen()
    #         Terminal.screen_data[0][0] = d
    #         x = 1
    #         y = 0

    Terminal.update_in_game_screen()

    i += 1
    if i >= len(tests):
        con = False
