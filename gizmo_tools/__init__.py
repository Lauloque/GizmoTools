# SPDX-License-Identifier: GPL-3.0-or-later


import bpy
from bpy.types import Menu

from .operators.display import *
from .operators.move import *
from .operators.rotate import *
from .prefs import VIEW3D_PT_gizmo_size_preferences

# -----------------------------------------------------------------------------
#    Gizmo Menu
# -----------------------------------------------------------------------------


class VIEW3D_MT_gizmo_size_menu(Menu):
    bl_label = "Gizmo"
    bl_idname = "VIEW3D_MT_gizmo_menu"

    def draw(self, context):
        layout = self.layout
        layout.operator("view3d.incease_gizmo_size", icon="ZOOM_IN")
        layout.operator("view3d.decease_gizmo_size", icon="ZOOM_OUT")


def draw_gizmo_menu(self, context):
    layout = self.layout
    layout.menu(VIEW3D_MT_gizmo_size_menu.bl_idname)


addon_keymaps = []


classes = (
    VIEW3D_PT_gizmo_size_preferences,
    VIEW3D_MT_gizmo_size_menu,
    VIEW3D_OT_incease_gizmo_size,
    VIEW3D_OT_decease_gizmo_size,
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
        km = kc.keymaps.new(name="Window", region_type="WINDOW", space_type="EMPTY")
        kmi = km.keymap_items.new(
            "view3d.incease_gizmo_size", type="PAGE_UP", value="PRESS"
        )  # GIZMO +
        km = kc.keymaps.new(name="Window", region_type="WINDOW", space_type="EMPTY")
        kmi = km.keymap_items.new(
            "view3d.decease_gizmo_size", type="PAGE_DOWN", value="PRESS"
        )  # GIZMO -
        km = kc.keymaps.new(name="Window", region_type="WINDOW", space_type="EMPTY")
        kmi = km.keymap_items.new(
            "view3d.move_local_x", type="LEFT_ARROW", alt=True, value="PRESS"
        )  # MOVE X
        km = kc.keymaps.new(name="Window", region_type="WINDOW", space_type="EMPTY")
        kmi = km.keymap_items.new(
            "view3d.move_local_nx", type="RIGHT_ARROW", alt=True, value="PRESS"
        )  # MOVE -X
        km = kc.keymaps.new(name="Window", region_type="WINDOW", space_type="EMPTY")
        kmi = km.keymap_items.new(
            "view3d.move_local_y", type="UP_ARROW", alt=True, value="PRESS"
        )  # MOVE Y
        km = kc.keymaps.new(name="Window", region_type="WINDOW", space_type="EMPTY")
        kmi = km.keymap_items.new(
            "view3d.move_local_ny", type="DOWN_ARROW", alt=True, value="PRESS"
        )  # MOVE -Y
        km = kc.keymaps.new(name="Window", region_type="WINDOW", space_type="EMPTY")
        kmi = km.keymap_items.new(
            "view3d.move_local_z", type="PAGE_UP", alt=True, value="PRESS"
        )  # MOVE Z
        km = kc.keymaps.new(name="Window", region_type="WINDOW", space_type="EMPTY")
        kmi = km.keymap_items.new(
            "view3d.move_local_nz", type="PAGE_DOWN", alt=True, value="PRESS"
        )  # MOVE -Z
        km = kc.keymaps.new(name="Window", region_type="WINDOW", space_type="EMPTY")
        kmi = km.keymap_items.new(
            "view3d.rotate_local_x",
            type="LEFT_ARROW",
            alt=True,
            shift=True,
            value="PRESS",
        )  # ROTATE X
        km = kc.keymaps.new(name="Window", region_type="WINDOW", space_type="EMPTY")
        kmi = km.keymap_items.new(
            "view3d.rotate_local_nx",
            type="RIGHT_ARROW",
            alt=True,
            shift=True,
            value="PRESS",
        )  # ROTATE -X
        km = kc.keymaps.new(name="Window", region_type="WINDOW", space_type="EMPTY")
        kmi = km.keymap_items.new(
            "view3d.rotate_local_y",
            type="UP_ARROW",
            alt=True,
            shift=True,
            value="PRESS",
        )  # ROTATE Y
        km = kc.keymaps.new(name="Window", region_type="WINDOW", space_type="EMPTY")
        kmi = km.keymap_items.new(
            "view3d.rotate_local_ny",
            type="DOWN_ARROW",
            alt=True,
            shift=True,
            value="PRESS",
        )  # ROTATE -Y
        km = kc.keymaps.new(name="Window", region_type="WINDOW", space_type="EMPTY")
        kmi = km.keymap_items.new(
            "view3d.rotate_local_z", type="PAGE_UP", alt=True, shift=True, value="PRESS"
        )  # ROTATE Z
        km = kc.keymaps.new(name="Window", region_type="WINDOW", space_type="EMPTY")
        kmi = km.keymap_items.new(
            "view3d.rotate_local_nz",
            type="PAGE_DOWN",
            alt=True,
            shift=True,
            value="PRESS",
        )  # ROTATE -Z
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
