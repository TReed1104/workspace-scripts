## Import the webbrowser module
import webbrowser

## List of tabs to open
tabs = {
    "https://www.socstech.support/scp/login.php",
    "https://www.github.com/treed1104",
    "https://ps.lincoln.ac.uk",
    "https://www2.deepfreeze.com/en/Home/Dashboard"
}

def OpenWebsites():
    for tab in tabs:
        webbrowser.open(tab)

## Script Entry
if __name__ == '__main__':
    OpenWebsites()
