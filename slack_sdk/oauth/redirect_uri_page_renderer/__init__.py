from typing import Optional


class RedirectUriPageRenderer:
    def __init__(
        self,
        *,
        install_path: str,
        redirect_uri_path: str,
        success_url: Optional[str] = None,
        failure_url: Optional[str] = None,
    ):
        self.install_path = install_path
        self.redirect_uri_path = redirect_uri_path
        self.success_url = success_url
        self.failure_url = failure_url

    def render_success_page(self, app_id: str, team_id: Optional[str]) -> str:
        url = self.success_url
        if url is None:
            if team_id is None:
                url = "slack://open"
            else:
                url = f"slack://app?team={team_id}&id={app_id}"
        return f"""
<html>
<head>
<meta http-equiv="refresh" content="0; URL={url}">
<style>
body {{
  padding: 10px 15px;
  font-family: verdana;
  text-align: center;
}}
</style>
</head>
<body>
<h2>Thank you!</h2>
<p>Redirecting to the Slack App... click <a href="{url}">here</a></p>
</body>
</html>
"""

    def render_failure_page(self, reason: str) -> str:
        return f"""
<html>
<head>
<style>
body {{
  padding: 10px 15px;
  font-family: verdana;
  text-align: center;
}}
</style>
</head>
<body>
<h2>Oops, Something Went Wrong!</h2>
<p>Please try again from <a href="{self.install_path}">here</a> or contact the app owner (reason: {reason})</p>
</body>
</html>
"""
