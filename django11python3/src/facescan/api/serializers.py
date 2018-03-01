from rest_framework import serializers

from facescan.models import Item


class BlogPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = [
            'slug',
            'name',
            'contact',
            'contents',
            'excludes',
            'image',
            'timestamp',
        ]
        read_only_field = ['name']

        def validate_title(self, value):
            qs = Item.objects.filter(title_iexact=value)
            if self.instance:
                qs = qs.excludde(slug = self.instance.slug)
            if qs.exists():
                raise serializers.ValidationError("title must be unique")
            return value


