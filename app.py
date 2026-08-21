import sys

import streamlit as st
from streamlit.runtime.scriptrunner import get_script_run_ctx


def main():
    st.title("Hello! HYW")


if __name__ == "__main__":
    if get_script_run_ctx() is None:
        # `python streamlit_sample.py`로 직접 실행된 경우: streamlit run으로 재실행
        from streamlit.web import cli as stcli

        sys.argv = ["streamlit", "run", *sys.argv]
        sys.exit(stcli.main())
    else:
        main()
