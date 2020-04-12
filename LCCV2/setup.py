import cx_Freeze

executables = [cx_Freeze.Executable("main.py", shortcutName="Anti-Viral Protocol", shortcutDir="DesktopFolder", base="Win32GUI",
                                    icon="resources/Images/Icon/GameIcon.ico")]

cx_Freeze.setup(
    name="Anti-Viral Protocol",
    version="1.0",
    options={"build_exe": {"packages": ["pygame", "sys"],
                           "include_files": ["resources"]}},
    executables=executables,
    description={"author": "Marudhu Paandian.K, Rishi Menon, Shabesa K.A.",
                 "disc": "simple platformer"}
    )
