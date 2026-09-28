# SPDX-License-Identifier: GPL-3.0-or-later

import bpy
from bpy.types import Operator

from .. import __package__ as base_package


class VIEW3D_OT_rotate_local_x(Operator):
    bl_idname = "view3d.rotate_local_x"
    bl_label = "Rotate on the local X axis"

    @classmethod
    def poll(cls, context):
        return context.active_object is not None

    def execute(self, context):
        prefs = context.preferences
        addon_prefs = prefs.addons[base_package].preferences
        ot = bpy.ops.transform.rotate
        ot(value=addon_prefs.rinc, orient_axis="X", orient_type="LOCAL")
        return {"FINISHED"}


class VIEW3D_OT_rotate_local_nx(Operator):
    bl_idname = "view3d.rotate_local_nx"
    bl_label = "Rotate on the local -X axis"

    @classmethod
    def poll(cls, context):
        return context.active_object is not None

    def execute(self, context):
        prefs = context.preferences
        addon_prefs = prefs.addons[base_package].preferences
        ot = bpy.ops.transform.rotate
        ot(value=addon_prefs.rinc * -1, orient_axis="X", orient_type="LOCAL")
        return {"FINISHED"}


class VIEW3D_OT_rotate_local_y(Operator):
    bl_idname = "view3d.rotate_local_y"
    bl_label = "Rotate on the local Y axis"

    @classmethod
    def poll(cls, context):
        return context.active_object is not None

    def execute(self, context):
        prefs = context.preferences
        addon_prefs = prefs.addons[base_package].preferences
        ot = bpy.ops.transform.rotate
        ot(value=addon_prefs.rinc, orient_axis="Y", orient_type="LOCAL")
        return {"FINISHED"}


class VIEW3D_OT_rotate_local_ny(Operator):
    bl_idname = "view3d.rotate_local_ny"
    bl_label = "Rotate on the local -Y axis"

    @classmethod
    def poll(cls, context):
        return context.active_object is not None

    def execute(self, context):
        prefs = context.preferences
        addon_prefs = prefs.addons[base_package].preferences
        ot = bpy.ops.transform.rotate
        ot(value=addon_prefs.rinc * -1, orient_axis="Y", orient_type="LOCAL")
        return {"FINISHED"}


class VIEW3D_OT_rotate_local_z(Operator):
    bl_idname = "view3d.rotate_local_z"
    bl_label = "Rotate on the local Z axis"

    @classmethod
    def poll(cls, context):
        return context.active_object is not None

    def execute(self, context):
        prefs = context.preferences
        addon_prefs = prefs.addons[base_package].preferences
        ot = bpy.ops.transform.rotate
        ot(value=addon_prefs.rinc, orient_axis="Z", orient_type="LOCAL")
        return {"FINISHED"}


class VIEW3D_OT_rotate_local_nz(Operator):
    bl_idname = "view3d.rotate_local_nz"
    bl_label = "Rotate on the local -Z axis"

    @classmethod
    def poll(cls, context):
        return context.active_object is not None

    def execute(self, context):
        prefs = context.preferences
        addon_prefs = prefs.addons[base_package].preferences
        ot = bpy.ops.transform.rotate
        ot(value=addon_prefs.rinc * -1, orient_axis="Z", orient_type="LOCAL")
        return {"FINISHED"}
