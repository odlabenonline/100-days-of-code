# # # # Karel the robot - Exercise
# # #
# # #
# # # # Move ROBOT to draw a square using the resource at
# # # # https://reeborg.ca/reeborg.html
# # # # Coding Exercise: Challenge : Code for the Robot to jump some hurdles
# # # #
# # # #
# # # # def jump_hurdle():
# # # #     turn_left()
# # # #     turn_left()
# # # #     turn_left()
# # # #     move()
# # # #     turn_left()
# # # #     turn_left()
# # # #     turn_left()
# # # #     move()
# # # #     turn_left()
# # # #
# # # #
# # # # for i in range(1, 10):
# # # #     move()
# # # #     turn_left()
# # # #     move()
# # # #     jump_hurdle()
# # #
# # # #
# # # # ############ RE WRITTEN CODE to include 2 functions ######
# # # # def turn_right():
# # # #     turn_left()
# # # #     turn_left()
# # # #     turn_left()
# # # #
# # # #
# # # # def jump_hurdle():
# # # #     turn_right()
# # # #     move()
# # # #     turn_right()
# # # #     move()
# # # #     turn_left()
# # # #
# # # #
# # # # for i in range(1, 7):
# # # #     move()
# # # #     turn_left()
# # # #     move()
# # # #     jump_hurdle()
# # # #
# # # # IN THE ABSENCE OF FOR LOOP, we could use WHILE LOOP as defined below
# # # # Loot into resource for solution
# # #
# # #
# # # ############# HURDLE 2 EXAMPLE in reeborg #######
# # #
# # # def turn_right():
# # #     turn_left()
# # #     turn_left()
# # #     turn_left()
# # #
# # #
# # # def jump():
# # #     move()
# # #     turn_left()
# # #     move()
# # #     turn_right()
# # #     move()
# # #     turn_right()
# # #     move()
# # #     turn_left()
# # #
# # #
# # # while not at_goal():
# # #     jump()
# # # print("FINISHED!")
# # # #
# # # #
# #
# # ##################### HURDLE 3 ###############
# # def turn_right():
# #     turn_left()
# #     turn_left()
# #     turn_left()
# #
# #
# # def jump():
# #     turn_left()
# #     move()
# #     turn_right()
# #     move()
# #     turn_right()
# #     move()
# #     turn_left()
# #
# #
# # while not at_goal():
# #     if wall_in_front():
# #         jump()
# #     else:
# #         move()
# #
#
#
#
#
# ################## HURDLE 4 #############
# def turn_right():
#     turn_left()
#     turn_left()
#     turn_left()
#
#
# def jump():
#     turn_left()
#     while wall_on_right():
#         move()
#     turn_right()
#     move()
#     turn_right()
#     while front_is_clear():
#         move()
#     turn_left()
#
#
# while not at_goal():
#     if wall_in_front():
#         jump()
#     else:
#         move()
#
