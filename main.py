import badge
import utime

class App(badge.BaseApp):
    def __init__(self) -> None:
        pass

    def on_open(self) -> None:
        badge.utils.set_led(1)
        badge.display.fill(1)
        badge.display.show()

    def draw_flashlight(self) -> None:
        badge.display.fill(1)
        flashlight_lines = [
            # flashlight icon
            ((85, 60), (85, 140))
            ((85, 140), (115, 140)),
            ((115, 140), (115, 60)),
            ((115, 60), (85, 60)),
            
            ((80, 60), (80, 45)),
            ((80, 45), (120, 45)),
            ((120, 45), (120, 60)),
            ((120, 60), (80, 60)),
            
            ((100, 45), (90, 25)),
            ((100, 45), (100, 25)),
            ((100, 45), (110, 25)),
            
            ((90, 80), (110, 80)),
            ((90, 95), (110, 95)),
            ((90, 110), (110, 110)),
            ((90, 125), (110, 125))
        ]

        # draw icon
        for start_point, end_point in flashlight_lines:
            x1, y1 = start_point
            x2, y2 = end_point
            print(f"Line from ({x1}, {y1}) to ({x2}, {y2})")

    def loop(self) -> None:
        utime.sleep(1)