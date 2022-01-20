from __future__ import annotations
from abc import ABC, abstractmethod

# GATEWAY INTERFACE
class Gateway(ABC):
	@abstractmethod
	def createPayment(self) -> str:
		pass

# FACTORY OF PAYMENT
class Payment (ABC):
	@abstractmethod
	def createGateway(self) -> Gateway:
		pass

# PRODUCT OF PIX
class Pix(Gateway):
	def createPayment (self) -> str:
		return "IMPLEMENT METHODS OF PIX GATEWAY"

# PRODUCT OF CIELO
class Cielo(Gateway):
	def createPayment (self) -> str:
		return "IMPLEMENT METHODS OF CIELO GATEWAY"

# CREATOR OF CIELO PAYMENT
class CieloPayment(Payment):
	def createGateway(self) -> Gateway:
		return Cielo()

# CREATOR OF PIX PAYMENT
class PixPayment(Payment):
	def createGateway(self) -> Gateway:
		return Pix()

# THAT IS CLIENT LOGICAL
def logicalOfCreatePayment(payment: Payment) -> None:
	print(payment.createGateway().createPayment())

# RUN A FUNCTION WITH PIX PAYMENT
logicalOfCreatePayment(PixPayment())

# RUN A FUNCTION WITH CIELO PAYMENT
logicalOfCreatePayment(CieloPayment())