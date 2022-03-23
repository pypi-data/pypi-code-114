from typing import List, Optional

from paka.cmark import lowlevel

from .types import ListType, NodeType


class Node:

    def __init__(self, node) -> None:
        self._node = node

    def free(self):
        """Free memory for node and its children (if any)."""
        lowlevel.node_free(self._node)

    def __visit(self, func: str):
        n = getattr(lowlevel, func)(self._node)
        if n:
            return self.__class__(n)
        return None

    def next(self):
        """Return next node, if available.

        :returns: A node or None.

        """
        return self.__visit("node_next")

    def previous(self):
        """Return previous node, if available.

        :returns: A node or None.

        """
        return self.__visit("node_previous")

    def parent(self):
        """Return a parent of node, if available.

        :returns: A node or None.

        """
        return self.__visit("node_parent")

    def first_child(self):
        """Return first child of node, if available.

        :returns: A node or None.

        """
        return self.__visit("node_first_child")

    def last_child(self):
        """Return last child of node, if available.

        :returns: A node or None.

        """
        return self.__visit("node_last_child")

    def __operate(self, func: str, n: "Node"):
        res = getattr(lowlevel, func)(self._node, n._node)
        return bool(res)

    def insert_before(self, sibling: "Node"):
        """Insert sibling before node.

        Returns
        -------
        bool
            ``True`` on success, ``False`` on failure.

        """
        return self.__operate("node_insert_before", sibling)

    def insert_after(self, sibling: "Node"):
        """Insert sibling after node.

        Returns
        -------
        bool
            ``True`` on success, ``False`` on failure.

        """
        return self.__operate("node_insert_after", sibling)

    def prepend_child(self, child: "Node"):
        """Prepend child to children of node.

        Returns
        -------
        bool
            ``True`` on success, ``False`` on failure.

        """
        return self.__operate("node_prepend_child", child)

    def append_child(self, child: "Node"):
        """Append child to children of node.

        Returns
        -------
        bool
            ``True`` on success, ``False`` on failure.

        """
        return self.__operate("node_append_child", child)

    def get_type(self):
        """Return type of node.

        :returns: One of :ref:`node types <node_types>`.

        """
        return lowlevel.node_get_type(self._node)

    def __get_info(self, func: str, free: bool = False) -> str:
        ct = getattr(lowlevel, func)(self._node)
        return lowlevel.text_from_c(ct, free)

    def __set_info(self, func: str, info: str) -> bool:
        ci = lowlevel.text_to_c(info)
        ct: int = getattr(lowlevel, func)(self._node, ci)
        return bool(ct)

    def get_type_string(self):
        """Return type of node as string."""
        return self.__get_info("node_get_type_string")

    def get_fence_info(self):
        """Return fence info from fenced code block.

        For nodes having type other than :py:data:`NODE_CODE_BLOCK`
        returns None.

        """
        return self.__get_info("node_get_fence_info")

    def set_fence_info(self, info: str):
        """Set fence info of fenced code block.

        Parameters
        ----------
        node
            Node on which to operate.
        info: str
            Fence info.

        Returns
        -------
        bool
            ``True`` on success, ``False`` on failure.

        """
        return self.__set_info("node_set_fence_info", info)

    def get_literal(self):
        """Return string contents of node.

        Returns None for nodes having type other than
        :py:data:`NODE_HTML_BLOCK`, :py:data:`NODE_TEXT`,
        :py:data:`NODE_HTML_INLINE`, :py:data:`NODE_CODE`
        or :py:data:`NODE_CODE_BLOCK`.

        """
        return self.__get_info("node_get_literal")

    def set_literal(self, contents: str):
        """Set string contents of node.

        Parameters
        ----------
        node
            Node on which to operate.
        contents: str
            New contents of node.

        Returns
        -------
        bool
            ``True`` on success, ``False`` on failure.

        """
        return self.__set_info("node_set_literal", contents)

    def get_heading_level(self) -> int:
        """Return level of heading.

        Returns
        -------
        int
            ``[1, 6]`` for headings, ``0`` for non-heading nodes.

        """
        return lowlevel.node_get_heading_level(self._node)

    def set_heading_level(self, level: int):
        """Set level of heading.

        Parameters
        ----------
        node
            Node on which to operate.
        level: int
            ``[1, 6]``

        Returns
        -------
        bool
            ``True`` on success, ``False`` on failure.

        """
        res = lowlevel.node_set_heading_level(self._node, level)
        return bool(res)

    def get_list_type(self) -> ListType:
        """Return list type of node.

        :returns: One of :ref:`list types <list_types>`.

        """
        return ListType(lowlevel.node_get_list_type(self._node))

    def set_list_type(self, list_type: ListType):
        """Set the list type of node.

        Parameters
        ----------
        node
            Node on which to operate.
        list_type
            One of :ref:`list types <list_types>`.

        Returns
        -------
        bool
            ``True`` on success, ``False`` on failure.

        """
        res = lowlevel.node_set_list_type(self._node, list_type.value)
        return bool(res)

    def get_list_delim(self):
        """Return type of list delimiter.

        :returns: One of :ref:`list delimiters <list_delimiters>`.

        """
        return lowlevel.node_get_list_delim(self._node)

    def set_list_delim(self, list_delim):
        """Set the type of list delimiter for node.

        Parameters
        ----------
        node
            Node on which to operate.
        list_delim
            One of :ref:`list delimiters <list_delimiters>`.

        Returns
        -------
        bool
            ``True`` on success, ``False`` on failure.

        """
        res = lowlevel.node_set_list_delim(self._node, list_delim)
        return bool(res)

    def get_list_start(self) -> int:
        """Return starting number of list.

        Returns
        -------
        int
            Starting number of an ordered list or ``0``.

        """
        return lowlevel.node_get_list_start(self._node)

    def set_list_start(self, start: int):
        """Set starting number of ordered list.

        Parameters
        ----------
        node
            Ordered list.
        start: int
            Starting number.

        Returns
        -------
        bool
            ``True`` on success, ``False`` on failure.

        """
        res = lowlevel.node_set_list_start(self._node, start)
        return bool(res)

    def get_list_tight(self) -> int:
        """Return 1 if node is a tight list.

        Returns
        -------
        int
            ``1`` if node is a tight list, ``0`` otherwise.

        """
        return lowlevel.node_get_list_tight(self._node)

    def set_list_tight(self, tight: int):
        """Set tightness of list.

        Parameters
        ----------
        node
            List.
        tight: int
            ``1`` for tight, ``0`` for loose.

        Returns
        -------
        int
            ``1`` on success, ``0`` on failure.

        """
        res = lowlevel.node_set_list_tight(self._node, tight)
        return int(res)

    def get_url(self) -> Optional[str]:
        """Return URL of image or link, or None."""
        return self.__get_info("node_get_url")

    def set_url(self, url: str):
        """Set URL of image or link.

        Parameters
        ----------
        node
            Image or link.
        url: str
            New URL.

        Returns
        -------
        bool
            ``True`` on success, ``False`` on failure.

        """
        return self.__set_info("node_set_url", url)

    def get_title(self):
        """Return title of image or link, or None."""
        return self.__get_info("node_get_title")

    def set_title(self, title: str):
        """Set title of image or link.

        Parameters
        ----------
        node
            Image or link.
        title: str
            New title.

        Returns
        -------
        bool
            ``True`` on success, ``False`` on failure.

        """
        return self.__set_info("node_set_title", title)

    def get_start_line(self) -> int:
        """Return line on which node begins.

        Returns
        -------
        int
            Line number (starts from ``1``).

        """
        return lowlevel.node_get_start_line(self._node)

    def get_start_column(self) -> int:
        """Return column at which node begins.

        Returns
        -------
        int
            Column number (starts from ``1``).

        """
        return lowlevel.node_get_start_column(self._node)

    def get_end_line(self) -> int:
        """Return line on which node ends.

        Returns
        -------
        int
            Line number (starts from ``1``).

        """
        return lowlevel.node_get_end_line(self._node)

    def get_end_column(self) -> int:
        """Return column at which node ends.

        Returns
        -------
        int
            Column number (starts from ``1``).

        """
        return lowlevel.node_get_end_column(self._node)
