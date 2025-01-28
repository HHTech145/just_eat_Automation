import zipfile

def create_proxy_auth_extension(proxy_host, proxy_port, username, password):
    manifest_json = """
    {
        "version": "1.0.0",
        "manifest_version": 2,
        "name": "Chrome Proxy",
        "permissions": [
            "proxy",
            "tabs",
            "unlimitedStorage",
            "storage",
            "<all_urls>"
        ],
        "background": {
            "scripts": ["background.js"]
        }
    }
    """
    
    background_js = f"""
    var config = {{
        mode: "fixed_servers",
        rules: {{
            singleProxy: {{
                scheme: "http",
                host: "{proxy_host}",
                port: parseInt({proxy_port})
            }},
            bypassList: ["localhost"]
        }}
    }};

    chrome.proxy.settings.set({{value: config, scope: "regular"}}, function() {{}});
    chrome.webRequest.onAuthRequired.addListener(
        function(details, callback) {{
            callback({{authCredentials: {{username: "{username}", password: "{password}"}}}});
        }},
        {{urls: ["<all_urls>"]}},
        ["blocking"]
    );
    """
    
    with zipfile.ZipFile("proxy_auth_plugin.zip", "w") as zp:
        zp.writestr("manifest.json", manifest_json)
        zp.writestr("background.js", background_js)

# Replace with your proxy details
create_proxy_auth_extension("45.135.38.245", "50100", "khalid05kKL", "KrGQkpmMiQ")
# khalid05kKL:KrGQkpmMiQ@45.135.38.245:50100
