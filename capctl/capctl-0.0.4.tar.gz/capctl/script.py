mac_helm_install = "brew install helm"
ubuntu_helm_install = """curl https://baltocdn.com/helm/signing.asc | sudo apt-key add - &&
        sudo apt-get install apt-transport-https --yes 
        echo "deb https://baltocdn.com/helm/stable/debian/ all main" | sudo tee /etc/apt/sources.list.d/helm-stable-debian.list 
        sudo apt-get update 
        sudo apt-get install -y helm"""

mac_telepresence_install = """brew install --cask macfuse
        brew install --cask osxfuse
        brew install datawire/blackbird/telepresence-legacy"""
ubuntu_telepresence_install = """curl -s https://packagecloud.io/install/repositories/datawireio/telepresence/script.deb.sh | sudo bash
        sudo apt install -y --no-install-recommends telepresence"""
