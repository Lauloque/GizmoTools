# ##### BEGIN GPL LICENSE BLOCK #####
#
#  This program is free software; you can redistribute it and/or
#  modify it under the terms of the GNU General Public License
#  as published by the Free Software Foundation; either version 2
#  of the License, or (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software Foundation,
#  Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA.
#
# ##### END GPL LICENSE BLOCK #####

from bpy.types import (
    AddonPreferences,
    Operator,
    Menu,
)
from bpy.props import FloatProperty
import rna_keymap_ui
import bpy
from math import radians
bl_info = {
    "name": "Gizmo Tools",
    "description": "Allows you to do simple gizmo operations using keyboard shortcuts.",
    "author": "Loïc \"L0Lock\" Dautry",
    "version": (0, 1, 2),
    "blender": (3, 2, 0),
    "location": "View3D/UV Editor → Header → View → Gizmo",
    "warning": "Under development.",
    "wiki_url": "https://github.com/L0Lock/GizmoTools",
    "tracker_url": "https://github.com/L0Lock/GizmoTools/issues",
    "category": "Interface"
}


# -----------------------------------------------------------------------------
#    Operator : Decrease size
# -----------------------------------------------------------------------------

class VIEW3D_OT_decease_gizmo_size(bpy.types.Operator):
    bl_idname = "view3d.decease_gizmo_size"
    bl_label = "Decrease Gizmo Size"

    def execute(self, context):

        prefs = context.preferences
        addon_prefs = prefs.addons[__name__].preferences
        view = prefs.view
        gs = view.gizmo_size
        print("Gizmo size =", gs)
        print("Increment =", addon_prefs.inc)

        gs -= int(addon_prefs.inc)
        view.gizmo_size = gs
        print("New Gizmo size =", gs)
        return {'FINISHED'}

# -----------------------------------------------------------------------------
#    Operator : Increase size
# -----------------------------------------------------------------------------


class VIEW3D_OT_incease_gizmo_size(bpy.types.Operator):
    bl_idname = "view3d.incease_gizmo_size"
    bl_label = "Increase Gizmo Size"

    def execute(self, context):

        prefs = context.preferences
        addon_prefs = prefs.addons[__name__].preferences
        view = prefs.view
        gs = view.gizmo_size
        print("Gizmo size =", gs)
        print("Increment =", addon_prefs.inc)

        gs += int(addon_prefs.inc)
        view.gizmo_size = gs
        print("New Gizmo size =", gs)
        return {'FINISHED'}

# -----------------------------------------------------------------------------
#    Operator : Move Local X
# -----------------------------------------------------------------------------


class VIEW3D_OT_move_local_x(bpy.types.Operator):
    bl_idname = "view3d.move_local_x"
    bl_label = "Move on the local X axis"
    bl_options = {"REGISTER","UNDO"}

    @classmethod
    def poll(cls, context):
        return context.active_object is not None

    def execute(self, context):
        prefs = context.preferences
        addon_prefs = prefs.addons[__name__].preferences
        ot = bpy.ops.transform.translate
        ot(value=(addon_prefs.tinc, 0, 0), orient_type='LOCAL')
        return {'FINISHED'}

# -----------------------------------------------------------------------------
#    Operator : Move Local nX
# -----------------------------------------------------------------------------


class VIEW3D_OT_move_local_nx(bpy.types.Operator):
    bl_idname = "view3d.move_local_nx"
    bl_label = "Move on the local -X axis"

    @classmethod
    def poll(cls, context):
        return context.active_object is not None

    def execute(self, context):
        prefs = context.preferences
        addon_prefs = prefs.addons[__name__].preferences
        ot = bpy.ops.transform.translate
        ot(value=(addon_prefs.tinc*-1, 0, 0), orient_type='LOCAL')
        return {'FINISHED'}

# -----------------------------------------------------------------------------
#    Operator : Move Local Y
# -----------------------------------------------------------------------------


class VIEW3D_OT_move_local_y(bpy.types.Operator):
    bl_idname = "view3d.move_local_y"
    bl_label = "Move on the local Y axis"

    @classmethod
    def poll(cls, context):
        return context.active_object is not None

    def execute(self, context):
        prefs = context.preferences
        addon_prefs = prefs.addons[__name__].preferences
        ot = bpy.ops.transform.translate
        ot(value=(0, addon_prefs.tinc, 0), orient_type='LOCAL')
        return {'FINISHED'}

# -----------------------------------------------------------------------------
#    Operator : Move Local nY
# -----------------------------------------------------------------------------


class VIEW3D_OT_move_local_ny(bpy.types.Operator):
    bl_idname = "view3d.move_local_ny"
    bl_label = "Move on the local -Y axis"

    @classmethod
    def poll(cls, context):
        return context.active_object is not None

    def execute(self, context):
        prefs = context.preferences
        addon_prefs = prefs.addons[__name__].preferences
        ot = bpy.ops.transform.translate
        ot(value=(0, addon_prefs.tinc*-1, 0), orient_type='LOCAL')
        return {'FINISHED'}

# -----------------------------------------------------------------------------
#    Operator : Move Local Z
# -----------------------------------------------------------------------------


class VIEW3D_OT_move_local_z(bpy.types.Operator):
    bl_idname = "view3d.move_local_z"
    bl_label = "Move on the local Z axis"

    @classmethod
    def poll(cls, context):
        return context.active_object is not None

    def execute(self, context):
        prefs = context.preferences
        addon_prefs = prefs.addons[__name__].preferences
        ot = bpy.ops.transform.translate
        ot(value=(0, 0, addon_prefs.tinc), orient_type='LOCAL')
        return {'FINISHED'}

# -----------------------------------------------------------------------------
#    Operator : Move Local nZ
# -----------------------------------------------------------------------------


class VIEW3D_OT_move_local_nz(bpy.types.Operator):
    bl_idname = "view3d.move_local_nz"
    bl_label = "Move on the local -Z axis"

    @classmethod
    def poll(cls, context):
        return context.active_object is not None

    def execute(self, context):
        prefs = context.preferences
        addon_prefs = prefs.addons[__name__].preferences
        ot = bpy.ops.transform.translate
        ot(value=(0, 0, addon_prefs.tinc*-1), orient_type='LOCAL')
        return {'FINISHED'}

# -----------------------------------------------------------------------------
#    Operator : Rotate Local X
# -----------------------------------------------------------------------------


class VIEW3D_OT_rotate_local_x(bpy.types.Operator):
    bl_idname = "view3d.rotate_local_x"
    bl_label = "Rotate on the local X axis"

    @classmethod
    def poll(cls, context):
        return context.active_object is not None

    def execute(self, context):
        prefs = context.preferences
        addon_prefs = prefs.addons[__name__].preferences
        ot = bpy.ops.transform.rotate
        ot(value=addon_prefs.rinc, orient_axis='X', orient_type='LOCAL')
        return {'FINISHED'}

# -----------------------------------------------------------------------------
#    Operator : Rotate Local nX
# -----------------------------------------------------------------------------


class VIEW3D_OT_rotate_local_nx(bpy.types.Operator):
    bl_idname = "view3d.rotate_local_nx"
    bl_label = "Rotate on the local -X axis"

    @classmethod
    def poll(cls, context):
        return context.active_object is not None

    def execute(self, context):
        prefs = context.preferences
        addon_prefs = prefs.addons[__name__].preferences
        ot = bpy.ops.transform.rotate
        ot(value=addon_prefs.rinc*-1, orient_axis='X', orient_type='LOCAL')
        return {'FINISHED'}

# -----------------------------------------------------------------------------
#    Operator : Rotate Local Y
# -----------------------------------------------------------------------------


class VIEW3D_OT_rotate_local_y(bpy.types.Operator):
    bl_idname = "view3d.rotate_local_y"
    bl_label = "Rotate on the local Y axis"

    @classmethod
    def poll(cls, context):
        return context.active_object is not None

    def execute(self, context):
        prefs = context.preferences
        addon_prefs = prefs.addons[__name__].preferences
        ot = bpy.ops.transform.rotate
        ot(value=addon_prefs.rinc, orient_axis='Y', orient_type='LOCAL')
        return {'FINISHED'}

# -----------------------------------------------------------------------------
#    Operator : Rotate Local nY
# -----------------------------------------------------------------------------


class VIEW3D_OT_rotate_local_ny(bpy.types.Operator):
    bl_idname = "view3d.rotate_local_ny"
    bl_label = "Rotate on the local -Y axis"

    @classmethod
    def poll(cls, context):
        return context.active_object is not None

    def execute(self, context):
        prefs = context.preferences
        addon_prefs = prefs.addons[__name__].preferences
        ot = bpy.ops.transform.rotate
        ot(value=addon_prefs.rinc*-1, orient_axis='Y', orient_type='LOCAL')
        return {'FINISHED'}

# -----------------------------------------------------------------------------
#    Operator : Rotate Local Z
# -----------------------------------------------------------------------------


class VIEW3D_OT_rotate_local_z(bpy.types.Operator):
    bl_idname = "view3d.rotate_local_z"
    bl_label = "Rotate on the local Z axis"

    @classmethod
    def poll(cls, context):
        return context.active_object is not None

    def execute(self, context):
        prefs = context.preferences
        addon_prefs = prefs.addons[__name__].preferences
        ot = bpy.ops.transform.rotate
        ot(value=addon_prefs.rinc, orient_axis='Z', orient_type='LOCAL')
        return {'FINISHED'}

# -----------------------------------------------------------------------------
#    Operator : Rotate Local nZ
# -----------------------------------------------------------------------------


class VIEW3D_OT_rotate_local_nz(bpy.types.Operator):
    bl_idname = "view3d.rotate_local_nz"
    bl_label = "Rotate on the local -Z axis"

    @classmethod
    def poll(cls, context):
        return context.active_object is not None

    def execute(self, context):
        prefs = context.preferences
        addon_prefs = prefs.addons[__name__].preferences
        ot = bpy.ops.transform.rotate
        ot(value=addon_prefs.rinc*-1, orient_axis='Z', orient_type='LOCAL')
        return {'FINISHED'}

# -----------------------------------------------------------------------------
#    Preferences
# -----------------------------------------------------------------------------


class VIEW3D_PT_gizmo_size_preferences(AddonPreferences):
    bl_idname = __name__

    # Gismo Size Increment value
    inc: FloatProperty(
        name="Gizmo Increment",
        description="Gizmo Size Increment in px",
        default=20,
        min=1,
        soft_max=100,
        step=100,
        precision=0,
        subtype="PIXEL"
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
        subtype="ANGLE"
    )

    # Draws addon preferences

    def draw(self, context):
        layout = self.layout

        # Increment value
        row = layout.row(align=True)
        row.prop(self, "inc", toggle=True)
        row.prop(self, "tinc", toggle=True)
        row.prop(self, "rinc", toggle=True)

# -----------------------------------------------------------------------------
#    Gizmo Menu
# -----------------------------------------------------------------------------


class VIEW3D_MT_gizmo_size_menu(bpy.types.Menu):
    bl_label = "Gizmo"
    bl_idname = "VIEW3D_MT_gizmo_menu"

    def draw(self, context):
        layout = self.layout
        layout.operator("view3d.incease_gizmo_size", icon="ZOOM_IN")
        layout.operator("view3d.decease_gizmo_size", icon="ZOOM_OUT")


def draw_gizmo_menu(self, context):
    layout = self.layout
    layout.menu(VIEW3D_MT_gizmo_size_menu.bl_idname)


# -----------------------------------------------------------------------------
#    Keymap
# -----------------------------------------------------------------------------
addon_keymaps = []


# -----------------------------------------------------------------------------
#    Register
# -----------------------------------------------------------------------------

classes = (
    VIEW3D_PT_gizmo_size_preferences,
    VIEW3D_OT_incease_gizmo_size,
    VIEW3D_OT_decease_gizmo_size,
    VIEW3D_MT_gizmo_size_menu,
    VIEW3D_OT_move_local_x,
    VIEW3D_OT_move_local_nx,
    VIEW3D_OT_move_local_y,
    VIEW3D_OT_move_local_ny,
    VIEW3D_OT_move_local_z,
    VIEW3D_OT_move_local_nz,
    VIEW3D_OT_rotate_local_x,
    VIEW3D_OT_rotate_local_nx,
    VIEW3D_OT_rotate_local_y,
    VIEW3D_OT_rotate_local_ny,
    VIEW3D_OT_rotate_local_z,
    VIEW3D_OT_rotate_local_nz,

)


def register():
    from bpy.utils import register_class
    for cls in classes:
        register_class(cls)

    bpy.types.VIEW3D_MT_view.append(draw_gizmo_menu)
    bpy.types.IMAGE_MT_view.append(draw_gizmo_menu)

    # Keymap reg
    wm = bpy.context.window_manager
    kc = wm.keyconfigs.addon
    if kc:
        km = kc.keymaps.new(
            name='Window', region_type='WINDOW', space_type='EMPTY')
        kmi = km.keymap_items.new(
            "view3d.incease_gizmo_size", type='PAGE_UP', value='PRESS')# GIZMO +
        km = kc.keymaps.new(
            name='Window', region_type='WINDOW', space_type='EMPTY')
        kmi = km.keymap_items.new(
            "view3d.decease_gizmo_size", type='PAGE_DOWN', value='PRESS')# GIZMO -
        km = kc.keymaps.new(
            name='Window', region_type='WINDOW', space_type='EMPTY')
        kmi = km.keymap_items.new(
            "view3d.move_local_x", type='LEFT_ARROW', alt=True, value='PRESS')# MOVE X
        km = kc.keymaps.new(
            name='Window', region_type='WINDOW', space_type='EMPTY')
        kmi = km.keymap_items.new(
            "view3d.move_local_nx", type='RIGHT_ARROW', alt=True, value='PRESS')# MOVE -X
        km = kc.keymaps.new(
            name='Window', region_type='WINDOW', space_type='EMPTY')
        kmi = km.keymap_items.new(
            "view3d.move_local_y", type='UP_ARROW', alt=True, value='PRESS')# MOVE Y
        km = kc.keymaps.new(
            name='Window', region_type='WINDOW', space_type='EMPTY')
        kmi = km.keymap_items.new(
            "view3d.move_local_ny", type='DOWN_ARROW', alt=True, value='PRESS')# MOVE -Y
        km = kc.keymaps.new(
            name='Window', region_type='WINDOW', space_type='EMPTY')
        kmi = km.keymap_items.new(
            "view3d.move_local_z", type='PAGE_UP', alt=True, value='PRESS')# MOVE Z
        km = kc.keymaps.new(
            name='Window', region_type='WINDOW', space_type='EMPTY')
        kmi = km.keymap_items.new(
            "view3d.move_local_nz", type='PAGE_DOWN', alt=True, value='PRESS')# MOVE -Z
        km = kc.keymaps.new(
            name='Window', region_type='WINDOW', space_type='EMPTY')
        kmi = km.keymap_items.new(
            "view3d.rotate_local_x", type='LEFT_ARROW', alt=True, shift=True, value='PRESS')# ROTATE X
        km = kc.keymaps.new(
            name='Window', region_type='WINDOW', space_type='EMPTY')
        kmi = km.keymap_items.new(
            "view3d.rotate_local_nx", type='RIGHT_ARROW', alt=True, shift=True, value='PRESS')# ROTATE -X
        km = kc.keymaps.new(
            name='Window', region_type='WINDOW', space_type='EMPTY')
        kmi = km.keymap_items.new(
            "view3d.rotate_local_y", type='UP_ARROW', alt=True, shift=True, value='PRESS')# ROTATE Y
        km = kc.keymaps.new(
            name='Window', region_type='WINDOW', space_type='EMPTY')
        kmi = km.keymap_items.new(
            "view3d.rotate_local_ny", type='DOWN_ARROW', alt=True, shift=True, value='PRESS')# ROTATE -Y
        km = kc.keymaps.new(
            name='Window', region_type='WINDOW', space_type='EMPTY')
        kmi = km.keymap_items.new(
            "view3d.rotate_local_z", type='PAGE_UP', alt=True, shift=True, value='PRESS')# ROTATE Z
        km = kc.keymaps.new(
            name='Window', region_type='WINDOW', space_type='EMPTY')
        kmi = km.keymap_items.new(
            "view3d.rotate_local_nz", type='PAGE_DOWN', alt=True, shift=True, value='PRESS')# ROTATE -Z
        addon_keymaps.append((km, kmi))


def unregister():
    from bpy.utils import unregister_class
    for cls in reversed(classes):
        unregister_class(cls)

    bpy.types.VIEW3D_MT_view.remove(draw_gizmo_menu)
    bpy.types.IMAGE_MT_view.remove(draw_gizmo_menu)

    # Keymap unreg
    for km, kmi in addon_keymaps:
        km.keymap_items.remove(kmi)
    addon_keymaps.clear()
