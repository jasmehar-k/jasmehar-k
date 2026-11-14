"""Runs gh-space-shooter with a purple space theme that matches the profile README.

Usage: python scripts/space_shooter.py <username> -o assets/space-shooter.gif [any gh-space-shooter flags]
"""
from gh_space_shooter.game import render_context as rc
from gh_space_shooter.game.drawables import starfield as sf
from gh_space_shooter.cli import app


def themed() -> rc.RenderContext:
    return rc.RenderContext(
        cell_size=12,
        cell_spacing=3,
        padding=40,
        background_color=(9, 0, 20),       # #090014
        grid_color=(30, 10, 60),           # #1e0a3c, empty cells
        enemy_colors={                     # contribution levels 1-4
            1: (91, 33, 182),              # #5b21b6
            2: (124, 58, 237),             # #7c3aed
            3: (167, 139, 250),            # #a78bfa
            4: (221, 214, 254),            # #ddd6fe
        },
        ship_color=(245, 184, 216),        # pastel pink
        bullet_color=(253, 230, 138),      # pastel yellow, also used for explosions
    )


rc.RenderContext.darkmode = staticmethod(themed)


def lavender_stars(self, draw, context):
    for star in self.stars:
        x, y = context.get_cell_position(star["x"], star["y"])
        b = star["brightness"]
        color = (int(221 * b), int(214 * b), int(254 * b), 255)  # tinted #ddd6fe
        if star["size"] == 1:
            draw.point([(x, y)], fill=color)
        else:
            draw.rectangle([x, y, x + star["size"] - 1, y + star["size"] - 1], fill=color)


sf.Starfield.draw = lavender_stars

if __name__ == "__main__":
    app()
