# SPDX-License-Identifier: GPL-3.0-or-later

import bpy
from bpy.types import Operator

from .. import __package__ as base_package
from ..prefs import get_preferences


class VIEW3D_OT_decease_gizmo_size(Operator):
    bl_idname = "view3d.decease_gizmo_size"
    bl_label = "Decrease Gizmo Size"

    def execute(self, context):

        prefs = context.preferences
        addon_prefs = get_preferences()
        view = prefs.view
        gs = view.gizmo_size
        print("Gizmo size =", gs)
        print("Increment =", addon_prefs.inc)

        gs -= int(addon_prefs.inc)
        view.gizmo_size = gs
        print("New Gizmo size =", gs)
        return {"FINISHED"}


class VIEW3D_OT_incease_gizmo_size(Operator):
    bl_idname = "view3d.incease_gizmo_size"
    bl_label = "Increase Gizmo Size"

    def execute(self, context):

        prefs = context.preferences
        addon_prefs = get_preferences()
        view = prefs.view
        gs = view.gizmo_size
        print("Gizmo size =", gs)
        print("Increment =", addon_prefs.inc)

        gs += int(addon_prefs.inc)
        view.gizmo_size = gs
        print("New Gizmo size =", gs)
        return {"FINISHED"}
