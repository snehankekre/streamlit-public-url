from streamlit.runtime.scriptrunner import get_script_run_ctx
from streamlit.web.server.browser_websocket_handler import BrowserWebSocketHandler

import streamlit as st
from streamlit import runtime


def get_public_url() -> str:
    ctx = get_script_run_ctx()
    if ctx is None:
        return None

    session_client = runtime.get_instance().get_client(ctx.session_id)
    if session_client is None:
        return None

    if not isinstance(session_client, BrowserWebSocketHandler):
        raise RuntimeError(
            f"SessionClient is not a BrowserWebSocketHandler! ({session_client})"
        )
    protocol, host = session_client.request.protocol, session_client.request.host
    return f"{protocol}://{host}"


st.write(get_public_url())
