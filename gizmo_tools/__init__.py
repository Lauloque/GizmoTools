# SPDX-License-Identifier: GPL-3.0-or-later


import bpy
from bpy.types import Menu

from .operators.display import *
from .operators.move import *
from .operators.rotate import *
from .prefs import VIEW3D_PT_gizmo_size_preferences


class VIEW3D_MT_gizmo_size_menu(Menu):
    bl_label = "Gizmo"
    bl_idname = "VIEW3D_MT_gizmo_menu"

    def draw(self, context):
        layout = self.layout
        layout.operator(
            "view3d.gizmo_size", text="Increase Gizmo Size", icon="ZOOM_IN"
        ).positive = True
        layout.operator(
            "view3d.gizmo_size", text="Decrease Gizmo Size", icon="ZOOM_OUT"
        ).positive = False
        layout.operator("view3d.gizmo_size_modal", icon="GIZMO")


def draw_gizmo_menu(self, context):
    layout = self.layout
    layout.menu(VIEW3D_MT_gizmo_size_menu.bl_idname)


addon_keymaps = []


classes = (
    VIEW3D_PT_gizmo_size_preferences,
    VIEW3D_MT_gizmo_size_menu,
    VIEW3D_OT_gizmo_size,
    VIEW3D_OT_gizmo_move,
    VIEW3D_OT_gizmo_rotate,
    VIEW3D_OT_gizmo_size_modal,
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
        # GIZMO SIZE +
        km = kc.keymaps.new(name="Window", region_type="WINDOW", space_type="EMPTY")
        kmi = km.keymap_items.new("view3d.gizmo_size", type="PAGE_UP", value="PRESS")
        kmi.properties.positive = True
        addon_keymaps.append((km, kmi))

        # GIZMO SIZE -
        km = kc.keymaps.new(name="Window", region_type="WINDOW", space_type="EMPTY")
        kmi = km.keymap_items.new("view3d.gizmo_size", type="PAGE_DOWN", value="PRESS")
        kmi.properties.positive = False
        addon_keymaps.append((km, kmi))

        # GIZMO SIZE MODAL
        km = kc.keymaps.new(name="Window", region_type="WINDOW", space_type="EMPTY")
        kmi = km.keymap_items.new(
            "view3d.gizmo_size_modal", "RIGHTMOUSE", "PRESS", alt=True
        )
        addon_keymaps.append((km, kmi))

        # Movements (X Y Z)
        movement_bindings = [
            ("LEFT_ARROW", "+X", {"alt": True}),
            ("RIGHT_ARROW", "-X", {"alt": True}),
            ("UP_ARROW", "+Y", {"alt": True}),
            ("DOWN_ARROW", "-Y", {"alt": True}),
            ("PAGE_UP", "+Z", {"alt": True}),
            ("PAGE_DOWN", "-Z", {"alt": True}),
        ]

        for key, axis, modifiers in movement_bindings:
            km = kc.keymaps.new(name="Window", region_type="WINDOW", space_type="EMPTY")
            kmi = km.keymap_items.new("view3d.gizmo_move", key, "PRESS", **modifiers)
            kmi.properties.axis = axis
            addon_keymaps.append((km, kmi))

        # Rotations (X Y Z)
        rotation_bindings = [
            ("LEFT_ARROW", "+X", {"alt": True, "shift": True}),
            ("RIGHT_ARROW", "-X", {"alt": True, "shift": True}),
            ("UP_ARROW", "+Y", {"alt": True, "shift": True}),
            ("DOWN_ARROW", "-Y", {"alt": True, "shift": True}),
            ("PAGE_UP", "+Z", {"alt": True, "shift": True}),
            ("PAGE_DOWN", "-Z", {"alt": True, "shift": True}),
        ]

        for key, axis, modifiers in rotation_bindings:
            km = kc.keymaps.new(name="Window", region_type="WINDOW", space_type="EMPTY")
            kmi = km.keymap_items.new("view3d.gizmo_rotate", key, "PRESS", **modifiers)
            kmi.properties.axis = axis
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
