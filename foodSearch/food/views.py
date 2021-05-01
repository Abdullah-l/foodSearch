from django.shortcuts import render, redirect
import os
from django.conf import settings
from django.http import HttpResponse, JsonResponse
import mysql.connector
from mysql.connector.errors import Error
import datetime


def home(request):
    return render(request, 'home.html')

def foodS(request):
    if 'q' in request.GET:
        sq = request.GET['q']
        print(sq)
        try:
            cnx = mysql.connector.connect(
                user='token_fdf9',
                host='127.0.0.1',
                port='3306',
                password='_NVHByRMtohsF29W',
                database='aaa1118_restaurants'
            )
            query = f"""SELECT MenuItem.name AS menuItemName, Restaurant.name AS restaurantName, MenuItem.description, MenuItem.cost, Restaurant.id, Rating.stars FROM MenuItem
                        INNER JOIN Menu ON Menu.id = MenuItem.menuId
                        INNER JOIN Restaurant ON Menu.id = Restaurant.menuId
                        INNER JOIN Rating ON Restaurant.ratingId = Rating.id
                        WHERE MenuItem.name LIKE %s
                        """
            cursor = cnx.cursor(dictionary=True)
            cursor.execute(query, ("%" + sq + "%", ))
            context = {}
            result = cursor.fetchall()
            context['result'] = result
            print(context)


        except mysql.connector.Error as err:
            print(err)
        else:
            # Invoked if no exception was thrown
            cnx.close()
        return render(request, 'foodS.html', context)
    else:
        return render(request, 'foodS.html')

def restaurantS(request):
    if 'q' in request.GET:
        sq = request.GET['q']
        print(sq)
        try:
            cnx = mysql.connector.connect(
                user='token_fdf9',
                host='127.0.0.1',
                port='3306',
                password='_NVHByRMtohsF29W',
                database='aaa1118_restaurants'
            )
            query = f"""SELECT Restaurant.name AS restaurantName, Rating.stars, Restaurant.id FROM Restaurant
                        INNER JOIN Rating ON Restaurant.ratingId = Rating.id
                        WHERE Restaurant.name LIKE %s
                        """
            cursor = cnx.cursor(dictionary=True)
            cursor.execute(query, ("%" + sq + "%", ))
            context = {}
            result = cursor.fetchall()
            context['result'] = result
            print(context)


        except mysql.connector.Error as err:
            print(err)
        else:
            # Invoked if no exception was thrown
            cnx.close()
        return render(request, 'restaurantS.html', context)
    else:
        return render(request, 'restaurantS.html')

def cuisineS(request):
    if 'q' in request.GET:
        sq = request.GET['q']
        try:
            cnx = mysql.connector.connect(
                user='token_fdf9',
                host='127.0.0.1',
                port='3306',
                password='_NVHByRMtohsF29W',
                database='aaa1118_restaurants'
            )
            query = f"""SELECT Restaurant.name AS restaurantName, Rating.stars, Cuisine.name AS cuisineName, Restaurant.id FROM Restaurant
                        INNER JOIN Rating ON Restaurant.ratingId = Rating.id
                        INNER JOIN CuisineOf ON CuisineOf.restaurantId = Restaurant.id
                        INNER JOIN Cuisine ON CuisineOf.cuisineId = Cuisine.id
                        WHERE Cuisine.name LIKE %s;
                        """
            cursor = cnx.cursor(dictionary=True)
            cursor.execute(query, ("%" + sq + "%", ))
            context = {}
            result = cursor.fetchall()
            context['result'] = result
            print(context)


        except mysql.connector.Error as err:
            print(err)
        else:
            # Invoked if no exception was thrown
            cnx.close()
        return render(request, 'cuisineS.html', context)
    else:
        return render(request, 'cuisineS.html')

def restaurant(request, id):
    try:
        cnx = mysql.connector.connect(
            user='token_fdf9',
            host='127.0.0.1',
            port='3306',
            password='_NVHByRMtohsF29W',
            database='aaa1118_restaurants'
        )
        query = f"""SELECT MenuItem.name AS menuItemName, MenuItem.description, MenuItem.cost, Restaurant.name AS restaurantName, Rating.stars FROM Restaurant
                    INNER JOIN Menu ON Menu.id = Restaurant.menuId
                    INNER JOIN MenuItem ON Menu.id = MenuItem.menuId
                    INNER JOIN Rating ON Rating.id = Restaurant.ratingId
                    WHERE Restaurant.id = %s;
                    """
        cursor = cnx.cursor(dictionary=True)
        cursor.execute(query, (id, ))
        context = {}
        result = cursor.fetchall()
        context['result'] = result
        print(context)


    except mysql.connector.Error as err:
        print(err)
    else:
        # Invoked if no exception was thrown
        cnx.close()
    return render(request, 'restaurant.html', context)