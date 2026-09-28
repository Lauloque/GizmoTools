# SPDX-License-Identifier: GPL-3.0-or-later

import bpy
from bpy.types import Operator

from .. import __package__ as base_package


class VIEW3D_OT_move_local_x(Operator):
    bl_idname = "view3d.move_local_x"
    bl_label = "Move on the local X axis"
    bl_options = {"REGISTER", "UNDO"}

    @classmethod
    def poll(cls, context):
        return context.active_object is not None

    def execute(self, context):
        prefs = context.preferences
        addon_prefs = prefs.addons[base_package].preferences
        ot = bpy.ops.transform.translate
        ot(value=(addon_prefs.tinc, 0, 0), orient_type="LOCAL")
        return {"FINISHED"}


class VIEW3D_OT_move_local_nx(Operator):
    bl_idname = "view3d.move_local_nx"
    bl_label = "Move on the local -X axis"

    @classmethod
    def poll(cls, context):
        return context.active_object is not None

    def execute(self, context):
        prefs = context.preferences
        addon_prefs = prefs.addons[base_package].preferences
        ot = bpy.ops.transform.translate
        ot(value=(addon_prefs.tinc * -1, 0, 0), orient_type="LOCAL")
        return {"FINISHED"}


class VIEW3D_OT_move_local_y(Operator):
    bl_idname = "view3d.move_local_y"
    bl_label = "Move on the local Y axis"

    @classmethod
    def poll(cls, context):
        return context.active_object is not None

    def execute(self, context):
        prefs = context.preferences
        addon_prefs = prefs.addons[base_package].preferences
        ot = bpy.ops.transform.translate
        ot(value=(0, addon_prefs.tinc, 0), orient_type="LOCAL")
        return {"FINISHED"}


class VIEW3D_OT_move_local_ny(Operator):
    bl_idname = "view3d.move_local_ny"
    bl_label = "Move on the local -Y axis"

    @classmethod
    def poll(cls, context):
        return context.active_object is not None

    def execute(self, context):
        prefs = context.preferences
        addon_prefs = prefs.addons[base_package].preferences
        ot = bpy.ops.transform.translate
        ot(value=(0, addon_prefs.tinc * -1, 0), orient_type="LOCAL")
        return {"FINISHED"}


class VIEW3D_OT_move_local_z(Operator):
    bl_idname = "view3d.move_local_z"
    bl_label = "Move on the local Z axis"

    @classmethod
    def poll(cls, context):
        return context.active_object is not None

    def execute(self, context):
        prefs = context.preferences
        addon_prefs = prefs.addons[base_package].preferences
        ot = bpy.ops.transform.translate
        ot(value=(0, 0, addon_prefs.tinc), orient_type="LOCAL")
        return {"FINISHED"}


class VIEW3D_OT_move_local_nz(Operator):
    bl_idname = "view3d.move_local_nz"
    bl_label = "Move on the local -Z axis"

    @classmethod
    def poll(cls, context):
        return context.active_object is not None

    def execute(self, context):
        prefs = context.preferences
        addon_prefs = prefs.addons[base_package].preferences
        ot = bpy.ops.transform.translate
        ot(value=(0, 0, addon_prefs.tinc * -1), orient_type="LOCAL")
        return {"FINISHED"}
