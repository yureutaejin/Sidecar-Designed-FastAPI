from fastapi import APIRouter
from api import check_usage
from typing import List
from apiKey import api_key_auth
from fastapi.responses import Response
import json

router = APIRouter(
    prefix="/master-access",
)

@router.get("/check_usage/dump_data/")
def usage_dump_data(api_name: str):
    value = check_usage.check_usage_dump(api_name=api_name)
    return value

@router.get("/check_usage/tracking_user/")
def usage_tracking_user(api_name: str):
    value = check_usage.check_usage_user_tracking(api_name=api_name)
    return value

@router.get("/api_key_generator/create")
def generator_endpoint(domain: str, origin: str, who: str, password: str, tier: str="client"):
    print("access api-key-generator endpoint")
    value = api_key_auth.key_generator(domain=domain, origin=origin, who=who, password=password, tier=tier)
    return value

@router.get("/api_key_generator/read")
def loader_endpoint():
    print("access api-key-loader endpoint")
    json_lines = "\n".join([str(item) for item in api_key_auth.key_loader()])
    return Response(content=json_lines, media_type="text/plain")

@router.get("/api_key_generator/delete")
def deleter_endpoint(domain: str, origin: str, who: str, developer_password: str):
    print("access api-key-deleter endpoint")
    value = api_key_auth.key_deleter(domain=domain, origin=origin, who=who, developer_password=developer_password)
    return value
