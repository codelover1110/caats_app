from django.shortcuts import render

from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status
from rest_framework.decorators import api_view
from datetime import datetime
import asyncpg
import os

# database = os.environ['DB_NAME']
# user = os.environ['DB_USERNAME']
# password = os.environ['DB_PASSWORD']
# host = 'localhost'
# port = '5432'

table_list = []

# Create your views here.
@api_view(['GET', 'PUT', 'DELETE'])
async def get_table_list(request, pk):
    return JsonResponse({'message': 'success'}, status=status.HTTP_201_CREATED) 

async def index(request):
    await query_tables()
    return JsonResponse({'message': 'success'}, status=status.HTTP_201_CREATED)


async def query_tables():
    conn = await asyncpg.connect(database='crypto_data', user = 'postgres', password = 'caats_pg_pw', host = '127.0.0.1', port = '5432')
    # conn = await asyncpg.connect(database='stockdb', user = 'trader', password = '1104David!', host = '192.168.1.64', port = '5432')
    values = await conn.fetch(
            "SELECT table_name FROM information_schema.tables WHERE table_schema='public'"
        )
    await conn.close()
    
    for item in values:
        table_list.append(item.get('table_name'))

    print(table_list)
    
    
