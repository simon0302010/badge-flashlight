import badge
import utime

class App(badge.BaseApp):
    def __init__(self) -> None:
        self.led_on = 0
        pass

    def on_open(self) -> None:
        self.turn_on()

    def draw_ui(self) -> None:
        badge.display.fill(1)
        flashlight_lines = [
            # flashlight icon
            ((85, 60), (85, 140)),
            ((85, 140), (115, 140)),
            ((115, 140), (115, 60)),
            ((115, 60), (85, 60)),
            
            ((80, 60), (80, 45)),
            ((80, 45), (120, 45)),
            ((120, 45), (120, 60)),
            ((120, 60), (80, 60)),
            
            ((90, 80), (110, 80)),
            ((90, 95), (110, 95)),
            ((90, 110), (110, 110)),
            ((90, 125), (110, 125))
        ]

        if self.led_on:
            flashlight_lines.extend([
                ((100, 45), (90, 25)),
                ((100, 45), (100, 25)),
                ((100, 45), (110, 25))
            ])

        # draw icon
        for start_point, end_point in flashlight_lines:
            x1, y1 = start_point
            x2, y2 = end_point
            badge.display.line(x1, y1, x2, y2, 0)

        badge.display.text("Press SW11 to toggle", 20, 160, 0)

        # arrow pointing towards SW11
        badge.display.line(180, 180, 180, 195, 0)
        badge.display.line(175, 190, 180, 195, 0)
        badge.display.line(185, 190, 180, 195, 0)
        
        badge.display.show()

    def turn_on(self) -> None:
        badge.utils.set_led(1)
        self.led_on = 1
        self.draw_ui()

    def turn_off(self) -> None:
        badge.utils.set_led(0)
        self.led_on = 0
        self.draw_ui()

    def loop(self) -> None:
        if badge.input.get_button(badge.input.Buttons.SW11):
            if self.led_on:
                self.turn_off()
            else:
                self.turn_on()
        utime.sleep_ms(50)