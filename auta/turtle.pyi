import tkinter as TK


class ScrolledCanvas(TK.Frame):
    def __getitem__(self, key):
        """Return the resource value for a KEY given as string."""

    def __init__(self, master, width=500, height=350, canvwidth=600, canvheight=500): ...


    def __repr__(self): ...


    def __setitem__(self, key, value): ...


    def __str__(self):
        """Return the window path name of this widget."""

    def addtag(self, *args, **kw): ...


    def addtag_above(self, *args, **kw): ...


    def addtag_all(self, *args, **kw): ...


    def addtag_below(self, *args, **kw): ...


    def addtag_closest(self, *args, **kw): ...


    def addtag_enclosed(self, *args, **kw): ...


    def addtag_overlapping(self, *args, **kw): ...


    def addtag_withtag(self, *args, **kw): ...


    def adjustScrolls(self):
        """
        Adjust scrollbars according to window- and canvas-size.
        """

    def after(self, ms, func=None, *args):
        """
        Call function once after given time.

        MS specifies the time in milliseconds. FUNC gives the
        function which shall be called. Additional parameters
        are given as parameters to the function call.  Return
        identifier to cancel scheduling with after_cancel.    """

    def after_cancel(self, id):
        """
        Cancel scheduling of function identified with ID.

        Identifier returned by after or after_idle must be
        given as first parameter.
        """

    def after_idle(self, func, *args):
        """
        Call FUNC once if the Tcl main loop has no event to
        process.

        Return an identifier to cancel the scheduling with
        after_cancel.    """

    def anchor(self, anchor=None):
        """
        The anchor value controls how to place the grid within the
        master when no row/column has any weight.

        The default anchor is nw.    """

    def bbox(self, *args):
        """
        'forward' method, which canvas itself has inherited...
        """

    def bell(self, displayof=0):
        """Ring a display's bell."""

    def bind(self, *args, **kwargs):
        """
        'forward' method, which canvas itself has inherited...
        """

    def bind_all(self, sequence=None, func=None, add=None):
        """
        Bind to all widgets at an event SEQUENCE a call to function FUNC.
        An additional boolean parameter ADD specifies whether FUNC will
        be called additionally to the other bound function or whether
        it will replace the previous function. See bind for the return value.    """

    def bind_class(self, className, sequence=None, func=None, add=None):
        """
        Bind to widgets with bindtag CLASSNAME at event
        SEQUENCE a call of function FUNC. An additional
        boolean parameter ADD specifies whether FUNC will be
        called additionally to the other bound function or
        whether it will replace the previous function. See bind for
        the return value.    """

    def bindtags(self, tagList=None):
        """
        Set or get the list of bindtags for this widget.

        With no argument return the list of all bindtags associated with
        this widget. With a list of strings as argument the bindtags are
        set to this list. The bindtags determine in which order events are
        processed (see bind).    """

    def canvasx(self, *args, **kw): ...


    def canvasy(self, *args, **kw): ...


    def cget(self, *args, **kwargs):
        """
        'forward' method, which canvas itself has inherited...
        """

    def clipboard_append(self, string, **kw):
        """
        Append STRING to the Tk clipboard.

        A widget specified at the optional displayof keyword
        argument specifies the target display. The clipboard
        can be retrieved with selection_get.    """

    def clipboard_clear(self, **kw):
        """
        Clear the data in the Tk clipboard.

        A widget specified for the optional displayof keyword
        argument specifies the target display.    """

    def clipboard_get(self, **kw):
        """
        Retrieve data from the clipboard on window's display.

        The window keyword defaults to the root window of the Tkinter
        application.

        The type keyword specifies the form in which the data is
        to be returned and should be an atom name such as STRING
        or FILE_NAME.  Type defaults to STRING, except on X11, where the default
        is to try UTF8_STRING and fall back to STRING.

        This command is equivalent to:

        selection_get(CLIPBOARD)
        """

    def columnconfigure(self, index, cnf={}, **kw):
        """
        Configure column INDEX of a grid.

        Valid resources are minsize (minimum size of the column),
        weight (how much does additional space propagate to this column)
        and pad (how much space to let additionally).    """

    def config(self, *args, **kwargs):
        """
        'forward' method, which canvas itself has inherited...
        """

    def configure(self, cnf=None, **kw):
        """
        Configure resources of a widget.

        The values for resources are specified as keyword
        arguments. To get an overview about
        the allowed keyword arguments call the method keys.
        """

    def coords(self, *args, **kw): ...


    def create_arc(self, *args, **kw): ...


    def create_bitmap(self, *args, **kw): ...


    def create_image(self, *args, **kw): ...


    def create_line(self, *args, **kw): ...


    def create_oval(self, *args, **kw): ...


    def create_polygon(self, *args, **kw): ...


    def create_rectangle(self, *args, **kw): ...


    def create_text(self, *args, **kw): ...


    def create_window(self, *args, **kw): ...


    def dchars(self, *args, **kw): ...


    def delete(self, *args, **kw): ...


    def deletecommand(self, name):
        """
        Internal function.

        Delete the Tcl command provided in NAME.    """

    def destroy(self):
        """Destroy this and all descendants widgets."""

    def dtag(self, *args, **kw): ...


    def event_add(self, virtual, *sequences):
        """
        Bind a virtual event VIRTUAL (of the form <<Name>>)
        to an event SEQUENCE such that the virtual event is triggered
        whenever SEQUENCE occurs.    """

    def event_delete(self, virtual, *sequences):
        """Unbind a virtual event VIRTUAL from SEQUENCE."""

    def event_generate(self, sequence, **kw):
        """
        Generate an event SEQUENCE. Additional
        keyword arguments specify parameter of the event
        (e.g. x, y, rootx, rooty).    """

    def event_info(self, virtual=None):
        """
        Return a list of all virtual events or the information
        about the SEQUENCE bound to the virtual event VIRTUAL.    """

    def find(self, *args, **kw): ...


    def find_above(self, *args, **kw): ...


    def find_all(self, *args, **kw): ...


    def find_below(self, *args, **kw): ...


    def find_closest(self, *args, **kw): ...


    def find_enclosed(self, *args, **kw): ...


    def find_overlapping(self, *args, **kw): ...


    def find_withtag(self, *args, **kw): ...


    def focus(self):
        """
        Direct input focus to this widget.

        If the application currently does not have the focus
        this widget will get the focus if the application gets
        the focus through the window manager.    """

    def focus_displayof(self):
        """
        Return the widget which has currently the focus on the
        display where this widget is located.

        Return None if the application does not have the focus.    """

    def focus_force(self):
        """
        'forward' method, which canvas itself has inherited...
        """

    def focus_get(self):
        """
        Return the widget which has currently the focus in the
        application.

        Use focus_displayof to allow working with several
        displays. Return None if application does not have
        the focus.    """

    def focus_lastfor(self):
        """
        Return the widget which would have the focus if top level
        for this widget gets the focus from the window manager.    """

    def focus_set(self):
        """
        Direct input focus to this widget.

        If the application currently does not have the focus
        this widget will get the focus if the application gets
        the focus through the window manager.    """

    def forget(self):
        """Unmap this widget and do not use it for the packing order."""

    def getboolean(self, s):
        """Return a boolean value for Tcl boolean values true and false given as parameter."""

    def getdouble(self, s): ...


    def getint(self, s): ...


    def gettags(self, *args, **kw): ...


    def getvar(self, name='PY_VAR'):
        """Return value of Tcl variable NAME."""

    def grab_current(self):
        """
        Return widget which has currently the grab in this application
        or None.    """

    def grab_release(self):
        """Release grab for this widget if currently set."""

    def grab_set(self):
        """
        Set grab for this widget.

        A grab directs all events to this and descendant
        widgets in the application.    """

    def grab_set_global(self):
        """
        Set global grab for this widget.

        A global grab directs all events to this and
        descendant widgets on the display. Use with caution -
        other applications do not get events anymore.    """

    def grab_status(self):
        """
        Return None, "local" or "global" if this widget has
        no, a local or a global grab.    """

    def grid(self, cnf={}, **kw):
        """
        Position a widget in the parent widget in a grid. Use as options:
        column=number - use cell identified with given column (starting with 0)
        columnspan=number - this widget will span several columns
        in=master - use master to contain this widget
        in_=master - see 'in' option description
        ipadx=amount - add internal padding in x direction
        ipady=amount - add internal padding in y direction
        padx=amount - add padding in x direction
        pady=amount - add padding in y direction
        row=number - use cell identified with given row (starting with 0)
        rowspan=number - this widget will span several rows
        sticky=NSEW - if cell is larger on which sides will this
                      widget stick to the cell boundary
        """

    def grid_anchor(self, anchor=None):
        """
        The anchor value controls how to place the grid within the
        master when no row/column has any weight.

        The default anchor is nw.    """

    def grid_bbox(self, column=None, row=None, col2=None, row2=None):
        """
        Return a tuple of integer coordinates for the bounding
        box of this widget controlled by the geometry manager grid.

        If COLUMN, ROW is given the bounding box applies from
        the cell with row and column 0 to the specified
        cell. If COL2 and ROW2 are given the bounding box
        starts at that cell.

        The returned integers specify the offset of the upper left
        corner in the master widget and the width and height.
        """

    def grid_columnconfigure(self, index, cnf={}, **kw):
        """
        Configure column INDEX of a grid.

        Valid resources are minsize (minimum size of the column),
        weight (how much does additional space propagate to this column)
        and pad (how much space to let additionally).    """

    def grid_configure(self, cnf={}, **kw):
        """
        Position a widget in the parent widget in a grid. Use as options:
        column=number - use cell identified with given column (starting with 0)
        columnspan=number - this widget will span several columns
        in=master - use master to contain this widget
        in_=master - see 'in' option description
        ipadx=amount - add internal padding in x direction
        ipady=amount - add internal padding in y direction
        padx=amount - add padding in x direction
        pady=amount - add padding in y direction
        row=number - use cell identified with given row (starting with 0)
        rowspan=number - this widget will span several rows
        sticky=NSEW - if cell is larger on which sides will this
                      widget stick to the cell boundary
        """

    def grid_forget(self):
        """Unmap this widget."""

    def grid_info(self):
        """
        Return information about the options
        for positioning this widget in a grid.    """

    def grid_location(self, x, y):
        """
        Return a tuple of column and row which identify the cell
        at which the pixel at position X and Y inside the master
        widget is located.    """

    def grid_propagate(self, flag=['_noarg_']):
        """
        Set or get the status for propagation of geometry information.

        A boolean argument specifies whether the geometry information
        of the slaves will determine the size of this widget. If no argument
        is given, the current setting will be returned.
        """

    def grid_remove(self):
        """Unmap this widget but remember the grid options."""

    def grid_rowconfigure(self, index, cnf={}, **kw):
        """
        Configure row INDEX of a grid.

        Valid resources are minsize (minimum size of the row),
        weight (how much does additional space propagate to this row)
        and pad (how much space to let additionally).    """

    def grid_size(self):
        """Return a tuple of the number of column and rows in the grid."""

    def grid_slaves(self, row=None, column=None):
        """
        Return a list of all slaves of this widget
        in its packing order.    """

    def icursor(self, *args, **kw): ...


    def image_names(self):
        """Return a list of all existing image names."""

    def image_types(self):
        """Return a list of all available image types (e.g. photo bitmap)."""

    def index(self, *args, **kw): ...


    def info(self):
        """
        Return information about the packing options
        for this widget.    """

    def insert(self, *args, **kw): ...


    def itemcget(self, *args, **kw): ...


    def itemconfig(self, *args, **kw): ...


    def itemconfigure(self, *args, **kw): ...


    def keys(self):
        """Return a list of all resource names of this widget."""

    def lift(self, aboveThis=None):
        """Raise this widget in the stacking order."""

    def location(self, x, y):
        """
        Return a tuple of column and row which identify the cell
        at which the pixel at position X and Y inside the master
        widget is located.    """

    def lower(self, belowThis=None):
        """Lower this widget in the stacking order."""

    def mainloop(self, n=0):
        """Call the mainloop of Tk."""

    def move(self, *args, **kw): ...


    def nametowidget(self, name):
        """
        Return the Tkinter instance of a widget identified by
        its Tcl name NAME.    """

    def onResize(self, event):
        """self-explanatory"""

    def option_add(self, pattern, value, priority=None):
        """
        Set a VALUE (second parameter) for an option
        PATTERN (first parameter).

        An optional third parameter gives the numeric priority
        (defaults to 80).    """

    def option_clear(self):
        """
        Clear the option database.

        It will be reloaded if option_add is called.    """

    def option_get(self, name, className):
        """
        Return the value for an option NAME for this widget
        with CLASSNAME.

        Values with higher priority override lower values.    """

    def option_readfile(self, fileName, priority=None):
        """
        Read file FILENAME into the option database.

        An optional second parameter gives the numeric
        priority.    """

    def pack(self, cnf={}, **kw):
        """
        Pack a widget in the parent widget. Use as options:
        after=widget - pack it after you have packed widget
        anchor=NSEW (or subset) - position widget according to
                                  given direction
        before=widget - pack it before you will pack widget
        expand=bool - expand widget if parent size grows
        fill=NONE or X or Y or BOTH - fill widget if widget grows
        in=master - use master to contain this widget
        in_=master - see 'in' option description
        ipadx=amount - add internal padding in x direction
        ipady=amount - add internal padding in y direction
        padx=amount - add padding in x direction
        pady=amount - add padding in y direction
        side=TOP or BOTTOM or LEFT or RIGHT -  where to add this widget.
        """

    def pack_configure(self, cnf={}, **kw):
        """
        Pack a widget in the parent widget. Use as options:
        after=widget - pack it after you have packed widget
        anchor=NSEW (or subset) - position widget according to
                                  given direction
        before=widget - pack it before you will pack widget
        expand=bool - expand widget if parent size grows
        fill=NONE or X or Y or BOTH - fill widget if widget grows
        in=master - use master to contain this widget
        in_=master - see 'in' option description
        ipadx=amount - add internal padding in x direction
        ipady=amount - add internal padding in y direction
        padx=amount - add padding in x direction
        pady=amount - add padding in y direction
        side=TOP or BOTTOM or LEFT or RIGHT -  where to add this widget.
        """

    def pack_forget(self):
        """Unmap this widget and do not use it for the packing order."""

    def pack_info(self):
        """
        Return information about the packing options
        for this widget.    """

    def pack_propagate(self, flag=['_noarg_']):
        """
        Set or get the status for propagation of geometry information.

        A boolean argument specifies whether the geometry information
        of the slaves will determine the size of this widget. If no argument
        is given the current setting will be returned.
        """

    def pack_slaves(self):
        """
        Return a list of all slaves of this widget
        in its packing order.    """

    def place(self, cnf={}, **kw):
        """
        Place a widget in the parent widget. Use as options:
        in=master - master relative to which the widget is placed
        in_=master - see 'in' option description
        x=amount - locate anchor of this widget at position x of master
        y=amount - locate anchor of this widget at position y of master
        relx=amount - locate anchor of this widget between 0.0 and 1.0
                      relative to width of master (1.0 is right edge)
        rely=amount - locate anchor of this widget between 0.0 and 1.0
                      relative to height of master (1.0 is bottom edge)
        anchor=NSEW (or subset) - position anchor according to given direction
        width=amount - width of this widget in pixel
        height=amount - height of this widget in pixel
        relwidth=amount - width of this widget between 0.0 and 1.0
                          relative to width of master (1.0 is the same width
                          as the master)
        relheight=amount - height of this widget between 0.0 and 1.0
                           relative to height of master (1.0 is the same
                           height as the master)
        bordermode="inside" or "outside" - whether to take border width of
                                           master widget into account
        """

    def place_configure(self, cnf={}, **kw):
        """
        Place a widget in the parent widget. Use as options:
        in=master - master relative to which the widget is placed
        in_=master - see 'in' option description
        x=amount - locate anchor of this widget at position x of master
        y=amount - locate anchor of this widget at position y of master
        relx=amount - locate anchor of this widget between 0.0 and 1.0
                      relative to width of master (1.0 is right edge)
        rely=amount - locate anchor of this widget between 0.0 and 1.0
                      relative to height of master (1.0 is bottom edge)
        anchor=NSEW (or subset) - position anchor according to given direction
        width=amount - width of this widget in pixel
        height=amount - height of this widget in pixel
        relwidth=amount - width of this widget between 0.0 and 1.0
                          relative to width of master (1.0 is the same width
                          as the master)
        relheight=amount - height of this widget between 0.0 and 1.0
                           relative to height of master (1.0 is the same
                           height as the master)
        bordermode="inside" or "outside" - whether to take border width of
                                           master widget into account
        """

    def place_forget(self):
        """Unmap this widget."""

    def place_info(self):
        """
        Return information about the placing options
        for this widget.    """

    def place_slaves(self):
        """
        Return a list of all slaves of this widget
        in its packing order.    """

    def postscript(self, *args, **kw): ...


    def propagate(self, flag=['_noarg_']):
        """
        Set or get the status for propagation of geometry information.

        A boolean argument specifies whether the geometry information
        of the slaves will determine the size of this widget. If no argument
        is given the current setting will be returned.
        """

    def quit(self):
        """Quit the Tcl interpreter. All widgets will be destroyed."""

    def register(self, func, subst=None, needcleanup=1):
        """
        Return a newly created Tcl function. If this
        function is called, the Python function FUNC will
        be executed. An optional function SUBST can
        be given which will be executed before FUNC.    """

    def reset(self, canvwidth=None, canvheight=None, bg=None):
        """Adjust canvas and scrollbars according to given canvas size."""

    def rowconfigure(self, index, cnf={}, **kw):
        """
        Configure row INDEX of a grid.

        Valid resources are minsize (minimum size of the row),
        weight (how much does additional space propagate to this row)
        and pad (how much space to let additionally).    """

    def scale(self, *args, **kw): ...


    def scan_dragto(self, *args, **kw): ...


    def scan_mark(self, *args, **kw): ...


    def select_adjust(self, *args, **kw): ...


    def select_clear(self, *args, **kw): ...


    def select_from(self, *args, **kw): ...


    def select_item(self, *args, **kw): ...


    def select_to(self, *args, **kw): ...


    def selection_clear(self, **kw):
        """Clear the current X selection."""

    def selection_get(self, **kw):
        """
        Return the contents of the current X selection.

        A keyword parameter selection specifies the name of
        the selection and defaults to PRIMARY.  A keyword
        parameter displayof specifies a widget on the display
        to use. A keyword parameter type specifies the form of data to be
        fetched, defaulting to STRING except on X11, where UTF8_STRING is tried
        before STRING.    """

    def selection_handle(self, command, **kw):
        """
        Specify a function COMMAND to call if the X
        selection owned by this widget is queried by another
        application.

        This function must return the contents of the
        selection. The function will be called with the
        arguments OFFSET and LENGTH which allows the chunking
        of very long selections. The following keyword
        parameters can be provided:
        selection - name of the selection (default PRIMARY),
        type - type of the selection (e.g. STRING, FILE_NAME).    """

    def selection_own(self, **kw):
        """
        Become owner of X selection.

        A keyword parameter selection specifies the name of
        the selection (default PRIMARY).    """

    def selection_own_get(self, **kw):
        """
        Return owner of X selection.

        The following keyword parameter can
        be provided:
        selection - name of the selection (default PRIMARY),
        type - type of the selection (e.g. STRING, FILE_NAME).    """

    def send(self, interp, cmd, *args):
        """Send Tcl command CMD to different interpreter INTERP to be executed."""

    def setvar(self, name='PY_VAR', value='1'):
        """Set Tcl variable NAME to VALUE."""

    def size(self):
        """Return a tuple of the number of column and rows in the grid."""

    def slaves(self):
        """
        Return a list of all slaves of this widget
        in its packing order.    """

    def tag_bind(self, *args, **kw): ...


    def tag_lower(self, *args, **kw): ...


    def tag_raise(self, *args, **kw): ...


    def tag_unbind(self, *args, **kw): ...


    def tk_bisque(self):
        """Change the color scheme to light brown as used in Tk 3.6 and before."""

    def tk_focusFollowsMouse(self):
        """
        The widget under mouse will get automatically focus. Can not
        be disabled easily.    """

    def tk_focusNext(self):
        """
        Return the next widget in the focus order which follows
        widget which has currently the focus.

        The focus order first goes to the next child, then to
        the children of the child recursively and then to the
        next sibling which is higher in the stacking order.  A
        widget is omitted if it has the takefocus resource set
        to 0.    """

    def tk_focusPrev(self):
        """Return previous widget in the focus order. See tk_focusNext for details."""

    def tk_setPalette(self, *args, **kw):
        """
        Set a new color scheme for all widget elements.

        A single color as argument will cause that all colors of Tk
        widget elements are derived from this.
        Alternatively several keyword parameters and its associated
        colors can be given. The following keywords are valid:
        activeBackground, foreground, selectColor,
        activeForeground, highlightBackground, selectBackground,
        background, highlightColor, selectForeground,
        disabledForeground, insertBackground, troughColor.    """

    def tk_strictMotif(self, boolean=None):
        """
        Set Tcl internal variable, whether the look and feel
        should adhere to Motif.

        A parameter of 1 means adhere to Motif (e.g. no color
        change if mouse passes over slider).
        Returns the set value.    """

    def tkraise(self, aboveThis=None):
        """Raise this widget in the stacking order."""

    def type(self, *args, **kw): ...


    def unbind(self, *args, **kwargs):
        """
        'forward' method, which canvas itself has inherited...
        """

    def unbind_all(self, sequence):
        """Unbind for all widgets for event SEQUENCE all functions."""

    def unbind_class(self, className, sequence):
        """
        Unbind for all widgets with bindtag CLASSNAME for event SEQUENCE
        all functions.    """

    def update(self):
        """Enter event loop until all pending events have been processed by Tcl."""

    def update_idletasks(self):
        """
        Enter event loop until all idle callbacks have been called. This
        will update the display of windows but not process events caused by
        the user.    """

    def wait_variable(self, name='PY_VAR'):
        """
        Wait until the variable is modified.

        A parameter of type IntVar, StringVar, DoubleVar or
        BooleanVar must be given.    """

    def wait_visibility(self, window=None):
        """
        Wait until the visibility of a WIDGET changes
        (e.g. it appears).

        If no parameter is given self is used.    """

    def wait_window(self, window=None):
        """
        Wait until a WIDGET is destroyed.

        If no parameter is given self is used.    """

    def waitvar(self, name='PY_VAR'):
        """
        Wait until the variable is modified.

        A parameter of type IntVar, StringVar, DoubleVar or
        BooleanVar must be given.    """

    def winfo_atom(self, name, displayof=0):
        """Return integer which represents atom NAME."""

    def winfo_atomname(self, id, displayof=0):
        """Return name of atom with identifier ID."""

    def winfo_cells(self):
        """Return number of cells in the colormap for this widget."""

    def winfo_children(self):
        """Return a list of all widgets which are children of this widget."""

    def winfo_class(self):
        """Return window class name of this widget."""

    def winfo_colormapfull(self):
        """Return true if at the last color request the colormap was full."""

    def winfo_containing(self, rootX, rootY, displayof=0):
        """Return the widget which is at the root coordinates ROOTX, ROOTY."""

    def winfo_depth(self):
        """Return the number of bits per pixel."""

    def winfo_exists(self):
        """Return true if this widget exists."""

    def winfo_fpixels(self, number):
        """
        Return the number of pixels for the given distance NUMBER
        (e.g. "3c") as float.    """

    def winfo_geometry(self):
        """Return geometry string for this widget in the form "widthxheight+X+Y"."""

    def winfo_height(self):
        """Return height of this widget."""

    def winfo_id(self):
        """Return identifier ID for this widget."""

    def winfo_interps(self, displayof=0):
        """Return the name of all Tcl interpreters for this display."""

    def winfo_ismapped(self):
        """Return true if this widget is mapped."""

    def winfo_manager(self):
        """Return the window manager name for this widget."""

    def winfo_name(self):
        """Return the name of this widget."""

    def winfo_parent(self):
        """Return the name of the parent of this widget."""

    def winfo_pathname(self, id, displayof=0):
        """Return the pathname of the widget given by ID."""

    def winfo_pixels(self, number):
        """Rounded integer value of winfo_fpixels."""

    def winfo_pointerx(self):
        """Return the x coordinate of the pointer on the root window."""

    def winfo_pointerxy(self):
        """Return a tuple of x and y coordinates of the pointer on the root window."""

    def winfo_pointery(self):
        """Return the y coordinate of the pointer on the root window."""

    def winfo_reqheight(self):
        """Return requested height of this widget."""

    def winfo_reqwidth(self):
        """Return requested width of this widget."""

    def winfo_rgb(self, color):
        """
        Return tuple of decimal values for red, green, blue for
        COLOR in this widget.    """

    def winfo_rootx(self):
        """
        Return x coordinate of upper left corner of this widget on the
        root window.    """

    def winfo_rooty(self):
        """
        Return y coordinate of upper left corner of this widget on the
        root window.    """

    def winfo_screen(self):
        """Return the screen name of this widget."""

    def winfo_screencells(self):
        """
        Return the number of the cells in the colormap of the screen
        of this widget.    """

    def winfo_screendepth(self):
        """
        Return the number of bits per pixel of the root window of the
        screen of this widget.    """

    def winfo_screenheight(self):
        """
        Return the number of pixels of the height of the screen of this widget
        in pixel.    """

    def winfo_screenmmheight(self):
        """
        Return the number of pixels of the height of the screen of
        this widget in mm.    """

    def winfo_screenmmwidth(self):
        """
        Return the number of pixels of the width of the screen of
        this widget in mm.    """

    def winfo_screenvisual(self):
        """
        Return one of the strings directcolor, grayscale, pseudocolor,
        staticcolor, staticgray, or truecolor for the default
        colormodel of this screen.    """

    def winfo_screenwidth(self):
        """
        Return the number of pixels of the width of the screen of
        this widget in pixel.    """

    def winfo_server(self):
        """
        Return information of the X-Server of the screen of this widget in
        the form "XmajorRminor vendor vendorVersion".    """

    def winfo_toplevel(self):
        """Return the toplevel widget of this widget."""

    def winfo_viewable(self):
        """Return true if the widget and all its higher ancestors are mapped."""

    def winfo_visual(self):
        """
        Return one of the strings directcolor, grayscale, pseudocolor,
        staticcolor, staticgray, or truecolor for the
        colormodel of this widget.    """

    def winfo_visualid(self):
        """Return the X identifier for the visual for this widget."""

    def winfo_visualsavailable(self, includeids=False):
        """
        Return a list of all visuals available for the screen
        of this widget.

        Each item in the list consists of a visual name (see winfo_visual), a
        depth and if includeids is true is given also the X identifier.    """

    def winfo_vrootheight(self):
        """
        Return the height of the virtual root window associated with this
        widget in pixels. If there is no virtual root window return the
        height of the screen.    """

    def winfo_vrootwidth(self):
        """
        Return the width of the virtual root window associated with this
        widget in pixel. If there is no virtual root window return the
        width of the screen.    """

    def winfo_vrootx(self):
        """
        Return the x offset of the virtual root relative to the root
        window of the screen of this widget.    """

    def winfo_vrooty(self):
        """
        Return the y offset of the virtual root relative to the root
        window of the screen of this widget.    """

    def winfo_width(self):
        """Return the width of this widget."""

    def winfo_x(self):
        """
        Return the x coordinate of the upper left corner of this widget
        in the parent.    """

    def winfo_y(self):
        """
        Return the y coordinate of the upper left corner of this widget
        in the parent.    """

    def xview(self, *args, **kw): ...


    def xview_moveto(self, *args, **kw): ...


    def xview_scroll(self, *args, **kw): ...


    def yview(self, *args, **kw): ...


    def yview_moveto(self, *args, **kw): ...


    def yview_scroll(self, *args, **kw): ...




class RawTurtle:
    def __init__(self, cv, mode='standard', colormode=1.0, delay=10): ...


    def addshape(self, name, shape=None):
        """
        Adds a turtle shape to TurtleScreen's shapelist.

        Arguments:
        (1) name is the name of a gif-file and shape is None.
            Installs the corresponding image shape.
            !! Image-shapes DO NOT rotate when turning the turtle,
            !! so they do not display the heading of the turtle!
        (2) name is an arbitrary string and shape is a tuple
            of pairs of coordinates. Installs the corresponding
            polygon shape
        (3) name is an arbitrary string and shape is a
            (compound) Shape object. Installs the corresponding
            compound shape.
        To use a shape, you have to issue the command shape(shapename).

        call: register_shape("turtle.gif")
        --or: register_shape("tri", ((0,0), (10,10), (-10,10)))

        Example (for a TurtleScreen instance named screen):
        >>> screen.register_shape("triangle", ((5,-3),(0,5),(-5,-3)))

        """

    def bgcolor(self, *args):
        """
        Set or return backgroundcolor of the TurtleScreen.

        Arguments (if given): a color string or three numbers
        in the range 0..colormode or a 3-tuple of such numbers.

        Example (for a TurtleScreen instance named screen):
        >>> screen.bgcolor("orange")
        >>> screen.bgcolor()
        'orange'
        >>> screen.bgcolor(0.5,0,0.5)
        >>> screen.bgcolor()
        '#800080'
        """

    def bgpic(self, picname=None):
        """
        Set background image or return name of current backgroundimage.

        Optional argument:
        picname -- a string, name of a gif-file or "nopic".

        If picname is a filename, set the corresponding image as background.
        If picname is "nopic", delete backgroundimage, if present.
        If picname is None, return the filename of the current backgroundimage.

        Example (for a TurtleScreen instance named screen):
        >>> screen.bgpic()
        'nopic'
        >>> screen.bgpic("landscape.gif")
        >>> screen.bgpic()
        'landscape.gif'
        """

    def clear(self):
        """
        Delete all drawings and all turtles from the TurtleScreen.

        No argument.

        Reset empty TurtleScreen to its initial state: white background,
        no backgroundimage, no eventbindings and tracing on.

        Example (for a TurtleScreen instance named screen):
        >>> screen.clear()

        Note: this method is not available as function.
        """

    def clearscreen(self):
        """
        Delete all drawings and all turtles from the TurtleScreen.

        No argument.

        Reset empty TurtleScreen to its initial state: white background,
        no backgroundimage, no eventbindings and tracing on.

        Example (for a TurtleScreen instance named screen):
        >>> screen.clear()

        Note: this method is not available as function.
        """

    def colormode(self, cmode=None):
        """
        Return the colormode or set it to 1.0 or 255.

        Optional argument:
        cmode -- one of the values 1.0 or 255

        r, g, b values of colortriples have to be in range 0..cmode.

        Example (for a TurtleScreen instance named screen):
        >>> screen.colormode()
        1.0
        >>> screen.colormode(255)
        >>> pencolor(240,160,80)
        """

    def delay(self, delay=None):
        """
         Return or set the drawing delay in milliseconds.

        Optional argument:
        delay -- positive integer

        Example (for a TurtleScreen instance named screen):
        >>> screen.delay(15)
        >>> screen.delay()
        15
        """

    def getcanvas(self):
        """
        Return the Canvas of this TurtleScreen.

        No argument.

        Example (for a Screen instance named screen):
        >>> cv = screen.getcanvas()
        >>> cv
        <turtle.ScrolledCanvas instance at 0x010742D8>
        """

    def getshapes(self):
        """
        Return a list of names of all currently available turtle shapes.

        No argument.

        Example (for a TurtleScreen instance named screen):
        >>> screen.getshapes()
        ['arrow', 'blank', 'circle', ... , 'turtle']
        """

    def listen(self, xdummy=None, ydummy=None):
        """
        Set focus on TurtleScreen (in order to collect key-events)

        No arguments.
        Dummy arguments are provided in order
        to be able to pass listen to the onclick method.

        Example (for a TurtleScreen instance named screen):
        >>> screen.listen()
        """

    def mainloop(self):
        """
        Starts event loop - calling Tkinter's mainloop function.

        No argument.

        Must be last statement in a turtle graphics program.
        Must NOT be used if a script is run from within IDLE in -n mode
        (No subprocess) - for interactive use of turtle graphics.

        Example (for a TurtleScreen instance named screen):
        >>> screen.mainloop()

        """

    def mode(self, mode=None):
        """
        Set turtle-mode ('standard', 'logo' or 'world') and perform reset.

        Optional argument:
        mode -- one of the strings 'standard', 'logo' or 'world'

        Mode 'standard' is compatible with turtle.py.
        Mode 'logo' is compatible with most Logo-Turtle-Graphics.
        Mode 'world' uses userdefined 'worldcoordinates'. *Attention*: in
        this mode angles appear distorted if x/y unit-ratio doesn't equal 1.
        If mode is not given, return the current mode.

             Mode      Initial turtle heading     positive angles
         ------------|-------------------------|-------------------
          'standard'    to the right (east)       counterclockwise
            'logo'        upward    (north)         clockwise

        Examples:
        >>> mode('logo')   # resets turtle heading to north
        >>> mode()
        'logo'
        """

    def numinput(self, title, prompt, default=None, minval=None, maxval=None):
        """
        Pop up a dialog window for input of a number.

        Arguments: title is the title of the dialog window,
        prompt is a text mostly describing what numerical information to input.
        default: default value
        minval: minimum value for imput
        maxval: maximum value for input

        The number input must be in the range minval .. maxval if these are
        given. If not, a hint is issued and the dialog remains open for
        correction. Return the number input.
        If the dialog is canceled,  return None.

        Example (for a TurtleScreen instance named screen):
        >>> screen.numinput("Poker", "Your stakes:", 1000, minval=10, maxval=10000)

        """

    def onclick(self, fun, btn=1, add=None):
        """
        Bind fun to mouse-click event on canvas.

        Arguments:
        fun -- a function with two arguments, the coordinates of the
               clicked point on the canvas.
        num -- the number of the mouse-button, defaults to 1

        Example (for a TurtleScreen instance named screen)

        >>> screen.onclick(goto)
        >>> # Subsequently clicking into the TurtleScreen will
        >>> # make the turtle move to the clicked point.
        >>> screen.onclick(None)
        """

    def onkey(self, fun, key):
        """
        Bind fun to key-release event of key.

        Arguments:
        fun -- a function with no arguments
        key -- a string: key (e.g. "a") or key-symbol (e.g. "space")

        In order to be able to register key-events, TurtleScreen
        must have focus. (See method listen.)

        Example (for a TurtleScreen instance named screen):

        >>> def f():
        ...     fd(50)
        ...     lt(60)
        ...
        >>> screen.onkey(f, "Up")
        >>> screen.listen()

        Subsequently the turtle can be moved by repeatedly pressing
        the up-arrow key, consequently drawing a hexagon

        """

    def onkeypress(self, fun, key=None):
        """
        Bind fun to key-press event of key if key is given,
        or to any key-press-event if no key is given.

        Arguments:
        fun -- a function with no arguments
        key -- a string: key (e.g. "a") or key-symbol (e.g. "space")

        In order to be able to register key-events, TurtleScreen
        must have focus. (See method listen.)

        Example (for a TurtleScreen instance named screen
        and a Turtle instance named turtle):

        >>> def f():
        ...     fd(50)
        ...     lt(60)
        ...
        >>> screen.onkeypress(f, "Up")
        >>> screen.listen()

        Subsequently the turtle can be moved by repeatedly pressing
        the up-arrow key, or by keeping pressed the up-arrow key.
        consequently drawing a hexagon.
        """

    def onkeyrelease(self, fun, key):
        """
        Bind fun to key-release event of key.

        Arguments:
        fun -- a function with no arguments
        key -- a string: key (e.g. "a") or key-symbol (e.g. "space")

        In order to be able to register key-events, TurtleScreen
        must have focus. (See method listen.)

        Example (for a TurtleScreen instance named screen):

        >>> def f():
        ...     fd(50)
        ...     lt(60)
        ...
        >>> screen.onkey(f, "Up")
        >>> screen.listen()

        Subsequently the turtle can be moved by repeatedly pressing
        the up-arrow key, consequently drawing a hexagon

        """

    def onscreenclick(self, fun, btn=1, add=None):
        """
        Bind fun to mouse-click event on canvas.

        Arguments:
        fun -- a function with two arguments, the coordinates of the
               clicked point on the canvas.
        num -- the number of the mouse-button, defaults to 1

        Example (for a TurtleScreen instance named screen)

        >>> screen.onclick(goto)
        >>> # Subsequently clicking into the TurtleScreen will
        >>> # make the turtle move to the clicked point.
        >>> screen.onclick(None)
        """

    def ontimer(self, fun, t=0):
        """
        Install a timer, which calls fun after t milliseconds.

        Arguments:
        fun -- a function with no arguments.
        t -- a number >= 0

        Example (for a TurtleScreen instance named screen):

        >>> running = True
        >>> def f():
        ...     if running:
        ...             fd(50)
        ...             lt(60)
        ...             screen.ontimer(f, 250)
        ...
        >>> f()   # makes the turtle marching around
        >>> running = False
        """

    def register_shape(self, name, shape=None):
        """
        Adds a turtle shape to TurtleScreen's shapelist.

        Arguments:
        (1) name is the name of a gif-file and shape is None.
            Installs the corresponding image shape.
            !! Image-shapes DO NOT rotate when turning the turtle,
            !! so they do not display the heading of the turtle!
        (2) name is an arbitrary string and shape is a tuple
            of pairs of coordinates. Installs the corresponding
            polygon shape
        (3) name is an arbitrary string and shape is a
            (compound) Shape object. Installs the corresponding
            compound shape.
        To use a shape, you have to issue the command shape(shapename).

        call: register_shape("turtle.gif")
        --or: register_shape("tri", ((0,0), (10,10), (-10,10)))

        Example (for a TurtleScreen instance named screen):
        >>> screen.register_shape("triangle", ((5,-3),(0,5),(-5,-3)))

        """

    def reset(self):
        """
        Reset all Turtles on the Screen to their initial state.

        No argument.

        Example (for a TurtleScreen instance named screen):
        >>> screen.reset()
        """

    def resetscreen(self):
        """
        Reset all Turtles on the Screen to their initial state.

        No argument.

        Example (for a TurtleScreen instance named screen):
        >>> screen.reset()
        """

    def screensize(self, canvwidth=None, canvheight=None, bg=None):
        """
        Resize the canvas the turtles are drawing on.

        Optional arguments:
        canvwidth -- positive integer, new width of canvas in pixels
        canvheight --  positive integer, new height of canvas in pixels
        bg -- colorstring or color-tuple, new backgroundcolor
        If no arguments are given, return current (canvaswidth, canvasheight)

        Do not alter the drawing window. To observe hidden parts of
        the canvas use the scrollbars. (Can make visible those parts
        of a drawing, which were outside the canvas before!)

        Example (for a Turtle instance named turtle):
        >>> turtle.screensize(2000,1500)
        >>> # e.g. to search for an erroneously escaped turtle ;-)
        """

    def setworldcoordinates(self, llx, lly, urx, ury):
        """
        Set up a user defined coordinate-system.

        Arguments:
        llx -- a number, x-coordinate of lower left corner of canvas
        lly -- a number, y-coordinate of lower left corner of canvas
        urx -- a number, x-coordinate of upper right corner of canvas
        ury -- a number, y-coordinate of upper right corner of canvas

        Set up user coodinat-system and switch to mode 'world' if necessary.
        This performs a screen.reset. If mode 'world' is already active,
        all drawings are redrawn according to the new coordinates.

        But ATTENTION: in user-defined coordinatesystems angles may appear
        distorted. (see Screen.mode())

        Example (for a TurtleScreen instance named screen):
        >>> screen.setworldcoordinates(-10,-0.5,50,1.5)
        >>> for _ in range(36):
        ...     left(10)
        ...     forward(0.5)
        """

    def textinput(self, title, prompt):
        """
        Pop up a dialog window for input of a string.

        Arguments: title is the title of the dialog window,
        prompt is a text mostly describing what information to input.

        Return the string input
        If the dialog is canceled, return None.

        Example (for a TurtleScreen instance named screen):
        >>> screen.textinput("NIM", "Name of first player:")

        """

    def tracer(self, n=None, delay=None):
        """
        Turns turtle animation on/off and set delay for update drawings.

        Optional arguments:
        n -- nonnegative  integer
        delay -- nonnegative  integer

        If n is given, only each n-th regular screen update is really performed.
        (Can be used to accelerate the drawing of complex graphics.)
        Second arguments sets delay value (see RawTurtle.delay())

        Example (for a TurtleScreen instance named screen):
        >>> screen.tracer(8, 25)
        >>> dist = 2
        >>> for i in range(200):
        ...     fd(dist)
        ...     rt(90)
        ...     dist += 2
        """

    def turtles(self):
        """
        Return the list of turtles on the screen.

        Example (for a TurtleScreen instance named screen):
        >>> screen.turtles()
        [<turtle.Turtle object at 0x00E11FB0>]
        """

    def update(self):
        """
        Perform a TurtleScreen update.
        """

    def window_height(self):
        """
         Return the height of the turtle window.

        Example (for a TurtleScreen instance named screen):
        >>> screen.window_height()
        480
        """

    def window_width(self):
        """
         Return the width of the turtle window.

        Example (for a TurtleScreen instance named screen):
        >>> screen.window_width()
        640
        """



def Screen():
    """
        Return the singleton screen object.
    If none exists at the moment, create a new one and return it,
    else return the existing one.    """


class RawTurtle:
    def __init__(self, canvas=None, shape='classic', undobuffersize=1000, visible=True): ...


    def back(self, distance):
        """
        Move the turtle backward by distance.

        Aliases: back | backward | bk

        Argument:
        distance -- a number

        Move the turtle backward by distance ,opposite to the direction the
        turtle is headed. Do not change the turtle's heading.

        Example (for a Turtle instance named turtle):
        >>> turtle.position()
        (0.00, 0.00)
        >>> turtle.backward(30)
        >>> turtle.position()
        (-30.00, 0.00)
        """

    def backward(self, distance):
        """
        Move the turtle backward by distance.

        Aliases: back | backward | bk

        Argument:
        distance -- a number

        Move the turtle backward by distance ,opposite to the direction the
        turtle is headed. Do not change the turtle's heading.

        Example (for a Turtle instance named turtle):
        >>> turtle.position()
        (0.00, 0.00)
        >>> turtle.backward(30)
        >>> turtle.position()
        (-30.00, 0.00)
        """

    def begin_fill(self):
        """
        Called just before drawing a shape to be filled.

        No argument.

        Example (for a Turtle instance named turtle):
        >>> turtle.color("black", "red")
        >>> turtle.begin_fill()
        >>> turtle.circle(60)
        >>> turtle.end_fill()
        """

    def begin_poly(self):
        """
        Start recording the vertices of a polygon.

        No argument.

        Start recording the vertices of a polygon. Current turtle position
        is first point of polygon.

        Example (for a Turtle instance named turtle):
        >>> turtle.begin_poly()
        """

    def bk(self, distance):
        """
        Move the turtle backward by distance.

        Aliases: back | backward | bk

        Argument:
        distance -- a number

        Move the turtle backward by distance ,opposite to the direction the
        turtle is headed. Do not change the turtle's heading.

        Example (for a Turtle instance named turtle):
        >>> turtle.position()
        (0.00, 0.00)
        >>> turtle.backward(30)
        >>> turtle.position()
        (-30.00, 0.00)
        """

    def circle(self, radius, extent=None, steps=None):
        """
         Draw a circle with given radius.

        Arguments:
        radius -- a number
        extent (optional) -- a number
        steps (optional) -- an integer

        Draw a circle with given radius. The center is radius units left
        of the turtle; extent - an angle - determines which part of the
        circle is drawn. If extent is not given, draw the entire circle.
        If extent is not a full circle, one endpoint of the arc is the
        current pen position. Draw the arc in counterclockwise direction
        if radius is positive, otherwise in clockwise direction. Finally
        the direction of the turtle is changed by the amount of extent.

        As the circle is approximated by an inscribed regular polygon,
        steps determines the number of steps to use. If not given,
        it will be calculated automatically. Maybe used to draw regular
        polygons.

        call: circle(radius)                  # full circle
        --or: circle(radius, extent)          # arc
        --or: circle(radius, extent, steps)
        --or: circle(radius, steps=6)         # 6-sided polygon

        Example (for a Turtle instance named turtle):
        >>> turtle.circle(50)
        >>> turtle.circle(120, 180)  # semicircle
        """

    def clear(self):
        """
        Delete the turtle's drawings from the screen. Do not move turtle.

        No arguments.

        Delete the turtle's drawings from the screen. Do not move turtle.
        State and position of the turtle as well as drawings of other
        turtles are not affected.

        Examples (for a Turtle instance named turtle):
        >>> turtle.clear()
        """

    def clearstamp(self, stampid):
        """
        Delete stamp with given stampid

        Argument:
        stampid - an integer, must be return value of previous stamp() call.

        Example (for a Turtle instance named turtle):
        >>> turtle.color("blue")
        >>> astamp = turtle.stamp()
        >>> turtle.fd(50)
        >>> turtle.clearstamp(astamp)
        """

    def clearstamps(self, n=None):
        """
        Delete all or first/last n of turtle's stamps.

        Optional argument:
        n -- an integer

        If n is None, delete all of pen's stamps,
        else if n > 0 delete first n stamps
        else if n < 0 delete last n stamps.

        Example (for a Turtle instance named turtle):
        >>> for i in range(8):
        ...     turtle.stamp(); turtle.fd(30)
        ...
        >>> turtle.clearstamps(2)
        >>> turtle.clearstamps(-2)
        >>> turtle.clearstamps()
        """

    def clone(self):
        """
        Create and return a clone of the turtle.

        No argument.

        Create and return a clone of the turtle with same position, heading
        and turtle properties.

        Example (for a Turtle instance named mick):
        mick = Turtle()
        joe = mick.clone()
        """

    def color(self, *args):
        """
        Return or set the pencolor and fillcolor.

        Arguments:
        Several input formats are allowed.
        They use 0, 1, 2, or 3 arguments as follows:

        color()
            Return the current pencolor and the current fillcolor
            as a pair of color specification strings as are returned
            by pencolor and fillcolor.
        color(colorstring), color((r,g,b)), color(r,g,b)
            inputs as in pencolor, set both, fillcolor and pencolor,
            to the given value.
        color(colorstring1, colorstring2),
        color((r1,g1,b1), (r2,g2,b2))
            equivalent to pencolor(colorstring1) and fillcolor(colorstring2)
            and analogously, if the other input format is used.

        If turtleshape is a polygon, outline and interior of that polygon
        is drawn with the newly set colors.
        For mor info see: pencolor, fillcolor

        Example (for a Turtle instance named turtle):
        >>> turtle.color('red', 'green')
        >>> turtle.color()
        ('red', 'green')
        >>> colormode(255)
        >>> color((40, 80, 120), (160, 200, 240))
        >>> color()
        ('#285078', '#a0c8f0')
        """

    def degrees(self, fullcircle=360.0):
        """
         Set angle measurement units to degrees.

        Optional argument:
        fullcircle -  a number

        Set angle measurement units, i. e. set number
        of 'degrees' for a full circle. Dafault value is
        360 degrees.

        Example (for a Turtle instance named turtle):
        >>> turtle.left(90)
        >>> turtle.heading()
        90

        Change angle measurement unit to grad (also known as gon,
        grade, or gradian and equals 1/100-th of the right angle.)
        >>> turtle.degrees(400.0)
        >>> turtle.heading()
        100

        """

    def distance(self, x, y=None):
        """
        Return the distance from the turtle to (x,y) in turtle step units.

        Arguments:
        x -- a number   or  a pair/vector of numbers   or   a turtle instance
        y -- a number       None                            None

        call: distance(x, y)         # two coordinates
        --or: distance((x, y))       # a pair (tuple) of coordinates
        --or: distance(vec)          # e.g. as returned by pos()
        --or: distance(mypen)        # where mypen is another turtle

        Example (for a Turtle instance named turtle):
        >>> turtle.pos()
        (0.00, 0.00)
        >>> turtle.distance(30,40)
        50.0
        >>> pen = Turtle()
        >>> pen.forward(77)
        >>> turtle.distance(pen)
        77.0
        """

    def dot(self, size=None, *color):
        """
        Draw a dot with diameter size, using color.

        Optional arguments:
        size -- an integer >= 1 (if given)
        color -- a colorstring or a numeric color tuple

        Draw a circular dot with diameter size, using color.
        If size is not given, the maximum of pensize+4 and 2*pensize is used.

        Example (for a Turtle instance named turtle):
        >>> turtle.dot()
        >>> turtle.fd(50); turtle.dot(20, "blue"); turtle.fd(50)
        """

    def down(self):
        """
        Pull the pen down -- drawing when moving.

        Aliases: pendown | pd | down

        No argument.

        Example (for a Turtle instance named turtle):
        >>> turtle.pendown()
        """

    def end_fill(self):
        """
        Fill the shape drawn after the call begin_fill().

        No argument.

        Example (for a Turtle instance named turtle):
        >>> turtle.color("black", "red")
        >>> turtle.begin_fill()
        >>> turtle.circle(60)
        >>> turtle.end_fill()
        """

    def end_poly(self):
        """
        Stop recording the vertices of a polygon.

        No argument.

        Stop recording the vertices of a polygon. Current turtle position is
        last point of polygon. This will be connected with the first point.

        Example (for a Turtle instance named turtle):
        >>> turtle.end_poly()
        """

    def fd(self, distance):
        """
        Move the turtle forward by the specified distance.

        Aliases: forward | fd

        Argument:
        distance -- a number (integer or float)

        Move the turtle forward by the specified distance, in the direction
        the turtle is headed.

        Example (for a Turtle instance named turtle):
        >>> turtle.position()
        (0.00, 0.00)
        >>> turtle.forward(25)
        >>> turtle.position()
        (25.00,0.00)
        >>> turtle.forward(-75)
        >>> turtle.position()
        (-50.00,0.00)
        """

    def fillcolor(self, *args):
        """
         Return or set the fillcolor.

        Arguments:
        Four input formats are allowed:
          - fillcolor()
            Return the current fillcolor as color specification string,
            possibly in hex-number format (see example).
            May be used as input to another color/pencolor/fillcolor call.
          - fillcolor(colorstring)
            s is a Tk color specification string, such as "red" or "yellow"
          - fillcolor((r, g, b))
            *a tuple* of r, g, and b, which represent, an RGB color,
            and each of r, g, and b are in the range 0..colormode,
            where colormode is either 1.0 or 255
          - fillcolor(r, g, b)
            r, g, and b represent an RGB color, and each of r, g, and b
            are in the range 0..colormode

        If turtleshape is a polygon, the interior of that polygon is drawn
        with the newly set fillcolor.

        Example (for a Turtle instance named turtle):
        >>> turtle.fillcolor('violet')
        >>> col = turtle.pencolor()
        >>> turtle.fillcolor(col)
        >>> turtle.fillcolor(0, .5, 0)
        """

    def filling(self):
        """
        Return fillstate (True if filling, False else).

        No argument.

        Example (for a Turtle instance named turtle):
        >>> turtle.begin_fill()
        >>> if turtle.filling():
        ...     turtle.pensize(5)
        ... else:
        ...     turtle.pensize(3)
        """

    def forward(self, distance):
        """
        Move the turtle forward by the specified distance.

        Aliases: forward | fd

        Argument:
        distance -- a number (integer or float)

        Move the turtle forward by the specified distance, in the direction
        the turtle is headed.

        Example (for a Turtle instance named turtle):
        >>> turtle.position()
        (0.00, 0.00)
        >>> turtle.forward(25)
        >>> turtle.position()
        (25.00,0.00)
        >>> turtle.forward(-75)
        >>> turtle.position()
        (-50.00,0.00)
        """

    def get_poly(self):
        """
        Return the lastly recorded polygon.

        No argument.

        Example (for a Turtle instance named turtle):
        >>> p = turtle.get_poly()
        >>> turtle.register_shape("myFavouriteShape", p)
        """

    def get_shapepoly(self):
        """
        Return the current shape polygon as tuple of coordinate pairs.

        No argument.

        Examples (for a Turtle instance named turtle):
        >>> turtle.shape("square")
        >>> turtle.shapetransform(4, -1, 0, 2)
        >>> turtle.get_shapepoly()
        ((50, -20), (30, 20), (-50, 20), (-30, -20))

        """

    def getpen(self):
        """
        Return the Turtleobject itself.

        No argument.

        Only reasonable use: as a function to return the 'anonymous turtle':

        Example:
        >>> pet = getturtle()
        >>> pet.fd(50)
        >>> pet
        <turtle.Turtle object at 0x0187D810>
        >>> turtles()
        [<turtle.Turtle object at 0x0187D810>]
        """

    def getscreen(self):
        """
        Return the TurtleScreen object, the turtle is drawing  on.

        No argument.

        Return the TurtleScreen object, the turtle is drawing  on.
        So TurtleScreen-methods can be called for that object.

        Example (for a Turtle instance named turtle):
        >>> ts = turtle.getscreen()
        >>> ts
        <turtle.TurtleScreen object at 0x0106B770>
        >>> ts.bgcolor("pink")
        """

    def getturtle(self):
        """
        Return the Turtleobject itself.

        No argument.

        Only reasonable use: as a function to return the 'anonymous turtle':

        Example:
        >>> pet = getturtle()
        >>> pet.fd(50)
        >>> pet
        <turtle.Turtle object at 0x0187D810>
        >>> turtles()
        [<turtle.Turtle object at 0x0187D810>]
        """

    def goto(self, x, y=None):
        """
        Move turtle to an absolute position.

        Aliases: setpos | setposition | goto:

        Arguments:
        x -- a number      or     a pair/vector of numbers
        y -- a number             None

        call: goto(x, y)         # two coordinates
        --or: goto((x, y))       # a pair (tuple) of coordinates
        --or: goto(vec)          # e.g. as returned by pos()

        Move turtle to an absolute position. If the pen is down,
        a line will be drawn. The turtle's orientation does not change.

        Example (for a Turtle instance named turtle):
        >>> tp = turtle.pos()
        >>> tp
        (0.00, 0.00)
        >>> turtle.setpos(60,30)
        >>> turtle.pos()
        (60.00,30.00)
        >>> turtle.setpos((20,80))
        >>> turtle.pos()
        (20.00,80.00)
        >>> turtle.setpos(tp)
        >>> turtle.pos()
        (0.00,0.00)
        """

    def heading(self):
        """
         Return the turtle's current heading.

        No arguments.

        Example (for a Turtle instance named turtle):
        >>> turtle.left(67)
        >>> turtle.heading()
        67.0
        """

    def hideturtle(self):
        """
        Makes the turtle invisible.

        Aliases: hideturtle | ht

        No argument.

        It's a good idea to do this while you're in the
        middle of a complicated drawing, because hiding
        the turtle speeds up the drawing observably.

        Example (for a Turtle instance named turtle):
        >>> turtle.hideturtle()
        """

    def home(self):
        """
        Move turtle to the origin - coordinates (0,0).

        No arguments.

        Move turtle to the origin - coordinates (0,0) and set its
        heading to its start-orientation (which depends on mode).

        Example (for a Turtle instance named turtle):
        >>> turtle.home()
        """

    def ht(self):
        """
        Makes the turtle invisible.

        Aliases: hideturtle | ht

        No argument.

        It's a good idea to do this while you're in the
        middle of a complicated drawing, because hiding
        the turtle speeds up the drawing observably.

        Example (for a Turtle instance named turtle):
        >>> turtle.hideturtle()
        """

    def isdown(self):
        """
        Return True if pen is down, False if it's up.

        No argument.

        Example (for a Turtle instance named turtle):
        >>> turtle.penup()
        >>> turtle.isdown()
        False
        >>> turtle.pendown()
        >>> turtle.isdown()
        True
        """

    def isvisible(self):
        """
        Return True if the Turtle is shown, False if it's hidden.

        No argument.

        Example (for a Turtle instance named turtle):
        >>> turtle.hideturtle()
        >>> print turtle.isvisible():
        False
        """

    def left(self, angle):
        """
        Turn turtle left by angle units.

        Aliases: left | lt

        Argument:
        angle -- a number (integer or float)

        Turn turtle left by angle units. (Units are by default degrees,
        but can be set via the degrees() and radians() functions.)
        Angle orientation depends on mode. (See this.)

        Example (for a Turtle instance named turtle):
        >>> turtle.heading()
        22.0
        >>> turtle.left(45)
        >>> turtle.heading()
        67.0
        """

    def lt(self, angle):
        """
        Turn turtle left by angle units.

        Aliases: left | lt

        Argument:
        angle -- a number (integer or float)

        Turn turtle left by angle units. (Units are by default degrees,
        but can be set via the degrees() and radians() functions.)
        Angle orientation depends on mode. (See this.)

        Example (for a Turtle instance named turtle):
        >>> turtle.heading()
        22.0
        >>> turtle.left(45)
        >>> turtle.heading()
        67.0
        """

    def onclick(self, fun, btn=1, add=None):
        """
        Bind fun to mouse-click event on this turtle on canvas.

        Arguments:
        fun --  a function with two arguments, to which will be assigned
                the coordinates of the clicked point on the canvas.
        num --  number of the mouse-button defaults to 1 (left mouse button).
        add --  True or False. If True, new binding will be added, otherwise
                it will replace a former binding.

        Example for the anonymous turtle, i. e. the procedural way:

        >>> def turn(x, y):
        ...     left(360)
        ...
        >>> onclick(turn)  # Now clicking into the turtle will turn it.
        >>> onclick(None)  # event-binding will be removed
        """

    def ondrag(self, fun, btn=1, add=None):
        """
        Bind fun to mouse-move event on this turtle on canvas.

        Arguments:
        fun -- a function with two arguments, to which will be assigned
               the coordinates of the clicked point on the canvas.
        num -- number of the mouse-button defaults to 1 (left mouse button).

        Every sequence of mouse-move-events on a turtle is preceded by a
        mouse-click event on that turtle.

        Example (for a Turtle instance named turtle):
        >>> turtle.ondrag(turtle.goto)

        Subsequently clicking and dragging a Turtle will move it
        across the screen thereby producing handdrawings (if pen is
        down).
        """

    def onrelease(self, fun, btn=1, add=None):
        """
        Bind fun to mouse-button-release event on this turtle on canvas.

        Arguments:
        fun -- a function with two arguments, to which will be assigned
                the coordinates of the clicked point on the canvas.
        num --  number of the mouse-button defaults to 1 (left mouse button).

        Example (for a MyTurtle instance named joe):
        >>> class MyTurtle(Turtle):
        ...     def glow(self,x,y):
        ...             self.fillcolor("red")
        ...     def unglow(self,x,y):
        ...             self.fillcolor("")
        ...
        >>> joe = MyTurtle()
        >>> joe.onclick(joe.glow)
        >>> joe.onrelease(joe.unglow)

        Clicking on joe turns fillcolor red, unclicking turns it to
        transparent.
        """

    def pd(self):
        """
        Pull the pen down -- drawing when moving.

        Aliases: pendown | pd | down

        No argument.

        Example (for a Turtle instance named turtle):
        >>> turtle.pendown()
        """

    def pen(self, pen=None, **pendict):
        """
        Return or set the pen's attributes.

        Arguments:
            pen -- a dictionary with some or all of the below listed keys.
            **pendict -- one or more keyword-arguments with the below
                         listed keys as keywords.

        Return or set the pen's attributes in a 'pen-dictionary'
        with the following key/value pairs:
           "shown"      :   True/False
           "pendown"    :   True/False
           "pencolor"   :   color-string or color-tuple
           "fillcolor"  :   color-string or color-tuple
           "pensize"    :   positive number
           "speed"      :   number in range 0..10
           "resizemode" :   "auto" or "user" or "noresize"
           "stretchfactor": (positive number, positive number)
           "shearfactor":   number
           "outline"    :   positive number
           "tilt"       :   number

        This dictionary can be used as argument for a subsequent
        pen()-call to restore the former pen-state. Moreover one
        or more of these attributes can be provided as keyword-arguments.
        This can be used to set several pen attributes in one statement.


        Examples (for a Turtle instance named turtle):
        >>> turtle.pen(fillcolor="black", pencolor="red", pensize=10)
        >>> turtle.pen()
        {'pensize': 10, 'shown': True, 'resizemode': 'auto', 'outline': 1,
        'pencolor': 'red', 'pendown': True, 'fillcolor': 'black',
        'stretchfactor': (1,1), 'speed': 3, 'shearfactor': 0.0}
        >>> penstate=turtle.pen()
        >>> turtle.color("yellow","")
        >>> turtle.penup()
        >>> turtle.pen()
        {'pensize': 10, 'shown': True, 'resizemode': 'auto', 'outline': 1,
        'pencolor': 'yellow', 'pendown': False, 'fillcolor': '',
        'stretchfactor': (1,1), 'speed': 3, 'shearfactor': 0.0}
        >>> p.pen(penstate, fillcolor="green")
        >>> p.pen()
        {'pensize': 10, 'shown': True, 'resizemode': 'auto', 'outline': 1,
        'pencolor': 'red', 'pendown': True, 'fillcolor': 'green',
        'stretchfactor': (1,1), 'speed': 3, 'shearfactor': 0.0}
        """

    def pencolor(self, *args):
        """
         Return or set the pencolor.

        Arguments:
        Four input formats are allowed:
          - pencolor()
            Return the current pencolor as color specification string,
            possibly in hex-number format (see example).
            May be used as input to another color/pencolor/fillcolor call.
          - pencolor(colorstring)
            s is a Tk color specification string, such as "red" or "yellow"
          - pencolor((r, g, b))
            *a tuple* of r, g, and b, which represent, an RGB color,
            and each of r, g, and b are in the range 0..colormode,
            where colormode is either 1.0 or 255
          - pencolor(r, g, b)
            r, g, and b represent an RGB color, and each of r, g, and b
            are in the range 0..colormode

        If turtleshape is a polygon, the outline of that polygon is drawn
        with the newly set pencolor.

        Example (for a Turtle instance named turtle):
        >>> turtle.pencolor('brown')
        >>> tup = (0.2, 0.8, 0.55)
        >>> turtle.pencolor(tup)
        >>> turtle.pencolor()
        '#33cc8c'
        """

    def pendown(self):
        """
        Pull the pen down -- drawing when moving.

        Aliases: pendown | pd | down

        No argument.

        Example (for a Turtle instance named turtle):
        >>> turtle.pendown()
        """

    def pensize(self, width=None):
        """
        Set or return the line thickness.

        Aliases:  pensize | width

        Argument:
        width -- positive number

        Set the line thickness to width or return it. If resizemode is set
        to "auto" and turtleshape is a polygon, that polygon is drawn with
        the same line thickness. If no argument is given, current pensize
        is returned.

        Example (for a Turtle instance named turtle):
        >>> turtle.pensize()
        1
        >>> turtle.pensize(10)   # from here on lines of width 10 are drawn
        """

    def penup(self):
        """
        Pull the pen up -- no drawing when moving.

        Aliases: penup | pu | up

        No argument

        Example (for a Turtle instance named turtle):
        >>> turtle.penup()
        """

    def pos(self):
        """
        Return the turtle's current location (x,y), as a Vec2D-vector.

        Aliases: pos | position

        No arguments.

        Example (for a Turtle instance named turtle):
        >>> turtle.pos()
        (0.00, 240.00)
        """

    def position(self):
        """
        Return the turtle's current location (x,y), as a Vec2D-vector.

        Aliases: pos | position

        No arguments.

        Example (for a Turtle instance named turtle):
        >>> turtle.pos()
        (0.00, 240.00)
        """

    def pu(self):
        """
        Pull the pen up -- no drawing when moving.

        Aliases: penup | pu | up

        No argument

        Example (for a Turtle instance named turtle):
        >>> turtle.penup()
        """

    def radians(self):
        """
         Set the angle measurement units to radians.

        No arguments.

        Example (for a Turtle instance named turtle):
        >>> turtle.heading()
        90
        >>> turtle.radians()
        >>> turtle.heading()
        1.5707963267948966
        """

    def reset(self):
        """
        Delete the turtle's drawings and restore its default values.

        No argument.

        Delete the turtle's drawings from the screen, re-center the turtle
        and set variables to the default values.

        Example (for a Turtle instance named turtle):
        >>> turtle.position()
        (0.00,-22.00)
        >>> turtle.heading()
        100.0
        >>> turtle.reset()
        >>> turtle.position()
        (0.00,0.00)
        >>> turtle.heading()
        0.0
        """

    def resizemode(self, rmode=None):
        """
        Set resizemode to one of the values: "auto", "user", "noresize".

        (Optional) Argument:
        rmode -- one of the strings "auto", "user", "noresize"

        Different resizemodes have the following effects:
          - "auto" adapts the appearance of the turtle
                   corresponding to the value of pensize.
          - "user" adapts the appearance of the turtle according to the
                   values of stretchfactor and outlinewidth (outline),
                   which are set by shapesize()
          - "noresize" no adaption of the turtle's appearance takes place.
        If no argument is given, return current resizemode.
        resizemode("user") is called by a call of shapesize with arguments.


        Examples (for a Turtle instance named turtle):
        >>> turtle.resizemode("noresize")
        >>> turtle.resizemode()
        'noresize'
        """

    def right(self, angle):
        """
        Turn turtle right by angle units.

        Aliases: right | rt

        Argument:
        angle -- a number (integer or float)

        Turn turtle right by angle units. (Units are by default degrees,
        but can be set via the degrees() and radians() functions.)
        Angle orientation depends on mode. (See this.)

        Example (for a Turtle instance named turtle):
        >>> turtle.heading()
        22.0
        >>> turtle.right(45)
        >>> turtle.heading()
        337.0
        """

    def rt(self, angle):
        """
        Turn turtle right by angle units.

        Aliases: right | rt

        Argument:
        angle -- a number (integer or float)

        Turn turtle right by angle units. (Units are by default degrees,
        but can be set via the degrees() and radians() functions.)
        Angle orientation depends on mode. (See this.)

        Example (for a Turtle instance named turtle):
        >>> turtle.heading()
        22.0
        >>> turtle.right(45)
        >>> turtle.heading()
        337.0
        """

    def seth(self, to_angle):
        """
        Set the orientation of the turtle to to_angle.

        Aliases:  setheading | seth

        Argument:
        to_angle -- a number (integer or float)

        Set the orientation of the turtle to to_angle.
        Here are some common directions in degrees:

         standard - mode:          logo-mode:
        -------------------|--------------------
           0 - east                0 - north
          90 - north              90 - east
         180 - west              180 - south
         270 - south             270 - west

        Example (for a Turtle instance named turtle):
        >>> turtle.setheading(90)
        >>> turtle.heading()
        90
        """

    def setheading(self, to_angle):
        """
        Set the orientation of the turtle to to_angle.

        Aliases:  setheading | seth

        Argument:
        to_angle -- a number (integer or float)

        Set the orientation of the turtle to to_angle.
        Here are some common directions in degrees:

         standard - mode:          logo-mode:
        -------------------|--------------------
           0 - east                0 - north
          90 - north              90 - east
         180 - west              180 - south
         270 - south             270 - west

        Example (for a Turtle instance named turtle):
        >>> turtle.setheading(90)
        >>> turtle.heading()
        90
        """

    def setpos(self, x, y=None):
        """
        Move turtle to an absolute position.

        Aliases: setpos | setposition | goto:

        Arguments:
        x -- a number      or     a pair/vector of numbers
        y -- a number             None

        call: goto(x, y)         # two coordinates
        --or: goto((x, y))       # a pair (tuple) of coordinates
        --or: goto(vec)          # e.g. as returned by pos()

        Move turtle to an absolute position. If the pen is down,
        a line will be drawn. The turtle's orientation does not change.

        Example (for a Turtle instance named turtle):
        >>> tp = turtle.pos()
        >>> tp
        (0.00, 0.00)
        >>> turtle.setpos(60,30)
        >>> turtle.pos()
        (60.00,30.00)
        >>> turtle.setpos((20,80))
        >>> turtle.pos()
        (20.00,80.00)
        >>> turtle.setpos(tp)
        >>> turtle.pos()
        (0.00,0.00)
        """

    def setposition(self, x, y=None):
        """
        Move turtle to an absolute position.

        Aliases: setpos | setposition | goto:

        Arguments:
        x -- a number      or     a pair/vector of numbers
        y -- a number             None

        call: goto(x, y)         # two coordinates
        --or: goto((x, y))       # a pair (tuple) of coordinates
        --or: goto(vec)          # e.g. as returned by pos()

        Move turtle to an absolute position. If the pen is down,
        a line will be drawn. The turtle's orientation does not change.

        Example (for a Turtle instance named turtle):
        >>> tp = turtle.pos()
        >>> tp
        (0.00, 0.00)
        >>> turtle.setpos(60,30)
        >>> turtle.pos()
        (60.00,30.00)
        >>> turtle.setpos((20,80))
        >>> turtle.pos()
        (20.00,80.00)
        >>> turtle.setpos(tp)
        >>> turtle.pos()
        (0.00,0.00)
        """

    def settiltangle(self, angle):
        """
        Rotate the turtleshape to point in the specified direction

        Argument: angle -- number

        Rotate the turtleshape to point in the direction specified by angle,
        regardless of its current tilt-angle. DO NOT change the turtle's
        heading (direction of movement).


        Examples (for a Turtle instance named turtle):
        >>> turtle.shape("circle")
        >>> turtle.shapesize(5,2)
        >>> turtle.settiltangle(45)
        >>> stamp()
        >>> turtle.fd(50)
        >>> turtle.settiltangle(-45)
        >>> stamp()
        >>> turtle.fd(50)
        """

    def setundobuffer(self, size):
        """
        Set or disable undobuffer.

        Argument:
        size -- an integer or None

        If size is an integer an empty undobuffer of given size is installed.
        Size gives the maximum number of turtle-actions that can be undone
        by the undo() function.
        If size is None, no undobuffer is present.

        Example (for a Turtle instance named turtle):
        >>> turtle.setundobuffer(42)
        """

    def setx(self, x):
        """
        Set the turtle's first coordinate to x

        Argument:
        x -- a number (integer or float)

        Set the turtle's first coordinate to x, leave second coordinate
        unchanged.

        Example (for a Turtle instance named turtle):
        >>> turtle.position()
        (0.00, 240.00)
        >>> turtle.setx(10)
        >>> turtle.position()
        (10.00, 240.00)
        """

    def sety(self, y):
        """
        Set the turtle's second coordinate to y

        Argument:
        y -- a number (integer or float)

        Set the turtle's first coordinate to x, second coordinate remains
        unchanged.

        Example (for a Turtle instance named turtle):
        >>> turtle.position()
        (0.00, 40.00)
        >>> turtle.sety(-10)
        >>> turtle.position()
        (0.00, -10.00)
        """

    def shape(self, name=None):
        """
        Set turtle shape to shape with given name / return current shapename.

        Optional argument:
        name -- a string, which is a valid shapename

        Set turtle shape to shape with given name or, if name is not given,
        return name of current shape.
        Shape with name must exist in the TurtleScreen's shape dictionary.
        Initially there are the following polygon shapes:
        'arrow', 'turtle', 'circle', 'square', 'triangle', 'classic'.
        To learn about how to deal with shapes see Screen-method register_shape.

        Example (for a Turtle instance named turtle):
        >>> turtle.shape()
        'arrow'
        >>> turtle.shape("turtle")
        >>> turtle.shape()
        'turtle'
        """

    def shapesize(self, stretch_wid=None, stretch_len=None, outline=None):
        """
        Set/return turtle's stretchfactors/outline. Set resizemode to "user".

        Optional arguments:
           stretch_wid : positive number
           stretch_len : positive number
           outline  : positive number

        Return or set the pen's attributes x/y-stretchfactors and/or outline.
        Set resizemode to "user".
        If and only if resizemode is set to "user", the turtle will be displayed
        stretched according to its stretchfactors:
        stretch_wid is stretchfactor perpendicular to orientation
        stretch_len is stretchfactor in direction of turtles orientation.
        outline determines the width of the shapes's outline.

        Examples (for a Turtle instance named turtle):
        >>> turtle.resizemode("user")
        >>> turtle.shapesize(5, 5, 12)
        >>> turtle.shapesize(outline=8)
        """

    def shapetransform(self, t11=None, t12=None, t21=None, t22=None):
        """
        Set or return the current transformation matrix of the turtle shape.

        Optional arguments: t11, t12, t21, t22 -- numbers.

        If none of the matrix elements are given, return the transformation
        matrix.
        Otherwise set the given elements and transform the turtleshape
        according to the matrix consisting of first row t11, t12 and
        second row t21, 22.
        Modify stretchfactor, shearfactor and tiltangle according to the
        given matrix.

        Examples (for a Turtle instance named turtle):
        >>> turtle.shape("square")
        >>> turtle.shapesize(4,2)
        >>> turtle.shearfactor(-0.5)
        >>> turtle.shapetransform()
        (4.0, -1.0, -0.0, 2.0)
        """

    def shearfactor(self, shear=None):
        """
        Set or return the current shearfactor.

        Optional argument: shear -- number, tangent of the shear angle

        Shear the turtleshape according to the given shearfactor shear,
        which is the tangent of the shear angle. DO NOT change the
        turtle's heading (direction of movement).
        If shear is not given: return the current shearfactor, i. e. the
        tangent of the shear angle, by which lines parallel to the
        heading of the turtle are sheared.

        Examples (for a Turtle instance named turtle):
        >>> turtle.shape("circle")
        >>> turtle.shapesize(5,2)
        >>> turtle.shearfactor(0.5)
        >>> turtle.shearfactor()
        >>> 0.5
        """

    def showturtle(self):
        """
        Makes the turtle visible.

        Aliases: showturtle | st

        No argument.

        Example (for a Turtle instance named turtle):
        >>> turtle.hideturtle()
        >>> turtle.showturtle()
        """

    def speed(self, speed=None):
        """
         Return or set the turtle's speed.

        Optional argument:
        speed -- an integer in the range 0..10 or a speedstring (see below)

        Set the turtle's speed to an integer value in the range 0 .. 10.
        If no argument is given: return current speed.

        If input is a number greater than 10 or smaller than 0.5,
        speed is set to 0.
        Speedstrings  are mapped to speedvalues in the following way:
            'fastest' :  0
            'fast'    :  10
            'normal'  :  6
            'slow'    :  3
            'slowest' :  1
        speeds from 1 to 10 enforce increasingly faster animation of
        line drawing and turtle turning.

        Attention:
        speed = 0 : *no* animation takes place. forward/back makes turtle jump
        and likewise left/right make the turtle turn instantly.

        Example (for a Turtle instance named turtle):
        >>> turtle.speed(3)
        """

    def st(self):
        """
        Makes the turtle visible.

        Aliases: showturtle | st

        No argument.

        Example (for a Turtle instance named turtle):
        >>> turtle.hideturtle()
        >>> turtle.showturtle()
        """

    def stamp(self):
        """
        Stamp a copy of the turtleshape onto the canvas and return its id.

        No argument.

        Stamp a copy of the turtle shape onto the canvas at the current
        turtle position. Return a stamp_id for that stamp, which can be
        used to delete it by calling clearstamp(stamp_id).

        Example (for a Turtle instance named turtle):
        >>> turtle.color("blue")
        >>> turtle.stamp()
        13
        >>> turtle.fd(50)
        """

    def tilt(self, angle):
        """
        Rotate the turtleshape by angle.

        Argument:
        angle - a number

        Rotate the turtleshape by angle from its current tilt-angle,
        but do NOT change the turtle's heading (direction of movement).

        Examples (for a Turtle instance named turtle):
        >>> turtle.shape("circle")
        >>> turtle.shapesize(5,2)
        >>> turtle.tilt(30)
        >>> turtle.fd(50)
        >>> turtle.tilt(30)
        >>> turtle.fd(50)
        """

    def tiltangle(self, angle=None):
        """
        Set or return the current tilt-angle.

        Optional argument: angle -- number

        Rotate the turtleshape to point in the direction specified by angle,
        regardless of its current tilt-angle. DO NOT change the turtle's
        heading (direction of movement).
        If angle is not given: return the current tilt-angle, i. e. the angle
        between the orientation of the turtleshape and the heading of the
        turtle (its direction of movement).

        Deprecated since Python 3.1

        Examples (for a Turtle instance named turtle):
        >>> turtle.shape("circle")
        >>> turtle.shapesize(5,2)
        >>> turtle.tilt(45)
        >>> turtle.tiltangle()
        """

    def towards(self, x, y=None):
        """
        Return the angle of the line from the turtle's position to (x, y).

        Arguments:
        x -- a number   or  a pair/vector of numbers   or   a turtle instance
        y -- a number       None                            None

        call: distance(x, y)         # two coordinates
        --or: distance((x, y))       # a pair (tuple) of coordinates
        --or: distance(vec)          # e.g. as returned by pos()
        --or: distance(mypen)        # where mypen is another turtle

        Return the angle, between the line from turtle-position to position
        specified by x, y and the turtle's start orientation. (Depends on
        modes - "standard" or "logo")

        Example (for a Turtle instance named turtle):
        >>> turtle.pos()
        (10.00, 10.00)
        >>> turtle.towards(0,0)
        225.0
        """

    def turtlesize(self, stretch_wid=None, stretch_len=None, outline=None):
        """
        Set/return turtle's stretchfactors/outline. Set resizemode to "user".

        Optional arguments:
           stretch_wid : positive number
           stretch_len : positive number
           outline  : positive number

        Return or set the pen's attributes x/y-stretchfactors and/or outline.
        Set resizemode to "user".
        If and only if resizemode is set to "user", the turtle will be displayed
        stretched according to its stretchfactors:
        stretch_wid is stretchfactor perpendicular to orientation
        stretch_len is stretchfactor in direction of turtles orientation.
        outline determines the width of the shapes's outline.

        Examples (for a Turtle instance named turtle):
        >>> turtle.resizemode("user")
        >>> turtle.shapesize(5, 5, 12)
        >>> turtle.shapesize(outline=8)
        """

    def undo(self):
        """
        undo (repeatedly) the last turtle action.

        No argument.

        undo (repeatedly) the last turtle action.
        Number of available undo actions is determined by the size of
        the undobuffer.

        Example (for a Turtle instance named turtle):
        >>> for i in range(4):
        ...     turtle.fd(50); turtle.lt(80)
        ...
        >>> for i in range(8):
        ...     turtle.undo()
        ...
        """

    def undobufferentries(self):
        """
        Return count of entries in the undobuffer.

        No argument.

        Example (for a Turtle instance named turtle):
        >>> while undobufferentries():
        ...     undo()
        """

    def up(self):
        """
        Pull the pen up -- no drawing when moving.

        Aliases: penup | pu | up

        No argument

        Example (for a Turtle instance named turtle):
        >>> turtle.penup()
        """

    def width(self, width=None):
        """
        Set or return the line thickness.

        Aliases:  pensize | width

        Argument:
        width -- positive number

        Set the line thickness to width or return it. If resizemode is set
        to "auto" and turtleshape is a polygon, that polygon is drawn with
        the same line thickness. If no argument is given, current pensize
        is returned.

        Example (for a Turtle instance named turtle):
        >>> turtle.pensize()
        1
        >>> turtle.pensize(10)   # from here on lines of width 10 are drawn
        """

    def write(self, arg, move=False, align='left', font=('Arial', 8, 'normal')):
        """
        Write text at the current turtle position.

        Arguments:
        arg -- info, which is to be written to the TurtleScreen
        move (optional) -- True/False
        align (optional) -- one of the strings "left", "center" or right"
        font (optional) -- a triple (fontname, fontsize, fonttype)

        Write text - the string representation of arg - at the current
        turtle position according to align ("left", "center" or right")
        and with the given font.
        If move is True, the pen is moved to the bottom-right corner
        of the text. By default, move is False.

        Example (for a Turtle instance named turtle):
        >>> turtle.write('Home = ', True, align="center")
        >>> turtle.write((0,0), True)
        """

    def xcor(self):
        """
         Return the turtle's x coordinate.

        No arguments.

        Example (for a Turtle instance named turtle):
        >>> reset()
        >>> turtle.left(60)
        >>> turtle.forward(100)
        >>> print turtle.xcor()
        50.0
        """

    def ycor(self):
        """
         Return the turtle's y coordinate
        ---
        No arguments.

        Example (for a Turtle instance named turtle):
        >>> reset()
        >>> turtle.left(60)
        >>> turtle.forward(100)
        >>> print turtle.ycor()
        86.6025403784
        """



class Turtle(RawTurtle):
    def __init__(self, shape='classic', undobuffersize=1000, visible=True): ...


    def back(self, distance):
        """
        Move the turtle backward by distance.

        Aliases: back | backward | bk

        Argument:
        distance -- a number

        Move the turtle backward by distance ,opposite to the direction the
        turtle is headed. Do not change the turtle's heading.

        Example (for a Turtle instance named turtle):
        >>> turtle.position()
        (0.00, 0.00)
        >>> turtle.backward(30)
        >>> turtle.position()
        (-30.00, 0.00)
        """

    def backward(self, distance):
        """
        Move the turtle backward by distance.

        Aliases: back | backward | bk

        Argument:
        distance -- a number

        Move the turtle backward by distance ,opposite to the direction the
        turtle is headed. Do not change the turtle's heading.

        Example (for a Turtle instance named turtle):
        >>> turtle.position()
        (0.00, 0.00)
        >>> turtle.backward(30)
        >>> turtle.position()
        (-30.00, 0.00)
        """

    def begin_fill(self):
        """
        Called just before drawing a shape to be filled.

        No argument.

        Example (for a Turtle instance named turtle):
        >>> turtle.color("black", "red")
        >>> turtle.begin_fill()
        >>> turtle.circle(60)
        >>> turtle.end_fill()
        """

    def begin_poly(self):
        """
        Start recording the vertices of a polygon.

        No argument.

        Start recording the vertices of a polygon. Current turtle position
        is first point of polygon.

        Example (for a Turtle instance named turtle):
        >>> turtle.begin_poly()
        """

    def bk(self, distance):
        """
        Move the turtle backward by distance.

        Aliases: back | backward | bk

        Argument:
        distance -- a number

        Move the turtle backward by distance ,opposite to the direction the
        turtle is headed. Do not change the turtle's heading.

        Example (for a Turtle instance named turtle):
        >>> turtle.position()
        (0.00, 0.00)
        >>> turtle.backward(30)
        >>> turtle.position()
        (-30.00, 0.00)
        """

    def circle(self, radius, extent=None, steps=None):
        """
         Draw a circle with given radius.

        Arguments:
        radius -- a number
        extent (optional) -- a number
        steps (optional) -- an integer

        Draw a circle with given radius. The center is radius units left
        of the turtle; extent - an angle - determines which part of the
        circle is drawn. If extent is not given, draw the entire circle.
        If extent is not a full circle, one endpoint of the arc is the
        current pen position. Draw the arc in counterclockwise direction
        if radius is positive, otherwise in clockwise direction. Finally
        the direction of the turtle is changed by the amount of extent.

        As the circle is approximated by an inscribed regular polygon,
        steps determines the number of steps to use. If not given,
        it will be calculated automatically. Maybe used to draw regular
        polygons.

        call: circle(radius)                  # full circle
        --or: circle(radius, extent)          # arc
        --or: circle(radius, extent, steps)
        --or: circle(radius, steps=6)         # 6-sided polygon

        Example (for a Turtle instance named turtle):
        >>> turtle.circle(50)
        >>> turtle.circle(120, 180)  # semicircle
        """

    def clear(self):
        """
        Delete the turtle's drawings from the screen. Do not move turtle.

        No arguments.

        Delete the turtle's drawings from the screen. Do not move turtle.
        State and position of the turtle as well as drawings of other
        turtles are not affected.

        Examples (for a Turtle instance named turtle):
        >>> turtle.clear()
        """

    def clearstamp(self, stampid):
        """
        Delete stamp with given stampid

        Argument:
        stampid - an integer, must be return value of previous stamp() call.

        Example (for a Turtle instance named turtle):
        >>> turtle.color("blue")
        >>> astamp = turtle.stamp()
        >>> turtle.fd(50)
        >>> turtle.clearstamp(astamp)
        """

    def clearstamps(self, n=None):
        """
        Delete all or first/last n of turtle's stamps.

        Optional argument:
        n -- an integer

        If n is None, delete all of pen's stamps,
        else if n > 0 delete first n stamps
        else if n < 0 delete last n stamps.

        Example (for a Turtle instance named turtle):
        >>> for i in range(8):
        ...     turtle.stamp(); turtle.fd(30)
        ...
        >>> turtle.clearstamps(2)
        >>> turtle.clearstamps(-2)
        >>> turtle.clearstamps()
        """

    def clone(self):
        """
        Create and return a clone of the turtle.

        No argument.

        Create and return a clone of the turtle with same position, heading
        and turtle properties.

        Example (for a Turtle instance named mick):
        mick = Turtle()
        joe = mick.clone()
        """

    def color(self, *args):
        """
        Return or set the pencolor and fillcolor.

        Arguments:
        Several input formats are allowed.
        They use 0, 1, 2, or 3 arguments as follows:

        color()
            Return the current pencolor and the current fillcolor
            as a pair of color specification strings as are returned
            by pencolor and fillcolor.
        color(colorstring), color((r,g,b)), color(r,g,b)
            inputs as in pencolor, set both, fillcolor and pencolor,
            to the given value.
        color(colorstring1, colorstring2),
        color((r1,g1,b1), (r2,g2,b2))
            equivalent to pencolor(colorstring1) and fillcolor(colorstring2)
            and analogously, if the other input format is used.

        If turtleshape is a polygon, outline and interior of that polygon
        is drawn with the newly set colors.
        For mor info see: pencolor, fillcolor

        Example (for a Turtle instance named turtle):
        >>> turtle.color('red', 'green')
        >>> turtle.color()
        ('red', 'green')
        >>> colormode(255)
        >>> color((40, 80, 120), (160, 200, 240))
        >>> color()
        ('#285078', '#a0c8f0')
        """

    def degrees(self, fullcircle=360.0):
        """
         Set angle measurement units to degrees.

        Optional argument:
        fullcircle -  a number

        Set angle measurement units, i. e. set number
        of 'degrees' for a full circle. Dafault value is
        360 degrees.

        Example (for a Turtle instance named turtle):
        >>> turtle.left(90)
        >>> turtle.heading()
        90

        Change angle measurement unit to grad (also known as gon,
        grade, or gradian and equals 1/100-th of the right angle.)
        >>> turtle.degrees(400.0)
        >>> turtle.heading()
        100

        """

    def distance(self, x, y=None):
        """
        Return the distance from the turtle to (x,y) in turtle step units.

        Arguments:
        x -- a number   or  a pair/vector of numbers   or   a turtle instance
        y -- a number       None                            None

        call: distance(x, y)         # two coordinates
        --or: distance((x, y))       # a pair (tuple) of coordinates
        --or: distance(vec)          # e.g. as returned by pos()
        --or: distance(mypen)        # where mypen is another turtle

        Example (for a Turtle instance named turtle):
        >>> turtle.pos()
        (0.00, 0.00)
        >>> turtle.distance(30,40)
        50.0
        >>> pen = Turtle()
        >>> pen.forward(77)
        >>> turtle.distance(pen)
        77.0
        """

    def dot(self, size=None, *color):
        """
        Draw a dot with diameter size, using color.

        Optional arguments:
        size -- an integer >= 1 (if given)
        color -- a colorstring or a numeric color tuple

        Draw a circular dot with diameter size, using color.
        If size is not given, the maximum of pensize+4 and 2*pensize is used.

        Example (for a Turtle instance named turtle):
        >>> turtle.dot()
        >>> turtle.fd(50); turtle.dot(20, "blue"); turtle.fd(50)
        """

    def down(self):
        """
        Pull the pen down -- drawing when moving.

        Aliases: pendown | pd | down

        No argument.

        Example (for a Turtle instance named turtle):
        >>> turtle.pendown()
        """

    def end_fill(self):
        """
        Fill the shape drawn after the call begin_fill().

        No argument.

        Example (for a Turtle instance named turtle):
        >>> turtle.color("black", "red")
        >>> turtle.begin_fill()
        >>> turtle.circle(60)
        >>> turtle.end_fill()
        """

    def end_poly(self):
        """
        Stop recording the vertices of a polygon.

        No argument.

        Stop recording the vertices of a polygon. Current turtle position is
        last point of polygon. This will be connected with the first point.

        Example (for a Turtle instance named turtle):
        >>> turtle.end_poly()
        """

    def fd(self, distance):
        """
        Move the turtle forward by the specified distance.

        Aliases: forward | fd

        Argument:
        distance -- a number (integer or float)

        Move the turtle forward by the specified distance, in the direction
        the turtle is headed.

        Example (for a Turtle instance named turtle):
        >>> turtle.position()
        (0.00, 0.00)
        >>> turtle.forward(25)
        >>> turtle.position()
        (25.00,0.00)
        >>> turtle.forward(-75)
        >>> turtle.position()
        (-50.00,0.00)
        """

    def fillcolor(self, *args):
        """
         Return or set the fillcolor.

        Arguments:
        Four input formats are allowed:
          - fillcolor()
            Return the current fillcolor as color specification string,
            possibly in hex-number format (see example).
            May be used as input to another color/pencolor/fillcolor call.
          - fillcolor(colorstring)
            s is a Tk color specification string, such as "red" or "yellow"
          - fillcolor((r, g, b))
            *a tuple* of r, g, and b, which represent, an RGB color,
            and each of r, g, and b are in the range 0..colormode,
            where colormode is either 1.0 or 255
          - fillcolor(r, g, b)
            r, g, and b represent an RGB color, and each of r, g, and b
            are in the range 0..colormode

        If turtleshape is a polygon, the interior of that polygon is drawn
        with the newly set fillcolor.

        Example (for a Turtle instance named turtle):
        >>> turtle.fillcolor('violet')
        >>> col = turtle.pencolor()
        >>> turtle.fillcolor(col)
        >>> turtle.fillcolor(0, .5, 0)
        """

    def filling(self):
        """
        Return fillstate (True if filling, False else).

        No argument.

        Example (for a Turtle instance named turtle):
        >>> turtle.begin_fill()
        >>> if turtle.filling():
        ...     turtle.pensize(5)
        ... else:
        ...     turtle.pensize(3)
        """

    def forward(self, distance):
        """
        Move the turtle forward by the specified distance.

        Aliases: forward | fd

        Argument:
        distance -- a number (integer or float)

        Move the turtle forward by the specified distance, in the direction
        the turtle is headed.

        Example (for a Turtle instance named turtle):
        >>> turtle.position()
        (0.00, 0.00)
        >>> turtle.forward(25)
        >>> turtle.position()
        (25.00,0.00)
        >>> turtle.forward(-75)
        >>> turtle.position()
        (-50.00,0.00)
        """

    def get_poly(self):
        """
        Return the lastly recorded polygon.

        No argument.

        Example (for a Turtle instance named turtle):
        >>> p = turtle.get_poly()
        >>> turtle.register_shape("myFavouriteShape", p)
        """

    def get_shapepoly(self):
        """
        Return the current shape polygon as tuple of coordinate pairs.

        No argument.

        Examples (for a Turtle instance named turtle):
        >>> turtle.shape("square")
        >>> turtle.shapetransform(4, -1, 0, 2)
        >>> turtle.get_shapepoly()
        ((50, -20), (30, 20), (-50, 20), (-30, -20))

        """

    def getpen(self):
        """
        Return the Turtleobject itself.

        No argument.

        Only reasonable use: as a function to return the 'anonymous turtle':

        Example:
        >>> pet = getturtle()
        >>> pet.fd(50)
        >>> pet
        <turtle.Turtle object at 0x0187D810>
        >>> turtles()
        [<turtle.Turtle object at 0x0187D810>]
        """

    def getscreen(self):
        """
        Return the TurtleScreen object, the turtle is drawing  on.

        No argument.

        Return the TurtleScreen object, the turtle is drawing  on.
        So TurtleScreen-methods can be called for that object.

        Example (for a Turtle instance named turtle):
        >>> ts = turtle.getscreen()
        >>> ts
        <turtle.TurtleScreen object at 0x0106B770>
        >>> ts.bgcolor("pink")
        """

    def getturtle(self):
        """
        Return the Turtleobject itself.

        No argument.

        Only reasonable use: as a function to return the 'anonymous turtle':

        Example:
        >>> pet = getturtle()
        >>> pet.fd(50)
        >>> pet
        <turtle.Turtle object at 0x0187D810>
        >>> turtles()
        [<turtle.Turtle object at 0x0187D810>]
        """

    def goto(self, x, y=None):
        """
        Move turtle to an absolute position.

        Aliases: setpos | setposition | goto:

        Arguments:
        x -- a number      or     a pair/vector of numbers
        y -- a number             None

        call: goto(x, y)         # two coordinates
        --or: goto((x, y))       # a pair (tuple) of coordinates
        --or: goto(vec)          # e.g. as returned by pos()

        Move turtle to an absolute position. If the pen is down,
        a line will be drawn. The turtle's orientation does not change.

        Example (for a Turtle instance named turtle):
        >>> tp = turtle.pos()
        >>> tp
        (0.00, 0.00)
        >>> turtle.setpos(60,30)
        >>> turtle.pos()
        (60.00,30.00)
        >>> turtle.setpos((20,80))
        >>> turtle.pos()
        (20.00,80.00)
        >>> turtle.setpos(tp)
        >>> turtle.pos()
        (0.00,0.00)
        """

    def heading(self):
        """
         Return the turtle's current heading.

        No arguments.

        Example (for a Turtle instance named turtle):
        >>> turtle.left(67)
        >>> turtle.heading()
        67.0
        """

    def hideturtle(self):
        """
        Makes the turtle invisible.

        Aliases: hideturtle | ht

        No argument.

        It's a good idea to do this while you're in the
        middle of a complicated drawing, because hiding
        the turtle speeds up the drawing observably.

        Example (for a Turtle instance named turtle):
        >>> turtle.hideturtle()
        """

    def home(self):
        """
        Move turtle to the origin - coordinates (0,0).

        No arguments.

        Move turtle to the origin - coordinates (0,0) and set its
        heading to its start-orientation (which depends on mode).

        Example (for a Turtle instance named turtle):
        >>> turtle.home()
        """

    def ht(self):
        """
        Makes the turtle invisible.

        Aliases: hideturtle | ht

        No argument.

        It's a good idea to do this while you're in the
        middle of a complicated drawing, because hiding
        the turtle speeds up the drawing observably.

        Example (for a Turtle instance named turtle):
        >>> turtle.hideturtle()
        """

    def isdown(self):
        """
        Return True if pen is down, False if it's up.

        No argument.

        Example (for a Turtle instance named turtle):
        >>> turtle.penup()
        >>> turtle.isdown()
        False
        >>> turtle.pendown()
        >>> turtle.isdown()
        True
        """

    def isvisible(self):
        """
        Return True if the Turtle is shown, False if it's hidden.

        No argument.

        Example (for a Turtle instance named turtle):
        >>> turtle.hideturtle()
        >>> print turtle.isvisible():
        False
        """

    def left(self, angle):
        """
        Turn turtle left by angle units.

        Aliases: left | lt

        Argument:
        angle -- a number (integer or float)

        Turn turtle left by angle units. (Units are by default degrees,
        but can be set via the degrees() and radians() functions.)
        Angle orientation depends on mode. (See this.)

        Example (for a Turtle instance named turtle):
        >>> turtle.heading()
        22.0
        >>> turtle.left(45)
        >>> turtle.heading()
        67.0
        """

    def lt(self, angle):
        """
        Turn turtle left by angle units.

        Aliases: left | lt

        Argument:
        angle -- a number (integer or float)

        Turn turtle left by angle units. (Units are by default degrees,
        but can be set via the degrees() and radians() functions.)
        Angle orientation depends on mode. (See this.)

        Example (for a Turtle instance named turtle):
        >>> turtle.heading()
        22.0
        >>> turtle.left(45)
        >>> turtle.heading()
        67.0
        """

    def onclick(self, fun, btn=1, add=None):
        """
        Bind fun to mouse-click event on this turtle on canvas.

        Arguments:
        fun --  a function with two arguments, to which will be assigned
                the coordinates of the clicked point on the canvas.
        num --  number of the mouse-button defaults to 1 (left mouse button).
        add --  True or False. If True, new binding will be added, otherwise
                it will replace a former binding.

        Example for the anonymous turtle, i. e. the procedural way:

        >>> def turn(x, y):
        ...     left(360)
        ...
        >>> onclick(turn)  # Now clicking into the turtle will turn it.
        >>> onclick(None)  # event-binding will be removed
        """

    def ondrag(self, fun, btn=1, add=None):
        """
        Bind fun to mouse-move event on this turtle on canvas.

        Arguments:
        fun -- a function with two arguments, to which will be assigned
               the coordinates of the clicked point on the canvas.
        num -- number of the mouse-button defaults to 1 (left mouse button).

        Every sequence of mouse-move-events on a turtle is preceded by a
        mouse-click event on that turtle.

        Example (for a Turtle instance named turtle):
        >>> turtle.ondrag(turtle.goto)

        Subsequently clicking and dragging a Turtle will move it
        across the screen thereby producing handdrawings (if pen is
        down).
        """

    def onrelease(self, fun, btn=1, add=None):
        """
        Bind fun to mouse-button-release event on this turtle on canvas.

        Arguments:
        fun -- a function with two arguments, to which will be assigned
                the coordinates of the clicked point on the canvas.
        num --  number of the mouse-button defaults to 1 (left mouse button).

        Example (for a MyTurtle instance named joe):
        >>> class MyTurtle(Turtle):
        ...     def glow(self,x,y):
        ...             self.fillcolor("red")
        ...     def unglow(self,x,y):
        ...             self.fillcolor("")
        ...
        >>> joe = MyTurtle()
        >>> joe.onclick(joe.glow)
        >>> joe.onrelease(joe.unglow)

        Clicking on joe turns fillcolor red, unclicking turns it to
        transparent.
        """

    def pd(self):
        """
        Pull the pen down -- drawing when moving.

        Aliases: pendown | pd | down

        No argument.

        Example (for a Turtle instance named turtle):
        >>> turtle.pendown()
        """

    def pen(self, pen=None, **pendict):
        """
        Return or set the pen's attributes.

        Arguments:
            pen -- a dictionary with some or all of the below listed keys.
            **pendict -- one or more keyword-arguments with the below
                         listed keys as keywords.

        Return or set the pen's attributes in a 'pen-dictionary'
        with the following key/value pairs:
           "shown"      :   True/False
           "pendown"    :   True/False
           "pencolor"   :   color-string or color-tuple
           "fillcolor"  :   color-string or color-tuple
           "pensize"    :   positive number
           "speed"      :   number in range 0..10
           "resizemode" :   "auto" or "user" or "noresize"
           "stretchfactor": (positive number, positive number)
           "shearfactor":   number
           "outline"    :   positive number
           "tilt"       :   number

        This dictionary can be used as argument for a subsequent
        pen()-call to restore the former pen-state. Moreover one
        or more of these attributes can be provided as keyword-arguments.
        This can be used to set several pen attributes in one statement.


        Examples (for a Turtle instance named turtle):
        >>> turtle.pen(fillcolor="black", pencolor="red", pensize=10)
        >>> turtle.pen()
        {'pensize': 10, 'shown': True, 'resizemode': 'auto', 'outline': 1,
        'pencolor': 'red', 'pendown': True, 'fillcolor': 'black',
        'stretchfactor': (1,1), 'speed': 3, 'shearfactor': 0.0}
        >>> penstate=turtle.pen()
        >>> turtle.color("yellow","")
        >>> turtle.penup()
        >>> turtle.pen()
        {'pensize': 10, 'shown': True, 'resizemode': 'auto', 'outline': 1,
        'pencolor': 'yellow', 'pendown': False, 'fillcolor': '',
        'stretchfactor': (1,1), 'speed': 3, 'shearfactor': 0.0}
        >>> p.pen(penstate, fillcolor="green")
        >>> p.pen()
        {'pensize': 10, 'shown': True, 'resizemode': 'auto', 'outline': 1,
        'pencolor': 'red', 'pendown': True, 'fillcolor': 'green',
        'stretchfactor': (1,1), 'speed': 3, 'shearfactor': 0.0}
        """

    def pencolor(self, *args):
        """
         Return or set the pencolor.

        Arguments:
        Four input formats are allowed:
          - pencolor()
            Return the current pencolor as color specification string,
            possibly in hex-number format (see example).
            May be used as input to another color/pencolor/fillcolor call.
          - pencolor(colorstring)
            s is a Tk color specification string, such as "red" or "yellow"
          - pencolor((r, g, b))
            *a tuple* of r, g, and b, which represent, an RGB color,
            and each of r, g, and b are in the range 0..colormode,
            where colormode is either 1.0 or 255
          - pencolor(r, g, b)
            r, g, and b represent an RGB color, and each of r, g, and b
            are in the range 0..colormode

        If turtleshape is a polygon, the outline of that polygon is drawn
        with the newly set pencolor.

        Example (for a Turtle instance named turtle):
        >>> turtle.pencolor('brown')
        >>> tup = (0.2, 0.8, 0.55)
        >>> turtle.pencolor(tup)
        >>> turtle.pencolor()
        '#33cc8c'
        """

    def pendown(self):
        """
        Pull the pen down -- drawing when moving.

        Aliases: pendown | pd | down

        No argument.

        Example (for a Turtle instance named turtle):
        >>> turtle.pendown()
        """

    def pensize(self, width=None):
        """
        Set or return the line thickness.

        Aliases:  pensize | width

        Argument:
        width -- positive number

        Set the line thickness to width or return it. If resizemode is set
        to "auto" and turtleshape is a polygon, that polygon is drawn with
        the same line thickness. If no argument is given, current pensize
        is returned.

        Example (for a Turtle instance named turtle):
        >>> turtle.pensize()
        1
        >>> turtle.pensize(10)   # from here on lines of width 10 are drawn
        """

    def penup(self):
        """
        Pull the pen up -- no drawing when moving.

        Aliases: penup | pu | up

        No argument

        Example (for a Turtle instance named turtle):
        >>> turtle.penup()
        """

    def pos(self):
        """
        Return the turtle's current location (x,y), as a Vec2D-vector.

        Aliases: pos | position

        No arguments.

        Example (for a Turtle instance named turtle):
        >>> turtle.pos()
        (0.00, 240.00)
        """

    def position(self):
        """
        Return the turtle's current location (x,y), as a Vec2D-vector.

        Aliases: pos | position

        No arguments.

        Example (for a Turtle instance named turtle):
        >>> turtle.pos()
        (0.00, 240.00)
        """

    def pu(self):
        """
        Pull the pen up -- no drawing when moving.

        Aliases: penup | pu | up

        No argument

        Example (for a Turtle instance named turtle):
        >>> turtle.penup()
        """

    def radians(self):
        """
         Set the angle measurement units to radians.

        No arguments.

        Example (for a Turtle instance named turtle):
        >>> turtle.heading()
        90
        >>> turtle.radians()
        >>> turtle.heading()
        1.5707963267948966
        """

    def reset(self):
        """
        Delete the turtle's drawings and restore its default values.

        No argument.

        Delete the turtle's drawings from the screen, re-center the turtle
        and set variables to the default values.

        Example (for a Turtle instance named turtle):
        >>> turtle.position()
        (0.00,-22.00)
        >>> turtle.heading()
        100.0
        >>> turtle.reset()
        >>> turtle.position()
        (0.00,0.00)
        >>> turtle.heading()
        0.0
        """

    def resizemode(self, rmode=None):
        """
        Set resizemode to one of the values: "auto", "user", "noresize".

        (Optional) Argument:
        rmode -- one of the strings "auto", "user", "noresize"

        Different resizemodes have the following effects:
          - "auto" adapts the appearance of the turtle
                   corresponding to the value of pensize.
          - "user" adapts the appearance of the turtle according to the
                   values of stretchfactor and outlinewidth (outline),
                   which are set by shapesize()
          - "noresize" no adaption of the turtle's appearance takes place.
        If no argument is given, return current resizemode.
        resizemode("user") is called by a call of shapesize with arguments.


        Examples (for a Turtle instance named turtle):
        >>> turtle.resizemode("noresize")
        >>> turtle.resizemode()
        'noresize'
        """

    def right(self, angle):
        """
        Turn turtle right by angle units.

        Aliases: right | rt

        Argument:
        angle -- a number (integer or float)

        Turn turtle right by angle units. (Units are by default degrees,
        but can be set via the degrees() and radians() functions.)
        Angle orientation depends on mode. (See this.)

        Example (for a Turtle instance named turtle):
        >>> turtle.heading()
        22.0
        >>> turtle.right(45)
        >>> turtle.heading()
        337.0
        """

    def rt(self, angle):
        """
        Turn turtle right by angle units.

        Aliases: right | rt

        Argument:
        angle -- a number (integer or float)

        Turn turtle right by angle units. (Units are by default degrees,
        but can be set via the degrees() and radians() functions.)
        Angle orientation depends on mode. (See this.)

        Example (for a Turtle instance named turtle):
        >>> turtle.heading()
        22.0
        >>> turtle.right(45)
        >>> turtle.heading()
        337.0
        """

    def seth(self, to_angle):
        """
        Set the orientation of the turtle to to_angle.

        Aliases:  setheading | seth

        Argument:
        to_angle -- a number (integer or float)

        Set the orientation of the turtle to to_angle.
        Here are some common directions in degrees:

         standard - mode:          logo-mode:
        -------------------|--------------------
           0 - east                0 - north
          90 - north              90 - east
         180 - west              180 - south
         270 - south             270 - west

        Example (for a Turtle instance named turtle):
        >>> turtle.setheading(90)
        >>> turtle.heading()
        90
        """

    def setheading(self, to_angle):
        """
        Set the orientation of the turtle to to_angle.

        Aliases:  setheading | seth

        Argument:
        to_angle -- a number (integer or float)

        Set the orientation of the turtle to to_angle.
        Here are some common directions in degrees:

         standard - mode:          logo-mode:
        -------------------|--------------------
           0 - east                0 - north
          90 - north              90 - east
         180 - west              180 - south
         270 - south             270 - west

        Example (for a Turtle instance named turtle):
        >>> turtle.setheading(90)
        >>> turtle.heading()
        90
        """

    def setpos(self, x, y=None):
        """
        Move turtle to an absolute position.

        Aliases: setpos | setposition | goto:

        Arguments:
        x -- a number      or     a pair/vector of numbers
        y -- a number             None

        call: goto(x, y)         # two coordinates
        --or: goto((x, y))       # a pair (tuple) of coordinates
        --or: goto(vec)          # e.g. as returned by pos()

        Move turtle to an absolute position. If the pen is down,
        a line will be drawn. The turtle's orientation does not change.

        Example (for a Turtle instance named turtle):
        >>> tp = turtle.pos()
        >>> tp
        (0.00, 0.00)
        >>> turtle.setpos(60,30)
        >>> turtle.pos()
        (60.00,30.00)
        >>> turtle.setpos((20,80))
        >>> turtle.pos()
        (20.00,80.00)
        >>> turtle.setpos(tp)
        >>> turtle.pos()
        (0.00,0.00)
        """

    def setposition(self, x, y=None):
        """
        Move turtle to an absolute position.

        Aliases: setpos | setposition | goto:

        Arguments:
        x -- a number      or     a pair/vector of numbers
        y -- a number             None

        call: goto(x, y)         # two coordinates
        --or: goto((x, y))       # a pair (tuple) of coordinates
        --or: goto(vec)          # e.g. as returned by pos()

        Move turtle to an absolute position. If the pen is down,
        a line will be drawn. The turtle's orientation does not change.

        Example (for a Turtle instance named turtle):
        >>> tp = turtle.pos()
        >>> tp
        (0.00, 0.00)
        >>> turtle.setpos(60,30)
        >>> turtle.pos()
        (60.00,30.00)
        >>> turtle.setpos((20,80))
        >>> turtle.pos()
        (20.00,80.00)
        >>> turtle.setpos(tp)
        >>> turtle.pos()
        (0.00,0.00)
        """

    def settiltangle(self, angle):
        """
        Rotate the turtleshape to point in the specified direction

        Argument: angle -- number

        Rotate the turtleshape to point in the direction specified by angle,
        regardless of its current tilt-angle. DO NOT change the turtle's
        heading (direction of movement).


        Examples (for a Turtle instance named turtle):
        >>> turtle.shape("circle")
        >>> turtle.shapesize(5,2)
        >>> turtle.settiltangle(45)
        >>> stamp()
        >>> turtle.fd(50)
        >>> turtle.settiltangle(-45)
        >>> stamp()
        >>> turtle.fd(50)
        """

    def setundobuffer(self, size):
        """
        Set or disable undobuffer.

        Argument:
        size -- an integer or None

        If size is an integer an empty undobuffer of given size is installed.
        Size gives the maximum number of turtle-actions that can be undone
        by the undo() function.
        If size is None, no undobuffer is present.

        Example (for a Turtle instance named turtle):
        >>> turtle.setundobuffer(42)
        """

    def setx(self, x):
        """
        Set the turtle's first coordinate to x

        Argument:
        x -- a number (integer or float)

        Set the turtle's first coordinate to x, leave second coordinate
        unchanged.

        Example (for a Turtle instance named turtle):
        >>> turtle.position()
        (0.00, 240.00)
        >>> turtle.setx(10)
        >>> turtle.position()
        (10.00, 240.00)
        """

    def sety(self, y):
        """
        Set the turtle's second coordinate to y

        Argument:
        y -- a number (integer or float)

        Set the turtle's first coordinate to x, second coordinate remains
        unchanged.

        Example (for a Turtle instance named turtle):
        >>> turtle.position()
        (0.00, 40.00)
        >>> turtle.sety(-10)
        >>> turtle.position()
        (0.00, -10.00)
        """

    def shape(self, name=None):
        """
        Set turtle shape to shape with given name / return current shapename.

        Optional argument:
        name -- a string, which is a valid shapename

        Set turtle shape to shape with given name or, if name is not given,
        return name of current shape.
        Shape with name must exist in the TurtleScreen's shape dictionary.
        Initially there are the following polygon shapes:
        'arrow', 'turtle', 'circle', 'square', 'triangle', 'classic'.
        To learn about how to deal with shapes see Screen-method register_shape.

        Example (for a Turtle instance named turtle):
        >>> turtle.shape()
        'arrow'
        >>> turtle.shape("turtle")
        >>> turtle.shape()
        'turtle'
        """

    def shapesize(self, stretch_wid=None, stretch_len=None, outline=None):
        """
        Set/return turtle's stretchfactors/outline. Set resizemode to "user".

        Optional arguments:
           stretch_wid : positive number
           stretch_len : positive number
           outline  : positive number

        Return or set the pen's attributes x/y-stretchfactors and/or outline.
        Set resizemode to "user".
        If and only if resizemode is set to "user", the turtle will be displayed
        stretched according to its stretchfactors:
        stretch_wid is stretchfactor perpendicular to orientation
        stretch_len is stretchfactor in direction of turtles orientation.
        outline determines the width of the shapes's outline.

        Examples (for a Turtle instance named turtle):
        >>> turtle.resizemode("user")
        >>> turtle.shapesize(5, 5, 12)
        >>> turtle.shapesize(outline=8)
        """

    def shapetransform(self, t11=None, t12=None, t21=None, t22=None):
        """
        Set or return the current transformation matrix of the turtle shape.

        Optional arguments: t11, t12, t21, t22 -- numbers.

        If none of the matrix elements are given, return the transformation
        matrix.
        Otherwise set the given elements and transform the turtleshape
        according to the matrix consisting of first row t11, t12 and
        second row t21, 22.
        Modify stretchfactor, shearfactor and tiltangle according to the
        given matrix.

        Examples (for a Turtle instance named turtle):
        >>> turtle.shape("square")
        >>> turtle.shapesize(4,2)
        >>> turtle.shearfactor(-0.5)
        >>> turtle.shapetransform()
        (4.0, -1.0, -0.0, 2.0)
        """

    def shearfactor(self, shear=None):
        """
        Set or return the current shearfactor.

        Optional argument: shear -- number, tangent of the shear angle

        Shear the turtleshape according to the given shearfactor shear,
        which is the tangent of the shear angle. DO NOT change the
        turtle's heading (direction of movement).
        If shear is not given: return the current shearfactor, i. e. the
        tangent of the shear angle, by which lines parallel to the
        heading of the turtle are sheared.

        Examples (for a Turtle instance named turtle):
        >>> turtle.shape("circle")
        >>> turtle.shapesize(5,2)
        >>> turtle.shearfactor(0.5)
        >>> turtle.shearfactor()
        >>> 0.5
        """

    def showturtle(self):
        """
        Makes the turtle visible.

        Aliases: showturtle | st

        No argument.

        Example (for a Turtle instance named turtle):
        >>> turtle.hideturtle()
        >>> turtle.showturtle()
        """

    def speed(self, speed=None):
        """
         Return or set the turtle's speed.

        Optional argument:
        speed -- an integer in the range 0..10 or a speedstring (see below)

        Set the turtle's speed to an integer value in the range 0 .. 10.
        If no argument is given: return current speed.

        If input is a number greater than 10 or smaller than 0.5,
        speed is set to 0.
        Speedstrings  are mapped to speedvalues in the following way:
            'fastest' :  0
            'fast'    :  10
            'normal'  :  6
            'slow'    :  3
            'slowest' :  1
        speeds from 1 to 10 enforce increasingly faster animation of
        line drawing and turtle turning.

        Attention:
        speed = 0 : *no* animation takes place. forward/back makes turtle jump
        and likewise left/right make the turtle turn instantly.

        Example (for a Turtle instance named turtle):
        >>> turtle.speed(3)
        """

    def st(self):
        """
        Makes the turtle visible.

        Aliases: showturtle | st

        No argument.

        Example (for a Turtle instance named turtle):
        >>> turtle.hideturtle()
        >>> turtle.showturtle()
        """

    def stamp(self):
        """
        Stamp a copy of the turtleshape onto the canvas and return its id.

        No argument.

        Stamp a copy of the turtle shape onto the canvas at the current
        turtle position. Return a stamp_id for that stamp, which can be
        used to delete it by calling clearstamp(stamp_id).

        Example (for a Turtle instance named turtle):
        >>> turtle.color("blue")
        >>> turtle.stamp()
        13
        >>> turtle.fd(50)
        """

    def tilt(self, angle):
        """
        Rotate the turtleshape by angle.

        Argument:
        angle - a number

        Rotate the turtleshape by angle from its current tilt-angle,
        but do NOT change the turtle's heading (direction of movement).

        Examples (for a Turtle instance named turtle):
        >>> turtle.shape("circle")
        >>> turtle.shapesize(5,2)
        >>> turtle.tilt(30)
        >>> turtle.fd(50)
        >>> turtle.tilt(30)
        >>> turtle.fd(50)
        """

    def tiltangle(self, angle=None):
        """
        Set or return the current tilt-angle.

        Optional argument: angle -- number

        Rotate the turtleshape to point in the direction specified by angle,
        regardless of its current tilt-angle. DO NOT change the turtle's
        heading (direction of movement).
        If angle is not given: return the current tilt-angle, i. e. the angle
        between the orientation of the turtleshape and the heading of the
        turtle (its direction of movement).

        Deprecated since Python 3.1

        Examples (for a Turtle instance named turtle):
        >>> turtle.shape("circle")
        >>> turtle.shapesize(5,2)
        >>> turtle.tilt(45)
        >>> turtle.tiltangle()
        """

    def towards(self, x, y=None):
        """
        Return the angle of the line from the turtle's position to (x, y).

        Arguments:
        x -- a number   or  a pair/vector of numbers   or   a turtle instance
        y -- a number       None                            None

        call: distance(x, y)         # two coordinates
        --or: distance((x, y))       # a pair (tuple) of coordinates
        --or: distance(vec)          # e.g. as returned by pos()
        --or: distance(mypen)        # where mypen is another turtle

        Return the angle, between the line from turtle-position to position
        specified by x, y and the turtle's start orientation. (Depends on
        modes - "standard" or "logo")

        Example (for a Turtle instance named turtle):
        >>> turtle.pos()
        (10.00, 10.00)
        >>> turtle.towards(0,0)
        225.0
        """

    def turtlesize(self, stretch_wid=None, stretch_len=None, outline=None):
        """
        Set/return turtle's stretchfactors/outline. Set resizemode to "user".

        Optional arguments:
           stretch_wid : positive number
           stretch_len : positive number
           outline  : positive number

        Return or set the pen's attributes x/y-stretchfactors and/or outline.
        Set resizemode to "user".
        If and only if resizemode is set to "user", the turtle will be displayed
        stretched according to its stretchfactors:
        stretch_wid is stretchfactor perpendicular to orientation
        stretch_len is stretchfactor in direction of turtles orientation.
        outline determines the width of the shapes's outline.

        Examples (for a Turtle instance named turtle):
        >>> turtle.resizemode("user")
        >>> turtle.shapesize(5, 5, 12)
        >>> turtle.shapesize(outline=8)
        """

    def undo(self):
        """
        undo (repeatedly) the last turtle action.

        No argument.

        undo (repeatedly) the last turtle action.
        Number of available undo actions is determined by the size of
        the undobuffer.

        Example (for a Turtle instance named turtle):
        >>> for i in range(4):
        ...     turtle.fd(50); turtle.lt(80)
        ...
        >>> for i in range(8):
        ...     turtle.undo()
        ...
        """

    def undobufferentries(self):
        """
        Return count of entries in the undobuffer.

        No argument.

        Example (for a Turtle instance named turtle):
        >>> while undobufferentries():
        ...     undo()
        """

    def up(self):
        """
        Pull the pen up -- no drawing when moving.

        Aliases: penup | pu | up

        No argument

        Example (for a Turtle instance named turtle):
        >>> turtle.penup()
        """

    def width(self, width=None):
        """
        Set or return the line thickness.

        Aliases:  pensize | width

        Argument:
        width -- positive number

        Set the line thickness to width or return it. If resizemode is set
        to "auto" and turtleshape is a polygon, that polygon is drawn with
        the same line thickness. If no argument is given, current pensize
        is returned.

        Example (for a Turtle instance named turtle):
        >>> turtle.pensize()
        1
        >>> turtle.pensize(10)   # from here on lines of width 10 are drawn
        """

    def write(self, arg, move=False, align='left', font=('Arial', 8, 'normal')):
        """
        Write text at the current turtle position.

        Arguments:
        arg -- info, which is to be written to the TurtleScreen
        move (optional) -- True/False
        align (optional) -- one of the strings "left", "center" or right"
        font (optional) -- a triple (fontname, fontsize, fonttype)

        Write text - the string representation of arg - at the current
        turtle position according to align ("left", "center" or right")
        and with the given font.
        If move is True, the pen is moved to the bottom-right corner
        of the text. By default, move is False.

        Example (for a Turtle instance named turtle):
        >>> turtle.write('Home = ', True, align="center")
        >>> turtle.write((0,0), True)
        """

    def xcor(self):
        """
         Return the turtle's x coordinate.

        No arguments.

        Example (for a Turtle instance named turtle):
        >>> reset()
        >>> turtle.left(60)
        >>> turtle.forward(100)
        >>> print turtle.xcor()
        50.0
        """

    def ycor(self):
        """
         Return the turtle's y coordinate
        ---
        No arguments.

        Example (for a Turtle instance named turtle):
        >>> reset()
        >>> turtle.left(60)
        >>> turtle.forward(100)
        >>> print turtle.ycor()
        86.6025403784
        """



class RawTurtle(TPen, TNavigator):
    def __init__(self, canvas=None, shape='classic', undobuffersize=1000, visible=True): ...


    def back(self, distance):
        """
        Move the turtle backward by distance.

        Aliases: back | backward | bk

        Argument:
        distance -- a number

        Move the turtle backward by distance ,opposite to the direction the
        turtle is headed. Do not change the turtle's heading.

        Example (for a Turtle instance named turtle):
        >>> turtle.position()
        (0.00, 0.00)
        >>> turtle.backward(30)
        >>> turtle.position()
        (-30.00, 0.00)
        """

    def backward(self, distance):
        """
        Move the turtle backward by distance.

        Aliases: back | backward | bk

        Argument:
        distance -- a number

        Move the turtle backward by distance ,opposite to the direction the
        turtle is headed. Do not change the turtle's heading.

        Example (for a Turtle instance named turtle):
        >>> turtle.position()
        (0.00, 0.00)
        >>> turtle.backward(30)
        >>> turtle.position()
        (-30.00, 0.00)
        """

    def begin_fill(self):
        """
        Called just before drawing a shape to be filled.

        No argument.

        Example (for a Turtle instance named turtle):
        >>> turtle.color("black", "red")
        >>> turtle.begin_fill()
        >>> turtle.circle(60)
        >>> turtle.end_fill()
        """

    def begin_poly(self):
        """
        Start recording the vertices of a polygon.

        No argument.

        Start recording the vertices of a polygon. Current turtle position
        is first point of polygon.

        Example (for a Turtle instance named turtle):
        >>> turtle.begin_poly()
        """

    def bk(self, distance):
        """
        Move the turtle backward by distance.

        Aliases: back | backward | bk

        Argument:
        distance -- a number

        Move the turtle backward by distance ,opposite to the direction the
        turtle is headed. Do not change the turtle's heading.

        Example (for a Turtle instance named turtle):
        >>> turtle.position()
        (0.00, 0.00)
        >>> turtle.backward(30)
        >>> turtle.position()
        (-30.00, 0.00)
        """

    def circle(self, radius, extent=None, steps=None):
        """
         Draw a circle with given radius.

        Arguments:
        radius -- a number
        extent (optional) -- a number
        steps (optional) -- an integer

        Draw a circle with given radius. The center is radius units left
        of the turtle; extent - an angle - determines which part of the
        circle is drawn. If extent is not given, draw the entire circle.
        If extent is not a full circle, one endpoint of the arc is the
        current pen position. Draw the arc in counterclockwise direction
        if radius is positive, otherwise in clockwise direction. Finally
        the direction of the turtle is changed by the amount of extent.

        As the circle is approximated by an inscribed regular polygon,
        steps determines the number of steps to use. If not given,
        it will be calculated automatically. Maybe used to draw regular
        polygons.

        call: circle(radius)                  # full circle
        --or: circle(radius, extent)          # arc
        --or: circle(radius, extent, steps)
        --or: circle(radius, steps=6)         # 6-sided polygon

        Example (for a Turtle instance named turtle):
        >>> turtle.circle(50)
        >>> turtle.circle(120, 180)  # semicircle
        """

    def clear(self):
        """
        Delete the turtle's drawings from the screen. Do not move turtle.

        No arguments.

        Delete the turtle's drawings from the screen. Do not move turtle.
        State and position of the turtle as well as drawings of other
        turtles are not affected.

        Examples (for a Turtle instance named turtle):
        >>> turtle.clear()
        """

    def clearstamp(self, stampid):
        """
        Delete stamp with given stampid

        Argument:
        stampid - an integer, must be return value of previous stamp() call.

        Example (for a Turtle instance named turtle):
        >>> turtle.color("blue")
        >>> astamp = turtle.stamp()
        >>> turtle.fd(50)
        >>> turtle.clearstamp(astamp)
        """

    def clearstamps(self, n=None):
        """
        Delete all or first/last n of turtle's stamps.

        Optional argument:
        n -- an integer

        If n is None, delete all of pen's stamps,
        else if n > 0 delete first n stamps
        else if n < 0 delete last n stamps.

        Example (for a Turtle instance named turtle):
        >>> for i in range(8):
        ...     turtle.stamp(); turtle.fd(30)
        ...
        >>> turtle.clearstamps(2)
        >>> turtle.clearstamps(-2)
        >>> turtle.clearstamps()
        """

    def clone(self):
        """
        Create and return a clone of the turtle.

        No argument.

        Create and return a clone of the turtle with same position, heading
        and turtle properties.

        Example (for a Turtle instance named mick):
        mick = Turtle()
        joe = mick.clone()
        """

    def color(self, *args):
        """
        Return or set the pencolor and fillcolor.

        Arguments:
        Several input formats are allowed.
        They use 0, 1, 2, or 3 arguments as follows:

        color()
            Return the current pencolor and the current fillcolor
            as a pair of color specification strings as are returned
            by pencolor and fillcolor.
        color(colorstring), color((r,g,b)), color(r,g,b)
            inputs as in pencolor, set both, fillcolor and pencolor,
            to the given value.
        color(colorstring1, colorstring2),
        color((r1,g1,b1), (r2,g2,b2))
            equivalent to pencolor(colorstring1) and fillcolor(colorstring2)
            and analogously, if the other input format is used.

        If turtleshape is a polygon, outline and interior of that polygon
        is drawn with the newly set colors.
        For mor info see: pencolor, fillcolor

        Example (for a Turtle instance named turtle):
        >>> turtle.color('red', 'green')
        >>> turtle.color()
        ('red', 'green')
        >>> colormode(255)
        >>> color((40, 80, 120), (160, 200, 240))
        >>> color()
        ('#285078', '#a0c8f0')
        """

    def degrees(self, fullcircle=360.0):
        """
         Set angle measurement units to degrees.

        Optional argument:
        fullcircle -  a number

        Set angle measurement units, i. e. set number
        of 'degrees' for a full circle. Dafault value is
        360 degrees.

        Example (for a Turtle instance named turtle):
        >>> turtle.left(90)
        >>> turtle.heading()
        90

        Change angle measurement unit to grad (also known as gon,
        grade, or gradian and equals 1/100-th of the right angle.)
        >>> turtle.degrees(400.0)
        >>> turtle.heading()
        100

        """

    def distance(self, x, y=None):
        """
        Return the distance from the turtle to (x,y) in turtle step units.

        Arguments:
        x -- a number   or  a pair/vector of numbers   or   a turtle instance
        y -- a number       None                            None

        call: distance(x, y)         # two coordinates
        --or: distance((x, y))       # a pair (tuple) of coordinates
        --or: distance(vec)          # e.g. as returned by pos()
        --or: distance(mypen)        # where mypen is another turtle

        Example (for a Turtle instance named turtle):
        >>> turtle.pos()
        (0.00, 0.00)
        >>> turtle.distance(30,40)
        50.0
        >>> pen = Turtle()
        >>> pen.forward(77)
        >>> turtle.distance(pen)
        77.0
        """

    def dot(self, size=None, *color):
        """
        Draw a dot with diameter size, using color.

        Optional arguments:
        size -- an integer >= 1 (if given)
        color -- a colorstring or a numeric color tuple

        Draw a circular dot with diameter size, using color.
        If size is not given, the maximum of pensize+4 and 2*pensize is used.

        Example (for a Turtle instance named turtle):
        >>> turtle.dot()
        >>> turtle.fd(50); turtle.dot(20, "blue"); turtle.fd(50)
        """

    def down(self):
        """
        Pull the pen down -- drawing when moving.

        Aliases: pendown | pd | down

        No argument.

        Example (for a Turtle instance named turtle):
        >>> turtle.pendown()
        """

    def end_fill(self):
        """
        Fill the shape drawn after the call begin_fill().

        No argument.

        Example (for a Turtle instance named turtle):
        >>> turtle.color("black", "red")
        >>> turtle.begin_fill()
        >>> turtle.circle(60)
        >>> turtle.end_fill()
        """

    def end_poly(self):
        """
        Stop recording the vertices of a polygon.

        No argument.

        Stop recording the vertices of a polygon. Current turtle position is
        last point of polygon. This will be connected with the first point.

        Example (for a Turtle instance named turtle):
        >>> turtle.end_poly()
        """

    def fd(self, distance):
        """
        Move the turtle forward by the specified distance.

        Aliases: forward | fd

        Argument:
        distance -- a number (integer or float)

        Move the turtle forward by the specified distance, in the direction
        the turtle is headed.

        Example (for a Turtle instance named turtle):
        >>> turtle.position()
        (0.00, 0.00)
        >>> turtle.forward(25)
        >>> turtle.position()
        (25.00,0.00)
        >>> turtle.forward(-75)
        >>> turtle.position()
        (-50.00,0.00)
        """

    def fillcolor(self, *args):
        """
         Return or set the fillcolor.

        Arguments:
        Four input formats are allowed:
          - fillcolor()
            Return the current fillcolor as color specification string,
            possibly in hex-number format (see example).
            May be used as input to another color/pencolor/fillcolor call.
          - fillcolor(colorstring)
            s is a Tk color specification string, such as "red" or "yellow"
          - fillcolor((r, g, b))
            *a tuple* of r, g, and b, which represent, an RGB color,
            and each of r, g, and b are in the range 0..colormode,
            where colormode is either 1.0 or 255
          - fillcolor(r, g, b)
            r, g, and b represent an RGB color, and each of r, g, and b
            are in the range 0..colormode

        If turtleshape is a polygon, the interior of that polygon is drawn
        with the newly set fillcolor.

        Example (for a Turtle instance named turtle):
        >>> turtle.fillcolor('violet')
        >>> col = turtle.pencolor()
        >>> turtle.fillcolor(col)
        >>> turtle.fillcolor(0, .5, 0)
        """

    def filling(self):
        """
        Return fillstate (True if filling, False else).

        No argument.

        Example (for a Turtle instance named turtle):
        >>> turtle.begin_fill()
        >>> if turtle.filling():
        ...     turtle.pensize(5)
        ... else:
        ...     turtle.pensize(3)
        """

    def forward(self, distance):
        """
        Move the turtle forward by the specified distance.

        Aliases: forward | fd

        Argument:
        distance -- a number (integer or float)

        Move the turtle forward by the specified distance, in the direction
        the turtle is headed.

        Example (for a Turtle instance named turtle):
        >>> turtle.position()
        (0.00, 0.00)
        >>> turtle.forward(25)
        >>> turtle.position()
        (25.00,0.00)
        >>> turtle.forward(-75)
        >>> turtle.position()
        (-50.00,0.00)
        """

    def get_poly(self):
        """
        Return the lastly recorded polygon.

        No argument.

        Example (for a Turtle instance named turtle):
        >>> p = turtle.get_poly()
        >>> turtle.register_shape("myFavouriteShape", p)
        """

    def get_shapepoly(self):
        """
        Return the current shape polygon as tuple of coordinate pairs.

        No argument.

        Examples (for a Turtle instance named turtle):
        >>> turtle.shape("square")
        >>> turtle.shapetransform(4, -1, 0, 2)
        >>> turtle.get_shapepoly()
        ((50, -20), (30, 20), (-50, 20), (-30, -20))

        """

    def getpen(self):
        """
        Return the Turtleobject itself.

        No argument.

        Only reasonable use: as a function to return the 'anonymous turtle':

        Example:
        >>> pet = getturtle()
        >>> pet.fd(50)
        >>> pet
        <turtle.Turtle object at 0x0187D810>
        >>> turtles()
        [<turtle.Turtle object at 0x0187D810>]
        """

    def getscreen(self):
        """
        Return the TurtleScreen object, the turtle is drawing  on.

        No argument.

        Return the TurtleScreen object, the turtle is drawing  on.
        So TurtleScreen-methods can be called for that object.

        Example (for a Turtle instance named turtle):
        >>> ts = turtle.getscreen()
        >>> ts
        <turtle.TurtleScreen object at 0x0106B770>
        >>> ts.bgcolor("pink")
        """

    def getturtle(self):
        """
        Return the Turtleobject itself.

        No argument.

        Only reasonable use: as a function to return the 'anonymous turtle':

        Example:
        >>> pet = getturtle()
        >>> pet.fd(50)
        >>> pet
        <turtle.Turtle object at 0x0187D810>
        >>> turtles()
        [<turtle.Turtle object at 0x0187D810>]
        """

    def goto(self, x, y=None):
        """
        Move turtle to an absolute position.

        Aliases: setpos | setposition | goto:

        Arguments:
        x -- a number      or     a pair/vector of numbers
        y -- a number             None

        call: goto(x, y)         # two coordinates
        --or: goto((x, y))       # a pair (tuple) of coordinates
        --or: goto(vec)          # e.g. as returned by pos()

        Move turtle to an absolute position. If the pen is down,
        a line will be drawn. The turtle's orientation does not change.

        Example (for a Turtle instance named turtle):
        >>> tp = turtle.pos()
        >>> tp
        (0.00, 0.00)
        >>> turtle.setpos(60,30)
        >>> turtle.pos()
        (60.00,30.00)
        >>> turtle.setpos((20,80))
        >>> turtle.pos()
        (20.00,80.00)
        >>> turtle.setpos(tp)
        >>> turtle.pos()
        (0.00,0.00)
        """

    def heading(self):
        """
         Return the turtle's current heading.

        No arguments.

        Example (for a Turtle instance named turtle):
        >>> turtle.left(67)
        >>> turtle.heading()
        67.0
        """

    def hideturtle(self):
        """
        Makes the turtle invisible.

        Aliases: hideturtle | ht

        No argument.

        It's a good idea to do this while you're in the
        middle of a complicated drawing, because hiding
        the turtle speeds up the drawing observably.

        Example (for a Turtle instance named turtle):
        >>> turtle.hideturtle()
        """

    def home(self):
        """
        Move turtle to the origin - coordinates (0,0).

        No arguments.

        Move turtle to the origin - coordinates (0,0) and set its
        heading to its start-orientation (which depends on mode).

        Example (for a Turtle instance named turtle):
        >>> turtle.home()
        """

    def ht(self):
        """
        Makes the turtle invisible.

        Aliases: hideturtle | ht

        No argument.

        It's a good idea to do this while you're in the
        middle of a complicated drawing, because hiding
        the turtle speeds up the drawing observably.

        Example (for a Turtle instance named turtle):
        >>> turtle.hideturtle()
        """

    def isdown(self):
        """
        Return True if pen is down, False if it's up.

        No argument.

        Example (for a Turtle instance named turtle):
        >>> turtle.penup()
        >>> turtle.isdown()
        False
        >>> turtle.pendown()
        >>> turtle.isdown()
        True
        """

    def isvisible(self):
        """
        Return True if the Turtle is shown, False if it's hidden.

        No argument.

        Example (for a Turtle instance named turtle):
        >>> turtle.hideturtle()
        >>> print turtle.isvisible():
        False
        """

    def left(self, angle):
        """
        Turn turtle left by angle units.

        Aliases: left | lt

        Argument:
        angle -- a number (integer or float)

        Turn turtle left by angle units. (Units are by default degrees,
        but can be set via the degrees() and radians() functions.)
        Angle orientation depends on mode. (See this.)

        Example (for a Turtle instance named turtle):
        >>> turtle.heading()
        22.0
        >>> turtle.left(45)
        >>> turtle.heading()
        67.0
        """

    def lt(self, angle):
        """
        Turn turtle left by angle units.

        Aliases: left | lt

        Argument:
        angle -- a number (integer or float)

        Turn turtle left by angle units. (Units are by default degrees,
        but can be set via the degrees() and radians() functions.)
        Angle orientation depends on mode. (See this.)

        Example (for a Turtle instance named turtle):
        >>> turtle.heading()
        22.0
        >>> turtle.left(45)
        >>> turtle.heading()
        67.0
        """

    def onclick(self, fun, btn=1, add=None):
        """
        Bind fun to mouse-click event on this turtle on canvas.

        Arguments:
        fun --  a function with two arguments, to which will be assigned
                the coordinates of the clicked point on the canvas.
        num --  number of the mouse-button defaults to 1 (left mouse button).
        add --  True or False. If True, new binding will be added, otherwise
                it will replace a former binding.

        Example for the anonymous turtle, i. e. the procedural way:

        >>> def turn(x, y):
        ...     left(360)
        ...
        >>> onclick(turn)  # Now clicking into the turtle will turn it.
        >>> onclick(None)  # event-binding will be removed
        """

    def ondrag(self, fun, btn=1, add=None):
        """
        Bind fun to mouse-move event on this turtle on canvas.

        Arguments:
        fun -- a function with two arguments, to which will be assigned
               the coordinates of the clicked point on the canvas.
        num -- number of the mouse-button defaults to 1 (left mouse button).

        Every sequence of mouse-move-events on a turtle is preceded by a
        mouse-click event on that turtle.

        Example (for a Turtle instance named turtle):
        >>> turtle.ondrag(turtle.goto)

        Subsequently clicking and dragging a Turtle will move it
        across the screen thereby producing handdrawings (if pen is
        down).
        """

    def onrelease(self, fun, btn=1, add=None):
        """
        Bind fun to mouse-button-release event on this turtle on canvas.

        Arguments:
        fun -- a function with two arguments, to which will be assigned
                the coordinates of the clicked point on the canvas.
        num --  number of the mouse-button defaults to 1 (left mouse button).

        Example (for a MyTurtle instance named joe):
        >>> class MyTurtle(Turtle):
        ...     def glow(self,x,y):
        ...             self.fillcolor("red")
        ...     def unglow(self,x,y):
        ...             self.fillcolor("")
        ...
        >>> joe = MyTurtle()
        >>> joe.onclick(joe.glow)
        >>> joe.onrelease(joe.unglow)

        Clicking on joe turns fillcolor red, unclicking turns it to
        transparent.
        """

    def pd(self):
        """
        Pull the pen down -- drawing when moving.

        Aliases: pendown | pd | down

        No argument.

        Example (for a Turtle instance named turtle):
        >>> turtle.pendown()
        """

    def pen(self, pen=None, **pendict):
        """
        Return or set the pen's attributes.

        Arguments:
            pen -- a dictionary with some or all of the below listed keys.
            **pendict -- one or more keyword-arguments with the below
                         listed keys as keywords.

        Return or set the pen's attributes in a 'pen-dictionary'
        with the following key/value pairs:
           "shown"      :   True/False
           "pendown"    :   True/False
           "pencolor"   :   color-string or color-tuple
           "fillcolor"  :   color-string or color-tuple
           "pensize"    :   positive number
           "speed"      :   number in range 0..10
           "resizemode" :   "auto" or "user" or "noresize"
           "stretchfactor": (positive number, positive number)
           "shearfactor":   number
           "outline"    :   positive number
           "tilt"       :   number

        This dictionary can be used as argument for a subsequent
        pen()-call to restore the former pen-state. Moreover one
        or more of these attributes can be provided as keyword-arguments.
        This can be used to set several pen attributes in one statement.


        Examples (for a Turtle instance named turtle):
        >>> turtle.pen(fillcolor="black", pencolor="red", pensize=10)
        >>> turtle.pen()
        {'pensize': 10, 'shown': True, 'resizemode': 'auto', 'outline': 1,
        'pencolor': 'red', 'pendown': True, 'fillcolor': 'black',
        'stretchfactor': (1,1), 'speed': 3, 'shearfactor': 0.0}
        >>> penstate=turtle.pen()
        >>> turtle.color("yellow","")
        >>> turtle.penup()
        >>> turtle.pen()
        {'pensize': 10, 'shown': True, 'resizemode': 'auto', 'outline': 1,
        'pencolor': 'yellow', 'pendown': False, 'fillcolor': '',
        'stretchfactor': (1,1), 'speed': 3, 'shearfactor': 0.0}
        >>> p.pen(penstate, fillcolor="green")
        >>> p.pen()
        {'pensize': 10, 'shown': True, 'resizemode': 'auto', 'outline': 1,
        'pencolor': 'red', 'pendown': True, 'fillcolor': 'green',
        'stretchfactor': (1,1), 'speed': 3, 'shearfactor': 0.0}
        """

    def pencolor(self, *args):
        """
         Return or set the pencolor.

        Arguments:
        Four input formats are allowed:
          - pencolor()
            Return the current pencolor as color specification string,
            possibly in hex-number format (see example).
            May be used as input to another color/pencolor/fillcolor call.
          - pencolor(colorstring)
            s is a Tk color specification string, such as "red" or "yellow"
          - pencolor((r, g, b))
            *a tuple* of r, g, and b, which represent, an RGB color,
            and each of r, g, and b are in the range 0..colormode,
            where colormode is either 1.0 or 255
          - pencolor(r, g, b)
            r, g, and b represent an RGB color, and each of r, g, and b
            are in the range 0..colormode

        If turtleshape is a polygon, the outline of that polygon is drawn
        with the newly set pencolor.

        Example (for a Turtle instance named turtle):
        >>> turtle.pencolor('brown')
        >>> tup = (0.2, 0.8, 0.55)
        >>> turtle.pencolor(tup)
        >>> turtle.pencolor()
        '#33cc8c'
        """

    def pendown(self):
        """
        Pull the pen down -- drawing when moving.

        Aliases: pendown | pd | down

        No argument.

        Example (for a Turtle instance named turtle):
        >>> turtle.pendown()
        """

    def pensize(self, width=None):
        """
        Set or return the line thickness.

        Aliases:  pensize | width

        Argument:
        width -- positive number

        Set the line thickness to width or return it. If resizemode is set
        to "auto" and turtleshape is a polygon, that polygon is drawn with
        the same line thickness. If no argument is given, current pensize
        is returned.

        Example (for a Turtle instance named turtle):
        >>> turtle.pensize()
        1
        >>> turtle.pensize(10)   # from here on lines of width 10 are drawn
        """

    def penup(self):
        """
        Pull the pen up -- no drawing when moving.

        Aliases: penup | pu | up

        No argument

        Example (for a Turtle instance named turtle):
        >>> turtle.penup()
        """

    def pos(self):
        """
        Return the turtle's current location (x,y), as a Vec2D-vector.

        Aliases: pos | position

        No arguments.

        Example (for a Turtle instance named turtle):
        >>> turtle.pos()
        (0.00, 240.00)
        """

    def position(self):
        """
        Return the turtle's current location (x,y), as a Vec2D-vector.

        Aliases: pos | position

        No arguments.

        Example (for a Turtle instance named turtle):
        >>> turtle.pos()
        (0.00, 240.00)
        """

    def pu(self):
        """
        Pull the pen up -- no drawing when moving.

        Aliases: penup | pu | up

        No argument

        Example (for a Turtle instance named turtle):
        >>> turtle.penup()
        """

    def radians(self):
        """
         Set the angle measurement units to radians.

        No arguments.

        Example (for a Turtle instance named turtle):
        >>> turtle.heading()
        90
        >>> turtle.radians()
        >>> turtle.heading()
        1.5707963267948966
        """

    def reset(self):
        """
        Delete the turtle's drawings and restore its default values.

        No argument.

        Delete the turtle's drawings from the screen, re-center the turtle
        and set variables to the default values.

        Example (for a Turtle instance named turtle):
        >>> turtle.position()
        (0.00,-22.00)
        >>> turtle.heading()
        100.0
        >>> turtle.reset()
        >>> turtle.position()
        (0.00,0.00)
        >>> turtle.heading()
        0.0
        """

    def resizemode(self, rmode=None):
        """
        Set resizemode to one of the values: "auto", "user", "noresize".

        (Optional) Argument:
        rmode -- one of the strings "auto", "user", "noresize"

        Different resizemodes have the following effects:
          - "auto" adapts the appearance of the turtle
                   corresponding to the value of pensize.
          - "user" adapts the appearance of the turtle according to the
                   values of stretchfactor and outlinewidth (outline),
                   which are set by shapesize()
          - "noresize" no adaption of the turtle's appearance takes place.
        If no argument is given, return current resizemode.
        resizemode("user") is called by a call of shapesize with arguments.


        Examples (for a Turtle instance named turtle):
        >>> turtle.resizemode("noresize")
        >>> turtle.resizemode()
        'noresize'
        """

    def right(self, angle):
        """
        Turn turtle right by angle units.

        Aliases: right | rt

        Argument:
        angle -- a number (integer or float)

        Turn turtle right by angle units. (Units are by default degrees,
        but can be set via the degrees() and radians() functions.)
        Angle orientation depends on mode. (See this.)

        Example (for a Turtle instance named turtle):
        >>> turtle.heading()
        22.0
        >>> turtle.right(45)
        >>> turtle.heading()
        337.0
        """

    def rt(self, angle):
        """
        Turn turtle right by angle units.

        Aliases: right | rt

        Argument:
        angle -- a number (integer or float)

        Turn turtle right by angle units. (Units are by default degrees,
        but can be set via the degrees() and radians() functions.)
        Angle orientation depends on mode. (See this.)

        Example (for a Turtle instance named turtle):
        >>> turtle.heading()
        22.0
        >>> turtle.right(45)
        >>> turtle.heading()
        337.0
        """

    def seth(self, to_angle):
        """
        Set the orientation of the turtle to to_angle.

        Aliases:  setheading | seth

        Argument:
        to_angle -- a number (integer or float)

        Set the orientation of the turtle to to_angle.
        Here are some common directions in degrees:

         standard - mode:          logo-mode:
        -------------------|--------------------
           0 - east                0 - north
          90 - north              90 - east
         180 - west              180 - south
         270 - south             270 - west

        Example (for a Turtle instance named turtle):
        >>> turtle.setheading(90)
        >>> turtle.heading()
        90
        """

    def setheading(self, to_angle):
        """
        Set the orientation of the turtle to to_angle.

        Aliases:  setheading | seth

        Argument:
        to_angle -- a number (integer or float)

        Set the orientation of the turtle to to_angle.
        Here are some common directions in degrees:

         standard - mode:          logo-mode:
        -------------------|--------------------
           0 - east                0 - north
          90 - north              90 - east
         180 - west              180 - south
         270 - south             270 - west

        Example (for a Turtle instance named turtle):
        >>> turtle.setheading(90)
        >>> turtle.heading()
        90
        """

    def setpos(self, x, y=None):
        """
        Move turtle to an absolute position.

        Aliases: setpos | setposition | goto:

        Arguments:
        x -- a number      or     a pair/vector of numbers
        y -- a number             None

        call: goto(x, y)         # two coordinates
        --or: goto((x, y))       # a pair (tuple) of coordinates
        --or: goto(vec)          # e.g. as returned by pos()

        Move turtle to an absolute position. If the pen is down,
        a line will be drawn. The turtle's orientation does not change.

        Example (for a Turtle instance named turtle):
        >>> tp = turtle.pos()
        >>> tp
        (0.00, 0.00)
        >>> turtle.setpos(60,30)
        >>> turtle.pos()
        (60.00,30.00)
        >>> turtle.setpos((20,80))
        >>> turtle.pos()
        (20.00,80.00)
        >>> turtle.setpos(tp)
        >>> turtle.pos()
        (0.00,0.00)
        """

    def setposition(self, x, y=None):
        """
        Move turtle to an absolute position.

        Aliases: setpos | setposition | goto:

        Arguments:
        x -- a number      or     a pair/vector of numbers
        y -- a number             None

        call: goto(x, y)         # two coordinates
        --or: goto((x, y))       # a pair (tuple) of coordinates
        --or: goto(vec)          # e.g. as returned by pos()

        Move turtle to an absolute position. If the pen is down,
        a line will be drawn. The turtle's orientation does not change.

        Example (for a Turtle instance named turtle):
        >>> tp = turtle.pos()
        >>> tp
        (0.00, 0.00)
        >>> turtle.setpos(60,30)
        >>> turtle.pos()
        (60.00,30.00)
        >>> turtle.setpos((20,80))
        >>> turtle.pos()
        (20.00,80.00)
        >>> turtle.setpos(tp)
        >>> turtle.pos()
        (0.00,0.00)
        """

    def settiltangle(self, angle):
        """
        Rotate the turtleshape to point in the specified direction

        Argument: angle -- number

        Rotate the turtleshape to point in the direction specified by angle,
        regardless of its current tilt-angle. DO NOT change the turtle's
        heading (direction of movement).


        Examples (for a Turtle instance named turtle):
        >>> turtle.shape("circle")
        >>> turtle.shapesize(5,2)
        >>> turtle.settiltangle(45)
        >>> stamp()
        >>> turtle.fd(50)
        >>> turtle.settiltangle(-45)
        >>> stamp()
        >>> turtle.fd(50)
        """

    def setundobuffer(self, size):
        """
        Set or disable undobuffer.

        Argument:
        size -- an integer or None

        If size is an integer an empty undobuffer of given size is installed.
        Size gives the maximum number of turtle-actions that can be undone
        by the undo() function.
        If size is None, no undobuffer is present.

        Example (for a Turtle instance named turtle):
        >>> turtle.setundobuffer(42)
        """

    def setx(self, x):
        """
        Set the turtle's first coordinate to x

        Argument:
        x -- a number (integer or float)

        Set the turtle's first coordinate to x, leave second coordinate
        unchanged.

        Example (for a Turtle instance named turtle):
        >>> turtle.position()
        (0.00, 240.00)
        >>> turtle.setx(10)
        >>> turtle.position()
        (10.00, 240.00)
        """

    def sety(self, y):
        """
        Set the turtle's second coordinate to y

        Argument:
        y -- a number (integer or float)

        Set the turtle's first coordinate to x, second coordinate remains
        unchanged.

        Example (for a Turtle instance named turtle):
        >>> turtle.position()
        (0.00, 40.00)
        >>> turtle.sety(-10)
        >>> turtle.position()
        (0.00, -10.00)
        """

    def shape(self, name=None):
        """
        Set turtle shape to shape with given name / return current shapename.

        Optional argument:
        name -- a string, which is a valid shapename

        Set turtle shape to shape with given name or, if name is not given,
        return name of current shape.
        Shape with name must exist in the TurtleScreen's shape dictionary.
        Initially there are the following polygon shapes:
        'arrow', 'turtle', 'circle', 'square', 'triangle', 'classic'.
        To learn about how to deal with shapes see Screen-method register_shape.

        Example (for a Turtle instance named turtle):
        >>> turtle.shape()
        'arrow'
        >>> turtle.shape("turtle")
        >>> turtle.shape()
        'turtle'
        """

    def shapesize(self, stretch_wid=None, stretch_len=None, outline=None):
        """
        Set/return turtle's stretchfactors/outline. Set resizemode to "user".

        Optional arguments:
           stretch_wid : positive number
           stretch_len : positive number
           outline  : positive number

        Return or set the pen's attributes x/y-stretchfactors and/or outline.
        Set resizemode to "user".
        If and only if resizemode is set to "user", the turtle will be displayed
        stretched according to its stretchfactors:
        stretch_wid is stretchfactor perpendicular to orientation
        stretch_len is stretchfactor in direction of turtles orientation.
        outline determines the width of the shapes's outline.

        Examples (for a Turtle instance named turtle):
        >>> turtle.resizemode("user")
        >>> turtle.shapesize(5, 5, 12)
        >>> turtle.shapesize(outline=8)
        """

    def shapetransform(self, t11=None, t12=None, t21=None, t22=None):
        """
        Set or return the current transformation matrix of the turtle shape.

        Optional arguments: t11, t12, t21, t22 -- numbers.

        If none of the matrix elements are given, return the transformation
        matrix.
        Otherwise set the given elements and transform the turtleshape
        according to the matrix consisting of first row t11, t12 and
        second row t21, 22.
        Modify stretchfactor, shearfactor and tiltangle according to the
        given matrix.

        Examples (for a Turtle instance named turtle):
        >>> turtle.shape("square")
        >>> turtle.shapesize(4,2)
        >>> turtle.shearfactor(-0.5)
        >>> turtle.shapetransform()
        (4.0, -1.0, -0.0, 2.0)
        """

    def shearfactor(self, shear=None):
        """
        Set or return the current shearfactor.

        Optional argument: shear -- number, tangent of the shear angle

        Shear the turtleshape according to the given shearfactor shear,
        which is the tangent of the shear angle. DO NOT change the
        turtle's heading (direction of movement).
        If shear is not given: return the current shearfactor, i. e. the
        tangent of the shear angle, by which lines parallel to the
        heading of the turtle are sheared.

        Examples (for a Turtle instance named turtle):
        >>> turtle.shape("circle")
        >>> turtle.shapesize(5,2)
        >>> turtle.shearfactor(0.5)
        >>> turtle.shearfactor()
        >>> 0.5
        """

    def showturtle(self):
        """
        Makes the turtle visible.

        Aliases: showturtle | st

        No argument.

        Example (for a Turtle instance named turtle):
        >>> turtle.hideturtle()
        >>> turtle.showturtle()
        """

    def speed(self, speed=None):
        """
         Return or set the turtle's speed.

        Optional argument:
        speed -- an integer in the range 0..10 or a speedstring (see below)

        Set the turtle's speed to an integer value in the range 0 .. 10.
        If no argument is given: return current speed.

        If input is a number greater than 10 or smaller than 0.5,
        speed is set to 0.
        Speedstrings  are mapped to speedvalues in the following way:
            'fastest' :  0
            'fast'    :  10
            'normal'  :  6
            'slow'    :  3
            'slowest' :  1
        speeds from 1 to 10 enforce increasingly faster animation of
        line drawing and turtle turning.

        Attention:
        speed = 0 : *no* animation takes place. forward/back makes turtle jump
        and likewise left/right make the turtle turn instantly.

        Example (for a Turtle instance named turtle):
        >>> turtle.speed(3)
        """

    def st(self):
        """
        Makes the turtle visible.

        Aliases: showturtle | st

        No argument.

        Example (for a Turtle instance named turtle):
        >>> turtle.hideturtle()
        >>> turtle.showturtle()
        """

    def stamp(self):
        """
        Stamp a copy of the turtleshape onto the canvas and return its id.

        No argument.

        Stamp a copy of the turtle shape onto the canvas at the current
        turtle position. Return a stamp_id for that stamp, which can be
        used to delete it by calling clearstamp(stamp_id).

        Example (for a Turtle instance named turtle):
        >>> turtle.color("blue")
        >>> turtle.stamp()
        13
        >>> turtle.fd(50)
        """

    def tilt(self, angle):
        """
        Rotate the turtleshape by angle.

        Argument:
        angle - a number

        Rotate the turtleshape by angle from its current tilt-angle,
        but do NOT change the turtle's heading (direction of movement).

        Examples (for a Turtle instance named turtle):
        >>> turtle.shape("circle")
        >>> turtle.shapesize(5,2)
        >>> turtle.tilt(30)
        >>> turtle.fd(50)
        >>> turtle.tilt(30)
        >>> turtle.fd(50)
        """

    def tiltangle(self, angle=None):
        """
        Set or return the current tilt-angle.

        Optional argument: angle -- number

        Rotate the turtleshape to point in the direction specified by angle,
        regardless of its current tilt-angle. DO NOT change the turtle's
        heading (direction of movement).
        If angle is not given: return the current tilt-angle, i. e. the angle
        between the orientation of the turtleshape and the heading of the
        turtle (its direction of movement).

        Deprecated since Python 3.1

        Examples (for a Turtle instance named turtle):
        >>> turtle.shape("circle")
        >>> turtle.shapesize(5,2)
        >>> turtle.tilt(45)
        >>> turtle.tiltangle()
        """

    def towards(self, x, y=None):
        """
        Return the angle of the line from the turtle's position to (x, y).

        Arguments:
        x -- a number   or  a pair/vector of numbers   or   a turtle instance
        y -- a number       None                            None

        call: distance(x, y)         # two coordinates
        --or: distance((x, y))       # a pair (tuple) of coordinates
        --or: distance(vec)          # e.g. as returned by pos()
        --or: distance(mypen)        # where mypen is another turtle

        Return the angle, between the line from turtle-position to position
        specified by x, y and the turtle's start orientation. (Depends on
        modes - "standard" or "logo")

        Example (for a Turtle instance named turtle):
        >>> turtle.pos()
        (10.00, 10.00)
        >>> turtle.towards(0,0)
        225.0
        """

    def turtlesize(self, stretch_wid=None, stretch_len=None, outline=None):
        """
        Set/return turtle's stretchfactors/outline. Set resizemode to "user".

        Optional arguments:
           stretch_wid : positive number
           stretch_len : positive number
           outline  : positive number

        Return or set the pen's attributes x/y-stretchfactors and/or outline.
        Set resizemode to "user".
        If and only if resizemode is set to "user", the turtle will be displayed
        stretched according to its stretchfactors:
        stretch_wid is stretchfactor perpendicular to orientation
        stretch_len is stretchfactor in direction of turtles orientation.
        outline determines the width of the shapes's outline.

        Examples (for a Turtle instance named turtle):
        >>> turtle.resizemode("user")
        >>> turtle.shapesize(5, 5, 12)
        >>> turtle.shapesize(outline=8)
        """

    def undo(self):
        """
        undo (repeatedly) the last turtle action.

        No argument.

        undo (repeatedly) the last turtle action.
        Number of available undo actions is determined by the size of
        the undobuffer.

        Example (for a Turtle instance named turtle):
        >>> for i in range(4):
        ...     turtle.fd(50); turtle.lt(80)
        ...
        >>> for i in range(8):
        ...     turtle.undo()
        ...
        """

    def undobufferentries(self):
        """
        Return count of entries in the undobuffer.

        No argument.

        Example (for a Turtle instance named turtle):
        >>> while undobufferentries():
        ...     undo()
        """

    def up(self):
        """
        Pull the pen up -- no drawing when moving.

        Aliases: penup | pu | up

        No argument

        Example (for a Turtle instance named turtle):
        >>> turtle.penup()
        """

    def width(self, width=None):
        """
        Set or return the line thickness.

        Aliases:  pensize | width

        Argument:
        width -- positive number

        Set the line thickness to width or return it. If resizemode is set
        to "auto" and turtleshape is a polygon, that polygon is drawn with
        the same line thickness. If no argument is given, current pensize
        is returned.

        Example (for a Turtle instance named turtle):
        >>> turtle.pensize()
        1
        >>> turtle.pensize(10)   # from here on lines of width 10 are drawn
        """

    def write(self, arg, move=False, align='left', font=('Arial', 8, 'normal')):
        """
        Write text at the current turtle position.

        Arguments:
        arg -- info, which is to be written to the TurtleScreen
        move (optional) -- True/False
        align (optional) -- one of the strings "left", "center" or right"
        font (optional) -- a triple (fontname, fontsize, fonttype)

        Write text - the string representation of arg - at the current
        turtle position according to align ("left", "center" or right")
        and with the given font.
        If move is True, the pen is moved to the bottom-right corner
        of the text. By default, move is False.

        Example (for a Turtle instance named turtle):
        >>> turtle.write('Home = ', True, align="center")
        >>> turtle.write((0,0), True)
        """

    def xcor(self):
        """
         Return the turtle's x coordinate.

        No arguments.

        Example (for a Turtle instance named turtle):
        >>> reset()
        >>> turtle.left(60)
        >>> turtle.forward(100)
        >>> print turtle.xcor()
        50.0
        """

    def ycor(self):
        """
         Return the turtle's y coordinate
        ---
        No arguments.

        Example (for a Turtle instance named turtle):
        >>> reset()
        >>> turtle.left(60)
        >>> turtle.forward(100)
        >>> print turtle.ycor()
        86.6025403784
        """



class Turtle(RawTurtle):
    def __init__(self, shape='classic', undobuffersize=1000, visible=True): ...


    def back(self, distance):
        """
        Move the turtle backward by distance.

        Aliases: back | backward | bk

        Argument:
        distance -- a number

        Move the turtle backward by distance ,opposite to the direction the
        turtle is headed. Do not change the turtle's heading.

        Example (for a Turtle instance named turtle):
        >>> turtle.position()
        (0.00, 0.00)
        >>> turtle.backward(30)
        >>> turtle.position()
        (-30.00, 0.00)
        """

    def backward(self, distance):
        """
        Move the turtle backward by distance.

        Aliases: back | backward | bk

        Argument:
        distance -- a number

        Move the turtle backward by distance ,opposite to the direction the
        turtle is headed. Do not change the turtle's heading.

        Example (for a Turtle instance named turtle):
        >>> turtle.position()
        (0.00, 0.00)
        >>> turtle.backward(30)
        >>> turtle.position()
        (-30.00, 0.00)
        """

    def begin_fill(self):
        """
        Called just before drawing a shape to be filled.

        No argument.

        Example (for a Turtle instance named turtle):
        >>> turtle.color("black", "red")
        >>> turtle.begin_fill()
        >>> turtle.circle(60)
        >>> turtle.end_fill()
        """

    def begin_poly(self):
        """
        Start recording the vertices of a polygon.

        No argument.

        Start recording the vertices of a polygon. Current turtle position
        is first point of polygon.

        Example (for a Turtle instance named turtle):
        >>> turtle.begin_poly()
        """

    def bk(self, distance):
        """
        Move the turtle backward by distance.

        Aliases: back | backward | bk

        Argument:
        distance -- a number

        Move the turtle backward by distance ,opposite to the direction the
        turtle is headed. Do not change the turtle's heading.

        Example (for a Turtle instance named turtle):
        >>> turtle.position()
        (0.00, 0.00)
        >>> turtle.backward(30)
        >>> turtle.position()
        (-30.00, 0.00)
        """

    def circle(self, radius, extent=None, steps=None):
        """
         Draw a circle with given radius.

        Arguments:
        radius -- a number
        extent (optional) -- a number
        steps (optional) -- an integer

        Draw a circle with given radius. The center is radius units left
        of the turtle; extent - an angle - determines which part of the
        circle is drawn. If extent is not given, draw the entire circle.
        If extent is not a full circle, one endpoint of the arc is the
        current pen position. Draw the arc in counterclockwise direction
        if radius is positive, otherwise in clockwise direction. Finally
        the direction of the turtle is changed by the amount of extent.

        As the circle is approximated by an inscribed regular polygon,
        steps determines the number of steps to use. If not given,
        it will be calculated automatically. Maybe used to draw regular
        polygons.

        call: circle(radius)                  # full circle
        --or: circle(radius, extent)          # arc
        --or: circle(radius, extent, steps)
        --or: circle(radius, steps=6)         # 6-sided polygon

        Example (for a Turtle instance named turtle):
        >>> turtle.circle(50)
        >>> turtle.circle(120, 180)  # semicircle
        """

    def clear(self):
        """
        Delete the turtle's drawings from the screen. Do not move turtle.

        No arguments.

        Delete the turtle's drawings from the screen. Do not move turtle.
        State and position of the turtle as well as drawings of other
        turtles are not affected.

        Examples (for a Turtle instance named turtle):
        >>> turtle.clear()
        """

    def clearstamp(self, stampid):
        """
        Delete stamp with given stampid

        Argument:
        stampid - an integer, must be return value of previous stamp() call.

        Example (for a Turtle instance named turtle):
        >>> turtle.color("blue")
        >>> astamp = turtle.stamp()
        >>> turtle.fd(50)
        >>> turtle.clearstamp(astamp)
        """

    def clearstamps(self, n=None):
        """
        Delete all or first/last n of turtle's stamps.

        Optional argument:
        n -- an integer

        If n is None, delete all of pen's stamps,
        else if n > 0 delete first n stamps
        else if n < 0 delete last n stamps.

        Example (for a Turtle instance named turtle):
        >>> for i in range(8):
        ...     turtle.stamp(); turtle.fd(30)
        ...
        >>> turtle.clearstamps(2)
        >>> turtle.clearstamps(-2)
        >>> turtle.clearstamps()
        """

    def clone(self):
        """
        Create and return a clone of the turtle.

        No argument.

        Create and return a clone of the turtle with same position, heading
        and turtle properties.

        Example (for a Turtle instance named mick):
        mick = Turtle()
        joe = mick.clone()
        """

    def color(self, *args):
        """
        Return or set the pencolor and fillcolor.

        Arguments:
        Several input formats are allowed.
        They use 0, 1, 2, or 3 arguments as follows:

        color()
            Return the current pencolor and the current fillcolor
            as a pair of color specification strings as are returned
            by pencolor and fillcolor.
        color(colorstring), color((r,g,b)), color(r,g,b)
            inputs as in pencolor, set both, fillcolor and pencolor,
            to the given value.
        color(colorstring1, colorstring2),
        color((r1,g1,b1), (r2,g2,b2))
            equivalent to pencolor(colorstring1) and fillcolor(colorstring2)
            and analogously, if the other input format is used.

        If turtleshape is a polygon, outline and interior of that polygon
        is drawn with the newly set colors.
        For mor info see: pencolor, fillcolor

        Example (for a Turtle instance named turtle):
        >>> turtle.color('red', 'green')
        >>> turtle.color()
        ('red', 'green')
        >>> colormode(255)
        >>> color((40, 80, 120), (160, 200, 240))
        >>> color()
        ('#285078', '#a0c8f0')
        """

    def degrees(self, fullcircle=360.0):
        """
         Set angle measurement units to degrees.

        Optional argument:
        fullcircle -  a number

        Set angle measurement units, i. e. set number
        of 'degrees' for a full circle. Dafault value is
        360 degrees.

        Example (for a Turtle instance named turtle):
        >>> turtle.left(90)
        >>> turtle.heading()
        90

        Change angle measurement unit to grad (also known as gon,
        grade, or gradian and equals 1/100-th of the right angle.)
        >>> turtle.degrees(400.0)
        >>> turtle.heading()
        100

        """

    def distance(self, x, y=None):
        """
        Return the distance from the turtle to (x,y) in turtle step units.

        Arguments:
        x -- a number   or  a pair/vector of numbers   or   a turtle instance
        y -- a number       None                            None

        call: distance(x, y)         # two coordinates
        --or: distance((x, y))       # a pair (tuple) of coordinates
        --or: distance(vec)          # e.g. as returned by pos()
        --or: distance(mypen)        # where mypen is another turtle

        Example (for a Turtle instance named turtle):
        >>> turtle.pos()
        (0.00, 0.00)
        >>> turtle.distance(30,40)
        50.0
        >>> pen = Turtle()
        >>> pen.forward(77)
        >>> turtle.distance(pen)
        77.0
        """

    def dot(self, size=None, *color):
        """
        Draw a dot with diameter size, using color.

        Optional arguments:
        size -- an integer >= 1 (if given)
        color -- a colorstring or a numeric color tuple

        Draw a circular dot with diameter size, using color.
        If size is not given, the maximum of pensize+4 and 2*pensize is used.

        Example (for a Turtle instance named turtle):
        >>> turtle.dot()
        >>> turtle.fd(50); turtle.dot(20, "blue"); turtle.fd(50)
        """

    def down(self):
        """
        Pull the pen down -- drawing when moving.

        Aliases: pendown | pd | down

        No argument.

        Example (for a Turtle instance named turtle):
        >>> turtle.pendown()
        """

    def end_fill(self):
        """
        Fill the shape drawn after the call begin_fill().

        No argument.

        Example (for a Turtle instance named turtle):
        >>> turtle.color("black", "red")
        >>> turtle.begin_fill()
        >>> turtle.circle(60)
        >>> turtle.end_fill()
        """

    def end_poly(self):
        """
        Stop recording the vertices of a polygon.

        No argument.

        Stop recording the vertices of a polygon. Current turtle position is
        last point of polygon. This will be connected with the first point.

        Example (for a Turtle instance named turtle):
        >>> turtle.end_poly()
        """

    def fd(self, distance):
        """
        Move the turtle forward by the specified distance.

        Aliases: forward | fd

        Argument:
        distance -- a number (integer or float)

        Move the turtle forward by the specified distance, in the direction
        the turtle is headed.

        Example (for a Turtle instance named turtle):
        >>> turtle.position()
        (0.00, 0.00)
        >>> turtle.forward(25)
        >>> turtle.position()
        (25.00,0.00)
        >>> turtle.forward(-75)
        >>> turtle.position()
        (-50.00,0.00)
        """

    def fillcolor(self, *args):
        """
         Return or set the fillcolor.

        Arguments:
        Four input formats are allowed:
          - fillcolor()
            Return the current fillcolor as color specification string,
            possibly in hex-number format (see example).
            May be used as input to another color/pencolor/fillcolor call.
          - fillcolor(colorstring)
            s is a Tk color specification string, such as "red" or "yellow"
          - fillcolor((r, g, b))
            *a tuple* of r, g, and b, which represent, an RGB color,
            and each of r, g, and b are in the range 0..colormode,
            where colormode is either 1.0 or 255
          - fillcolor(r, g, b)
            r, g, and b represent an RGB color, and each of r, g, and b
            are in the range 0..colormode

        If turtleshape is a polygon, the interior of that polygon is drawn
        with the newly set fillcolor.

        Example (for a Turtle instance named turtle):
        >>> turtle.fillcolor('violet')
        >>> col = turtle.pencolor()
        >>> turtle.fillcolor(col)
        >>> turtle.fillcolor(0, .5, 0)
        """

    def filling(self):
        """
        Return fillstate (True if filling, False else).

        No argument.

        Example (for a Turtle instance named turtle):
        >>> turtle.begin_fill()
        >>> if turtle.filling():
        ...     turtle.pensize(5)
        ... else:
        ...     turtle.pensize(3)
        """

    def forward(self, distance):
        """
        Move the turtle forward by the specified distance.

        Aliases: forward | fd

        Argument:
        distance -- a number (integer or float)

        Move the turtle forward by the specified distance, in the direction
        the turtle is headed.

        Example (for a Turtle instance named turtle):
        >>> turtle.position()
        (0.00, 0.00)
        >>> turtle.forward(25)
        >>> turtle.position()
        (25.00,0.00)
        >>> turtle.forward(-75)
        >>> turtle.position()
        (-50.00,0.00)
        """

    def get_poly(self):
        """
        Return the lastly recorded polygon.

        No argument.

        Example (for a Turtle instance named turtle):
        >>> p = turtle.get_poly()
        >>> turtle.register_shape("myFavouriteShape", p)
        """

    def get_shapepoly(self):
        """
        Return the current shape polygon as tuple of coordinate pairs.

        No argument.

        Examples (for a Turtle instance named turtle):
        >>> turtle.shape("square")
        >>> turtle.shapetransform(4, -1, 0, 2)
        >>> turtle.get_shapepoly()
        ((50, -20), (30, 20), (-50, 20), (-30, -20))

        """

    def getpen(self):
        """
        Return the Turtleobject itself.

        No argument.

        Only reasonable use: as a function to return the 'anonymous turtle':

        Example:
        >>> pet = getturtle()
        >>> pet.fd(50)
        >>> pet
        <turtle.Turtle object at 0x0187D810>
        >>> turtles()
        [<turtle.Turtle object at 0x0187D810>]
        """

    def getscreen(self):
        """
        Return the TurtleScreen object, the turtle is drawing  on.

        No argument.

        Return the TurtleScreen object, the turtle is drawing  on.
        So TurtleScreen-methods can be called for that object.

        Example (for a Turtle instance named turtle):
        >>> ts = turtle.getscreen()
        >>> ts
        <turtle.TurtleScreen object at 0x0106B770>
        >>> ts.bgcolor("pink")
        """

    def getturtle(self):
        """
        Return the Turtleobject itself.

        No argument.

        Only reasonable use: as a function to return the 'anonymous turtle':

        Example:
        >>> pet = getturtle()
        >>> pet.fd(50)
        >>> pet
        <turtle.Turtle object at 0x0187D810>
        >>> turtles()
        [<turtle.Turtle object at 0x0187D810>]
        """

    def goto(self, x, y=None):
        """
        Move turtle to an absolute position.

        Aliases: setpos | setposition | goto:

        Arguments:
        x -- a number      or     a pair/vector of numbers
        y -- a number             None

        call: goto(x, y)         # two coordinates
        --or: goto((x, y))       # a pair (tuple) of coordinates
        --or: goto(vec)          # e.g. as returned by pos()

        Move turtle to an absolute position. If the pen is down,
        a line will be drawn. The turtle's orientation does not change.

        Example (for a Turtle instance named turtle):
        >>> tp = turtle.pos()
        >>> tp
        (0.00, 0.00)
        >>> turtle.setpos(60,30)
        >>> turtle.pos()
        (60.00,30.00)
        >>> turtle.setpos((20,80))
        >>> turtle.pos()
        (20.00,80.00)
        >>> turtle.setpos(tp)
        >>> turtle.pos()
        (0.00,0.00)
        """

    def heading(self):
        """
         Return the turtle's current heading.

        No arguments.

        Example (for a Turtle instance named turtle):
        >>> turtle.left(67)
        >>> turtle.heading()
        67.0
        """

    def hideturtle(self):
        """
        Makes the turtle invisible.

        Aliases: hideturtle | ht

        No argument.

        It's a good idea to do this while you're in the
        middle of a complicated drawing, because hiding
        the turtle speeds up the drawing observably.

        Example (for a Turtle instance named turtle):
        >>> turtle.hideturtle()
        """

    def home(self):
        """
        Move turtle to the origin - coordinates (0,0).

        No arguments.

        Move turtle to the origin - coordinates (0,0) and set its
        heading to its start-orientation (which depends on mode).

        Example (for a Turtle instance named turtle):
        >>> turtle.home()
        """

    def ht(self):
        """
        Makes the turtle invisible.

        Aliases: hideturtle | ht

        No argument.

        It's a good idea to do this while you're in the
        middle of a complicated drawing, because hiding
        the turtle speeds up the drawing observably.

        Example (for a Turtle instance named turtle):
        >>> turtle.hideturtle()
        """

    def isdown(self):
        """
        Return True if pen is down, False if it's up.

        No argument.

        Example (for a Turtle instance named turtle):
        >>> turtle.penup()
        >>> turtle.isdown()
        False
        >>> turtle.pendown()
        >>> turtle.isdown()
        True
        """

    def isvisible(self):
        """
        Return True if the Turtle is shown, False if it's hidden.

        No argument.

        Example (for a Turtle instance named turtle):
        >>> turtle.hideturtle()
        >>> print turtle.isvisible():
        False
        """

    def left(self, angle):
        """
        Turn turtle left by angle units.

        Aliases: left | lt

        Argument:
        angle -- a number (integer or float)

        Turn turtle left by angle units. (Units are by default degrees,
        but can be set via the degrees() and radians() functions.)
        Angle orientation depends on mode. (See this.)

        Example (for a Turtle instance named turtle):
        >>> turtle.heading()
        22.0
        >>> turtle.left(45)
        >>> turtle.heading()
        67.0
        """

    def lt(self, angle):
        """
        Turn turtle left by angle units.

        Aliases: left | lt

        Argument:
        angle -- a number (integer or float)

        Turn turtle left by angle units. (Units are by default degrees,
        but can be set via the degrees() and radians() functions.)
        Angle orientation depends on mode. (See this.)

        Example (for a Turtle instance named turtle):
        >>> turtle.heading()
        22.0
        >>> turtle.left(45)
        >>> turtle.heading()
        67.0
        """

    def onclick(self, fun, btn=1, add=None):
        """
        Bind fun to mouse-click event on this turtle on canvas.

        Arguments:
        fun --  a function with two arguments, to which will be assigned
                the coordinates of the clicked point on the canvas.
        num --  number of the mouse-button defaults to 1 (left mouse button).
        add --  True or False. If True, new binding will be added, otherwise
                it will replace a former binding.

        Example for the anonymous turtle, i. e. the procedural way:

        >>> def turn(x, y):
        ...     left(360)
        ...
        >>> onclick(turn)  # Now clicking into the turtle will turn it.
        >>> onclick(None)  # event-binding will be removed
        """

    def ondrag(self, fun, btn=1, add=None):
        """
        Bind fun to mouse-move event on this turtle on canvas.

        Arguments:
        fun -- a function with two arguments, to which will be assigned
               the coordinates of the clicked point on the canvas.
        num -- number of the mouse-button defaults to 1 (left mouse button).

        Every sequence of mouse-move-events on a turtle is preceded by a
        mouse-click event on that turtle.

        Example (for a Turtle instance named turtle):
        >>> turtle.ondrag(turtle.goto)

        Subsequently clicking and dragging a Turtle will move it
        across the screen thereby producing handdrawings (if pen is
        down).
        """

    def onrelease(self, fun, btn=1, add=None):
        """
        Bind fun to mouse-button-release event on this turtle on canvas.

        Arguments:
        fun -- a function with two arguments, to which will be assigned
                the coordinates of the clicked point on the canvas.
        num --  number of the mouse-button defaults to 1 (left mouse button).

        Example (for a MyTurtle instance named joe):
        >>> class MyTurtle(Turtle):
        ...     def glow(self,x,y):
        ...             self.fillcolor("red")
        ...     def unglow(self,x,y):
        ...             self.fillcolor("")
        ...
        >>> joe = MyTurtle()
        >>> joe.onclick(joe.glow)
        >>> joe.onrelease(joe.unglow)

        Clicking on joe turns fillcolor red, unclicking turns it to
        transparent.
        """

    def pd(self):
        """
        Pull the pen down -- drawing when moving.

        Aliases: pendown | pd | down

        No argument.

        Example (for a Turtle instance named turtle):
        >>> turtle.pendown()
        """

    def pen(self, pen=None, **pendict):
        """
        Return or set the pen's attributes.

        Arguments:
            pen -- a dictionary with some or all of the below listed keys.
            **pendict -- one or more keyword-arguments with the below
                         listed keys as keywords.

        Return or set the pen's attributes in a 'pen-dictionary'
        with the following key/value pairs:
           "shown"      :   True/False
           "pendown"    :   True/False
           "pencolor"   :   color-string or color-tuple
           "fillcolor"  :   color-string or color-tuple
           "pensize"    :   positive number
           "speed"      :   number in range 0..10
           "resizemode" :   "auto" or "user" or "noresize"
           "stretchfactor": (positive number, positive number)
           "shearfactor":   number
           "outline"    :   positive number
           "tilt"       :   number

        This dictionary can be used as argument for a subsequent
        pen()-call to restore the former pen-state. Moreover one
        or more of these attributes can be provided as keyword-arguments.
        This can be used to set several pen attributes in one statement.


        Examples (for a Turtle instance named turtle):
        >>> turtle.pen(fillcolor="black", pencolor="red", pensize=10)
        >>> turtle.pen()
        {'pensize': 10, 'shown': True, 'resizemode': 'auto', 'outline': 1,
        'pencolor': 'red', 'pendown': True, 'fillcolor': 'black',
        'stretchfactor': (1,1), 'speed': 3, 'shearfactor': 0.0}
        >>> penstate=turtle.pen()
        >>> turtle.color("yellow","")
        >>> turtle.penup()
        >>> turtle.pen()
        {'pensize': 10, 'shown': True, 'resizemode': 'auto', 'outline': 1,
        'pencolor': 'yellow', 'pendown': False, 'fillcolor': '',
        'stretchfactor': (1,1), 'speed': 3, 'shearfactor': 0.0}
        >>> p.pen(penstate, fillcolor="green")
        >>> p.pen()
        {'pensize': 10, 'shown': True, 'resizemode': 'auto', 'outline': 1,
        'pencolor': 'red', 'pendown': True, 'fillcolor': 'green',
        'stretchfactor': (1,1), 'speed': 3, 'shearfactor': 0.0}
        """

    def pencolor(self, *args):
        """
         Return or set the pencolor.

        Arguments:
        Four input formats are allowed:
          - pencolor()
            Return the current pencolor as color specification string,
            possibly in hex-number format (see example).
            May be used as input to another color/pencolor/fillcolor call.
          - pencolor(colorstring)
            s is a Tk color specification string, such as "red" or "yellow"
          - pencolor((r, g, b))
            *a tuple* of r, g, and b, which represent, an RGB color,
            and each of r, g, and b are in the range 0..colormode,
            where colormode is either 1.0 or 255
          - pencolor(r, g, b)
            r, g, and b represent an RGB color, and each of r, g, and b
            are in the range 0..colormode

        If turtleshape is a polygon, the outline of that polygon is drawn
        with the newly set pencolor.

        Example (for a Turtle instance named turtle):
        >>> turtle.pencolor('brown')
        >>> tup = (0.2, 0.8, 0.55)
        >>> turtle.pencolor(tup)
        >>> turtle.pencolor()
        '#33cc8c'
        """

    def pendown(self):
        """
        Pull the pen down -- drawing when moving.

        Aliases: pendown | pd | down

        No argument.

        Example (for a Turtle instance named turtle):
        >>> turtle.pendown()
        """

    def pensize(self, width=None):
        """
        Set or return the line thickness.

        Aliases:  pensize | width

        Argument:
        width -- positive number

        Set the line thickness to width or return it. If resizemode is set
        to "auto" and turtleshape is a polygon, that polygon is drawn with
        the same line thickness. If no argument is given, current pensize
        is returned.

        Example (for a Turtle instance named turtle):
        >>> turtle.pensize()
        1
        >>> turtle.pensize(10)   # from here on lines of width 10 are drawn
        """

    def penup(self):
        """
        Pull the pen up -- no drawing when moving.

        Aliases: penup | pu | up

        No argument

        Example (for a Turtle instance named turtle):
        >>> turtle.penup()
        """

    def pos(self):
        """
        Return the turtle's current location (x,y), as a Vec2D-vector.

        Aliases: pos | position

        No arguments.

        Example (for a Turtle instance named turtle):
        >>> turtle.pos()
        (0.00, 240.00)
        """

    def position(self):
        """
        Return the turtle's current location (x,y), as a Vec2D-vector.

        Aliases: pos | position

        No arguments.

        Example (for a Turtle instance named turtle):
        >>> turtle.pos()
        (0.00, 240.00)
        """

    def pu(self):
        """
        Pull the pen up -- no drawing when moving.

        Aliases: penup | pu | up

        No argument

        Example (for a Turtle instance named turtle):
        >>> turtle.penup()
        """

    def radians(self):
        """
         Set the angle measurement units to radians.

        No arguments.

        Example (for a Turtle instance named turtle):
        >>> turtle.heading()
        90
        >>> turtle.radians()
        >>> turtle.heading()
        1.5707963267948966
        """

    def reset(self):
        """
        Delete the turtle's drawings and restore its default values.

        No argument.

        Delete the turtle's drawings from the screen, re-center the turtle
        and set variables to the default values.

        Example (for a Turtle instance named turtle):
        >>> turtle.position()
        (0.00,-22.00)
        >>> turtle.heading()
        100.0
        >>> turtle.reset()
        >>> turtle.position()
        (0.00,0.00)
        >>> turtle.heading()
        0.0
        """

    def resizemode(self, rmode=None):
        """
        Set resizemode to one of the values: "auto", "user", "noresize".

        (Optional) Argument:
        rmode -- one of the strings "auto", "user", "noresize"

        Different resizemodes have the following effects:
          - "auto" adapts the appearance of the turtle
                   corresponding to the value of pensize.
          - "user" adapts the appearance of the turtle according to the
                   values of stretchfactor and outlinewidth (outline),
                   which are set by shapesize()
          - "noresize" no adaption of the turtle's appearance takes place.
        If no argument is given, return current resizemode.
        resizemode("user") is called by a call of shapesize with arguments.


        Examples (for a Turtle instance named turtle):
        >>> turtle.resizemode("noresize")
        >>> turtle.resizemode()
        'noresize'
        """

    def right(self, angle):
        """
        Turn turtle right by angle units.

        Aliases: right | rt

        Argument:
        angle -- a number (integer or float)

        Turn turtle right by angle units. (Units are by default degrees,
        but can be set via the degrees() and radians() functions.)
        Angle orientation depends on mode. (See this.)

        Example (for a Turtle instance named turtle):
        >>> turtle.heading()
        22.0
        >>> turtle.right(45)
        >>> turtle.heading()
        337.0
        """

    def rt(self, angle):
        """
        Turn turtle right by angle units.

        Aliases: right | rt

        Argument:
        angle -- a number (integer or float)

        Turn turtle right by angle units. (Units are by default degrees,
        but can be set via the degrees() and radians() functions.)
        Angle orientation depends on mode. (See this.)

        Example (for a Turtle instance named turtle):
        >>> turtle.heading()
        22.0
        >>> turtle.right(45)
        >>> turtle.heading()
        337.0
        """

    def seth(self, to_angle):
        """
        Set the orientation of the turtle to to_angle.

        Aliases:  setheading | seth

        Argument:
        to_angle -- a number (integer or float)

        Set the orientation of the turtle to to_angle.
        Here are some common directions in degrees:

         standard - mode:          logo-mode:
        -------------------|--------------------
           0 - east                0 - north
          90 - north              90 - east
         180 - west              180 - south
         270 - south             270 - west

        Example (for a Turtle instance named turtle):
        >>> turtle.setheading(90)
        >>> turtle.heading()
        90
        """

    def setheading(self, to_angle):
        """
        Set the orientation of the turtle to to_angle.

        Aliases:  setheading | seth

        Argument:
        to_angle -- a number (integer or float)

        Set the orientation of the turtle to to_angle.
        Here are some common directions in degrees:

         standard - mode:          logo-mode:
        -------------------|--------------------
           0 - east                0 - north
          90 - north              90 - east
         180 - west              180 - south
         270 - south             270 - west

        Example (for a Turtle instance named turtle):
        >>> turtle.setheading(90)
        >>> turtle.heading()
        90
        """

    def setpos(self, x, y=None):
        """
        Move turtle to an absolute position.

        Aliases: setpos | setposition | goto:

        Arguments:
        x -- a number      or     a pair/vector of numbers
        y -- a number             None

        call: goto(x, y)         # two coordinates
        --or: goto((x, y))       # a pair (tuple) of coordinates
        --or: goto(vec)          # e.g. as returned by pos()

        Move turtle to an absolute position. If the pen is down,
        a line will be drawn. The turtle's orientation does not change.

        Example (for a Turtle instance named turtle):
        >>> tp = turtle.pos()
        >>> tp
        (0.00, 0.00)
        >>> turtle.setpos(60,30)
        >>> turtle.pos()
        (60.00,30.00)
        >>> turtle.setpos((20,80))
        >>> turtle.pos()
        (20.00,80.00)
        >>> turtle.setpos(tp)
        >>> turtle.pos()
        (0.00,0.00)
        """

    def setposition(self, x, y=None):
        """
        Move turtle to an absolute position.

        Aliases: setpos | setposition | goto:

        Arguments:
        x -- a number      or     a pair/vector of numbers
        y -- a number             None

        call: goto(x, y)         # two coordinates
        --or: goto((x, y))       # a pair (tuple) of coordinates
        --or: goto(vec)          # e.g. as returned by pos()

        Move turtle to an absolute position. If the pen is down,
        a line will be drawn. The turtle's orientation does not change.

        Example (for a Turtle instance named turtle):
        >>> tp = turtle.pos()
        >>> tp
        (0.00, 0.00)
        >>> turtle.setpos(60,30)
        >>> turtle.pos()
        (60.00,30.00)
        >>> turtle.setpos((20,80))
        >>> turtle.pos()
        (20.00,80.00)
        >>> turtle.setpos(tp)
        >>> turtle.pos()
        (0.00,0.00)
        """

    def settiltangle(self, angle):
        """
        Rotate the turtleshape to point in the specified direction

        Argument: angle -- number

        Rotate the turtleshape to point in the direction specified by angle,
        regardless of its current tilt-angle. DO NOT change the turtle's
        heading (direction of movement).


        Examples (for a Turtle instance named turtle):
        >>> turtle.shape("circle")
        >>> turtle.shapesize(5,2)
        >>> turtle.settiltangle(45)
        >>> stamp()
        >>> turtle.fd(50)
        >>> turtle.settiltangle(-45)
        >>> stamp()
        >>> turtle.fd(50)
        """

    def setundobuffer(self, size):
        """
        Set or disable undobuffer.

        Argument:
        size -- an integer or None

        If size is an integer an empty undobuffer of given size is installed.
        Size gives the maximum number of turtle-actions that can be undone
        by the undo() function.
        If size is None, no undobuffer is present.

        Example (for a Turtle instance named turtle):
        >>> turtle.setundobuffer(42)
        """

    def setx(self, x):
        """
        Set the turtle's first coordinate to x

        Argument:
        x -- a number (integer or float)

        Set the turtle's first coordinate to x, leave second coordinate
        unchanged.

        Example (for a Turtle instance named turtle):
        >>> turtle.position()
        (0.00, 240.00)
        >>> turtle.setx(10)
        >>> turtle.position()
        (10.00, 240.00)
        """

    def sety(self, y):
        """
        Set the turtle's second coordinate to y

        Argument:
        y -- a number (integer or float)

        Set the turtle's first coordinate to x, second coordinate remains
        unchanged.

        Example (for a Turtle instance named turtle):
        >>> turtle.position()
        (0.00, 40.00)
        >>> turtle.sety(-10)
        >>> turtle.position()
        (0.00, -10.00)
        """

    def shape(self, name=None):
        """
        Set turtle shape to shape with given name / return current shapename.

        Optional argument:
        name -- a string, which is a valid shapename

        Set turtle shape to shape with given name or, if name is not given,
        return name of current shape.
        Shape with name must exist in the TurtleScreen's shape dictionary.
        Initially there are the following polygon shapes:
        'arrow', 'turtle', 'circle', 'square', 'triangle', 'classic'.
        To learn about how to deal with shapes see Screen-method register_shape.

        Example (for a Turtle instance named turtle):
        >>> turtle.shape()
        'arrow'
        >>> turtle.shape("turtle")
        >>> turtle.shape()
        'turtle'
        """

    def shapesize(self, stretch_wid=None, stretch_len=None, outline=None):
        """
        Set/return turtle's stretchfactors/outline. Set resizemode to "user".

        Optional arguments:
           stretch_wid : positive number
           stretch_len : positive number
           outline  : positive number

        Return or set the pen's attributes x/y-stretchfactors and/or outline.
        Set resizemode to "user".
        If and only if resizemode is set to "user", the turtle will be displayed
        stretched according to its stretchfactors:
        stretch_wid is stretchfactor perpendicular to orientation
        stretch_len is stretchfactor in direction of turtles orientation.
        outline determines the width of the shapes's outline.

        Examples (for a Turtle instance named turtle):
        >>> turtle.resizemode("user")
        >>> turtle.shapesize(5, 5, 12)
        >>> turtle.shapesize(outline=8)
        """

    def shapetransform(self, t11=None, t12=None, t21=None, t22=None):
        """
        Set or return the current transformation matrix of the turtle shape.

        Optional arguments: t11, t12, t21, t22 -- numbers.

        If none of the matrix elements are given, return the transformation
        matrix.
        Otherwise set the given elements and transform the turtleshape
        according to the matrix consisting of first row t11, t12 and
        second row t21, 22.
        Modify stretchfactor, shearfactor and tiltangle according to the
        given matrix.

        Examples (for a Turtle instance named turtle):
        >>> turtle.shape("square")
        >>> turtle.shapesize(4,2)
        >>> turtle.shearfactor(-0.5)
        >>> turtle.shapetransform()
        (4.0, -1.0, -0.0, 2.0)
        """

    def shearfactor(self, shear=None):
        """
        Set or return the current shearfactor.

        Optional argument: shear -- number, tangent of the shear angle

        Shear the turtleshape according to the given shearfactor shear,
        which is the tangent of the shear angle. DO NOT change the
        turtle's heading (direction of movement).
        If shear is not given: return the current shearfactor, i. e. the
        tangent of the shear angle, by which lines parallel to the
        heading of the turtle are sheared.

        Examples (for a Turtle instance named turtle):
        >>> turtle.shape("circle")
        >>> turtle.shapesize(5,2)
        >>> turtle.shearfactor(0.5)
        >>> turtle.shearfactor()
        >>> 0.5
        """

    def showturtle(self):
        """
        Makes the turtle visible.

        Aliases: showturtle | st

        No argument.

        Example (for a Turtle instance named turtle):
        >>> turtle.hideturtle()
        >>> turtle.showturtle()
        """

    def speed(self, speed=None):
        """
         Return or set the turtle's speed.

        Optional argument:
        speed -- an integer in the range 0..10 or a speedstring (see below)

        Set the turtle's speed to an integer value in the range 0 .. 10.
        If no argument is given: return current speed.

        If input is a number greater than 10 or smaller than 0.5,
        speed is set to 0.
        Speedstrings  are mapped to speedvalues in the following way:
            'fastest' :  0
            'fast'    :  10
            'normal'  :  6
            'slow'    :  3
            'slowest' :  1
        speeds from 1 to 10 enforce increasingly faster animation of
        line drawing and turtle turning.

        Attention:
        speed = 0 : *no* animation takes place. forward/back makes turtle jump
        and likewise left/right make the turtle turn instantly.

        Example (for a Turtle instance named turtle):
        >>> turtle.speed(3)
        """

    def st(self):
        """
        Makes the turtle visible.

        Aliases: showturtle | st

        No argument.

        Example (for a Turtle instance named turtle):
        >>> turtle.hideturtle()
        >>> turtle.showturtle()
        """

    def stamp(self):
        """
        Stamp a copy of the turtleshape onto the canvas and return its id.

        No argument.

        Stamp a copy of the turtle shape onto the canvas at the current
        turtle position. Return a stamp_id for that stamp, which can be
        used to delete it by calling clearstamp(stamp_id).

        Example (for a Turtle instance named turtle):
        >>> turtle.color("blue")
        >>> turtle.stamp()
        13
        >>> turtle.fd(50)
        """

    def tilt(self, angle):
        """
        Rotate the turtleshape by angle.

        Argument:
        angle - a number

        Rotate the turtleshape by angle from its current tilt-angle,
        but do NOT change the turtle's heading (direction of movement).

        Examples (for a Turtle instance named turtle):
        >>> turtle.shape("circle")
        >>> turtle.shapesize(5,2)
        >>> turtle.tilt(30)
        >>> turtle.fd(50)
        >>> turtle.tilt(30)
        >>> turtle.fd(50)
        """

    def tiltangle(self, angle=None):
        """
        Set or return the current tilt-angle.

        Optional argument: angle -- number

        Rotate the turtleshape to point in the direction specified by angle,
        regardless of its current tilt-angle. DO NOT change the turtle's
        heading (direction of movement).
        If angle is not given: return the current tilt-angle, i. e. the angle
        between the orientation of the turtleshape and the heading of the
        turtle (its direction of movement).

        Deprecated since Python 3.1

        Examples (for a Turtle instance named turtle):
        >>> turtle.shape("circle")
        >>> turtle.shapesize(5,2)
        >>> turtle.tilt(45)
        >>> turtle.tiltangle()
        """

    def towards(self, x, y=None):
        """
        Return the angle of the line from the turtle's position to (x, y).

        Arguments:
        x -- a number   or  a pair/vector of numbers   or   a turtle instance
        y -- a number       None                            None

        call: distance(x, y)         # two coordinates
        --or: distance((x, y))       # a pair (tuple) of coordinates
        --or: distance(vec)          # e.g. as returned by pos()
        --or: distance(mypen)        # where mypen is another turtle

        Return the angle, between the line from turtle-position to position
        specified by x, y and the turtle's start orientation. (Depends on
        modes - "standard" or "logo")

        Example (for a Turtle instance named turtle):
        >>> turtle.pos()
        (10.00, 10.00)
        >>> turtle.towards(0,0)
        225.0
        """

    def turtlesize(self, stretch_wid=None, stretch_len=None, outline=None):
        """
        Set/return turtle's stretchfactors/outline. Set resizemode to "user".

        Optional arguments:
           stretch_wid : positive number
           stretch_len : positive number
           outline  : positive number

        Return or set the pen's attributes x/y-stretchfactors and/or outline.
        Set resizemode to "user".
        If and only if resizemode is set to "user", the turtle will be displayed
        stretched according to its stretchfactors:
        stretch_wid is stretchfactor perpendicular to orientation
        stretch_len is stretchfactor in direction of turtles orientation.
        outline determines the width of the shapes's outline.

        Examples (for a Turtle instance named turtle):
        >>> turtle.resizemode("user")
        >>> turtle.shapesize(5, 5, 12)
        >>> turtle.shapesize(outline=8)
        """

    def undo(self):
        """
        undo (repeatedly) the last turtle action.

        No argument.

        undo (repeatedly) the last turtle action.
        Number of available undo actions is determined by the size of
        the undobuffer.

        Example (for a Turtle instance named turtle):
        >>> for i in range(4):
        ...     turtle.fd(50); turtle.lt(80)
        ...
        >>> for i in range(8):
        ...     turtle.undo()
        ...
        """

    def undobufferentries(self):
        """
        Return count of entries in the undobuffer.

        No argument.

        Example (for a Turtle instance named turtle):
        >>> while undobufferentries():
        ...     undo()
        """

    def up(self):
        """
        Pull the pen up -- no drawing when moving.

        Aliases: penup | pu | up

        No argument

        Example (for a Turtle instance named turtle):
        >>> turtle.penup()
        """

    def width(self, width=None):
        """
        Set or return the line thickness.

        Aliases:  pensize | width

        Argument:
        width -- positive number

        Set the line thickness to width or return it. If resizemode is set
        to "auto" and turtleshape is a polygon, that polygon is drawn with
        the same line thickness. If no argument is given, current pensize
        is returned.

        Example (for a Turtle instance named turtle):
        >>> turtle.pensize()
        1
        >>> turtle.pensize(10)   # from here on lines of width 10 are drawn
        """

    def write(self, arg, move=False, align='left', font=('Arial', 8, 'normal')):
        """
        Write text at the current turtle position.

        Arguments:
        arg -- info, which is to be written to the TurtleScreen
        move (optional) -- True/False
        align (optional) -- one of the strings "left", "center" or right"
        font (optional) -- a triple (fontname, fontsize, fonttype)

        Write text - the string representation of arg - at the current
        turtle position according to align ("left", "center" or right")
        and with the given font.
        If move is True, the pen is moved to the bottom-right corner
        of the text. By default, move is False.

        Example (for a Turtle instance named turtle):
        >>> turtle.write('Home = ', True, align="center")
        >>> turtle.write((0,0), True)
        """

    def xcor(self):
        """
         Return the turtle's x coordinate.

        No arguments.

        Example (for a Turtle instance named turtle):
        >>> reset()
        >>> turtle.left(60)
        >>> turtle.forward(100)
        >>> print turtle.xcor()
        50.0
        """

    def ycor(self):
        """
         Return the turtle's y coordinate
        ---
        No arguments.

        Example (for a Turtle instance named turtle):
        >>> reset()
        >>> turtle.left(60)
        >>> turtle.forward(100)
        >>> print turtle.ycor()
        86.6025403784
        """



class Shape(object):
    def __init__(self, type_, data=None): ...


    def addcomponent(self, poly, fill, outline=None):
        """
        Add component to a shape of type compound.

        Arguments: poly is a polygon, i. e. a tuple of number pairs.
        fill is the fillcolor of the component,
        outline is the outline color of the component.

        call (for a Shapeobject namend s):
        --   s.addcomponent(((0,0), (10,10), (-10,10)), "red", "blue")

        Example:
        >>> poly = ((0,0),(10,-5),(0,10),(-10,-5))
        >>> s = Shape("compound")
        >>> s.addcomponent(poly, "red", "blue")
        >>> # .. add more components and then use register_shape()
        """



class Vec2D(tuple):
    def __abs__(self): ...


    def __add__(self, other): ...


    def __getnewargs__(self): ...


    def __mul__(self, other): ...


    def __neg__(self): ...


    def __new__(cls, x, y): ...


    def __repr__(self): ...


    def __rmul__(self, other): ...


    def __sub__(self, other): ...


    def rotate(self, angle):
        """
        rotate self counterclockwise by angle
        """



def addshape(name, shape=None):
    """
    Adds a turtle shape to TurtleScreen's shapelist.

    Arguments:
    (1) name is the name of a gif-file and shape is None.
        Installs the corresponding image shape.
        !! Image-shapes DO NOT rotate when turning the turtle,
        !! so they do not display the heading of the turtle!
    (2) name is an arbitrary string and shape is a tuple
        of pairs of coordinates. Installs the corresponding
        polygon shape
    (3) name is an arbitrary string and shape is a
        (compound) Shape object. Installs the corresponding
        compound shape.
    To use a shape, you have to issue the command shape(shapename).

    call: register_shape("turtle.gif")
    --or: register_shape("tri", ((0,0), (10,10), (-10,10)))

    Example:
    >>> register_shape("triangle", ((5,-3),(0,5),(-5,-3)))

    """


def bgcolor(*args):
    """
    Set or return backgroundcolor of the TurtleScreen.

    Arguments (if given): a color string or three numbers
    in the range 0..colormode or a 3-tuple of such numbers.

    Example:
    >>> bgcolor("orange")
    >>> bgcolor()
    'orange'
    >>> bgcolor(0.5,0,0.5)
    >>> bgcolor()
    '#800080'
    """


def bgpic(picname=None):
    """
    Set background image or return name of current backgroundimage.

    Optional argument:
    picname -- a string, name of a gif-file or "nopic".

    If picname is a filename, set the corresponding image as background.
    If picname is "nopic", delete backgroundimage, if present.
    If picname is None, return the filename of the current backgroundimage.

    Example:
    >>> bgpic()
    'nopic'
    >>> bgpic("landscape.gif")
    >>> bgpic()
    'landscape.gif'
    """


def bye():
    """
    Shut the turtlegraphics window.

    Example:
    >>> bye()
    """


def clearscreen():
    """
    Delete all drawings and all turtles from the TurtleScreen.

    No argument.

    Reset empty TurtleScreen to its initial state: white background,
    no backgroundimage, no eventbindings and tracing on.

    Example:
    >>> clear()

    Note: this method is not available as function.
    """


def colormode(cmode=None):
    """
    Return the colormode or set it to 1.0 or 255.

    Optional argument:
    cmode -- one of the values 1.0 or 255

    r, g, b values of colortriples have to be in range 0..cmode.

    Example:
    >>> colormode()
    1.0
    >>> colormode(255)
    >>> pencolor(240,160,80)
    """


def delay(delay=None):
    """
     Return or set the drawing delay in milliseconds.

    Optional argument:
    delay -- positive integer

    Example:
    >>> delay(15)
    >>> delay()
    15
    """


def exitonclick():
    """
    Go into mainloop until the mouse is clicked.

    No arguments.

    Bind bye() method to mouseclick on TurtleScreen.
    If "using_IDLE" - value in configuration dictionary is False
    (default value), enter mainloop.
    If IDLE with -n switch (no subprocess) is used, this value should be
    set to True in turtle.cfg. In this case IDLE's mainloop
    is active also for the client script.

    This is a method of the Screen-class and not available for
    TurtleScreen instances.

    Example:
    >>> exitonclick()

    """


def getcanvas():
    """
    Return the Canvas of this TurtleScreen.

    No argument.

    Example:
    >>> cv = getcanvas()
    >>> cv
    <turtle.ScrolledCanvas instance at 0x010742D8>
    """


def getshapes():
    """
    Return a list of names of all currently available turtle shapes.

    No argument.

    Example:
    >>> getshapes()
    ['arrow', 'blank', 'circle', ... , 'turtle']
    """


def listen(xdummy=None, ydummy=None):
    """
    Set focus on TurtleScreen (in order to collect key-events)

    No arguments.
    Dummy arguments are provided in order
    to be able to pass listen to the onclick method.

    Example:
    >>> listen()
    """


def mainloop():
    """
    Starts event loop - calling Tkinter's mainloop function.

    No argument.

    Must be last statement in a turtle graphics program.
    Must NOT be used if a script is run from within IDLE in -n mode
    (No subprocess) - for interactive use of turtle graphics.

    Example:
    >>> mainloop()

    """


def mode(mode=None):
    """
    Set turtle-mode ('standard', 'logo' or 'world') and perform reset.

    Optional argument:
    mode -- one of the strings 'standard', 'logo' or 'world'

    Mode 'standard' is compatible with turtle.py.
    Mode 'logo' is compatible with most Logo-Turtle-Graphics.
    Mode 'world' uses userdefined 'worldcoordinates'. *Attention*: in
    this mode angles appear distorted if x/y unit-ratio doesn't equal 1.
    If mode is not given, return the current mode.

         Mode      Initial turtle heading     positive angles
     ------------|-------------------------|-------------------
      'standard'    to the right (east)       counterclockwise
        'logo'        upward    (north)         clockwise

    Examples:
    >>> mode('logo')   # resets turtle heading to north
    >>> mode()
    'logo'
    """


def numinput(title, prompt, default=None, minval=None, maxval=None):
    """
    Pop up a dialog window for input of a number.

    Arguments: title is the title of the dialog window,
    prompt is a text mostly describing what numerical information to input.
    default: default value
    minval: minimum value for imput
    maxval: maximum value for input

    The number input must be in the range minval .. maxval if these are
    given. If not, a hint is issued and the dialog remains open for
    correction. Return the number input.
    If the dialog is canceled,  return None.

    Example:
    >>> numinput("Poker", "Your stakes:", 1000, minval=10, maxval=10000)

    """


def onkey(fun, key):
    """
    Bind fun to key-release event of key.

    Arguments:
    fun -- a function with no arguments
    key -- a string: key (e.g. "a") or key-symbol (e.g. "space")

    In order to be able to register key-events, TurtleScreen
    must have focus. (See method listen.)

    Example:

    >>> def f():
    ...     fd(50)
    ...     lt(60)
    ...
    >>> onkey(f, "Up")
    >>> listen()

    Subsequently the turtle can be moved by repeatedly pressing
    the up-arrow key, consequently drawing a hexagon

    """


def onkeypress(fun, key=None):
    """
    Bind fun to key-press event of key if key is given,
    or to any key-press-event if no key is given.

    Arguments:
    fun -- a function with no arguments
    key -- a string: key (e.g. "a") or key-symbol (e.g. "space")

    In order to be able to register key-events, TurtleScreen
    must have focus. (See method listen.)

    Example (for a TurtleScreen instance named screen
    and a Turtle instance named turtle):

    >>> def f():
    ...     fd(50)
    ...     lt(60)
    ...
    >>> onkeypress(f, "Up")
    >>> listen()

    Subsequently the turtle can be moved by repeatedly pressing
    the up-arrow key, or by keeping pressed the up-arrow key.
    consequently drawing a hexagon.
    """


def onkeyrelease(fun, key):
    """
    Bind fun to key-release event of key.

    Arguments:
    fun -- a function with no arguments
    key -- a string: key (e.g. "a") or key-symbol (e.g. "space")

    In order to be able to register key-events, TurtleScreen
    must have focus. (See method listen.)

    Example:

    >>> def f():
    ...     fd(50)
    ...     lt(60)
    ...
    >>> onkey(f, "Up")
    >>> listen()

    Subsequently the turtle can be moved by repeatedly pressing
    the up-arrow key, consequently drawing a hexagon

    """


def onscreenclick(fun, btn=1, add=None):
    """
    Bind fun to mouse-click event on canvas.

    Arguments:
    fun -- a function with two arguments, the coordinates of the
           clicked point on the canvas.
    num -- the number of the mouse-button, defaults to 1

    Example (for a TurtleScreen instance named screen)

    >>> onclick(goto)
    >>> # Subsequently clicking into the TurtleScreen will
    >>> # make the turtle move to the clicked point.
    >>> onclick(None)
    """


def ontimer(fun, t=0):
    """
    Install a timer, which calls fun after t milliseconds.

    Arguments:
    fun -- a function with no arguments.
    t -- a number >= 0

    Example:

    >>> running = True
    >>> def f():
    ...     if running:
    ...             fd(50)
    ...             lt(60)
    ...             ontimer(f, 250)
    ...
    >>> f()   # makes the turtle marching around
    >>> running = False
    """


def register_shape(name, shape=None):
    """
    Adds a turtle shape to TurtleScreen's shapelist.

    Arguments:
    (1) name is the name of a gif-file and shape is None.
        Installs the corresponding image shape.
        !! Image-shapes DO NOT rotate when turning the turtle,
        !! so they do not display the heading of the turtle!
    (2) name is an arbitrary string and shape is a tuple
        of pairs of coordinates. Installs the corresponding
        polygon shape
    (3) name is an arbitrary string and shape is a
        (compound) Shape object. Installs the corresponding
        compound shape.
    To use a shape, you have to issue the command shape(shapename).

    call: register_shape("turtle.gif")
    --or: register_shape("tri", ((0,0), (10,10), (-10,10)))

    Example:
    >>> register_shape("triangle", ((5,-3),(0,5),(-5,-3)))

    """


def resetscreen():
    """
    Reset all Turtles on the Screen to their initial state.

    No argument.

    Example:
    >>> reset()
    """


def screensize(canvwidth=None, canvheight=None, bg=None):
    """
    Resize the canvas the turtles are drawing on.

    Optional arguments:
    canvwidth -- positive integer, new width of canvas in pixels
    canvheight --  positive integer, new height of canvas in pixels
    bg -- colorstring or color-tuple, new backgroundcolor
    If no arguments are given, return current (canvaswidth, canvasheight)

    Do not alter the drawing window. To observe hidden parts of
    the canvas use the scrollbars. (Can make visible those parts
    of a drawing, which were outside the canvas before!)

    Example (for a Turtle instance named turtle):
    >>> turtle.screensize(2000,1500)
    >>> # e.g. to search for an erroneously escaped turtle ;-)
    """


def setup(width=0.5, height=0.75, startx=None, starty=None):
    """
     Set the size and position of the main window.

    Arguments:
    width: as integer a size in pixels, as float a fraction of the 
      Default is 50% of 
    height: as integer the height in pixels, as float a fraction of the
       Default is 75% of 
    startx: if positive, starting position in pixels from the left
      edge of the screen, if negative from the right edge
      Default, startx=None is to center window horizontally.
    starty: if positive, starting position in pixels from the top
      edge of the screen, if negative from the bottom edge
      Default, starty=None is to center window vertically.

    Examples:
    >>> setup (width=200, height=200, startx=0, starty=0)

    sets window to 200x200 pixels, in upper left of screen

    >>> setup(width=.75, height=0.5, startx=None, starty=None)

    sets window to 75% of screen by 50% of screen and centers
    """


def setworldcoordinates(llx, lly, urx, ury):
    """
    Set up a user defined coordinate-system.

    Arguments:
    llx -- a number, x-coordinate of lower left corner of canvas
    lly -- a number, y-coordinate of lower left corner of canvas
    urx -- a number, x-coordinate of upper right corner of canvas
    ury -- a number, y-coordinate of upper right corner of canvas

    Set up user coodinat-system and switch to mode 'world' if necessary.
    This performs a reset. If mode 'world' is already active,
    all drawings are redrawn according to the new coordinates.

    But ATTENTION: in user-defined coordinatesystems angles may appear
    distorted. (see Screen.mode())

    Example:
    >>> setworldcoordinates(-10,-0.5,50,1.5)
    >>> for _ in range(36):
    ...     left(10)
    ...     forward(0.5)
    """


def textinput(title, prompt):
    """
    Pop up a dialog window for input of a string.

    Arguments: title is the title of the dialog window,
    prompt is a text mostly describing what information to input.

    Return the string input
    If the dialog is canceled, return None.

    Example:
    >>> textinput("NIM", "Name of first player:")

    """


def title(titlestring):
    """
    Set title of turtle-window

    Argument:
    titlestring -- a string, to appear in the titlebar of the
                   turtle graphics window.

    This is a method of Screen-class. Not available for TurtleScreen-
    objects.

    Example:
    >>> title("Welcome to the turtle-zoo!")
    """


def tracer(n=None, delay=None):
    """
    Turns turtle animation on/off and set delay for update drawings.

    Optional arguments:
    n -- nonnegative  integer
    delay -- nonnegative  integer

    If n is given, only each n-th regular screen update is really performed.
    (Can be used to accelerate the drawing of complex graphics.)
    Second arguments sets delay value (see RawTurtle.delay())

    Example:
    >>> tracer(8, 25)
    >>> dist = 2
    >>> for i in range(200):
    ...     fd(dist)
    ...     rt(90)
    ...     dist += 2
    """


def turtles():
    """
    Return the list of turtles on the 

    Example:
    >>> turtles()
    [<turtle.Turtle object at 0x00E11FB0>]
    """


def update():
    """
    Perform a TurtleScreen update.
    """


def window_height():
    """
     Return the height of the turtle window.

    Example:
    >>> window_height()
    480
    """


def window_width():
    """
     Return the width of the turtle window.

    Example:
    >>> window_width()
    640
    """


def back(distance):
    """
    Move the turtle backward by distance.

    Aliases: back | backward | bk

    Argument:
    distance -- a number

    Move the turtle backward by distance ,opposite to the direction the
    turtle is headed. Do not change the turtle's heading.

    Example:
    >>> position()
    (0.00, 0.00)
    >>> backward(30)
    >>> position()
    (-30.00, 0.00)
    """


def backward(distance):
    """
    Move the turtle backward by distance.

    Aliases: back | backward | bk

    Argument:
    distance -- a number

    Move the turtle backward by distance ,opposite to the direction the
    turtle is headed. Do not change the turtle's heading.

    Example:
    >>> position()
    (0.00, 0.00)
    >>> backward(30)
    >>> position()
    (-30.00, 0.00)
    """


def begin_fill():
    """
    Called just before drawing a shape to be filled.

    No argument.

    Example:
    >>> color("black", "red")
    >>> begin_fill()
    >>> circle(60)
    >>> end_fill()
    """


def begin_poly():
    """
    Start recording the vertices of a polygon.

    No argument.

    Start recording the vertices of a polygon. Current turtle position
    is first point of polygon.

    Example:
    >>> begin_poly()
    """


def bk(distance):
    """
    Move the turtle backward by distance.

    Aliases: back | backward | bk

    Argument:
    distance -- a number

    Move the turtle backward by distance ,opposite to the direction the
    turtle is headed. Do not change the turtle's heading.

    Example:
    >>> position()
    (0.00, 0.00)
    >>> backward(30)
    >>> position()
    (-30.00, 0.00)
    """


def circle(radius, extent=None, steps=None):
    """
     Draw a circle with given radius.

    Arguments:
    radius -- a number
    extent (optional) -- a number
    steps (optional) -- an integer

    Draw a circle with given radius. The center is radius units left
    of the turtle; extent - an angle - determines which part of the
    circle is drawn. If extent is not given, draw the entire circle.
    If extent is not a full circle, one endpoint of the arc is the
    current pen position. Draw the arc in counterclockwise direction
    if radius is positive, otherwise in clockwise direction. Finally
    the direction of the turtle is changed by the amount of extent.

    As the circle is approximated by an inscribed regular polygon,
    steps determines the number of steps to use. If not given,
    it will be calculated automatically. Maybe used to draw regular
    polygons.

    call: circle(radius)                  # full circle
    --or: circle(radius, extent)          # arc
    --or: circle(radius, extent, steps)
    --or: circle(radius, steps=6)         # 6-sided polygon

    Example:
    >>> circle(50)
    >>> circle(120, 180)  # semicircle
    """


def clear():
    """
    Delete the turtle's drawings from the screen. Do not move 

    No arguments.

    Delete the turtle's drawings from the screen. Do not move 
    State and position of the turtle as well as drawings of other
    turtles are not affected.

    Examples:
    >>> clear()
    """


def clearstamp(stampid):
    """
    Delete stamp with given stampid

    Argument:
    stampid - an integer, must be return value of previous stamp() call.

    Example:
    >>> color("blue")
    >>> astamp = stamp()
    >>> fd(50)
    >>> clearstamp(astamp)
    """


def clearstamps(n=None):
    """
    Delete all or first/last n of turtle's stamps.

    Optional argument:
    n -- an integer

    If n is None, delete all of pen's stamps,
    else if n > 0 delete first n stamps
    else if n < 0 delete last n stamps.

    Example:
    >>> for i in range(8):
    ...     stamp(); fd(30)
    ...
    >>> clearstamps(2)
    >>> clearstamps(-2)
    >>> clearstamps()
    """


def clone():
    """
    Create and return a clone of the 

    No argument.

    Create and return a clone of the turtle with same position, heading
    and turtle properties.

    Example (for a Turtle instance named mick):
    mick = Turtle()
    joe = mick.clone()
    """


def color(*args):
    """
    Return or set the pencolor and fillcolor.

    Arguments:
    Several input formats are allowed.
    They use 0, 1, 2, or 3 arguments as follows:

    color()
        Return the current pencolor and the current fillcolor
        as a pair of color specification strings as are returned
        by pencolor and fillcolor.
    color(colorstring), color((r,g,b)), color(r,g,b)
        inputs as in pencolor, set both, fillcolor and pencolor,
        to the given value.
    color(colorstring1, colorstring2),
    color((r1,g1,b1), (r2,g2,b2))
        equivalent to pencolor(colorstring1) and fillcolor(colorstring2)
        and analogously, if the other input format is used.

    If turtleshape is a polygon, outline and interior of that polygon
    is drawn with the newly set colors.
    For mor info see: pencolor, fillcolor

    Example:
    >>> color('red', 'green')
    >>> color()
    ('red', 'green')
    >>> colormode(255)
    >>> color((40, 80, 120), (160, 200, 240))
    >>> color()
    ('#285078', '#a0c8f0')
    """


def degrees(fullcircle=360.0):
    """
     Set angle measurement units to degrees.

    Optional argument:
    fullcircle -  a number

    Set angle measurement units, i. e. set number
    of 'degrees' for a full circle. Dafault value is
    360 degrees.

    Example:
    >>> left(90)
    >>> heading()
    90

    Change angle measurement unit to grad (also known as gon,
    grade, or gradian and equals 1/100-th of the right angle.)
    >>> degrees(400.0)
    >>> heading()
    100

    """


def distance(x, y=None):
    """
    Return the distance from the turtle to (x,y) in turtle step units.

    Arguments:
    x -- a number   or  a pair/vector of numbers   or   a turtle instance
    y -- a number       None                            None

    call: distance(x, y)         # two coordinates
    --or: distance((x, y))       # a pair (tuple) of coordinates
    --or: distance(vec)          # e.g. as returned by pos()
    --or: distance(mypen)        # where mypen is another turtle

    Example:
    >>> pos()
    (0.00, 0.00)
    >>> distance(30,40)
    50.0
    >>> pen = Turtle()
    >>> pen.forward(77)
    >>> distance(pen)
    77.0
    """


def dot(size=None, *color):
    """
    Draw a dot with diameter size, using color.

    Optional arguments:
    size -- an integer >= 1 (if given)
    color -- a colorstring or a numeric color tuple

    Draw a circular dot with diameter size, using color.
    If size is not given, the maximum of pensize+4 and 2*pensize is used.

    Example:
    >>> dot()
    >>> fd(50); dot(20, "blue"); fd(50)
    """


def down():
    """
    Pull the pen down -- drawing when moving.

    Aliases: pendown | pd | down

    No argument.

    Example:
    >>> pendown()
    """


def end_fill():
    """
    Fill the shape drawn after the call begin_fill().

    No argument.

    Example:
    >>> color("black", "red")
    >>> begin_fill()
    >>> circle(60)
    >>> end_fill()
    """


def end_poly():
    """
    Stop recording the vertices of a polygon.

    No argument.

    Stop recording the vertices of a polygon. Current turtle position is
    last point of polygon. This will be connected with the first point.

    Example:
    >>> end_poly()
    """


def fd(distance):
    """
    Move the turtle forward by the specified distance.

    Aliases: forward | fd

    Argument:
    distance -- a number (integer or float)

    Move the turtle forward by the specified distance, in the direction
    the turtle is headed.

    Example:
    >>> position()
    (0.00, 0.00)
    >>> forward(25)
    >>> position()
    (25.00,0.00)
    >>> forward(-75)
    >>> position()
    (-50.00,0.00)
    """


def fillcolor(*args):
    """
     Return or set the fillcolor.

    Arguments:
    Four input formats are allowed:
      - fillcolor()
        Return the current fillcolor as color specification string,
        possibly in hex-number format (see example).
        May be used as input to another color/pencolor/fillcolor call.
      - fillcolor(colorstring)
        s is a Tk color specification string, such as "red" or "yellow"
      - fillcolor((r, g, b))
        *a tuple* of r, g, and b, which represent, an RGB color,
        and each of r, g, and b are in the range 0..colormode,
        where colormode is either 1.0 or 255
      - fillcolor(r, g, b)
        r, g, and b represent an RGB color, and each of r, g, and b
        are in the range 0..colormode

    If turtleshape is a polygon, the interior of that polygon is drawn
    with the newly set fillcolor.

    Example:
    >>> fillcolor('violet')
    >>> col = pencolor()
    >>> fillcolor(col)
    >>> fillcolor(0, .5, 0)
    """


def filling():
    """
    Return fillstate (True if filling, False else).

    No argument.

    Example:
    >>> begin_fill()
    >>> if filling():
    ...     pensize(5)
    ... else:
    ...     pensize(3)
    """


def forward(distance):
    """
    Move the turtle forward by the specified distance.

    Aliases: forward | fd

    Argument:
    distance -- a number (integer or float)

    Move the turtle forward by the specified distance, in the direction
    the turtle is headed.

    Example:
    >>> position()
    (0.00, 0.00)
    >>> forward(25)
    >>> position()
    (25.00,0.00)
    >>> forward(-75)
    >>> position()
    (-50.00,0.00)
    """


def get_poly():
    """
    Return the lastly recorded polygon.

    No argument.

    Example:
    >>> p = get_poly()
    >>> register_shape("myFavouriteShape", p)
    """


def getpen():
    """
    Return the Turtleobject itself.

    No argument.

    Only reasonable use: as a function to return the 'anonymous turtle':

    Example:
    >>> pet = getturtle()
    >>> pet.fd(50)
    >>> pet
    <Turtle object at 0x0187D810>
    >>> turtles()
    [<Turtle object at 0x0187D810>]
    """


def getscreen():
    """
    Return the TurtleScreen object, the turtle is drawing  on.

    No argument.

    Return the TurtleScreen object, the turtle is drawing  on.
    So TurtleScreen-methods can be called for that object.

    Example:
    >>> ts = getscreen()
    >>> ts
    <TurtleScreen object at 0x0106B770>
    >>> ts.bgcolor("pink")
    """


def get_shapepoly():
    """
    Return the current shape polygon as tuple of coordinate pairs.

    No argument.

    Examples:
    >>> shape("square")
    >>> shapetransform(4, -1, 0, 2)
    >>> get_shapepoly()
    ((50, -20), (30, 20), (-50, 20), (-30, -20))

    """


def getturtle():
    """
    Return the Turtleobject itself.

    No argument.

    Only reasonable use: as a function to return the 'anonymous turtle':

    Example:
    >>> pet = getturtle()
    >>> pet.fd(50)
    >>> pet
    <Turtle object at 0x0187D810>
    >>> turtles()
    [<Turtle object at 0x0187D810>]
    """


def goto(x, y=None):
    """
    Move turtle to an absolute position.

    Aliases: setpos | setposition | goto:

    Arguments:
    x -- a number      or     a pair/vector of numbers
    y -- a number             None

    call: goto(x, y)         # two coordinates
    --or: goto((x, y))       # a pair (tuple) of coordinates
    --or: goto(vec)          # e.g. as returned by pos()

    Move turtle to an absolute position. If the pen is down,
    a line will be drawn. The turtle's orientation does not change.

    Example:
    >>> tp = pos()
    >>> tp
    (0.00, 0.00)
    >>> setpos(60,30)
    >>> pos()
    (60.00,30.00)
    >>> setpos((20,80))
    >>> pos()
    (20.00,80.00)
    >>> setpos(tp)
    >>> pos()
    (0.00,0.00)
    """


def heading():
    """
     Return the turtle's current heading.

    No arguments.

    Example:
    >>> left(67)
    >>> heading()
    67.0
    """


def hideturtle():
    """
    Makes the turtle invisible.

    Aliases: hideturtle | ht

    No argument.

    It's a good idea to do this while you're in the
    middle of a complicated drawing, because hiding
    the turtle speeds up the drawing observably.

    Example:
    >>> hideturtle()
    """


def home():
    """
    Move turtle to the origin - coordinates (0,0).

    No arguments.

    Move turtle to the origin - coordinates (0,0) and set its
    heading to its start-orientation (which depends on mode).

    Example:
    >>> home()
    """


def ht():
    """
    Makes the turtle invisible.

    Aliases: hideturtle | ht

    No argument.

    It's a good idea to do this while you're in the
    middle of a complicated drawing, because hiding
    the turtle speeds up the drawing observably.

    Example:
    >>> hideturtle()
    """


def isdown():
    """
    Return True if pen is down, False if it's up.

    No argument.

    Example:
    >>> penup()
    >>> isdown()
    False
    >>> pendown()
    >>> isdown()
    True
    """


def isvisible():
    """
    Return True if the Turtle is shown, False if it's hidden.

    No argument.

    Example:
    >>> hideturtle()
    >>> print isvisible():
    False
    """


def left(angle):
    """
    Turn turtle left by angle units.

    Aliases: left | lt

    Argument:
    angle -- a number (integer or float)

    Turn turtle left by angle units. (Units are by default degrees,
    but can be set via the degrees() and radians() functions.)
    Angle orientation depends on mode. (See this.)

    Example:
    >>> heading()
    22.0
    >>> left(45)
    >>> heading()
    67.0
    """


def lt(angle):
    """
    Turn turtle left by angle units.

    Aliases: left | lt

    Argument:
    angle -- a number (integer or float)

    Turn turtle left by angle units. (Units are by default degrees,
    but can be set via the degrees() and radians() functions.)
    Angle orientation depends on mode. (See this.)

    Example:
    >>> heading()
    22.0
    >>> left(45)
    >>> heading()
    67.0
    """


def onclick(fun, btn=1, add=None):
    """
    Bind fun to mouse-click event on this turtle on canvas.

    Arguments:
    fun --  a function with two arguments, to which will be assigned
            the coordinates of the clicked point on the canvas.
    num --  number of the mouse-button defaults to 1 (left mouse button).
    add --  True or False. If True, new binding will be added, otherwise
            it will replace a former binding.

    Example for the anonymous turtle, i. e. the procedural way:

    >>> def turn(x, y):
    ...     left(360)
    ...
    >>> onclick(turn)  # Now clicking into the turtle will turn it.
    >>> onclick(None)  # event-binding will be removed
    """


def ondrag(fun, btn=1, add=None):
    """
    Bind fun to mouse-move event on this turtle on canvas.

    Arguments:
    fun -- a function with two arguments, to which will be assigned
           the coordinates of the clicked point on the canvas.
    num -- number of the mouse-button defaults to 1 (left mouse button).

    Every sequence of mouse-move-events on a turtle is preceded by a
    mouse-click event on that 

    Example:
    >>> ondrag(goto)

    Subsequently clicking and dragging a Turtle will move it
    across the screen thereby producing handdrawings (if pen is
    down).
    """


def onrelease(fun, btn=1, add=None):
    """
    Bind fun to mouse-button-release event on this turtle on canvas.

    Arguments:
    fun -- a function with two arguments, to which will be assigned
            the coordinates of the clicked point on the canvas.
    num --  number of the mouse-button defaults to 1 (left mouse button).

    Example (for a MyTurtle instance named joe):
    >>> class MyTurtle(Turtle):
    ...     def glow(self,x,y):
    ...             self.fillcolor("red")
    ...     def unglow(self,x,y):
    ...             self.fillcolor("")
    ...
    >>> joe = MyTurtle()
    >>> joe.onclick(joe.glow)
    >>> joe.onrelease(joe.unglow)

    Clicking on joe turns fillcolor red, unclicking turns it to
    transparent.
    """


def pd():
    """
    Pull the pen down -- drawing when moving.

    Aliases: pendown | pd | down

    No argument.

    Example:
    >>> pendown()
    """


def pen(pen=None, **pendict):
    """
    Return or set the pen's attributes.

    Arguments:
        pen -- a dictionary with some or all of the below listed keys.
        **pendict -- one or more keyword-arguments with the below
                     listed keys as keywords.

    Return or set the pen's attributes in a 'pen-dictionary'
    with the following key/value pairs:
       "shown"      :   True/False
       "pendown"    :   True/False
       "pencolor"   :   color-string or color-tuple
       "fillcolor"  :   color-string or color-tuple
       "pensize"    :   positive number
       "speed"      :   number in range 0..10
       "resizemode" :   "auto" or "user" or "noresize"
       "stretchfactor": (positive number, positive number)
       "shearfactor":   number
       "outline"    :   positive number
       "tilt"       :   number

    This dictionary can be used as argument for a subsequent
    pen()-call to restore the former pen-state. Moreover one
    or more of these attributes can be provided as keyword-arguments.
    This can be used to set several pen attributes in one statement.


    Examples:
    >>> pen(fillcolor="black", pencolor="red", pensize=10)
    >>> pen()
    {'pensize': 10, 'shown': True, 'resizemode': 'auto', 'outline': 1,
    'pencolor': 'red', 'pendown': True, 'fillcolor': 'black',
    'stretchfactor': (1,1), 'speed': 3, 'shearfactor': 0.0}
    >>> penstate=pen()
    >>> color("yellow","")
    >>> penup()
    >>> pen()
    {'pensize': 10, 'shown': True, 'resizemode': 'auto', 'outline': 1,
    'pencolor': 'yellow', 'pendown': False, 'fillcolor': '',
    'stretchfactor': (1,1), 'speed': 3, 'shearfactor': 0.0}
    >>> p.pen(penstate, fillcolor="green")
    >>> p.pen()
    {'pensize': 10, 'shown': True, 'resizemode': 'auto', 'outline': 1,
    'pencolor': 'red', 'pendown': True, 'fillcolor': 'green',
    'stretchfactor': (1,1), 'speed': 3, 'shearfactor': 0.0}
    """


def pencolor(*args):
    """
     Return or set the pencolor.

    Arguments:
    Four input formats are allowed:
      - pencolor()
        Return the current pencolor as color specification string,
        possibly in hex-number format (see example).
        May be used as input to another color/pencolor/fillcolor call.
      - pencolor(colorstring)
        s is a Tk color specification string, such as "red" or "yellow"
      - pencolor((r, g, b))
        *a tuple* of r, g, and b, which represent, an RGB color,
        and each of r, g, and b are in the range 0..colormode,
        where colormode is either 1.0 or 255
      - pencolor(r, g, b)
        r, g, and b represent an RGB color, and each of r, g, and b
        are in the range 0..colormode

    If turtleshape is a polygon, the outline of that polygon is drawn
    with the newly set pencolor.

    Example:
    >>> pencolor('brown')
    >>> tup = (0.2, 0.8, 0.55)
    >>> pencolor(tup)
    >>> pencolor()
    '#33cc8c'
    """


def pendown():
    """
    Pull the pen down -- drawing when moving.

    Aliases: pendown | pd | down

    No argument.

    Example:
    >>> pendown()
    """


def pensize(width=None):
    """
    Set or return the line thickness.

    Aliases:  pensize | width

    Argument:
    width -- positive number

    Set the line thickness to width or return it. If resizemode is set
    to "auto" and turtleshape is a polygon, that polygon is drawn with
    the same line thickness. If no argument is given, current pensize
    is returned.

    Example:
    >>> pensize()
    1
    >>> pensize(10)   # from here on lines of width 10 are drawn
    """


def penup():
    """
    Pull the pen up -- no drawing when moving.

    Aliases: penup | pu | up

    No argument

    Example:
    >>> penup()
    """


def pos():
    """
    Return the turtle's current location (x,y), as a Vec2D-vector.

    Aliases: pos | position

    No arguments.

    Example:
    >>> pos()
    (0.00, 240.00)
    """


def position():
    """
    Return the turtle's current location (x,y), as a Vec2D-vector.

    Aliases: pos | position

    No arguments.

    Example:
    >>> pos()
    (0.00, 240.00)
    """


def pu():
    """
    Pull the pen up -- no drawing when moving.

    Aliases: penup | pu | up

    No argument

    Example:
    >>> penup()
    """


def radians():
    """
     Set the angle measurement units to radians.

    No arguments.

    Example:
    >>> heading()
    90
    >>> radians()
    >>> heading()
    1.5707963267948966
    """


def right(angle):
    """
    Turn turtle right by angle units.

    Aliases: right | rt

    Argument:
    angle -- a number (integer or float)

    Turn turtle right by angle units. (Units are by default degrees,
    but can be set via the degrees() and radians() functions.)
    Angle orientation depends on mode. (See this.)

    Example:
    >>> heading()
    22.0
    >>> right(45)
    >>> heading()
    337.0
    """


def reset():
    """
    Delete the turtle's drawings and restore its default values.

    No argument.

    Delete the turtle's drawings from the screen, re-center the turtle
    and set variables to the default values.

    Example:
    >>> position()
    (0.00,-22.00)
    >>> heading()
    100.0
    >>> reset()
    >>> position()
    (0.00,0.00)
    >>> heading()
    0.0
    """


def resizemode(rmode=None):
    """
    Set resizemode to one of the values: "auto", "user", "noresize".

    (Optional) Argument:
    rmode -- one of the strings "auto", "user", "noresize"

    Different resizemodes have the following effects:
      - "auto" adapts the appearance of the turtle
               corresponding to the value of pensize.
      - "user" adapts the appearance of the turtle according to the
               values of stretchfactor and outlinewidth (outline),
               which are set by shapesize()
      - "noresize" no adaption of the turtle's appearance takes place.
    If no argument is given, return current resizemode.
    resizemode("user") is called by a call of shapesize with arguments.


    Examples:
    >>> resizemode("noresize")
    >>> resizemode()
    'noresize'
    """


def rt(angle):
    """
    Turn turtle right by angle units.

    Aliases: right | rt

    Argument:
    angle -- a number (integer or float)

    Turn turtle right by angle units. (Units are by default degrees,
    but can be set via the degrees() and radians() functions.)
    Angle orientation depends on mode. (See this.)

    Example:
    >>> heading()
    22.0
    >>> right(45)
    >>> heading()
    337.0
    """


def seth(to_angle):
    """
    Set the orientation of the turtle to to_angle.

    Aliases:  setheading | seth

    Argument:
    to_angle -- a number (integer or float)

    Set the orientation of the turtle to to_angle.
    Here are some common directions in degrees:

     standard - mode:          logo-mode:
    -------------------|--------------------
       0 - east                0 - north
      90 - north              90 - east
     180 - west              180 - south
     270 - south             270 - west

    Example:
    >>> setheading(90)
    >>> heading()
    90
    """


def setheading(to_angle):
    """
    Set the orientation of the turtle to to_angle.

    Aliases:  setheading | seth

    Argument:
    to_angle -- a number (integer or float)

    Set the orientation of the turtle to to_angle.
    Here are some common directions in degrees:

     standard - mode:          logo-mode:
    -------------------|--------------------
       0 - east                0 - north
      90 - north              90 - east
     180 - west              180 - south
     270 - south             270 - west

    Example:
    >>> setheading(90)
    >>> heading()
    90
    """


def setpos(x, y=None):
    """
    Move turtle to an absolute position.

    Aliases: setpos | setposition | goto:

    Arguments:
    x -- a number      or     a pair/vector of numbers
    y -- a number             None

    call: goto(x, y)         # two coordinates
    --or: goto((x, y))       # a pair (tuple) of coordinates
    --or: goto(vec)          # e.g. as returned by pos()

    Move turtle to an absolute position. If the pen is down,
    a line will be drawn. The turtle's orientation does not change.

    Example:
    >>> tp = pos()
    >>> tp
    (0.00, 0.00)
    >>> setpos(60,30)
    >>> pos()
    (60.00,30.00)
    >>> setpos((20,80))
    >>> pos()
    (20.00,80.00)
    >>> setpos(tp)
    >>> pos()
    (0.00,0.00)
    """


def setposition(x, y=None):
    """
    Move turtle to an absolute position.

    Aliases: setpos | setposition | goto:

    Arguments:
    x -- a number      or     a pair/vector of numbers
    y -- a number             None

    call: goto(x, y)         # two coordinates
    --or: goto((x, y))       # a pair (tuple) of coordinates
    --or: goto(vec)          # e.g. as returned by pos()

    Move turtle to an absolute position. If the pen is down,
    a line will be drawn. The turtle's orientation does not change.

    Example:
    >>> tp = pos()
    >>> tp
    (0.00, 0.00)
    >>> setpos(60,30)
    >>> pos()
    (60.00,30.00)
    >>> setpos((20,80))
    >>> pos()
    (20.00,80.00)
    >>> setpos(tp)
    >>> pos()
    (0.00,0.00)
    """


def settiltangle(angle):
    """
    Rotate the turtleshape to point in the specified direction

    Argument: angle -- number

    Rotate the turtleshape to point in the direction specified by angle,
    regardless of its current tilt-angle. DO NOT change the turtle's
    heading (direction of movement).


    Examples:
    >>> shape("circle")
    >>> shapesize(5,2)
    >>> settiltangle(45)
    >>> stamp()
    >>> fd(50)
    >>> settiltangle(-45)
    >>> stamp()
    >>> fd(50)
    """


def setundobuffer(size):
    """
    Set or disable undobuffer.

    Argument:
    size -- an integer or None

    If size is an integer an empty undobuffer of given size is installed.
    Size gives the maximum number of turtle-actions that can be undone
    by the undo() function.
    If size is None, no undobuffer is present.

    Example:
    >>> setundobuffer(42)
    """


def setx(x):
    """
    Set the turtle's first coordinate to x

    Argument:
    x -- a number (integer or float)

    Set the turtle's first coordinate to x, leave second coordinate
    unchanged.

    Example:
    >>> position()
    (0.00, 240.00)
    >>> setx(10)
    >>> position()
    (10.00, 240.00)
    """


def sety(y):
    """
    Set the turtle's second coordinate to y

    Argument:
    y -- a number (integer or float)

    Set the turtle's first coordinate to x, second coordinate remains
    unchanged.

    Example:
    >>> position()
    (0.00, 40.00)
    >>> sety(-10)
    >>> position()
    (0.00, -10.00)
    """


def shape(name=None):
    """
    Set turtle shape to shape with given name / return current shapename.

    Optional argument:
    name -- a string, which is a valid shapename

    Set turtle shape to shape with given name or, if name is not given,
    return name of current shape.
    Shape with name must exist in the TurtleScreen's shape dictionary.
    Initially there are the following polygon shapes:
    'arrow', 'turtle', 'circle', 'square', 'triangle', 'classic'.
    To learn about how to deal with shapes see Screen-method register_shape.

    Example:
    >>> shape()
    'arrow'
    >>> shape("turtle")
    >>> shape()
    'turtle'
    """


def shapesize(stretch_wid=None, stretch_len=None, outline=None):
    """
    Set/return turtle's stretchfactors/outline. Set resizemode to "user".

    Optional arguments:
       stretch_wid : positive number
       stretch_len : positive number
       outline  : positive number

    Return or set the pen's attributes x/y-stretchfactors and/or outline.
    Set resizemode to "user".
    If and only if resizemode is set to "user", the turtle will be displayed
    stretched according to its stretchfactors:
    stretch_wid is stretchfactor perpendicular to orientation
    stretch_len is stretchfactor in direction of turtles orientation.
    outline determines the width of the shapes's outline.

    Examples:
    >>> resizemode("user")
    >>> shapesize(5, 5, 12)
    >>> shapesize(outline=8)
    """


def shapetransform(t11=None, t12=None, t21=None, t22=None):
    """
    Set or return the current transformation matrix of the turtle shape.

    Optional arguments: t11, t12, t21, t22 -- numbers.

    If none of the matrix elements are given, return the transformation
    matrix.
    Otherwise set the given elements and transform the turtleshape
    according to the matrix consisting of first row t11, t12 and
    second row t21, 22.
    Modify stretchfactor, shearfactor and tiltangle according to the
    given matrix.

    Examples:
    >>> shape("square")
    >>> shapesize(4,2)
    >>> shearfactor(-0.5)
    >>> shapetransform()
    (4.0, -1.0, -0.0, 2.0)
    """


def shearfactor(shear=None):
    """
    Set or return the current shearfactor.

    Optional argument: shear -- number, tangent of the shear angle

    Shear the turtleshape according to the given shearfactor shear,
    which is the tangent of the shear angle. DO NOT change the
    turtle's heading (direction of movement).
    If shear is not given: return the current shearfactor, i. e. the
    tangent of the shear angle, by which lines parallel to the
    heading of the turtle are sheared.

    Examples:
    >>> shape("circle")
    >>> shapesize(5,2)
    >>> shearfactor(0.5)
    >>> shearfactor()
    >>> 0.5
    """


def showturtle():
    """
    Makes the turtle visible.

    Aliases: showturtle | st

    No argument.

    Example:
    >>> hideturtle()
    >>> showturtle()
    """


def speed(speed=None):
    """
     Return or set the turtle's speed.

    Optional argument:
    speed -- an integer in the range 0..10 or a speedstring (see below)

    Set the turtle's speed to an integer value in the range 0 .. 10.
    If no argument is given: return current speed.

    If input is a number greater than 10 or smaller than 0.5,
    speed is set to 0.
    Speedstrings  are mapped to speedvalues in the following way:
        'fastest' :  0
        'fast'    :  10
        'normal'  :  6
        'slow'    :  3
        'slowest' :  1
    speeds from 1 to 10 enforce increasingly faster animation of
    line drawing and turtle turning.

    Attention:
    speed = 0 : *no* animation takes place. forward/back makes turtle jump
    and likewise left/right make the turtle turn instantly.

    Example:
    >>> speed(3)
    """


def st():
    """
    Makes the turtle visible.

    Aliases: showturtle | st

    No argument.

    Example:
    >>> hideturtle()
    >>> showturtle()
    """


def stamp():
    """
    Stamp a copy of the turtleshape onto the canvas and return its id.

    No argument.

    Stamp a copy of the turtle shape onto the canvas at the current
    turtle position. Return a stamp_id for that stamp, which can be
    used to delete it by calling clearstamp(stamp_id).

    Example:
    >>> color("blue")
    >>> stamp()
    13
    >>> fd(50)
    """


def tilt(angle):
    """
    Rotate the turtleshape by angle.

    Argument:
    angle - a number

    Rotate the turtleshape by angle from its current tilt-angle,
    but do NOT change the turtle's heading (direction of movement).

    Examples:
    >>> shape("circle")
    >>> shapesize(5,2)
    >>> tilt(30)
    >>> fd(50)
    >>> tilt(30)
    >>> fd(50)
    """


def tiltangle(angle=None):
    """
    Set or return the current tilt-angle.

    Optional argument: angle -- number

    Rotate the turtleshape to point in the direction specified by angle,
    regardless of its current tilt-angle. DO NOT change the turtle's
    heading (direction of movement).
    If angle is not given: return the current tilt-angle, i. e. the angle
    between the orientation of the turtleshape and the heading of the
    turtle (its direction of movement).

    Deprecated since Python 3.1

    Examples:
    >>> shape("circle")
    >>> shapesize(5,2)
    >>> tilt(45)
    >>> tiltangle()
    """


def towards(x, y=None):
    """
    Return the angle of the line from the turtle's position to (x, y).

    Arguments:
    x -- a number   or  a pair/vector of numbers   or   a turtle instance
    y -- a number       None                            None

    call: distance(x, y)         # two coordinates
    --or: distance((x, y))       # a pair (tuple) of coordinates
    --or: distance(vec)          # e.g. as returned by pos()
    --or: distance(mypen)        # where mypen is another turtle

    Return the angle, between the line from turtle-position to position
    specified by x, y and the turtle's start orientation. (Depends on
    modes - "standard" or "logo")

    Example:
    >>> pos()
    (10.00, 10.00)
    >>> towards(0,0)
    225.0
    """


def turtlesize(stretch_wid=None, stretch_len=None, outline=None):
    """
    Set/return turtle's stretchfactors/outline. Set resizemode to "user".

    Optional arguments:
       stretch_wid : positive number
       stretch_len : positive number
       outline  : positive number

    Return or set the pen's attributes x/y-stretchfactors and/or outline.
    Set resizemode to "user".
    If and only if resizemode is set to "user", the turtle will be displayed
    stretched according to its stretchfactors:
    stretch_wid is stretchfactor perpendicular to orientation
    stretch_len is stretchfactor in direction of turtles orientation.
    outline determines the width of the shapes's outline.

    Examples:
    >>> resizemode("user")
    >>> shapesize(5, 5, 12)
    >>> shapesize(outline=8)
    """


def undo():
    """
    undo (repeatedly) the last turtle action.

    No argument.

    undo (repeatedly) the last turtle action.
    Number of available undo actions is determined by the size of
    the undobuffer.

    Example:
    >>> for i in range(4):
    ...     fd(50); lt(80)
    ...
    >>> for i in range(8):
    ...     undo()
    ...
    """


def undobufferentries():
    """
    Return count of entries in the undobuffer.

    No argument.

    Example:
    >>> while undobufferentries():
    ...     undo()
    """


def up():
    """
    Pull the pen up -- no drawing when moving.

    Aliases: penup | pu | up

    No argument

    Example:
    >>> penup()
    """


def width(width=None):
    """
    Set or return the line thickness.

    Aliases:  pensize | width

    Argument:
    width -- positive number

    Set the line thickness to width or return it. If resizemode is set
    to "auto" and turtleshape is a polygon, that polygon is drawn with
    the same line thickness. If no argument is given, current pensize
    is returned.

    Example:
    >>> pensize()
    1
    >>> pensize(10)   # from here on lines of width 10 are drawn
    """


def write(arg, move=False, align='left', font=('Arial', 8, 'normal')):
    """
    Write text at the current turtle position.

    Arguments:
    arg -- info, which is to be written to the TurtleScreen
    move (optional) -- True/False
    align (optional) -- one of the strings "left", "center" or right"
    font (optional) -- a triple (fontname, fontsize, fonttype)

    Write text - the string representation of arg - at the current
    turtle position according to align ("left", "center" or right")
    and with the given font.
    If move is True, the pen is moved to the bottom-right corner
    of the text. By default, move is False.

    Example:
    >>> write('Home = ', True, align="center")
    >>> write((0,0), True)
    """


def xcor():
    """
     Return the turtle's x coordinate.

    No arguments.

    Example:
    >>> reset()
    >>> left(60)
    >>> forward(100)
    >>> print xcor()
    50.0
    """


def ycor():
    """
     Return the turtle's y coordinate
    ---
    No arguments.

    Example:
    >>> reset()
    >>> left(60)
    >>> forward(100)
    >>> print ycor()
    86.6025403784
    """


def write_docstringdict(filename='turtle_docstringdict'):
    """
        Create and write docstring-dictionary to file.

    Optional argument:
    filename -- a string, used as filename
                default value is turtle_docstringdict

    Has to be called explicitly, (not used by the turtle-graphics classes)
    The docstring dictionary will be written to the Python script <filname>.py
    It is intended to serve as a template for translation of the docstrings
    into different languages.
    """


def done():
    """
    Starts event loop - calling Tkinter's mainloop function.

    No argument.

    Must be last statement in a turtle graphics program.
    Must NOT be used if a script is run from within IDLE in -n mode
    (No subprocess) - for interactive use of turtle graphics.

    Example:
    >>> mainloop()

    """


class Terminator (Exception):
    pass


