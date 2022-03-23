class setup:
    ''' '''
    def __init__(self, driver):
        self.driver = driver
        
    def find(self, css_selector, attribute=None, parent=None):
        if not parent:
            parent = self.driver
        element = parent.find_element_by_css_selector(css_selector)
        if attribute:
            attribute = element.get_attribute(attribute)
            return element, attribute
        return element

    def finds(self, css_selector, parent=None):
        if not parent:
            parent = self.driver
        elements = parent.find_elements_by_css_selector(css_selector)
        return elements

    def click(self, css_selector, parent=None):
        if not parent:
            parent = self.driver
        element = parent.find_element_by_css_selector(css_selector)
        element.click()

    def text(self, css_selector, parent=None):
        if not parent:
            parent = self.driver
        element = parent.find_element_by_css_selector(css_selector)
        return element.text

    def send(self, css_selector, text, parent=None):
        if not parent:
            parent = self.driver
        element = parent.find_element_by_css_selector(css_selector)
        element.send_keys(text)