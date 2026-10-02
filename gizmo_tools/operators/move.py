# SPDX-License-Identifier: GPL-3.0-or-later

import bpy
from bpy.props import EnumProperty
from bpy.types import Operator

from ..bl_logger import logger
from ..prefs import get_preferences

AXES = {
    "+X": (1, 0, 0),
    "-X": (-1, 0, 0),
    "+Y": (0, 1, 0),
    "-Y": (0, -1, 0),
    "+Z": (0, 0, 1),
    "-Z": (0, 0, -1),
}


class VIEW3D_OT_gizmo_move(Operator):
    bl_idname = "view3d.gizmo_move"
    bl_label = "Move the gizmo's selection on a given axis and direction"
    bl_options = {"REGISTER"}

    axis: EnumProperty(
        name="Axis",
        description="Axis of action",
        items=[(a, a, f"{a} axis") for a in AXES],
        default="+X",
    )

    @classmethod
    def poll(cls, context):
        return context.active_object is not None

    def execute(self, context):
        tinc = get_preferences().tinc
        vector = tuple(c * tinc for c in AXES[self.axis])

        logger.info(f"Gizmo Move by {vector}")

        return bpy.ops.transform.translate(value=vector, orient_type="LOCAL")
