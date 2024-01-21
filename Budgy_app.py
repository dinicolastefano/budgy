from st_on_hover_tabs import on_hover_tabs
import streamlit as st
import streamlit_float # recommended

# Note - on the page's first load - when user comes in from the url rather than clicking on the tab, the active page will be derived from the url or from the `loadPageName` parameter. Please make sure all params in the data array object are inputed.

st.set_page_config(layout="wide")

streamlit_float.float_init(include_unstable_primary=False)

#if the rendering gets too buggy that you don't feel comfortable, a simple time.sleep(2) helps after this component.
time.sleep(2) # optional

data_ = [
            {"index":0, "label":"Example", "page":"example", "href":"http://localhost:8501/"},
            {"index":1, "label":"Page", "page":"page", "icon":"ri-logout-box-r-line", "href":"http://localhost:8501/page"}
        ]

if "currentPage" not in st.session_state: # required as component will be looking for this in session state to change page via `switch_page`
    st.session_state["currentPage"] = data_[0] 
else:
    st.session_state["currentPage"] = data_[0] 


with st.container():
    defaultSidebar = CustomSidebarDefault(closeNavOnLoad=False, backgroundColor="brown", loadPageName="example", data=data_, LocalOrSessionStorage=1, serverRendering=False, webMedium="local") 
    defaultSidebar.load_custom_sidebar()
    defaultSidebar.change_page()
    
    streamlit_float.float_parent(css="position:fixed; top:-1000px;") # gets rid of the whitespace created from the iframes used to build the component - no big forehead.
