import asyncio
from enum import IntEnum

import pygame

import game.scenes.Game
import system.Display
from game.scenes.Game import GameMode


class InstanceState(IntEnum):
    none = 0
    mainmenu = 1
    game = 2
    pause = 3
    gameover = 4


class Instance:
    def __init__(self):
        pygame.init()
        self.display = system.Display(1280, 720,
                                      "Tajemnicze bąbelki z kosmosu (Łódzki Game Jam 9/Global Game Jam 2025)")
        self.display.set_icon("assets/sprites/logo.png")
        self.display.frames = 60

        self.actualState = InstanceState.none
        self.previousState = InstanceState.none

        self.scenes = []
        self.scenes.append(game.scenes.MainMenu(self.display))
        self.scenes.append(game.scenes.Game(self.display))
        self.scenes.append(game.scenes.Pause(self.display))
        self.scenes.append(game.scenes.Gameover(self.display))

    def update_instance_states(self, new_state):
        self.previousState = self.actualState
        self.actualState = new_state

    async def loop(self):
        while pygame.get_init():
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return

            self.display.clear()

            actual_scene = None
            previous_scene = None
            if self.actualState != InstanceState.none:
                actual_scene = self.scenes[self.actualState - 1]
            if self.previousState != InstanceState.none:
                previous_scene = self.scenes[self.previousState - 1]

            match self.actualState:
                case InstanceState.none:
                    self.update_instance_states(InstanceState.mainmenu)
                    self.scenes[self.actualState - 1].resume()
                case InstanceState.mainmenu:
                    actual_scene.process_input(pygame.key.get_pressed(), pygame.joystick.Joystick,
                                       pygame.mouse.get_pressed(), pygame.mouse.get_pos())
                    game_val = actual_scene.update()
                    match game_val:
                        case 0:
                            self.update_instance_states(InstanceState.game)
                            self.scenes[self.actualState - 1].set(GameMode.no_limit)
                        case 1:
                            self.update_instance_states(InstanceState.game)
                            self.scenes[self.actualState - 1].set(GameMode.time_limit)
                        case 2:
                            self.update_instance_states(InstanceState.game)
                            self.scenes[self.actualState - 1].set(GameMode.mixed_limit)
                        case 3:
                            pygame.quit()
                            break
                        case _:
                            pass
                    actual_scene.render()
                case InstanceState.game:
                    actual_scene.process_input(pygame.key.get_pressed(), pygame.joystick.Joystick,
                                               pygame.mouse.get_pressed(), pygame.mouse.get_pos())
                    game_val = actual_scene.update()
                    match game_val:
                        case 1:
                            self.update_instance_states(InstanceState.pause)
                            self.scenes[self.actualState - 1].resume()
                        case 2:
                            self.update_instance_states(InstanceState.gameover)
                            self.scenes[self.actualState - 1].set(self.scenes[self.previousState - 1].game_mode,
                                                                  (self.scenes[self.previousState - 1].score, -1))
                        case 3:
                            self.update_instance_states(InstanceState.gameover)
                            self.scenes[self.actualState - 1].set(self.scenes[self.previousState - 1].game_mode,
                                                                  (self.scenes[self.previousState - 1].score, -1))
                        case 4:
                            self.update_instance_states(InstanceState.gameover)
                            self.scenes[self.actualState - 1].set(self.scenes[self.previousState - 1].game_mode,
                                                                  (self.scenes[self.previousState - 1].score,
                                                                   self.scenes[self.previousState - 1].timer.elapsed_time))
                        case _:
                            pass
                    actual_scene.render()
                case InstanceState.pause:
                    actual_scene.process_input(pygame.key.get_pressed(), pygame.joystick.Joystick,
                                               pygame.mouse.get_pressed(), pygame.mouse.get_pos())
                    game_val = actual_scene.update()
                    match game_val:
                        case 0:
                            self.update_instance_states(InstanceState.game)
                            self.scenes[self.actualState - 1].resume()
                        case 1:
                            self.update_instance_states(InstanceState.mainmenu)
                            self.scenes[self.actualState - 1].resume()
                        case _:
                            pass
                    if self.previousState is InstanceState.game:
                        previous_scene.render()
                    actual_scene.render()
                case InstanceState.gameover:
                    actual_scene.process_input(pygame.key.get_pressed(), pygame.joystick.Joystick,
                                               pygame.mouse.get_pressed(), pygame.mouse.get_pos())
                    if actual_scene.update():
                        self.update_instance_states(InstanceState.mainmenu)
                        self.scenes[self.actualState - 1].resume()
                    if self.previousState is InstanceState.game:
                        previous_scene.render()
                    actual_scene.render()
                case _:
                    pass

            self.display.display_and_wait()
            await asyncio.sleep(0)

        pygame.quit()