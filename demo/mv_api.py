# piv_tool.py
from langchain.tools import tool
import json

@tool("call_piv_api", return_direct=True)
def call_piv_api(params_json: str) -> str:
    """
    简化 DEMO：模拟调用公司 API
    """
    params = json.loads(params_json)
    # 这里可以替换成实际 requests.post 调用公司 API
    result = {"PIV": params.get("a", 0) + params.get("b", 0), "status": "success"}
    return json.dumps(result)
