# SPDX-License-Identifier: GPL-3.0-or-later

import logging
import platform
from math import radians

import bpy
import rna_keymap_ui
from bpy.props import BoolProperty, FloatProperty
from bpy.types import AddonPreferences


def update_developer_print(self, context):
    """Toggle logging based on preferences"""
    from .bl_logger import logger

    if self.developer_print:
        logger.setLevel(logging.DEBUG)
    else:
        logger.setLevel(logging.CRITICAL + 1)


class VIEW3D_PT_gizmo_size_preferences(AddonPreferences):
    bl_idname = __package__

    # Gismo Size Increment value
    inc: FloatProperty(
        name="Gizmo Increment",
        description="Gizmo Size Increment in px",
        default=20,
        min=1,
        soft_max=100,
        step=100,
        precision=0,
        subtype="PIXEL",
    )

    # Translate Increment value
    tinc: FloatProperty(
        name="Translate Increment",
        description="Translate Increment",
        default=0.01,
        soft_min=0,
        soft_max=100,
        step=1,
        precision=3,
    )

    # Rotate Increment value
    rinc: FloatProperty(
        name="Rotate Increment",
        description="Rotate Increment",
        default=radians(1),
        soft_min=0,
        soft_max=360,
        step=1,
        precision=3,
        subtype="ANGLE",
    )

    # Developer prints
    developer_print: BoolProperty(
        name="Toggle developer log in System Console",
        description=(
            "Helps with debugging issues in the addon.\n"
            "Please use this for any bug report.\n"
            "Keep it disabled for better performances."
        ),
        default=False,
        update=update_developer_print,
    )

    # Draws addon preferences

    def draw(self, context):
        layout = self.layout

        # Increment value
        row = layout.row(align=True)
        row.prop(self, "inc", toggle=True)
        row.prop(self, "tinc", toggle=True)
        row.prop(self, "rinc", toggle=True)

        row = layout.row()
        row.prop(self, "developer_print")
        if "Windows" in platform.system():
            row.operator("wm.console_toggle", icon="CONSOLE", text="")
        else:
            split = layout.split(factor=0.35)
            split.label(text="")
            split.label(
                text="For Mac and Linux, you need to start Blender from the terminal to see the logs.",
                icon="INFO",
            )

        box = layout.box()
        box.label(text="Keymaps")

        draw_keymaps(box)


def get_preferences():
    return bpy.context.preferences.addons[__package__].preferences


def draw_keymaps(box):
    wm = bpy.context.window_manager
    kc = wm.keyconfigs.user

    for km in kc.keymaps:
        # filter kmi's from gizmo tools only
        keymap_items = [
            kmi for kmi in km.keymap_items if kmi.idname.startswith("view3d.gizmo_")
        ]

        if not keymap_items:
            continue

        box.label(text=km.name)
        box.context_pointer_set("keymap", km)

        for kmi in keymap_items:
            row = box.row()
            rna_keymap_ui.draw_kmi(
                ["ADDON", "USER", "DEFAULT"],
                kc,
                km,
                kmi,
                row,
                1,
            )
