# game/screens/screen_telepathy.rpy
# ═══════════════════════════════════════════════════
# ТЕЛЕПАТИЧНИЙ ТЕКСТ — ЕЛЕОНОР
# ═══════════════════════════════════════════════════
# Текст по центру екрану. Букви плавно хвилюються вгору-вниз.
# Імітація телепатичного зв'язку — не say window, а окремий screen.
#
# Використання:
#   $ telepathy("Я чую твої думки, Марті.")
#   або
#   $ telepathy("Це не так працює.", color="#d8b4fe")

init python:
    import math

    class WaveText(renpy.Displayable):
        """Текст з хвильовим ефектом — букви піднімаються і опускаються."""

        def __init__(self, text, size=28, color="#d8b4fe", wave_amp=6, wave_speed=2.0, wave_freq=0.3, font=None, **kwargs):
            super(WaveText, self).__init__(**kwargs)
            self.text = text
            self.size = size
            self.color = color
            self.wave_amp = wave_amp      # амплітуда хвилі (px)
            self.wave_speed = wave_speed  # швидкість (циклів/сек)
            self.wave_freq = wave_freq    # частота (чим менше — довша хвиля)
            self.font = font or "DejaVuSans.ttf"
            self.chars = []
            for ch in text:
                self.chars.append(
                    Text(ch, size=self.size, color=self.color, font=self.font)
                )

        def render(self, width, height, st, at):
            renders = []
            positions = []
            x_offset = 0

            for i, ch_disp in enumerate(self.chars):
                cr = renpy.render(ch_disp, width, height, st, at)
                cw, ch = cr.get_size()
                # Синусоїдальний зсув по Y
                y_off = self.wave_amp * math.sin(st * self.wave_speed * 2 * math.pi + i * self.wave_freq * 2 * math.pi)
                renders.append(cr)
                positions.append((x_offset, y_off))
                x_offset += cw

            # Загальна ширина тексту
            total_w = x_offset
            total_h = self.size + self.wave_amp * 2 + 10

            rv = renpy.Render(total_w, total_h)
            for cr, (px, py) in zip(renders, positions):
                rv.blit(cr, (px, self.wave_amp + py))

            renpy.redraw(self, 0)  # перемальовувати кожен кадр
            return rv

        def event(self, ev, x, y, st):
            return None

        def visit(self):
            return self.chars

    def telepathy(text, color="#d8b4fe", duration=None):
        """Показує телепатичний текст по центру екрану.
        Чекає на клік гравця (або duration секунд).
        """
        renpy.show_screen("telepathy_display", text=text, color=color)
        if duration:
            renpy.pause(duration)
        else:
            renpy.pause()  # чекає на клік
        renpy.hide_screen("telepathy_display")


screen telepathy_display(text, color="#d8b4fe"):
    modal False
    zorder 200

    # Затемнення
    add Solid("#00000088")

    # Хвильовий текст по центру
    fixed:
        align (0.5, 0.5)
        add WaveText(text, size=30, color=color, wave_amp=5, wave_speed=1.5, wave_freq=0.25)
