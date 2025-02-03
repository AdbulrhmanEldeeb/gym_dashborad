import streamlit as st
import os
from components.utils import load_plotly_html
from components.categories import ChartCategories
from components.enums import DashboardSections
from config.config import configure
class GymAnalyticsDashboard:
    def __init__(self):
        self.vis_folder = configure.VISUALIZATIONS_FOLDER
        self.chart_categories = ChartCategories(self.vis_folder).chart_categories

    def setup_page(self):
        st.set_page_config(
            page_title=configure.page_title,
            page_icon=configure.page_icon,
            layout=configure.layout
        )

    def render(self):
        # Sidebar setup
        st.sidebar.title(configure.sidebar_title)
        st.sidebar.image(configure.sidebar_image)
        page = st.sidebar.radio(
            configure.sidebar_radio_title,
            [DashboardSections.OVERVIEW.value] + list(self.chart_categories.keys())
        )

        if page == DashboardSections.OVERVIEW.value:
            self.render_overview()
        else:
            self.render_section(page)

    def render_overview(self):
        st.title(configure.overview_title)
        st.markdown(configure.overview_description)

        # Display section descriptions
        for section in self.chart_categories.keys():
            st.markdown(f"- **{section}**")

        st.markdown(configure.overview_tail)

    def render_section(self, page):
        st.title(f"🔍 {page}")
        category_charts = self.chart_categories[page]

        for i, chart_name in enumerate(category_charts):
            chart_path = os.path.join(self.vis_folder, chart_name)

            container_id = f"chart_{i}"
            html_content = load_plotly_html(chart_path)

            # Combined HTML with fullscreen functionality
            full_html = f"""
            <div id="{container_id}" style="width: 100%; height: 500px;">
                {html_content}
            </div>
            <button id="fullscreen-btn-{i}" onclick="
                const element = document.getElementById('{container_id}').querySelector('.plotly-graph-div');
                if (element.requestFullscreen) {{
                    element.requestFullscreen();
                }} else if (element.mozRequestFullScreen) {{
                    element.mozRequestFullScreen();
                }} else if (element.webkitRequestFullscreen) {{
                    element.webkitRequestFullscreen();
                }} else if (element.msRequestFullscreen) {{
                    element.msRequestFullscreen();
                }}
            " style="
                margin: 10px 0;
                padding: 8px 15px;
                background-color: #4CAF50;
                color: white;
                border: none;
                border-radius: 4px;
                cursor: pointer;">
                View Fullscreen
            </button>

            <script>
            document.addEventListener("fullscreenchange", function() {{
                const btn = document.getElementById("fullscreen-btn-{i}");
                if (!document.fullscreenElement) {{
                    btn.style.display = "block";
                }}
            }});
            </script>
            """

            # Full-width display
            st.subheader(chart_name.replace('.html', '').replace('_', ' '))
            st.components.v1.html(full_html, height=600)

# Run dashboard
if __name__ == "__main__":
    dashboard = GymAnalyticsDashboard()
    dashboard.setup_page()
    dashboard.render()
