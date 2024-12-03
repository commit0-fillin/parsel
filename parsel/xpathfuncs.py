import re
from typing import Any, Callable, Optional
from lxml import etree
from w3lib.html import HTML5_WHITESPACE
regex = f'[{HTML5_WHITESPACE}]+'
replace_html5_whitespaces = re.compile(regex).sub

def set_xpathfunc(fname: str, func: Optional[Callable]) -> None:
    """Register a custom extension function to use in XPath expressions.

    The function ``func`` registered under ``fname`` identifier will be called
    for every matching node, being passed a ``context`` parameter as well as
    any parameters passed from the corresponding XPath expression.

    If ``func`` is ``None``, the extension function will be removed.

    See more `in lxml documentation`_.

    .. _`in lxml documentation`: https://lxml.de/extensions.html#xpath-extension-functions

    """
    ns = etree.FunctionNamespace(None)
    if func is None:
        if fname in ns:
            del ns[fname]
    else:
        ns[fname] = func

def has_class(context: Any, *classes: str) -> bool:
    """has-class function.

    Return True if all ``classes`` are present in element's class attr.

    """
    if not context.eval_context.get('is_xpath'):
        raise ValueError("has-class() function can only be used in XPath")
    
    elem = context.context_node
    elem_classes = elem.get('class', '').split()
    return all(cls in elem_classes for cls in classes)
