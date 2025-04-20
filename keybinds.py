keyconfig_version = (3, 4, 6)
keyconfig_data = \
[("Screen",
  {"space_type": 'EMPTY', "region_type": 'WINDOW'},
  {"items":
   [("screen.animation_step", {"type": 'TIMER0', "value": 'ANY', "any": True}, None),
    ("screen.region_blend", {"type": 'TIMERREGION', "value": 'ANY', "any": True}, None),
    ("screen.space_context_cycle",
     {"type": 'TAB', "value": 'PRESS', "ctrl": True},
     {"properties":
      [("direction", 'NEXT'),
       ],
      },
     ),
    ("screen.space_context_cycle",
     {"type": 'TAB', "value": 'PRESS', "shift": True, "ctrl": True},
     {"properties":
      [("direction", 'PREV'),
       ],
      },
     ),
    ("screen.workspace_cycle",
     {"type": 'PAGE_DOWN', "value": 'PRESS', "ctrl": True},
     {"properties":
      [("direction", 'NEXT'),
       ],
      },
     ),
    ("screen.workspace_cycle",
     {"type": 'PAGE_UP', "value": 'PRESS', "ctrl": True},
     {"properties":
      [("direction", 'PREV'),
       ],
      },
     ),
    ("screen.region_quadview", {"type": 'Q', "value": 'PRESS', "ctrl": True, "alt": True}, None),
    ("screen.repeat_last", {"type": 'R', "value": 'PRESS', "shift": True, "repeat": True}, None),
    ("file.execute", {"type": 'RET', "value": 'PRESS'}, None),
    ("file.execute", {"type": 'NUMPAD_ENTER', "value": 'PRESS'}, None),
    ("file.cancel", {"type": 'ESC', "value": 'PRESS'}, None),
    ("asset.catalog_undo", {"type": 'Z', "value": 'PRESS', "ctrl": True, "repeat": True}, None),
    ("asset.catalog_redo", {"type": 'Z', "value": 'PRESS', "shift": True, "ctrl": True, "repeat": True}, None),
    ("ed.undo", {"type": 'Z', "value": 'PRESS', "ctrl": True, "repeat": True}, None),
    ("ed.redo", {"type": 'Z', "value": 'PRESS', "shift": True, "ctrl": True, "repeat": True}, None),
    ("render.render",
     {"type": 'BACK_SLASH', "value": 'PRESS'},
     {"properties":
      [("use_viewport", True),
       ],
      },
     ),
    ("render.render",
     {"type": 'F12', "value": 'PRESS', "ctrl": True},
     {"properties":
      [("animation", True),
       ("use_viewport", True),
       ],
      },
     ),
    ("render.view_cancel", {"type": 'ESC', "value": 'PRESS'}, None),
    ("render.view_show", {"type": 'F11', "value": 'PRESS'}, None),
    ("render.play_rendered_anim", {"type": 'F11', "value": 'PRESS', "ctrl": True}, None),
    ("screen.screen_full_area", {"type": 'SPACE', "value": 'PRESS', "ctrl": True}, None),
    ("screen.screen_full_area",
     {"type": 'SPACE', "value": 'PRESS', "ctrl": True, "alt": True},
     {"properties":
      [("use_hide_panels", True),
       ],
      },
     ),
    ("screen.redo_last", {"type": 'F9', "value": 'PRESS'}, None),
    ],
   },
  ),
 ]


if __name__ == "__main__":
    # Only add keywords that are supported.
    from bpy.app import version as blender_version
    keywords = {}
    if blender_version >= (2, 92, 0):
        keywords["keyconfig_version"] = keyconfig_version
    import os
    from bl_keymap_utils.io import keyconfig_import_from_data
    keyconfig_import_from_data(
        os.path.splitext(os.path.basename(__file__))[0],
        keyconfig_data,
        **keywords,
    )
