class TV:
    _numTV = 0

    def _init__(self, marca, estado):
        self._marca = marca
        self._estado = estado
        self._canal = 1
        self._volumen = 1
        self._precio = 500

        TV._numTV += 1

    @classmethod
    def getNumTV(cls):
         return cls._numTV
    
    @classmethod 
    def setNumTV(cls, numTV: int):
         cls._numTV = numTV

    def getMarca(self):
         return self._marca
    
    def setMarca(self, marca):
         self.marca = marca

    def getCanal(self):
         return self._canal
    
    def setCalan(self, canal):
         if 1 <= canal <= 120 and self._estado:
              self._canal = canal

    def getPrecio(self):
         return self._precio
    
    def setPrecio(self, precio):
         self.getPrecio = precio

    def getVolumen(self):
         return self._volumen

    def setVolumen(self, volumen):
         if 0 <= volumen <= 7 and self._estado:
              self._volumen = volumen

    def getControl(self):
         return self._control
    
    def setControl(self, control):
         self.control = control

    def turnOn(self):
         self.estado = True

    def turnOff(self):
         self.estado = False

    def getEstado(self):
         return self.estado

    def canalDown(self):
        if self.estado and 1 < self.canal <= 120:
            self.canal -= 1

    def canalUp(self):
        if self.estado and 1 <= self.canal < 120:
            self.canal += 1

    def volumenDown(self):
        if self.estado and 0 < self.volumen <= 7:
            self.volumen -= 1

    def volumenUp(self):
        if self.estado and 0 <= self.volumen < 7:
            self.volumen += 1
    
         