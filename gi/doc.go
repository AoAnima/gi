// Copyright (c) 2018, The GoKi Authors. All rights reserved.
// Use of this source code is governed by a BSD-style
// license that can be found in the LICENSE file.

/*
Package Gi (GoGi) provides a Graphical Interface based on GoKi Tree Node structs

2D and 3D (TBD) scenegraphs supported, each rendering to respective Viewport
which in turn can be integrated within the other type of scenegraph.

The 2D scenegraph supports:

	* Widget nodes for GUI actions (Buttons, Menus etc) -- render directly via Paint
	* Layouts for placing widgets, which are also container nodes
	* CSS-based styling, directly on Node Props (properties), and CSS StyleSheet
	* svg sub-package with SVG Viewport and shapes, paths, etc -- full SVG support
	* Icon is a wrapper around an SVG -- any SVG icon can be used

Layout Logic

All 2D scenegraphs are controlled by the Layout, which provides the logic for
organizing widgets / elements within the constraints of the display.
Typically start with a vertical LayoutVert in the viewport, with LayoutHoriz's
within that, or a LayoutGrid for more complex layouts:

	win := gi.NewWindow2D("test-window", "Test Window", width, height, true)
	vp := win.WinViewport2D()
	updt := vp.UpdateStart()

	vlay := win.SetMainVLay() // or SetMainFrame

	row1 := vlay.AddNewChild(gi.KiT_Layout, "row1").(*gi.Layout)
	row1.Lay = gi.LayoutHoriz

	...

    vp.UpdateEnd(updt)

Controlling the layout involves the following style properties:

	* width / height: sets the preferred size of item -- layout tries to give
      this amount of space unless it can't in which case it falls back on:

	* min-width / min-height: minimum size -- will not scale below this size.
      if not specified, it defaults to 1 em (the size of 1 character)

	* max-width / max-height: maximum size -- will not exceed this size if
      specified, otherwise if 0 it is ignored and preferred size is used.  If
      a negative number is specified, then the item stretches to take up
      available room.  The Stretch node is a builtin type that has this
      property set automatically, and can be added to any layout to fill up
      any available space.  The preferred size of the item is used to
      determine how much of the space is used by each stretchable element, so
      you can set that to achieve different proportional spacing.  By default
      the Stretch is just the minimum 1em in preferred size.

	* align-horiz / align-vert: for the other dimension in a Layout (e.g., for
      LayoutHoriz, the vertical dimension) this specifies how the items are
      aligned within the available space (e.g., tops, bottoms, centers).  In
      the dimension of the Layout (horiz for LayoutHoriz) it determines how
      extra space is allocated (only if there aren't any infinitely stretchy
      elements), e.g., right / left / center or justified.

	* SetFixedWidth / Height method can be used to set all size params to the
      same value, causing that item to be definitively sized.  This is
      convenient for sizing the Space node which adds a fixed amount of space
      (1em by default).

    * See the wiki for more detailed documentation.

Signals

All widgets send appropriate signals about user actions -- Connect to those
and check the signal type to determine the type of event.  Only one connection
per receiver -- handle all the different signal types in one function.

Views

Views are Widgets that automatically display and interact with standard Go
data, including structs, maps, slices, and the primitive data elements
(string, int, etc).  This implements a form of model / view separation between
data and GUI representation thereof, where the models are the Go data elements
themselves.

Views provide automatic, powerful GUI access to essentially any data in any
other Go package.  Furthermore, the ValueView framework allows for easy
customization and extension of the GUI representation, based on the classic Go
"Stringer"-like interface paradigm -- simply define a ValueView() method on
any type, returning giv.ValueView that manages the interface between data
structures and GUI representations.

See giv sub-package for all the View elements

SVG for Icons, Displays, etc

SVG (Structured Vector Graphics) is used icons, and for rendering any kind of
graphical output (drawing a graph, dial, etc).  See svg sub-package, and
examples/svg for an svg viewer, and examples/marbles for an svg animation.

Overlay

The gi.Window contains an OverlayVp viewport with nodes that are rendered on
top of the regular scenegraph -- this is used for drag-n-drop and other kinds
of transient control / manipulation functionality.  Overlay elements are not
subject to the standard layout constraints (via having the Overlay NodeFlag
set)

*/
package gi
