# use plain attributes instead of getters and setters
class Resistor(object):
    """Record basic properties of a resistor"""

    def __init__(self, ohms):
        self.ohms = ohms
        self.current = 0
        self.voltage = 0


class VoltageResistence(Resistor):
    """use property to set stuff"""
    def __init__(self, ohms):
        super().__init__(ohms)
        self._voltage = 0

    @property
    def voltage(self):
        return self._voltage

    @voltage.setter
    def voltage(self, voltage):
        """set the voltage, and update corresponding current"""
        self._voltage = voltage
        self.current = self._voltage / self.ohms


class BoundedResistence(Resistor):
    """Restrict resistor ohms to postive"""
    def __init__(self, ohms):
        self.ohms = ohms

    @property
    def ohms(self):
        return self._ohms

    @ohms.setter
    def ohms(self, value):
        if value <= 0:
            raise ValueError('ohms must be positive!')
        self._ohms = value


class FixedResistence(Resistor):
    """Example of using setter to prevent value from being modified after initial constructor call"""
    def __init__(self, ohms):
        self.ohms = ohms

    @property
    def ohms(self):
        return self._ohms

    @ohms.setter
    def ohms(self, value):
        if hasattr(self, '_ohms'):
            raise ValueError('cannot modify ohms')
        if value <= 0:
            raise ValueError('ohms must be positive!')
        self._ohms = value
