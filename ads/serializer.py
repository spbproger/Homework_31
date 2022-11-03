from rest_framework import serializers

from ads.models import Ad, Category


class IsPublishedValidator:
    def __call__(self, value):
        if value:
            raise serializers.ValidationError("Значение поля 'is_published' при создании объявления не может быть True.")


class CategoryCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class AdListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ad
        fields = '__all__'


class AdDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ad
        fields = '__all__'


class AdCreateSerializer(serializers.ModelSerializer):
    category = serializers.SlugRelatedField(
        required=False,
        slug_field='name',
        queryset=Category.objects.all(),
    )
    is_published = serializers.BooleanField(validators=[IsPublishedValidator()])

    class Meta:
        model = Ad
        fields = '__all__'

    def is_valid(self, raise_exception=False):
        self._category = self.initial_data.pop('category')
        return super().is_valid(raise_exception=raise_exception)

    def create(self, validated_data):
        ad = Ad.objects.create(**validated_data)
        if self._category:
            category_obj = Category.objects.get_or_create(name=self._category)[0]
            ad.category = category_obj
            ad.save()
        return ad


class AdUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ad
        fields = '__all__'


class AdDestroySerializer(serializers.ModelSerializer):
    class Meta:
        model = Ad
        fields = ['id']
