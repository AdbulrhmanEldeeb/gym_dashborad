from components.dashboard import GymAnalyticsDashboard

def main():
    dashboard = GymAnalyticsDashboard()
    dashboard.setup_page()
    dashboard.render()

if __name__ == "__main__":
    main()

