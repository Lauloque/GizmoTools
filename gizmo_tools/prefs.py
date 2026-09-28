# SPDX-License-Identifier: GPL-3.0-or-later

from math import radians

import bpy
from bpy.props import FloatProperty
from bpy.types import AddonPreferences


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

    # Draws addon preferences

    def draw(self, context):
        layout = self.layout

        # Increment value
        row = layout.row(align=True)
        row.prop(self, "inc", toggle=True)
        row.prop(self, "tinc", toggle=True)
        row.prop(self, "rinc", toggle=True)


def get_preferences():
    return bpy.context.preferences.addons[__package__].preferences
