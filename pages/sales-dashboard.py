import streamlit as st
import streamlit.components.v1 as components
from css import css

st.markdown("<h1 style='text-align: center; color: black;'>Sales Analytics Dashboard</h1>", unsafe_allow_html=True)

st.markdown(
    """
    <div style="width: 70%; margin: 0 auto; text-align: center; font-size: 1.1rem;">
        <p>
        Built to help businesses track performance, customer behavior, and shipping efficiency across multiple dimensions,  
        it combines powerful filtering capabilities with intuitive visualizations. 
        From high-level KPIs to detailed customer analytics,
        this dashboard delivers the key metrics business leaders need to make informed decisions.
        </p>
    </div>
    """, 
    unsafe_allow_html=True
)

st.markdown(f"<style>{css}</style>", unsafe_allow_html=True)
# components.iframe("https://public.tableau.com/views/Sales-Dashboard_17384750055410/OverviewDashboard?:language=en-US&publish=yes&:sid=&:redirect=auth&:display_count=n&:origin=viz_share_link", height=500)
components.html(
    """
    <div class='tableauPlaceholder' id='viz1739637274389' style='position: relative; margin: 0 auto;'><noscript><a href='#'><img alt='Overview Dashboard ' src='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;Sa&#47;Sales-Dashboard_17384750055410&#47;OverviewDashboard&#47;1_rss.png' style='border: none' /></a></noscript><object class='tableauViz'  style='display:none;'><param name='host_url' value='https%3A%2F%2Fpublic.tableau.com%2F' /> <param name='embed_code_version' value='3' /> <param name='site_root' value='' /><param name='name' value='Sales-Dashboard_17384750055410&#47;OverviewDashboard' /><param name='tabs' value='no' /><param name='toolbar' value='yes' /><param name='static_image' value='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;Sa&#47;Sales-Dashboard_17384750055410&#47;OverviewDashboard&#47;1.png' /> <param name='animate_transition' value='yes' /><param name='display_static_image' value='yes' /><param name='display_spinner' value='yes' /><param name='display_overlay' value='yes' /><param name='display_count' value='yes' /><param name='language' value='en-US' /><param name='filter' value='publish=yes' /></object></div>                <script type='text/javascript'>                    var divElement = document.getElementById('viz1739637274389');                    var vizElement = divElement.getElementsByTagName('object')[0];                    if ( divElement.offsetWidth > 800 ) { vizElement.style.width='1200px';vizElement.style.height='827px';} else if ( divElement.offsetWidth > 500 ) { vizElement.style.width='1200px';vizElement.style.height='827px';} else { vizElement.style.width='100%';vizElement.style.height='2327px';}                     var scriptElement = document.createElement('script');                    scriptElement.src = 'https://public.tableau.com/javascripts/api/viz_v1.js';                    vizElement.parentNode.insertBefore(scriptElement, vizElement);                </script>
    """,
 height = 900)

