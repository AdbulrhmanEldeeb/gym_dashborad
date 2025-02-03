class PageConfig:
    # Visualizations folder
    VISUALIZATIONS_FOLDER = r'vis'
    
    # Page configuration
    page_title="Comprehensive Gym Analytics Dashboard"
    page_icon="💪"
    layout= "wide"


    # sidebar
    sidebar_title = "🏋️ Gym Analytics Dashboard"
    sidebar_image ="dashboard/assets/train.webp" 
    sidebar_radio_title = "Navigate Sections"

    # overview 
    overview_title = "🏋️ Gym Analytics Dashboard"
    overview_description = """
    ### Welcome to the Gym Analytics Visualization Platform

    This dashboard provides a deep dive into various aspects of gym membership, 
    attendance, and member characteristics. Navigate through the sections to 
    explore different insights.

    #### Dashboard Sections:
    """
    overview_tail = """
    #### How to Use:
    - Use the sidebar to navigate between different analytical sections
    - Each section contains multiple related visualizations
    - Scroll through charts to explore detailed insights
    """
    
configure = PageConfig()

