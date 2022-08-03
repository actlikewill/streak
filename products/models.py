from django.db import models
from treebeard.mp_tree import MP_Node
from taggit.models import TagBase, ItemBase
from taggit.managers import TaggableManager


class HierarchicalTag (TagBase, MP_Node):
  node_order_by = [ 'name' ]


class Product(ItemBase):
  name = models.CharField(max_length=100)

  def __str__(self):
    return f'Product: {self.name}'

class ProductCategory(models.Model):
  product = models.ForeignKey(Product, on_delete=models.CASCADE)
  category = models.ForeignKey(HierarchicalTag, null=True, blank=True, on_delete=models.CASCADE)

  def __str__(self):
    return f'ProductCategory: {self.category.name}'
