from datetime import datetime

from sqlalchemy import Column, Integer, ForeignKey, DateTime
from sqlalchemy.orm import relationship

from ecommerce.db import Base
from ecommerce.products.models import Product
from ecommerce.user.models import User


class Cart(Base):
    __tablename__ = "cart"

    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey(User.id, ondelete="CASCADE"), )
    cart_items = relationship("CartItems", back_populates="cart")
    user_cart = relationship("User", back_populates="cart")
    created_date = Column(DateTime, default=datetime.now)


class CartItems(Base):
    __tablename__ = "cart_items"

    id = Column(Integer, primary_key=True, autoincrement=True)
    cart_id = Column(Integer, ForeignKey("cart.id", ondelete="CASCADE"), )
    product_id = Column(Integer, ForeignKey(Product.id, ondelete="CASCADE"), )
    cart = relationship("Cart", back_populates="cart_items")
    created_date = Column(DateTime, default=datetime.now)
