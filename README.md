Repository containing a game done during Łódzki Game Jam 9 (which is part of Global Game Jam 2025).\
This project won't be continued, because it has been desired to be only for game jam project.

Programming: Ciachociech\
Art: limbo

Language: Python\
Libraries: pygame 2.6.1 (Python 3.12)\
Suggested IDE: JetBrains PyCharm

It is suggested to use "pyinstaller" to generate an executable application and/or "pygbag" to create a Web build.

After getting feedback from game jam's jury and other participants, there are some propositions worth to consider or implement:
- add time counter between choosing a game mode (from main menu) and start a game, also highlight all animals from initial list in some simple way (to give a message that animals are interactable)
- add invincible frames (i-frames) for bubbles which are supposed to break, this allow to catch animals inside those bubbles, which stop to grow and move
- show less bubbles:
  - decrase a number of bubbles (for many people the number of bubbles are too big)
  - don't show bubbles which are not able to catch a rabbit (the smallest animal)
- a challenge mode should contain stricted combination of animals:
  - eliminate randomizing by giving a constant seed to randomizing
  - if this game would get a multiplayer support then challenge can be changed every day/week
- eliminate or weaken randomizing aspect by setting a properties of bubbles like max size and its lifetime
