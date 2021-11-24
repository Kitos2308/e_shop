from rest_framework import viewsets
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from .serializers import *
from .models import *
from django.shortcuts import get_object_or_404
# Create your views here.


# class CategoryViewSet(viewsets.ModelViewSet):
#     queryset = Category.objects.all().order_by('name')
#     serializer_class = CategorySerializer


class CategoryViewSet(viewsets.ModelViewSet):
    renderer_classes = [JSONRenderer]
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    lookup_field = 'category_slug'
    # extra_kwargs = {
    #     'url': {'lookup_field': 'category_slug'}}
    # slug_field = 'category_slug'

    def list(self, request, *args, **kwargs):
        try:
            # print('category category ------------------------')
            categories =Category.objects.all()
            serializer = CategorySerializer(categories, many=True )
            return Response({"resultCode":"0", "data":serializer.data})
        except Exception as ex:
            return Response({"resultCode":"10", "data":str(ex)})

    def retrieve(self, request,  *args, **kwargs):

        print(kwargs)
        # post = get_object_or_404(Category, slug=kwargs['pk'])
        print('category category ------------------------')
        categories = Category.objects.filter(slug=kwargs['category_slug'])
        serializer = CategorySerializer(categories, many=True)
        print(serializer.data)
        # print(post)
        return Response(serializer.data)


class SubCategoryViewSet(viewsets.ModelViewSet):
    renderer_classes = [JSONRenderer]
    queryset = Subcategory.objects.all()
    serializer_class = SubCategorySerializer
    lookup_field = 'subcategory_slug'

    def retrieve(self, request,  *args, **kwargs):

        # slug_1 = kwargs['category_slug_']
        slug_2 = kwargs['subcategory_slug']
        categories = Subcategory.objects.filter(slug=slug_2)
        category_serializer = SubCategorySerializer(categories, many=True)
        print(category_serializer.data)
        return Response(category_serializer.data)


class SubCategoryProductViewSet(viewsets.ModelViewSet):
    renderer_classes = [JSONRenderer]
    queryset = SubcategoryProduct.objects.all()
    serializer_class = SubCategoryProductSerializer
    lookup_field = 'subcategoryproduct_slug'

    def retrieve(self, request,  *args, **kwargs):

        # slug_1 = kwargs['category_slug_']
        slug_2 = kwargs['subcategoryproduct_slug']
        categories = SubcategoryProduct.objects.filter(slug=slug_2)
        category_serializer = SubCategoryProductSerializer(categories, many=True)
        return Response(category_serializer.data)


class SubCategoryProductLastViewSet(viewsets.ModelViewSet):
    renderer_classes = [JSONRenderer]
    queryset = SubcategoryProductLast.objects.all()
    serializer_class = SubCategoryProductSerializerLast
    lookup_field = 'subcategoryproductlast_slug'

    def retrieve(self, request,  *args, **kwargs):

        # slug_1 = kwargs['category_slug_']
        slug_2 = kwargs['subcategoryproductlast_slug']
        categories = SubcategoryProductLast.objects.filter(slug=slug_2)
        category_serializer = SubCategoryProductSerializerLast(categories, many=True)
        return Response(category_serializer.data)


# class SubCategoryViewSet(viewsets.ModelViewSet):
#     queryset = Subcategory.objects.all().order_by('name')
#     serializer_class = SubCategorySerializer


# example for raw query


# class AirportView(viewsets.ModelViewSet):
#     renderer_classes = [JSONRenderer]
#     queryset = Airport.objects.all()
#     serializer_class = AirportSerializer
#
#     def list(self, request, *args, **kwargs):
#
#         airports =Airport.objects.raw('''
#         select airports.id , airports.parent_id, cities_translate.title as title_city , airports.code_iata, cities_translate.language_id,
#          airports_translate.title , airports.ord, airports.parent_id, airports.created_date, airports.city_id,
#          airports.airport_group_id
#          from airports
#         left outer join airports parent on airports.parent_id = parent.id
#         left outer join airports_translate on airports_translate.airport_id = coalesce(airports.id, parent.id)
#         left outer join cities on coalesce(airports.city_id, parent.city_id)=cities.id
#         left outer join cities_translate on cities_translate.city_id=coalesce(airports.city_id, parent.city_id)
#         where airports_translate.language_id=%s and cities_translate.language_id=%s
#         order by airports.ord''', [2,2])
#         serializer = AirportSerializer(airports, many=True )
#         return Response(serializer.data)
#     #
#     def retrieve(self, request, *args, **kwargs):
#         pk = kwargs['pk']
#         airport = Airport.objects.raw('''
#         select airports.id , cities_translate.title as title_city , airports.code_iata, cities_translate.language_id,
#          airports_translate.title , airports.ord, airports.photo_path
#         from airports
#         left outer join airports parent on airports.parent_id = parent.id
#         left outer join airports_translate on airports_translate.airport_id = coalesce(airports.id, parent.id)
#         left outer join cities on coalesce(airports.city_id, parent.city_id)=cities.id
#         left outer join cities_translate on cities_translate.city_id=coalesce(airports.city_id, parent.city_id)
#         where airports_translate.language_id=%s and cities_translate.language_id=%s and airports.id=%s
#         order by airports.ord ''', [2, 2, pk])
#         city = City.objects.raw('''select cities_translate.id, cities_translate.city_id, cities_translate.title from cities_translate where
#         language_id=%s
#            ''', [2] )
#         airports_translate = AirportTranslate.objects.raw('''select airports_translate.id, airports_translate.title,
#          airports_translate.language_id from airports_translate where airport_id = %s
#                   ''', [pk])
#         languages = Language.objects.raw('''select languages.id , languages.name from languages order by languages.id''')
#         serializer_city = CityTranslateSerializer(city, many=True)
#         serializer_airport = AirportSerializer(airport, many=True)
#         serializer_languages = LanguageSerializer(languages, many=True)
#         serializer_airport_translate = AirportTranslateSerializer(airports_translate, many=True)
#         return Response({'airport_data': serializer_airport.data[0], 'list_city_title':serializer_city.data,
#                          'list_airport_title': serializer_airport_translate.data, 'languages':serializer_languages.data})