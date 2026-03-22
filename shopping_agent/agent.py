from __future__ import annotations

import asyncio, base64, json, logging, os, ssl
import urllib.error, urllib.parse, urllib.request
from dataclasses import dataclass, field

import certifi
from fastapi import FastAPI, Request, Response, WebSocket, WebSocketDisconnect
from google.adk.agents import Agent
from google.adk.agents.live_request_queue import LiveRequestQueue
from google.adk.agents.run_config import RunConfig, StreamingMode
from google.adk.runners import Runner
from google.adk.sessions import InMemorySessionService
from google.adk.tools import ToolContext
from google.genai import errors as genai_errors
from google.genai import types
