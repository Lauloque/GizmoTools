# SPDX-License-Identifier: GPL-3.0-or-later

from math import radians

import bpy
from bpy.props import EnumProperty
from bpy.types import Operator

from ..bl_logger import logger
from ..prefs import get_preferences
from .constants import AXES


class VIEW3D_OT_gizmo_rotate(Operator):
    bl_idname = "view3d.gizmo_rotate"
    bl_label = "Rotate the gizmo's selection on a given axis and direction"
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
        angle = get_preferences().rinc
        if self.axis.startswith("-"):
            angle = -angle
        axis = self.axis[-1]

        logger.info(f"Gizmo Rotate by {angle} on axis {axis}")

        return bpy.ops.transform.rotate(
            value=angle, orient_axis=axis, orient_type="LOCAL"
        )
