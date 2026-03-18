
import io, re
from io, import BytesIO
import streamlit as st
from huggingface_hub import InferenceClient
import config

from groq import generate_response


MATH_SYSTEM = """u r smart sole like me teacher totaly correct asners
dfdfdfdfd
dfdfdfdfd"""

CHAT_CSS = """
style>
.wrap {max-height: 520px; overflow-y: auto; padding-right: 6px;}
.card{border:1px solid #e6e6e6;background:#fff;border-radius:10px;padding:14px 16px;margin:10px 0;
box-shadow:0 1px 2px rgba(0,0,0,0.04);}
.q{font-weight:700;color:#0a6ebd;margin-bottom:8px;}
.meta{display:inline-block;background:#FF9800;color:#fff;padding:2px 8px;border-radius:12px;font-size:12px;margin-left:8px}
.a{white-space:pre-wrap;color:#333;line-height:1.5;}
</style>
"""

def export_txt(history):
    txt = "".join([f""])