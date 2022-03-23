class setup:
    ''' '''
    def __init__(self, driver):
        self.driver = driver
        
    def find(self, css_selector, attribute=None, parent=driver):
        element = parent.find_element_by_css_selector(css_selector)
        if attribute:
            attribute = element.get_attribute(attribute)
            return element, attribute
        return element

    def finds(css_selector, parent=driver):
        elements = parent.find_elements_by_css_selector(css_selector)
        return elements

    def click(css_selector, parent=driver):
        element = parent.find_element_by_css_selector(css_selector)
        element.click()

    def text(css_selector, parent=driver):
        element = parent.find_element_by_css_selector(css_selector)
        return element.text

    def send(css_selector, text, parent=driver):
        element = parent.find_element_by_css_selector(css_selector)
        element.send_keys(text)