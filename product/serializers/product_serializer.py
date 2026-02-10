from rest_framework import serializers
from product.models import Product, Category
from product.serializers.category_serializer import CategorySerializer


class ProductSerializer(serializers.ModelSerializer):
    categories_id = serializers.PrimaryKeyRelatedField(
        queryset=Category.objects.all(),
        many=True,
        write_only=True
    )

    category = CategorySerializer(many=True, read_only=True)

    class Meta:
        model = Product
        fields = [
            "id",
            "title",
            "description",
            "price",
            "active",
            "category",
            "categories_id",
        ]


    def create(self, validated_data):
        categories_data = validated_data.pop("categories_id")
        product = Product.objects.create(**validated_data)
        product.category.set(categories_data)

        return product