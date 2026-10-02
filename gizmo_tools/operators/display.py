# SPDX-License-Identifier: GPL-3.0-or-later

from bpy.props import BoolProperty
from bpy.types import Operator

from ..bl_logger import logger
from ..prefs import get_preferences


class VIEW3D_OT_gizmo_size(Operator):
    bl_idname = "view3d.gizmo_size"
    bl_label = "Change Gizmo Size"

    positive: BoolProperty(
        name="Direction",
        description="Direction of action. Positive if enabled, otherwise negative",
        default=True,
    )

    @classmethod
    def description(cls, context, properties):
        return (
            "Increase gizmo size" if properties.direction > 0 else "Decrease gizmo size"
        )

    def execute(self, context):
        view = context.preferences.view
        inc = int(get_preferences().inc)
        direction = 1 if self.positive else -1
        value = direction * inc

        logger.info(
            f"{'Gizmo Increasing' if self.positive else 'decreasing'} by {value}, should go  from {view.gizmo_size} to {view.gizmo_size + value}"
        )

        view.gizmo_size += value
        return {"FINISHED"}
