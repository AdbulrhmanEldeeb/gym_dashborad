class PageConfig:
    # Visualizations folder
    VISUALIZATIONS_FOLDER = r'visualizations'
    
    # Page configuration
    page_title="Comprehensive Gym Analytics Dashboard"
    page_icon="💪"
    layout= "wide"


    # sidebar
    sidebar_title = "🏋️ Gym Analytics Dashboard"
    sidebar_image ="assets/train.webp" 
    sidebar_radio_title = "Navigate Sections"

    # overview 
    overview_title = "🏋️ Gym Analytics Dashboard"
    overview_description = """
    ### Welcome to the Gym Analytics Visualization Platform

    This dashboard provides a deep dive into various aspects of [gym membership](https://www.kaggle.com/datasets/ka66ledata/gym-membership-dataset), 
    attendance, and member characteristics. Navigate through the sections to 
    explore different insights.
    ### 📂 Notebooks & Repositories  

    - **GitHub Notebooks:** [Gym Analytics](https://github.com/AdbulrhmanEldeeb/gym_dataset)  
    - **Kaggle Notebook:** [Gym Membership Data Analysis](https://www.kaggle.com/code/abdulrhmaneldeeb/gym-eda0)  
    - **Dashboard Repository:** [Gym Dashboard](https://github.com/AdbulrhmanEldeeb/gym_dashborad)  

    #### Dashboard Sections:
    """
    overview_tail = """
    #### How to Use:
    - Use the sidebar to navigate between different analytical sections
    - Each section contains multiple related visualizations
    - Scroll through charts to explore detailed insights
    """
    
configure = PageConfig()

