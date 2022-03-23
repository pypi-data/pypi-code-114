from import_export.fields import Field
from import_export.resources import ModelResource
from import_export.widgets import CharWidget, ForeignKeyWidget

from .models import (
    Bundle,
    BundleItem,
    Category,
    Fee,
    Product,
    RecommendedItem,
    Service,
    Specification,
    Unit,
)

product_fields = [
    "created_at",
    "effective_at",
    "modified_at",
    "reg_number",
    "inner_id",
    "uid",
    "parent",
    "name",
    "alias_name",
    "slug",
    "description",
    "category",
    "unit",
    "status",
    "max_order",
    "min_order",
    "is_partial",
]


class ProductResourceBase(ModelResource):
    parent = Field(
        attribute="parent",
        column_name="parent",
        widget=ForeignKeyWidget(Category, field="inner_id"),
    )
    slug = Field(
        attribute="slug",
        readonly=True,
        column_name="slug",
        widget=CharWidget(),
    )
    category = Field(
        attribute="category",
        column_name="category",
        widget=ForeignKeyWidget(Category, field="slug"),
    )
    unit = Field(
        attribute="unit",
        column_name="unit",
        widget=ForeignKeyWidget(Unit, field="slug"),
    )


class ProductResource(ProductResourceBase):
    class Meta:
        model = Product
        fields = product_fields
        export_order = product_fields


class ServiceResource(ProductResourceBase):
    class Meta:
        model = Service
        fields = product_fields + ["price"]
        export_order = product_fields + ["price"]
        import_id_fields = ("inner_id",)


class FeeResource(ProductResourceBase):
    class Meta:
        model = Fee
        fields = product_fields + ["price"]
        export_order = product_fields + ["price"]
        import_id_fields = ("inner_id",)


class UnitResource(ModelResource):
    slug = Field(
        attribute="slug",
        readonly=True,
        column_name="slug",
        widget=CharWidget(),
    )

    class Meta:
        model = Unit
        export_order = ("id", "name", "slug", "html")
        import_id_fields = ("slug",)


class BundleResource(ProductResourceBase):
    class Meta:
        model = Bundle
        fields = product_fields
        export_order = product_fields
        import_id_fields = ("inner_id",)


class BundleItemResource(ModelResource):
    product = Field(
        attribute="product",
        column_name="product",
        widget=ForeignKeyWidget(Product, field="inner_id"),
    )
    item = Field(
        attribute="item",
        column_name="item",
        widget=ForeignKeyWidget(Product, field="inner_id"),
    )

    class Meta:
        model = BundleItem
        export_order = ("id", "product", "item", "quantity", "required")
        import_id_fields = ("product", "item")


class CategoryResource(ModelResource):
    slug = Field(
        attribute="slug",
        readonly=True,
        column_name="slug",
        widget=CharWidget(),
    )
    parent = Field(
        attribute="parent",
        column_name="parent",
        widget=ForeignKeyWidget(Category, field="slug"),
    )

    class Meta:
        model = Category
        exclude = ("lft", "rght", "tree_id", "level")
        export_order = ("id", "name", "slug", "parent")
        import_id_fields = ("slug",)


class SpecificationResource(ModelResource):
    product = Field(
        attribute="product",
        column_name="product",
        widget=ForeignKeyWidget(Product, field="inner_id"),
    )

    class Meta:
        model = Specification
        export_order = ("id", "product", "feature", "description", "value", "note")
        import_id_fields = ("id",)


class RecommendedItemResource(ModelResource):
    product = Field(
        attribute="product",
        column_name="product",
        widget=ForeignKeyWidget(Product, field="inner_id"),
    )
    item = Field(
        attribute="item",
        column_name="item",
        widget=ForeignKeyWidget(Product, field="inner_id"),
    )

    class Meta:
        model = RecommendedItem
        export_order = ("id", "product", "item", "quantity", "required")
        import_id_fields = ("product", "item")
