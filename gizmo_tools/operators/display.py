# SPDX-License-Identifier: GPL-3.0-or-later

from bpy.props import BoolProperty, IntProperty
from bpy.types import Operator

from ..bl_logger import logger
from ..prefs import get_preferences


class VIEW3D_OT_gizmo_size(Operator):
    bl_idname = "view3d.gizmo_size"
    bl_label = "Change Gizmo Size"
    bl_description = "Increase or decrease the gizmo size"

    positive: BoolProperty(
        name="Direction",
        description="Direction of action. Positive if enabled, otherwise negative",
        default=True,
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


class VIEW3D_OT_gizmo_size_modal(Operator):
    bl_idname = "view3d.gizmo_size_modal"
    bl_label = "Gizmo Size (modal)"
    bl_description = "Change Gizmo Size by dragging your mouse up and down"
    bl_options = {"BLOCKING", "GRAB_CURSOR"}

    pixels_per_unit: IntProperty(
        name="Pixels per unit",
        description="Mouse travel needed to change the size by 1",
        default=4,
        min=1,
    )

    def invoke(self, context, event):
        self._start_y = event.mouse_y
        self._start_size = context.preferences.view.gizmo_size

        context.window_manager.modal_handler_add(self)
        return {"RUNNING_MODAL"}

    def modal(self, context, event):
        view = context.preferences.view

        if event.type == "MOUSEMOVE":
            delta = (event.mouse_y - self._start_y) // self.pixels_per_unit
            view.gizmo_size = max(10, min(200, self._start_size + delta))
            context.area.header_text_set(f"Gizmo Size: {view.gizmo_size}")
            context.area.tag_redraw()

        elif (event.type in {"RIGHTMOUSE"} and event.value == "RELEASE") or (
            event.type in {"LEFTMOUSE"} and event.value == "PRESS"
        ):
            context.area.header_text_set(None)
            return {"FINISHED"}

        elif event.type in {"ESC"} and event.value == "PRESS":
            view.gizmo_size = self._start_size
            context.area.header_text_set(None)
            return {"CANCELLED"}

        return {"RUNNING_MODAL"}
